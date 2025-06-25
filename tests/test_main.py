# tests/test_main.py
import pytest
from pathlib import Path
import re
from dw6.main import register_meta_requirement, META_LOG_FILE

@pytest.fixture(autouse=True)
def cleanup_log_file():
    """Fixture to clean up the meta log file before and after a test."""
    if META_LOG_FILE.exists():
        META_LOG_FILE.unlink()
    yield
    if META_LOG_FILE.exists():
        META_LOG_FILE.unlink()

def test_register_meta_requirement_creates_file_and_logs_entry():
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

def test_register_meta_requirement_increments_id():
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
