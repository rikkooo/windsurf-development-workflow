
# dw6_test_bed_v7 - Cycle 2 - Technical Specification

**Date:** 2025-06-26

## 1. Overview

This cycle is dedicated to validating the critical bug fix for the workflow's state transition logic. The primary goal is to execute a complete, standard development cycle (`Engineer` -> `Coder` -> `Validator` -> `Deployer`) to confirm that the state machine now progresses correctly. This will restore core functionality and confidence in the DW6 protocol.

## 2. Scope

### In Scope

*   Approve the `Engineer` stage and verify the transition to the `Coder` stage.
*   During the `Coder` stage, make a minor, non-functional change to a source file (`src/dw6/main.py`).
*   Create a simple, passing test case in `tests/test_main.py` to satisfy the `Validator` stage requirements.
*   Approve the `Validator` stage and verify the transition to the `Deployer` stage.
*   Satisfy the `Deployer` stage requirements by creating and pushing a new Git tag.
*   Verify that the workflow correctly completes the cycle and advances the `RequirementPointer`.

### Out of Scope

*   Implementing any new features or functional changes.
*   Addressing any other known issues documented in `docs/DW6_ISSUES.md`.
*   Modifying the `Researcher` stage logic.

## 3. System Architecture

No architectural changes are planned for this cycle. The focus is solely on validating the existing workflow logic.

## 4. Data Model

No data model changes are planned for this cycle.

## 5. Functional Requirements

*   **SYS-01:** As the system, I must transition from the `Engineer` stage to the `Coder` stage upon approval.
    *   **Acceptance Criteria:** Running `dw6 approve` in the `Engineer` stage changes the `CurrentStage` to `Coder`.
*   **SYS-02:** As the system, I must successfully complete a full workflow cycle.
    *   **Acceptance Criteria:** The workflow must progress sequentially through `Engineer`, `Coder`, `Validator`, and `Deployer` upon approval of each stage, culminating in the increment of the `RequirementPointer`.

## 6. Implementation Plan

1.  **Approve Engineer Stage:** Run `dw6 approve` to transition from `Engineer` to `Coder`.
2.  **Modify Code:** In the `Coder` stage, add a new comment to the `src/dw6/main.py` file.
3.  **Commit Code Changes:** Commit the modification.
4.  **Approve Coder Stage:** Run `dw6 approve` to generate the deliverable and transition to `Validator`.
5.  **Create Test:** In the `Validator` stage, create a new test file `tests/test_main.py` with a single, simple passing test function (e.g., `def test_placeholder(): assert True`).
6.  **Commit Test:** Commit the new test file.
7.  **Approve Validator Stage:** Run `dw6 approve` to run tests and transition to `Deployer`.
8.  **Create Git Tag:** In the `Deployer` stage, create a new version tag (e.g., `v0.2.0`).
9.  **Push Git Tag:** Push the new tag to the remote repository.
10. **Approve Deployer Stage:** Run `dw6 approve` to complete the cycle.
11. **Verify Final State:** Run `dw6 status` to confirm the `CurrentStage` is `Engineer` and the `RequirementPointer` has been incremented.

## 7. Questions & Assumptions

*   **Assumption:** The fix implemented in `src/dw6/state_manager.py` correctly reorders the stages.
*   **Assumption:** The validation logic for the `Validator` and `Deployer` stages is functioning correctly.

