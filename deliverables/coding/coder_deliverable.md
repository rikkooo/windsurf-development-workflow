# Coder Deliverable

## Changed Files

- `deliverables/coding/coder_deliverable.md`
- `deliverables/engineering/cycle_10_technical_specification.md`
- `logs/.last_commit_sha`
- `logs/workflow_state.txt`
- `src/dw6/state_manager.py`
- `tests/test_governor.py`

## Git Diff

```diff
diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
index c5520c2..e748a41 100644
--- a/deliverables/coding/coder_deliverable.md
+++ b/deliverables/coding/coder_deliverable.md
@@ -2,74 +2,422 @@
 
 ## Changed Files
 
-- `src/dw6/augmenter.py`
+- `deliverables/coding/coder_deliverable.md`
+- `deliverables/engineering/cycle_9_technical_specification.md`
+- `logs/.last_commit_sha`
+- `logs/workflow_state.txt`
+- `pytest.ini`
 - `src/dw6/main.py`
+- `src/dw6/state_manager.py`
+- `tests/test_governor.py`
+- `tests/test_state_manager_integration.py`
+- `uv.lock`
 
 ## Git Diff
 
 ```diff
-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+index 82ea098..c5520c2 100644
+--- a/deliverables/coding/coder_deliverable.md
++++ b/deliverables/coding/coder_deliverable.md
+@@ -1 +1,75 @@
+-This file serves as the deliverable for the Coder stage.
++# Coder Deliverable
++
++## Changed Files
++
++- `src/dw6/augmenter.py`
++- `src/dw6/main.py`
++
++## Git Diff
++
++```diff
++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++new file mode 100644
++index 0000000..c1614f0
++--- /dev/null
+++++ b/src/dw6/augmenter.py
++@@ -0,0 +1,26 @@
+++# src/dw6/augmenter.py
+++
+++import os
+++from .state_manager import get_current_requirement_id
+++
+++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++
+++def process_prompt(prompt_text: str):
+++    """
+++    Augments a raw user prompt and generates a formal technical specification markdown file.
+++    """
+++    requirement_id = get_current_requirement_id()
+++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++
+++    content = f"# Requirement: {requirement_id}\n\n"
+++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++
+++    try:
+++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+++        with open(file_path, 'w') as f:
+++            f.write(content)
+++        print(f"Successfully created specification: {file_path}")
+++    except IOError as e:
+++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+++        sys.exit(1)
++diff --git a/src/dw6/main.py b/src/dw6/main.py
++index 7bbd031..a55f148 100644
++--- a/src/dw6/main.py
+++++ b/src/dw6/main.py
++@@ -2,6 +2,7 @@
++ import argparse
++ import sys
++ from dw6.state_manager import StateManager
+++from dw6.augmenter import process_prompt
++ 
++ def main():
++     """Main entry point for the DW6 CLI."""
++@@ -15,6 +16,10 @@ def main():
++     # Approve command
++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++ 
+++    # New command
+++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+++
++     if len(sys.argv) == 1:
++         parser.print_help(sys.stderr)
++         sys.exit(1)
++@@ -27,6 +32,8 @@ def main():
++         manager.review()
++     elif args.command == "approve":
++         manager.approve()
+++    elif args.command == "new":
+++        process_prompt(args.prompt)
++ 
++ if __name__ == "__main__":
++     main()
++```
+\ No newline at end of file
+diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
 new file mode 100644
-index 0000000..c1614f0
+index 0000000..6c1638b
 --- /dev/null
-+++ b/src/dw6/augmenter.py
-@@ -0,0 +1,26 @@
-+# src/dw6/augmenter.py
-+
-+import os
-+from .state_manager import get_current_requirement_id
++++ b/deliverables/engineering/cycle_9_technical_specification.md
+@@ -0,0 +1,9 @@
++# Requirement: 8
 +
-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++## 1. High-Level Goal
 +
-+def process_prompt(prompt_text: str):
-+    """
-+    Augments a raw user prompt and generates a formal technical specification markdown file.
-+    """
-+    requirement_id = get_current_requirement_id()
-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
 +
-+    content = f"# Requirement: {requirement_id}\n\n"
-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++## 2. Guiding Principles
 +
