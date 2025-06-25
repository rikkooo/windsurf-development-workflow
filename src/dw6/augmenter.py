# src/dw6/augmenter.py

import os
import sys
from .state_manager import WorkflowState

WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""

def process_prompt(prompt_text: str):
    """
    Augments a raw user prompt and generates a formal technical specification markdown file.
    """
    state = WorkflowState()
    requirement_id = state.get("RequirementPointer")
    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"

    content = f"# Requirement: {requirement_id}\n\n"
    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"

    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Successfully created specification: {file_path}")
    except IOError as e:
        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
        sys.exit(1)
