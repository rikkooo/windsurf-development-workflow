# tests/conftest.py

"""
Shared fixtures for the DW6 test suite.
This file contains pytest fixtures that can be reused across multiple test files.
"""

import pytest
import os
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock

from fastapi.testclient import TestClient
from dw6.mcp_server import app


@pytest.fixture(scope="session")
def client():
    """
    Create a TestClient instance for the FastAPI application.
    This fixture has session scope to improve test performance.
    """
    return TestClient(app)


@pytest.fixture
def temp_file():
    """
    Create a temporary file for testing.
    The file is automatically deleted after the test completes.
    """
    fd, path = tempfile.mkstemp()
    try:
        yield Path(path)
    finally:
        os.close(fd)
        os.unlink(path)


@pytest.fixture
def temp_dir():
    """
    Create a temporary directory for testing.
    The directory is automatically deleted after the test completes.
    """
    with tempfile.TemporaryDirectory() as tmpdirname:
        yield Path(tmpdirname)


@pytest.fixture
def mock_workflow_state():
    """
    Create a mock workflow state for testing.
    
    Returns a tuple of (stage, requirement) that can be used to
    configure the mock state file.
    """
    return ("Coder", "23")


@pytest.fixture
def setup_workflow_state_file(temp_file, mock_workflow_state):
    """
    Set up a workflow state file with mock content.
    
    Args:
        temp_file: A temporary file path
        mock_workflow_state: A tuple of (stage, requirement)
    
    Returns:
        Path to the temporary workflow state file
    """
    stage, req = mock_workflow_state
    content = f"CurrentStage: {stage}\nRequirementPointer: {req}"
    temp_file.write_text(content)
    return temp_file


@pytest.fixture
def mock_git_context():
    """
    Create mock Git context information for testing.
    
    Returns:
        Dictionary with mock Git context values
    """
    return {
        "branch": "master",
        "latest_commit": "abc123",
        "status": "clean"
    }


@pytest.fixture
def mock_meta_requirements():
    """
    Create mock meta-requirements for testing.
    
    Returns:
        List of mock meta-requirements
    """
    return [
        "[ID:1] [TS:2025-06-26 03:27:28 UTC] Design and implement a maintenance mode",
        "[ID:2] [TS:2025-06-26 03:30:45 UTC] Add comprehensive tests for all components"
    ]


@pytest.fixture
def setup_meta_requirements_file(temp_file, mock_meta_requirements):
    """
    Set up a meta-requirements log file with mock content.
    
    Args:
        temp_file: A temporary file path
        mock_meta_requirements: List of meta-requirement strings
    
    Returns:
        Path to the temporary meta-requirements file
    """
    content = "\n".join(mock_meta_requirements)
    temp_file.write_text(content)
    return temp_file