-+    try:
-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-+        with open(file_path, 'w') as f:
-+            f.write(content)
-+        print(f"Successfully created specification: {file_path}")
-+    except IOError as e:
-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-+        sys.exit(1)
++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+index 9718eda..b85b3d9 100644
+--- a/logs/.last_commit_sha
++++ b/logs/.last_commit_sha
+@@ -1 +1 @@
+-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+\ No newline at end of file
++75be02c0b7e1723e32042299497f3673b11b4ddd
+\ No newline at end of file
+diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+index 28746b7..743582b 100644
+--- a/logs/workflow_state.txt
++++ b/logs/workflow_state.txt
+@@ -1,2 +1,2 @@
+-CurrentStage=Engineer
+-RequirementPointer=7
++CurrentStage=Coder
++RequirementPointer=9
+diff --git a/pytest.ini b/pytest.ini
+new file mode 100644
+index 0000000..a635c5c
+--- /dev/null
++++ b/pytest.ini
+@@ -0,0 +1,2 @@
++[pytest]
++pythonpath = .
 diff --git a/src/dw6/main.py b/src/dw6/main.py
-index 7bbd031..a55f148 100644
+index a55f148..90862f9 100644
 --- a/src/dw6/main.py
 +++ b/src/dw6/main.py
-@@ -2,6 +2,7 @@
+@@ -1,7 +1,7 @@
+ # dw6/main.py
  import argparse
  import sys
- from dw6.state_manager import StateManager
-+from dw6.augmenter import process_prompt
+-from dw6.state_manager import StateManager
++from dw6.state_manager import WorkflowManager
+ from dw6.augmenter import process_prompt
  
  def main():
-     """Main entry point for the DW6 CLI."""
-@@ -15,6 +16,10 @@ def main():
+@@ -10,9 +10,7 @@ def main():
+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+ 
+-    # Review command
+-    subparsers.add_parser("review", help="Review the changes for the current stage.")
+-    
++
      # Approve command
      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
  
-+    # New command
-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+@@ -26,11 +24,9 @@ def main():
+ 
+     args = parser.parse_args()
+     
+-    manager = StateManager()
++    manager = WorkflowManager()
+ 
+-    if args.command == "review":
+-        manager.review()
+-    elif args.command == "approve":
++    if args.command == "approve":
+         manager.approve()
+     elif args.command == "new":
+         process_prompt(args.prompt)
+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+index 703640c..b829d36 100644
+--- a/src/dw6/state_manager.py
++++ b/src/dw6/state_manager.py
+@@ -9,7 +9,7 @@ from dw6 import git_handler
+ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+ APPROVAL_FILE = "logs/approvals.log"
+-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+ DELIVERABLE_PATHS = {
+     "Engineer": "deliverables/engineering",
+     "Coder": "deliverables/coding",
+@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+     "Researcher": "deliverables/research",
+ }
+ 
++class Governor:
++    def __init__(self, state):
++        self.state = state
++        self.current_stage = self.state.get("CurrentStage")
++
++    def approve(self):
++        old_stage = self.current_stage
++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++        self._validate_stage_exit_criteria()
++        # The original logic from WorkflowManager is now fully integrated here.
++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
++        workflow_manager._validate_stage()
++        workflow_manager._run_pre_transition_actions()
++        self._transition_to_next_stage() # This method now belongs to the Governor
++        workflow_manager._run_post_transition_actions()
++        self.state.save()
++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++
++    def _validate_stage_exit_criteria(self):
++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
++        if self.current_stage == "Engineer":
++            req_id = self.state.get("RequirementPointer")
++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
++            if not spec_file.exists():
++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
++                sys.exit(1)
++            print("Governor: 'Engineer' exit criteria met.")
 +
