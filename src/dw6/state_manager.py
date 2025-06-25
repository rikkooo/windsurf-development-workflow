import re
import sys
import os
import subprocess
from pathlib import Path
from datetime import datetime, timezone
from dw6 import git_handler

MASTER_FILE = "docs/WORKFLOW_MASTER.md"
REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
APPROVAL_FILE = "logs/approvals.log"
STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
DELIVERABLE_PATHS = {
    "Engineer": "deliverables/engineering",
    "Coder": "deliverables/coding",
    "Validator": "deliverables/testing",
    "Deployer": "deliverables/deployment",
    "Researcher": "deliverables/research",
}

class Governor:
    def __init__(self, state):
        self.state = state
        self.current_stage = self.state.get("CurrentStage")

    def approve(self):
        old_stage = self.current_stage
        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
        self._validate_stage_exit_criteria()
        # The original logic from WorkflowManager is now fully integrated here.
        workflow_manager = WorkflowManager() # We still need access to its methods for now.
        workflow_manager._validate_stage()
        workflow_manager._run_pre_transition_actions()
        self._transition_to_next_stage() # This method now belongs to the Governor
        workflow_manager._run_post_transition_actions()
        self.state.save()
        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")

    def _validate_stage_exit_criteria(self):
        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
        if self.current_stage == "Engineer":
            req_id = self.state.get("RequirementPointer")
            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
            if not spec_file.exists():
                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
                sys.exit(1)
            print("Governor: 'Engineer' exit criteria met.")

    def _transition_to_next_stage(self):
        current_index = STAGES.index(self.current_stage)
        # After 'Deployer', the cycle is complete
        if self.current_stage == "Deployer":
            self._complete_requirement_cycle()
            self.current_stage = STAGES[0]
        else:
            self.current_stage = STAGES[current_index + 1]
        self.state.set("CurrentStage", self.current_stage)

    def _complete_requirement_cycle(self):
        req_id = int(self.state.get("RequirementPointer"))
        os.makedirs("logs", exist_ok=True)
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        with open(APPROVAL_FILE, "a") as f:
            f.write(f"Requirement {req_id} approved at {timestamp}\n")
        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
        next_req_id = req_id + 1
        self.state.set("RequirementPointer", next_req_id)
        print(f"[INFO] Advanced to next requirement: {next_req_id}.")

class WorkflowManager:
    def __init__(self):
        self.state = WorkflowState()
        self.governor = Governor(self.state) # The manager now has a governor
        self.current_stage = self.state.get("CurrentStage")

    def get_state(self):
        return self.state.data

    def approve(self):
        # The manager now simply delegates to the governor.
        self.governor.approve()

    def _validate_stage(self):
        print(f"Validating deliverables for stage: {self.current_stage}")
        if self.current_stage == "Coder":
            self._generate_coder_deliverable()
        elif self.current_stage == "Validator":
            self._validate_tests()
        elif self.current_stage == "Deployer":
            self._validate_deployment()
        print("Stage validation successful.")

    def _generate_coder_deliverable(self):
        print("Generating Coder deliverable...")
        changed_files, diff_string = git_handler.get_changes_since_last_commit()
        if not changed_files:
            print("No changes detected since the start of the Coder stage.")
            return
        deliverable_path = Path("deliverables/coding/coder_deliverable.md")
        deliverable_path.parent.mkdir(parents=True, exist_ok=True)
        with open(deliverable_path, "w") as f:
            f.write("# Coder Deliverable\n\n")
            f.write("## Changed Files\n\n")
            for file_path in changed_files:
                f.write(f"- `{file_path}`\n")
            f.write("\n## Git Diff\n\n")
            f.write("```diff\n")
            f.write(diff_string)
            f.write("\n```")
        print(f"Coder deliverable created at: {deliverable_path}")

    def _validate_tests(self):
        print("Running test validation...")
        tests_dir = Path("tests")
        if not tests_dir.is_dir() or not any(tests_dir.glob("test_*.py")):
            print("ERROR: No test files found in the 'tests' directory.", file=sys.stderr)
            sys.exit(1)
        try:
            # Use sys.executable to ensure we're using the python from the current venv
            python_executable = sys.executable
            collect_result = subprocess.run([python_executable, "-m", "pytest", "--collect-only"], capture_output=True, text=True, check=True)
            if "no tests collected" in collect_result.stdout.lower():
                print("ERROR: Pytest collected no tests.", file=sys.stderr)
                print(collect_result.stdout, file=sys.stderr)
                sys.exit(1)
            match = re.search(r"collected (\d+) items", collect_result.stdout)
            if not match or int(match.group(1)) == 0:
                print("ERROR: Pytest collected no tests.", file=sys.stderr)
                print(collect_result.stdout, file=sys.stderr)
                sys.exit(1)
            print(f"Pytest collected {match.group(1)} tests. Running them now...")
            result = subprocess.run([python_executable, "-m", "pytest"], capture_output=True, text=True)
            if result.returncode != 0:
                print("Pytest validation failed:", file=sys.stderr)
                print(result.stdout, file=sys.stderr)
                print(result.stderr, file=sys.stderr)
                sys.exit(1)
            print("Pytest validation successful.")
        except (FileNotFoundError, subprocess.CalledProcessError):
            print("ERROR: pytest command not found or failed to run. Is it installed in your venv?", file=sys.stderr)
            sys.exit(1)

    def _validate_deployment(self):
        print("Validating deployment...")
        if not git_handler.is_github_token_present():
            sys.exit(1)
        latest_commit = git_handler.get_latest_commit_hash()
        all_remote_tags = git_handler.get_remote_tags_with_commits()
        if all_remote_tags is None:
            all_remote_tags = {}
        matching_tags = [tag for tag, commit in all_remote_tags.items() if commit == latest_commit]
        if not matching_tags:
            print("Warning: Could not retrieve remote tags. Falling back to local tag check.")
            local_tags = git_handler.get_local_tags_for_commit(latest_commit)
            if not local_tags:
                print(f"ERROR: The latest commit ({latest_commit[:7]}) has not been tagged.", file=sys.stderr)
                sys.exit(1)
            matching_tags = local_tags
        print(f"Deployment validation successful: Latest commit is tagged with: {', '.join(matching_tags)}.")
        print("Pushing changes to remote repository...")
        git_handler.push_to_remote()

    def _run_pre_transition_actions(self):
        pass

    def _run_post_transition_actions(self):
        if self.current_stage == "Coder":
            git_handler.save_current_commit_sha()



class WorkflowState:
    def __init__(self):
        self.state_file = Path("logs/workflow_state.txt")
        self.data = {}
        if self.state_file.exists():
            with open(self.state_file, "r") as f:
                for line in f:
                    key, value = line.strip().split("=", 1)
                    self.data[key] = value
        else:
            self.initialize_state()

    def initialize_state(self):
        self.data = {
            "CurrentStage": "Engineer",
            "RequirementPointer": "1"
        }
        self.save()

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = str(value)

    def save(self):
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_file, "w") as f:
            for key, value in self.data.items():
                f.write(f"{key}={value}\n")
