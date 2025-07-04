# tests/test_governor.py
import pytest
from unittest.mock import MagicMock
from pathlib import Path
import sys

from dw6.state_manager import Governor, WorkflowState

@pytest.fixture
def mock_state(mocker):
    """Fixture to create a mock WorkflowState."""
    state = MagicMock(spec=WorkflowState)
    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
    return state

def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
    """Verify the Governor blocks approval if the spec file is missing."""
    # Arrange: Set the state to Engineer and mock the requirement pointer
    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
    
    # Ensure the spec file does NOT exist for this test
    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
    if spec_file.exists():
        spec_file.unlink()

    governor = Governor(mock_state)

    # Act & Assert: The approval should fail with a SystemExit
    with pytest.raises(SystemExit) as e:
        governor._validate_stage_exit_criteria()
    
    assert e.type == SystemExit
    assert e.value.code == 1

def test_governor_allows_engineer_approval_with_spec_file(mock_state):
    """Verify the Governor allows approval if the spec file exists."""
    # Arrange: Set the state to Engineer and mock the requirement pointer
    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
    
    # Ensure the spec file DOES exist for this test
    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
    spec_file.parent.mkdir(parents=True, exist_ok=True)
    spec_file.touch()

    governor = Governor(mock_state)

    # Act & Assert: The approval should pass without raising an exception
    try:
        governor._validate_stage_exit_criteria()
    except SystemExit:
        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
    finally:
        # Clean up the created file
        if spec_file.exists():
            spec_file.unlink()

def test_governor_enforces_rules_on_approve(mocker, capsys):
    """Verify that the Governor prints the correct rule for the current stage."""
    # Arrange
    mock_state = mocker.MagicMock(spec=WorkflowState)
    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
    governor = Governor(mock_state)
    # Mock the exit criteria validation to prevent SystemExit
    mocker.patch.object(governor, '_validate_stage_exit_criteria')
    # Mock the rest of the approval process to isolate the rule enforcement
    mocker.patch.object(governor, '_transition_to_next_stage')
    mocker.patch('dw6.state_manager.WorkflowManager')

    # Act
    governor.approve()

    # Assert
    captured = capsys.readouterr()
    # Check that each rule is printed
    for rule in Governor.RULES["Coder"]:
        assert rule in captured.out

@pytest.mark.parametrize("stage, allowed_command", [
    (stage, command) 
    for stage, commands in Governor.RULES.items() 
    for command in commands
])
def test_governor_authorizes_allowed_commands(mock_state, stage, allowed_command):
    """Verify that the Governor authorizes all allowed commands for each stage."""
    # Arrange
    mock_state.get.return_value = stage
    governor = Governor(mock_state)
    
    # Act & Assert
    try:
        governor.authorize(allowed_command + " --some-arg") # Test with an argument
    except PermissionError:
        pytest.fail(f"Governor incorrectly denied command '{allowed_command}' for stage '{stage}'.")

def test_governor_denies_forbidden_command(mock_state):
    """Verify that the Governor denies a command that is not allowed."""
    # Arrange
    stage = "Engineer"
    forbidden_command = "git commit -m 'should not be allowed'"
    mock_state.get.return_value = stage
    governor = Governor(mock_state)

    # Act & Assert
    with pytest.raises(PermissionError) as e:
        governor.authorize(forbidden_command)
    
    assert "Action denied" in str(e.value)
