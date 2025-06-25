# src/dw6/mcp_server.py

"""
DW6 Context Engineering Server

This server implements the Model Context Protocol (MCP) to provide rich,
real-time context about the dw6_test_bed_v7 project to an MCP client
(e.g., the Cascade AI assistant).
"""

import asyncio
from pathlib import Path
from fastapi import FastAPI
import uvicorn
from dw6 import git_handler

# Placeholder for actual MCP server implementation from an SDK

class StateProvider:
    """Provides context about the current workflow state."""
    def __init__(self):
        self.state_file = Path("logs/workflow_state.txt")

    def get_context(self):
        """Reads the current state from the log file."""
        if not self.state_file.exists():
            return {"error": "Workflow state file not found."}
        
        content = self.state_file.read_text().strip().split('\n')
        state = {}
        for line in content:
            if '=' in line:
                key, value = line.split('=', 1)
                state[key] = value
            elif ': ' in line:
                key, value = line.split(': ', 1)
                state[key] = value
        return state

class GitProvider:
    """Provides context from the git repository."""
    def __init__(self):
        try:
            self.repo = git_handler.get_repo()
        except (SystemExit, Exception) as e:
            self.repo = None

    def get_context(self):
        """Returns key information from git."""
        if not self.repo:
            return {"error": "Git repository not found."}
            
        try:
            status = "clean" if git_handler.is_working_directory_clean() else "dirty"
            return {
                "branch": self.repo.active_branch.name,
                "latest_commit": git_handler.get_latest_commit_hash(),
                "status": status
            }
        except (SystemExit, Exception) as e:
            return {"error": f"Git repository error: {str(e)}"}

class RequirementsProvider:
    """Provides context from the meta-requirements log."""
    def __init__(self):
        self.log_file = Path("logs/meta_requirements.log")

    def get_context(self):
        """Reads the meta-requirements from the log file."""
        if not self.log_file.exists():
            return {"requirements": []}
        
        return {"requirements": self.log_file.read_text().strip().split('\n')}


# --- FastAPI Server Setup ---

app = FastAPI(
    title="DW6 MCP Server",
    description="Provides project context to AI assistants via the Model Context Protocol.",
    version="1.0.0"
)

# Instantiate providers
state_provider = StateProvider()
git_provider = GitProvider()
requirements_provider = RequirementsProvider()

@app.get("/", summary="Root endpoint providing server info")
def read_root():
    return {"message": "DW6 MCP Server is running."}

@app.get("/context/state", summary="Get workflow state")
def get_state_context():
    return state_provider.get_context()

@app.get("/context/git", summary="Get Git repository context")
def get_git_context():
    return git_provider.get_context()

@app.get("/context/requirements", summary="Get meta-requirements")
def get_requirements_context():
    return requirements_provider.get_context()


if __name__ == "__main__":
    print("Starting DW6 MCP Server...")
    print("Access the interactive API docs at http://127.0.0.1:8000/docs")
    uvicorn.run(app, host="127.0.0.1", port=8000)