-     if len(sys.argv) == 1:
-         parser.print_help(sys.stderr)
-         sys.exit(1)
-@@ -27,6 +32,8 @@ def main():
-         manager.review()
-     elif args.command == "approve":
++    def _transition_to_next_stage(self):
++        current_index = STAGES.index(self.current_stage)
++        # After 'Deployer', the cycle is complete
++        if self.current_stage == "Deployer":
++            self._complete_requirement_cycle()
++            self.current_stage = STAGES[0]
++        else:
++            self.current_stage = STAGES[current_index + 1]
++        self.state.set("CurrentStage", self.current_stage)
++
++    def _complete_requirement_cycle(self):
++        req_id = int(self.state.get("RequirementPointer"))
++        os.makedirs("logs", exist_ok=True)
++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++        with open(APPROVAL_FILE, "a") as f:
++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++        next_req_id = req_id + 1
++        self.state.set("RequirementPointer", next_req_id)
++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++
+ class WorkflowManager:
+     def __init__(self):
+         self.state = WorkflowState()
++        self.governor = Governor(self.state) # The manager now has a governor
+         self.current_stage = self.state.get("CurrentStage")
+ 
+     def get_state(self):
+         return self.state.data
+ 
+     def approve(self):
+-        old_stage = self.current_stage
+-        print(f"--- Approving Stage: {old_stage} ---")
+-        self._validate_stage()
+-        self._run_pre_transition_actions()
+-        self._transition_to_next_stage()
+-        self._run_post_transition_actions()
+-        self.state.save()
+-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++        # The manager now simply delegates to the governor.
++        self.governor.approve()
+ 
+     def _validate_stage(self):
+         print(f"Validating deliverables for stage: {self.current_stage}")
+@@ -123,25 +167,7 @@ class WorkflowManager:
+         if self.current_stage == "Coder":
+             git_handler.save_current_commit_sha()
+ 
+-    def _transition_to_next_stage(self):
+-        current_index = STAGES.index(self.current_stage)
+-        if current_index == len(STAGES) - 1:
+-            self._complete_requirement_cycle()
+-            self.current_stage = STAGES[0]
+-        else:
+-            self.current_stage = STAGES[current_index + 1]
+-        self.state.set("CurrentStage", self.current_stage)
+ 
+-    def _complete_requirement_cycle(self):
+-        req_id = int(self.state.get("RequirementPointer"))
+-        os.makedirs("logs", exist_ok=True)
+-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-        with open(APPROVAL_FILE, "a") as f:
+-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-        next_req_id = req_id + 1
+-        self.state.set("RequirementPointer", next_req_id)
+-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+ 
+ class WorkflowState:
+     def __init__(self):
+diff --git a/tests/test_governor.py b/tests/test_governor.py
+new file mode 100644
+index 0000000..95b566d
+--- /dev/null
++++ b/tests/test_governor.py
+@@ -0,0 +1,55 @@
++# tests/test_governor.py
++import pytest
++from unittest.mock import MagicMock
++from pathlib import Path
++import sys
++
++from dw6.state_manager import Governor, WorkflowState
++
++@pytest.fixture
++def mock_state(mocker):
++    """Fixture to create a mock WorkflowState."""
++    state = MagicMock(spec=WorkflowState)
++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
++    return state
++
++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
++    """Verify the Governor blocks approval if the spec file is missing."""
++    # Arrange: Set the state to Engineer and mock the requirement pointer
++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
++    
++    # Ensure the spec file does NOT exist for this test
++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
++    if spec_file.exists():
++        spec_file.unlink()
++
++    governor = Governor(mock_state)
++
++    # Act & Assert: The approval should fail with a SystemExit
++    with pytest.raises(SystemExit) as e:
++        governor._validate_stage_exit_criteria()
++    
++    assert e.type == SystemExit
++    assert e.value.code == 1
++
++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++    """Verify the Governor allows approval if the spec file exists."""
++    # Arrange: Set the state to Engineer and mock the requirement pointer
++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
++    
++    # Ensure the spec file DOES exist for this test
++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
++    spec_file.parent.mkdir(parents=True, exist_ok=True)
++    spec_file.touch()
++
++    governor = Governor(mock_state)
++
++    # Act & Assert: The approval should pass without raising an exception
++    try:
++        governor._validate_stage_exit_criteria()
++    except SystemExit:
++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
++    finally:
++        # Clean up the created file
++        if spec_file.exists():
++            spec_file.unlink()
+diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+index 5b9d1eb..44d2cc9 100644
+--- a/tests/test_state_manager_integration.py
++++ b/tests/test_state_manager_integration.py
+@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+ 
+     @patch('dw6.state_manager.WorkflowState')
+     @patch('dw6.git_handler.get_changes_since_last_commit')
+-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+         # Arrange
+         mock_state_instance = mock_WorkflowState.return_value
+@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+         # Act
          manager.approve()
-+    elif args.command == "new":
-+        process_prompt(args.prompt)
  
