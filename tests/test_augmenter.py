# tests/test_augmenter.py

import os
import pytest
from src.dw6.augmenter import process_prompt, WORKING_PHILOSOPHY

# It's good practice to mock dependencies like this to isolate tests.
@pytest.fixture
def mock_workflow_state(mocker):
    """Fixture to mock the WorkflowState and its get method."""
    # We target 'src.dw6.augmenter.WorkflowState' because that's where it's imported and used.
    mock_state = mocker.patch('src.dw6.augmenter.WorkflowState', autospec=True)
    mock_instance = mock_state.return_value
    mock_instance.get.return_value = '999' # Use a consistent mock requirement ID
    return mock_instance

@pytest.fixture
def cleanup_spec_file():
    """Fixture to clean up the generated spec file after the test runs."""
    yield
    # Use the same mock requirement ID for cleanup to ensure we delete the correct file.
    file_path = f"deliverables/engineering/cycle_999_technical_specification.md"
    if os.path.exists(file_path):
        os.remove(file_path)

def test_process_prompt_creates_file_with_correct_content(mock_workflow_state, cleanup_spec_file):
    """Tests that process_prompt creates the spec file with the correct content."""
    # Arrange
    test_prompt = "This is a test prompt for the augmenter."
    requirement_id = '999' # Use the same mock ID as the fixture
    expected_file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"

    # Act
    process_prompt(test_prompt)

    # Assert
    assert os.path.exists(expected_file_path), "Specification file was not created."

    with open(expected_file_path, 'r') as f:
        content = f.read()

    assert f"# Requirement: {requirement_id}" in content
    assert f"## 1. High-Level Goal\n\n{test_prompt}" in content
    assert f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}" in content
