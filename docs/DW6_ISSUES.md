# DW6 Protocol Issues - dw6_test_bed_v7 Evaluation

This document tracks issues, flaws, and potential improvements discovered during the evaluation of the DW6 protocol.

---

## Cycle 1 Findings (`dw6_test_bed_v7`)

### Setup & Initialization

1.  **Issue: Manual Git Remote Configuration**
    *   **Description:** The workflow requires the user to manually run `git remote add origin ...`. 
    *   **Impact:** Critical. Breaks automation and requires unnecessary user intervention.
    *   **Suggested Fix:** The agent should execute this command automatically using the stored PAT.

2.  **Issue: Manual Environment Activation**
    *   **Description:** The workflow prompts the user to run `source .venv/bin/activate`.
    *   **Impact:** Critical. The agent should manage its own environment.
    *   **Suggested Fix:** Use `uv run` to execute commands within the project's virtual environment, eliminating the need for manual activation.

3.  **Issue: Pre-populated/Dirty Template Files**
    *   **Description:** The DW6 template in `/home/ubuntu/devs/dw/dw6` contains project-specific data from previous test runs (e.g., in `deliverables/engineering/...` and `docs/DW6_ISSUES.md`).
    *   **Impact:** High. It requires the agent to perform cleanup and can lead to confusion.
    *   **Suggested Fix:** The master template must be scrubbed of all project-specific content and be truly generic.

### Workflow Logic

4.  **Issue: Incorrect State Transition from Engineer**
    *   **Description:** After approving the `Engineer` stage, the workflow incorrectly transitions to `Researcher` instead of `Coder`.
    *   **Impact:** Critical. This is a fundamental flaw in the state machine's logic.
    *   **Suggested Fix:** The `_approve_stage` method in `src/dw6/state_manager.py` must be corrected to transition from `Engineer` to `Coder`.

---

## Historical Issues (from `dw6_test_bed_v5`)

*These issues are believed to be resolved but are kept for historical reference.*

- **Environment/Dependency Installation:** Resolved by switching to `uv`.
- **GitHub Integration & Automation:** Resolved by using `github-mcp-server`.
- **Programmatic GitHub Authentication:** Resolved by using PAT in the remote URL.
- **Broken/Silent `status` Command:** Resolved by fixing method calls and adding print statements in `cli.py`.
- **`engineer start` KeyError:** Resolved by fixing the key access in `cli.py`.
- **Confusing Approval Message:** Believed to be resolved by fixing the log message in `state_manager.py`.