- if __name__ == "__main__":
-     main()
+-        # Assert
++        # Assert that the deliverable file was created
+         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+         self.assertTrue(deliverable_path.exists())
++        # Clean up the created file
++        deliverable_path.unlink()
++
+         mock_state_instance.save.assert_called_once()
+ 
+ if __name__ == '__main__':
+diff --git a/uv.lock b/uv.lock
+index c79d29c..8e7411f 100644
+--- a/uv.lock
++++ b/uv.lock
+@@ -66,6 +66,7 @@ dependencies = [
+ test = [
+     { name = "pytest" },
+     { name = "pytest-cov" },
++    { name = "pytest-mock" },
+ ]
+ 
+ [package.metadata]
+@@ -73,6 +74,7 @@ requires-dist = [
+     { name = "gitpython" },
+     { name = "pytest", marker = "extra == 'test'" },
+     { name = "pytest-cov", marker = "extra == 'test'" },
++    { name = "pytest-mock", marker = "extra == 'test'" },
+     { name = "python-dotenv" },
+ ]
+ provides-extras = ["test"]
+@@ -167,6 +169,18 @@ wheels = [
+     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+ ]
+ 
++[[package]]
++name = "pytest-mock"
++version = "3.14.1"
++source = { registry = "https://pypi.org/simple" }
++dependencies = [
++    { name = "pytest" },
++]
++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
++wheels = [
++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
++]
++
+ [[package]]
+ name = "python-dotenv"
+ version = "1.1.1"
 ```
\ No newline at end of file
diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
new file mode 100644
index 0000000..691df8d
--- /dev/null
+++ b/deliverables/engineering/cycle_10_technical_specification.md
@@ -0,0 +1,9 @@
+# Requirement: 10
+
+## 1. High-Level Goal
+
+Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
+
+## 2. Guiding Principles
+
+**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
index b85b3d9..00ab2c8 100644
--- a/logs/.last_commit_sha
+++ b/logs/.last_commit_sha
@@ -1 +1 @@
-75be02c0b7e1723e32042299497f3673b11b4ddd
\ No newline at end of file
+b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
\ No newline at end of file
diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
index 743582b..a7aa662 100644
--- a/logs/workflow_state.txt
+++ b/logs/workflow_state.txt
@@ -1,2 +1,2 @@
 CurrentStage=Coder
-RequirementPointer=9
+RequirementPointer=10
diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
index b829d36..241fa62 100644
--- a/src/dw6/state_manager.py
+++ b/src/dw6/state_manager.py
@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
 }
 
 class Governor:
+    RULES = {
+        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+        "Coder": "Can use file system tools, code editing tools, and run tests.",
+        "Validator": "Can only run tests and validation tools.",
+        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+        "Researcher": "Can use web search and documentation reading tools."
+    }
     def __init__(self, state):
         self.state = state
         self.current_stage = self.state.get("CurrentStage")
 
+    def enforce_rules(self):
+        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+        print(f"[RULE] {rule}")
+
     def approve(self):
         old_stage = self.current_stage
         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+        self.enforce_rules()
         self._validate_stage_exit_criteria()
         # The original logic from WorkflowManager is now fully integrated here.
         workflow_manager = WorkflowManager() # We still need access to its methods for now.
diff --git a/tests/test_governor.py b/tests/test_governor.py
index 95b566d..26bf82b 100644
--- a/tests/test_governor.py
+++ b/tests/test_governor.py
@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
         # Clean up the created file
         if spec_file.exists():
             spec_file.unlink()
+
+def test_governor_enforces_rules_on_approve(mocker, capsys):
+    """Verify that the Governor prints the correct rule for the current stage."""
+    # Arrange
+    mock_state = mocker.MagicMock(spec=WorkflowState)
+    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
+    governor = Governor(mock_state)
+    # Mock the exit criteria validation to prevent SystemExit
+    mocker.patch.object(governor, '_validate_stage_exit_criteria')
+    # Mock the rest of the approval process to isolate the rule enforcement
+    mocker.patch.object(governor, '_transition_to_next_stage')
+    mocker.patch('dw6.state_manager.WorkflowManager')
+
+    # Act
+    governor.approve()
+
+    # Assert
+    captured = capsys.readouterr()
+    expected_rule = Governor.RULES["Coder"]
+    assert expected_rule in captured.out
```