# Research Report: Prompt Augmentation System

This document outlines the plan to implement a prompt augmentation system that enriches user prompts with project context from the MCP Server.

The implementation will involve the following steps:

1. A new `PromptAugmenter` class will be created in a new file, `src/dw6/augmenter.py`. This class will be responsible for fetching context from the MCP server.
2. The `PromptAugmenter` will have an `augment_prompt` method that connects to the MCP server's `/context/state`, `/context/git`, and `/context/requirements` endpoints to fetch the current workflow state, Git status, and meta-requirements.
3. The `new` command in `src/dw6/main.py` will be updated to use the `PromptAugmenter` to enrich the user's new requirement before generating the technical specification.
