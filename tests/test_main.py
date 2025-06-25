# tests/test_main.py
import pytest
from pathlib import Path
import re
from dw6.main import (
    register_meta_requirement,
    register_technical_debt,
    META_LOG_FILE,
    TECH_DEBT_FILE,
    main,
)

@pytest.fixture
def mock_log_files(mocker, tmp_path):
    """Fixture to mock log file paths to use a temporary directory."""
    mock_meta_log = tmp_path / "meta_requirements.log"
    mock_tech_debt_log = tmp_path / "technical_debt.log"
    mocker.patch("dw6.main.META_LOG_FILE", mock_meta_log)
    mocker.patch("dw6.main.TECH_DEBT_FILE", mock_tech_debt_log)
    return mock_meta_log, mock_tech_debt_log

def test_register_meta_requirement_creates_file_and_logs_entry(mock_log_files):
    """Verify that the first call creates the log file and adds the first entry correctly."""
    mock_meta_log, _ = mock_log_files
    description = "This is the first meta requirement."

    register_meta_requirement(description)

    assert mock_meta_log.exists()
    with open(mock_meta_log, "r") as f:
        content = f.read()
    
    assert "[ID:1]" in content
    assert description in content
    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)

def test_register_meta_requirement_increments_id(mock_log_files):
    """Verify that subsequent calls increment the requirement ID."""
    mock_meta_log, _ = mock_log_files
    description1 = "First requirement."
    description2 = "Second requirement."

    register_meta_requirement(description1)
    register_meta_requirement(description2)

    with open(mock_meta_log, "r") as f:
        lines = f.readlines()
    
    assert len(lines) == 2
    assert "[ID:1]" in lines[0]
    assert description1 in lines[0]
    assert "[ID:2]" in lines[1]
    assert description2 in lines[1]

def test_register_technical_debt_creates_file_and_logs_entry(mock_log_files):
    """Verify that the first call creates the tech debt log file and adds the first entry."""
    _, mock_tech_debt_log = mock_log_files
    description = "This is the first technical debt."

    register_technical_debt(description)

    assert mock_tech_debt_log.exists()
    with open(mock_tech_debt_log, "r") as f:
        content = f.read()
    
    assert "[ID:1]" in content
    assert description in content
    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)

@pytest.fixture
def mock_main_dependencies(mocker):
    """Fixture to mock dependencies of the main function for the 'do' command tests."""
    mock_workflow_manager_class = mocker.patch('dw6.main.WorkflowManager', autospec=True)
    mock_workflow_manager_instance = mock_workflow_manager_class.return_value
    mock_governor = mocker.MagicMock()
    mock_workflow_manager_instance.governor = mock_governor

    mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
    return mock_governor, mock_subprocess_run

def test_do_command_authorizes_action(mocker, mock_main_dependencies):
    """Verify the 'do' command authorizes an action and does not execute it."""
    mock_governor, mock_subprocess_run = mock_main_dependencies
    mock_governor.authorize.return_value = None
    
    mocker.patch('sys.argv', ['dw6', 'do', 'ls -l'])
    
    main()

    mock_governor.authorize.assert_called_once_with('ls -l')
    mock_subprocess_run.assert_not_called()

def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
    """Verify the 'do' command blocks an action when the Governor denies it."""
    mock_governor, mock_subprocess_run = mock_main_dependencies
    mock_governor.authorize.side_effect = PermissionError("Action denied")

    mocker.patch('sys.argv', ['dw6', 'do', 'git push'])

    with pytest.raises(SystemExit) as e:
        main()
    
    assert e.value.code == 1
    mock_governor.authorize.assert_called_once_with('git push')
    mock_subprocess_run.assert_not_called()
