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
