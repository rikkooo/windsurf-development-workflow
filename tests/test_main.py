# tests/test_main.py
import pytest
from pathlib import Path
import re
from dw6.main import register_meta_requirement, META_LOG_FILE

@pytest.fixture
def cleanup_log_file():
    """Fixture to clean up the meta log file before and after a test."""
    if META_LOG_FILE.exists():
        META_LOG_FILE.unlink()
    yield
    if META_LOG_FILE.exists():
        META_LOG_FILE.unlink()

def test_register_meta_requirement_creates_file_and_logs_entry(cleanup_log_file):
    """Verify that the first call creates the log file and adds the first entry correctly."""
    # Arrange
    description = "This is the first meta requirement."

    # Act
    register_meta_requirement(description)

    # Assert
    assert META_LOG_FILE.exists()
    with open(META_LOG_FILE, "r") as f:
        content = f.read()
    
    assert "[ID:1]" in content
    assert description in content
    # A simple regex to check for the timestamp format
    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)

def test_register_meta_requirement_increments_id(cleanup_log_file):
    """Verify that subsequent calls increment the requirement ID."""
    # Arrange
    description1 = "First requirement."
    description2 = "Second requirement."

    # Act
    register_meta_requirement(description1)
    register_meta_requirement(description2)

    # Assert
    with open(META_LOG_FILE, "r") as f:
        lines = f.readlines()
    
    assert len(lines) == 2
    assert "[ID:1]" in lines[0]
    assert description1 in lines[0]
    assert "[ID:2]" in lines[1]
    assert description2 in lines[1]


@pytest.fixture
def mock_main_dependencies(mocker):
    """Fixture to mock dependencies of the main function for the 'do' command tests."""
    # Since autospec=True is used, we need to configure the mock instance
    # to have the 'governor' attribute.
    mock_workflow_manager_class = mocker.patch('dw6.main.WorkflowManager', autospec=True)
    mock_workflow_manager_instance = mock_workflow_manager_class.return_value
    mock_governor = mocker.MagicMock()
    mock_workflow_manager_instance.governor = mock_governor

    mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
    return mock_governor, mock_subprocess_run

def test_do_command_authorizes_action(mocker, mock_main_dependencies):
    """Verify the 'do' command authorizes an action and does not execute it."""
    # Arrange
    mock_governor, mock_subprocess_run = mock_main_dependencies
    mock_governor.authorize.return_value = None # Simulate authorization success
    
    mocker.patch('sys.argv', ['dw6', 'do', 'ls -l'])
    
    # Act
    from dw6.main import main
    main()

    # Assert
    mock_governor.authorize.assert_called_once_with('ls -l')
    mock_subprocess_run.assert_not_called()

def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
    """Verify the 'do' command blocks an action when the Governor denies it."""
    # Arrange
    mock_governor, mock_subprocess_run = mock_main_dependencies
    mock_governor.authorize.side_effect = PermissionError("Action denied")

    mocker.patch('sys.argv', ['dw6', 'do', 'git push'])

    # Act & Assert
    with pytest.raises(SystemExit) as e:
        from dw6.main import main
        main()
    
    assert e.value.code == 1
    mock_governor.authorize.assert_called_once_with('git push')
    mock_subprocess_run.assert_not_called()
