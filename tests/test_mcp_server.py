# tests/test_mcp_server.py

"""
Tests for the FastAPI-based MCP server.
These tests validate that all endpoints return the expected responses
under various conditions.
"""

import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
from fastapi.testclient import TestClient

from dw6.mcp_server import app, StateProvider, GitProvider, RequirementsProvider


@pytest.fixture
def client():
    """Fixture for creating a TestClient instance."""
    return TestClient(app)


@pytest.fixture
def mock_git_repo():
    """Fixture that provides a mock Git repository."""
    mock_repo = MagicMock()
    mock_repo.active_branch.name = "master"
    
    with patch("dw6.git_handler.get_repo", return_value=mock_repo):
        with patch("dw6.git_handler.is_working_directory_clean", return_value=True):
            with patch("dw6.git_handler.get_latest_commit_hash", return_value="abc123"):
                yield


@pytest.fixture
def mock_git_repo_error():
    """Fixture that simulates an error with the Git repository."""
    with patch("dw6.git_handler.get_repo", side_effect=Exception("Git error")):
        yield


class TestStateProvider:
    def test_get_context_success(self, mocker, tmp_path):
        state_file = tmp_path / "workflow_state.txt"
        state_file.write_text("CurrentStage=Engineer\nRequirementPointer=1")
        
        provider = StateProvider()
        mocker.patch.object(provider, 'state_file', state_file)
        
        context = provider.get_context()
        assert context == {"CurrentStage": "Engineer", "RequirementPointer": "1"}

    def test_get_context_file_not_found(self, mocker, tmp_path):
        provider = StateProvider()
        mocker.patch.object(provider, 'state_file', tmp_path / "non_existent_file.txt")
        
        context = provider.get_context()
        assert "error" in context
        assert context["error"] == "Workflow state file not found."


class TestGitProvider:
    def test_get_context_success(self, mock_git_repo):
        provider = GitProvider()
        context = provider.get_context()
        assert context == {
            "branch": "master",
            "latest_commit": "abc123",
            "status": "clean"
        }

    def test_get_context_with_error(self, mock_git_repo_error):
        provider = GitProvider()
        context = provider.get_context()
        assert "error" in context
        assert "Git repository not found." in context["error"]


class TestRequirementsProvider:
    def test_get_context_success(self, mocker, tmp_path):
        log_file = tmp_path / "meta_requirements.log"
        log_file.write_text("req1\nreq2")
        
        provider = RequirementsProvider()
        mocker.patch.object(provider, 'log_file', log_file)
        
        context = provider.get_context()
        assert "requirements" in context
        assert context["requirements"] == ["req1", "req2"]

    def test_get_context_file_not_found(self, mocker, tmp_path):
        provider = RequirementsProvider()
        mocker.patch.object(provider, 'log_file', tmp_path / "non_existent_file.txt")
        
        context = provider.get_context()
        assert context == {"requirements": []}


@pytest.mark.parametrize("endpoint,expected_keys", [
    ("/context/state", ["CurrentStage", "RequirementPointer"]),
    ("/context/git", ["branch", "latest_commit", "status"]),
    ("/context/requirements", ["requirements"])
])
def test_endpoint_response_structure(client, endpoint, expected_keys, tmp_path, mocker):
    """Test that each endpoint returns responses with the expected structure."""
    # Setup mock files
    state_file = tmp_path / "workflow_state.txt"
    state_file.write_text("CurrentStage=Engineer\nRequirementPointer=1")
    mocker.patch("dw6.mcp_server.state_provider.state_file", state_file)

    req_file = tmp_path / "meta_requirements.log"
    req_file.write_text("req1")
    mocker.patch("dw6.mcp_server.requirements_provider.log_file", req_file)

    # Mock git
    mock_repo = MagicMock()
    mock_repo.active_branch.name = "master"
    mocker.patch("dw6.git_handler.get_repo", return_value=mock_repo)
    mocker.patch("dw6.git_handler.is_working_directory_clean", return_value=True)
    mocker.patch("dw6.git_handler.get_latest_commit_hash", return_value="abc123")

    response = client.get(endpoint)
    assert response.status_code == 200
    
    json_response = response.json()
    if "error" in json_response:
        assert False, f"Unexpected error response: {json_response}"
        
    for key in expected_keys:
        assert key in json_response, f"Expected key '{key}' not found in response"
