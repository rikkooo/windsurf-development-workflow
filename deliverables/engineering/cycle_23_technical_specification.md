# Requirement: 23

## 1. High-Level Goal

Improve the DW6 workflow

## 2. Guiding Principles

**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.

# Technical Specification: Fix Coder Stage Deliverable Generation

## 1. Problem

The `test_approve_coder_stage_creates_deliverable` test in `tests/test_state_manager_integration.py` is failing. This is because the `WorkflowManager.approve()` method does not generate a deliverable file when transitioning out of the `Coder` stage. The `_run_post_transition_actions` method is called, but it currently only saves the commit SHA and does not create the deliverable file.

## 2. Proposed Solution

I will modify the `_run_post_transition_actions` method in `src/dw6/state_manager.py`. I will add logic to check if the current stage is `Coder`. If it is, the method will:

1.  Get the changes since the last commit using `git_handler.get_changes_since_last_commit()`.
2.  Create a markdown-formatted deliverable containing the diff of the changes.
3.  Save this deliverable to the `deliverables/coding/` directory.

This will ensure that a record of the work done in the `Coder` stage is created upon approval, which will fix the failing test.
