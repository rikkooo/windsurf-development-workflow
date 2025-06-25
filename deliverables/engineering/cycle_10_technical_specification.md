# Requirement: 10

## 1. High-Level Goal

Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.

## 2. Guiding Principles

**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
