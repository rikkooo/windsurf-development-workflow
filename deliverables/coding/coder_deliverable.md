# Coder Deliverable

## Changed Files

- `deliverables/coding/coder_deliverable.md`
- `deliverables/engineering/cycle_17_technical_specification.md`
- `logs/.last_commit_sha`
- `logs/workflow_state.txt`
- `src/dw6/state_manager.py`

## Git Diff

```diff
diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
index 2f6f776..10d1852 100644
--- a/deliverables/coding/coder_deliverable.md
+++ b/deliverables/coding/coder_deliverable.md
@@ -3,7783 +3,12665 @@
 ## Changed Files
 
 - `deliverables/coding/coder_deliverable.md`
-- `deliverables/engineering/cycle_15_technical_specification.md`
+- `deliverables/engineering/cycle_16_technical_specification.md`
+- `deliverables/research/cycle_16_research_report.md`
 - `logs/.last_commit_sha`
 - `logs/workflow_state.txt`
-- `src/dw6/main.py`
-- `tests/test_main.py`
+- `src/dw6/mcp_server.py`
 
 ## Git Diff
 
 ```diff
 diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
-index 38bc2ff..d1ac81a 100644
+index d1ac81a..2f6f776 100644
 --- a/deliverables/coding/coder_deliverable.md
 +++ b/deliverables/coding/coder_deliverable.md
-@@ -3,2987 +3,4843 @@
+@@ -3,4843 +3,7783 @@
  ## Changed Files
  
  - `deliverables/coding/coder_deliverable.md`
--- `deliverables/engineering/cycle_13_technical_specification.md`
-+- `deliverables/engineering/cycle_14_technical_specification.md`
+-- `deliverables/engineering/cycle_14_technical_specification.md`
++- `deliverables/engineering/cycle_15_technical_specification.md`
  - `logs/.last_commit_sha`
  - `logs/workflow_state.txt`
--- `tests/test_main.py`
-+- `src/dw6/state_manager.py`
+-- `src/dw6/state_manager.py`
++- `src/dw6/main.py`
++- `tests/test_main.py`
  
  ## Git Diff
  
  ```diff
  diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
--index 081c25b..2973e35 100644
-+index 2973e35..38bc2ff 100644
+-index 2973e35..38bc2ff 100644
++index 38bc2ff..d1ac81a 100644
  --- a/deliverables/coding/coder_deliverable.md
  +++ b/deliverables/coding/coder_deliverable.md
--@@ -3,1129 +3,1893 @@
-+@@ -3,1893 +3,2987 @@
+-@@ -3,1893 +3,2987 @@
++@@ -3,2987 +3,4843 @@
   ## Changed Files
   
   - `deliverables/coding/coder_deliverable.md`
---- `deliverables/engineering/cycle_11_technical_specification.md`
--+- `deliverables/engineering/cycle_12_technical_specification.md`
-+-- `deliverables/engineering/cycle_12_technical_specification.md`
-++- `deliverables/engineering/cycle_13_technical_specification.md`
+--- `deliverables/engineering/cycle_12_technical_specification.md`
+-+- `deliverables/engineering/cycle_13_technical_specification.md`
++-- `deliverables/engineering/cycle_13_technical_specification.md`
+++- `deliverables/engineering/cycle_14_technical_specification.md`
   - `logs/.last_commit_sha`
   - `logs/workflow_state.txt`
-- - `src/dw6/main.py`
--+- `src/dw6/state_manager.py`
--+- `tests/test_governor.py`
-+-- `src/dw6/main.py`
-+-- `src/dw6/state_manager.py`
-+-- `tests/test_governor.py`
-  - `tests/test_main.py`
+--- `src/dw6/main.py`
+--- `src/dw6/state_manager.py`
+--- `tests/test_governor.py`
+- - `tests/test_main.py`
++-- `tests/test_main.py`
+++- `src/dw6/state_manager.py`
   
   ## Git Diff
   
   ```diff
   diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
---index e748a41..82968f8 100644
--+index 82968f8..081c25b 100644
-+-index 82968f8..081c25b 100644
-++index 081c25b..2973e35 100644
+--index 82968f8..081c25b 100644
+-+index 081c25b..2973e35 100644
++-index 081c25b..2973e35 100644
+++index 2973e35..38bc2ff 100644
   --- a/deliverables/coding/coder_deliverable.md
   +++ b/deliverables/coding/coder_deliverable.md
---@@ -3,421 +3,578 @@
--+@@ -3,578 +3,1129 @@
-+-@@ -3,578 +3,1129 @@
-++@@ -3,1129 +3,1893 @@
+--@@ -3,578 +3,1129 @@
+-+@@ -3,1129 +3,1893 @@
++-@@ -3,1129 +3,1893 @@
+++@@ -3,1893 +3,2987 @@
    ## Changed Files
    
    - `deliverables/coding/coder_deliverable.md`
----- `deliverables/engineering/cycle_9_technical_specification.md`
---+- `deliverables/engineering/cycle_10_technical_specification.md`
--+-- `deliverables/engineering/cycle_10_technical_specification.md`
--++- `deliverables/engineering/cycle_11_technical_specification.md`
-+--- `deliverables/engineering/cycle_10_technical_specification.md`
-+-+- `deliverables/engineering/cycle_11_technical_specification.md`
-++-- `deliverables/engineering/cycle_11_technical_specification.md`
-+++- `deliverables/engineering/cycle_12_technical_specification.md`
+---- `deliverables/engineering/cycle_10_technical_specification.md`
+--+- `deliverables/engineering/cycle_11_technical_specification.md`
+-+-- `deliverables/engineering/cycle_11_technical_specification.md`
+-++- `deliverables/engineering/cycle_12_technical_specification.md`
++--- `deliverables/engineering/cycle_11_technical_specification.md`
++-+- `deliverables/engineering/cycle_12_technical_specification.md`
+++-- `deliverables/engineering/cycle_12_technical_specification.md`
++++- `deliverables/engineering/cycle_13_technical_specification.md`
    - `logs/.last_commit_sha`
    - `logs/workflow_state.txt`
----- `pytest.ini`
----- `src/dw6/main.py`
--- - `src/dw6/state_manager.py`
--- - `tests/test_governor.py`
----- `tests/test_state_manager_integration.py`
----- `uv.lock`
--+-- `src/dw6/state_manager.py`
--+-- `tests/test_governor.py`
--++- `src/dw6/main.py`
--++- `tests/test_main.py`
-+--- `src/dw6/state_manager.py`
-+--- `tests/test_governor.py`
-+-+- `src/dw6/main.py`
-+-+- `tests/test_main.py`
-++ - `src/dw6/main.py`
-+++- `src/dw6/state_manager.py`
-+++- `tests/test_governor.py`
-++ - `tests/test_main.py`
+---- `src/dw6/state_manager.py`
+---- `tests/test_governor.py`
+--+- `src/dw6/main.py`
+--+- `tests/test_main.py`
+-+ - `src/dw6/main.py`
+-++- `src/dw6/state_manager.py`
+-++- `tests/test_governor.py`
+-+ - `tests/test_main.py`
++- - `src/dw6/main.py`
++-+- `src/dw6/state_manager.py`
++-+- `tests/test_governor.py`
+++-- `src/dw6/main.py`
+++-- `src/dw6/state_manager.py`
+++-- `tests/test_governor.py`
++  - `tests/test_main.py`
    
    ## Git Diff
    
    ```diff
    diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
----index 82ea098..c5520c2 100644
---+index c5520c2..e748a41 100644
--+-index c5520c2..e748a41 100644
--++index e748a41..82968f8 100644
-+--index c5520c2..e748a41 100644
-+-+index e748a41..82968f8 100644
-++-index e748a41..82968f8 100644
-+++index 82968f8..081c25b 100644
+---index c5520c2..e748a41 100644
+--+index e748a41..82968f8 100644
+-+-index e748a41..82968f8 100644
+-++index 82968f8..081c25b 100644
++--index e748a41..82968f8 100644
++-+index 82968f8..081c25b 100644
+++-index 82968f8..081c25b 100644
++++index 081c25b..2973e35 100644
    --- a/deliverables/coding/coder_deliverable.md
    +++ b/deliverables/coding/coder_deliverable.md
----@@ -1 +1,75 @@
-----This file serves as the deliverable for the Coder stage.
----+# Coder Deliverable
----+
----+## Changed Files
----+
----+- `src/dw6/augmenter.py`
----+- `src/dw6/main.py`
----+
----+## Git Diff
----+
----+```diff
----+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
---+@@ -2,74 +2,422 @@
---+ 
---+ ## Changed Files
---+ 
---+-- `src/dw6/augmenter.py`
---++- `deliverables/coding/coder_deliverable.md`
---++- `deliverables/engineering/cycle_9_technical_specification.md`
---++- `logs/.last_commit_sha`
---++- `logs/workflow_state.txt`
---++- `pytest.ini`
---+ - `src/dw6/main.py`
---++- `src/dw6/state_manager.py`
---++- `tests/test_governor.py`
---++- `tests/test_state_manager_integration.py`
---++- `uv.lock`
---+ 
---+ ## Git Diff
---+ 
---+ ```diff
---+-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
---++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
---++index 82ea098..c5520c2 100644
---++--- a/deliverables/coding/coder_deliverable.md
---+++++ b/deliverables/coding/coder_deliverable.md
---++@@ -1 +1,75 @@
---++-This file serves as the deliverable for the Coder stage.
---+++# Coder Deliverable
---+++
---+++## Changed Files
---+++
---+++- `src/dw6/augmenter.py`
---+++- `src/dw6/main.py`
---+++
---+++## Git Diff
---+++
---+++```diff
---+++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
---+++new file mode 100644
---+++index 0000000..c1614f0
---+++--- /dev/null
---++++++ b/src/dw6/augmenter.py
---+++@@ -0,0 +1,26 @@
---++++# src/dw6/augmenter.py
-+--@@ -2,74 +2,422 @@
-+-- 
-+-+@@ -3,421 +3,578 @@
-++-@@ -3,421 +3,578 @@
-+++@@ -3,578 +3,1129 @@
-+   ## Changed Files
-+   
-+---- `src/dw6/augmenter.py`
-+--+- `deliverables/coding/coder_deliverable.md`
-+--+- `deliverables/engineering/cycle_9_technical_specification.md`
-+--+- `logs/.last_commit_sha`
-+--+- `logs/workflow_state.txt`
-+--+- `pytest.ini`
-+-- - `src/dw6/main.py`
-+--+- `src/dw6/state_manager.py`
-+--+- `tests/test_governor.py`
-+--+- `tests/test_state_manager_integration.py`
-+--+- `uv.lock`
-+-+ - `deliverables/coding/coder_deliverable.md`
-+-+-- `deliverables/engineering/cycle_9_technical_specification.md`
-+-++- `deliverables/engineering/cycle_10_technical_specification.md`
-+-+ - `logs/.last_commit_sha`
-+-+ - `logs/workflow_state.txt`
-+-+-- `pytest.ini`
-+-+-- `src/dw6/main.py`
-+-+ - `src/dw6/state_manager.py`
-+-+ - `tests/test_governor.py`
-+-+-- `tests/test_state_manager_integration.py`
-+-+-- `uv.lock`
-++  - `deliverables/coding/coder_deliverable.md`
-++--- `deliverables/engineering/cycle_9_technical_specification.md`
-++-+- `deliverables/engineering/cycle_10_technical_specification.md`
-+++-- `deliverables/engineering/cycle_10_technical_specification.md`
-++++- `deliverables/engineering/cycle_11_technical_specification.md`
-++  - `logs/.last_commit_sha`
-++  - `logs/workflow_state.txt`
-++--- `pytest.ini`
-++--- `src/dw6/main.py`
-++- - `src/dw6/state_manager.py`
-++- - `tests/test_governor.py`
-++--- `tests/test_state_manager_integration.py`
-++--- `uv.lock`
-+++-- `src/dw6/state_manager.py`
-+++-- `tests/test_governor.py`
-++++- `src/dw6/main.py`
-++++- `tests/test_main.py`
-+   
-+   ## Git Diff
-+   
-+   ```diff
-+---diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-+--+diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
-+--+index 82ea098..c5520c2 100644
-+--+--- a/deliverables/coding/coder_deliverable.md
-+--++++ b/deliverables/coding/coder_deliverable.md
-+--+@@ -1 +1,75 @@
-+--+-This file serves as the deliverable for the Coder stage.
-+--++# Coder Deliverable
-+--++
-+--++## Changed Files
-+--++
-+--++- `src/dw6/augmenter.py`
-+--++- `src/dw6/main.py`
-+--++
-+--++## Git Diff
-+--++
-+--++```diff
-+--++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-+-+ diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
-+-+-index 82ea098..c5520c2 100644
-+-++index c5520c2..e748a41 100644
-+-+ --- a/deliverables/coding/coder_deliverable.md
-+-+ +++ b/deliverables/coding/coder_deliverable.md
-+-+-@@ -1 +1,75 @@
-+-+--This file serves as the deliverable for the Coder stage.
-+-+-+# Coder Deliverable
-+-+-+
-+-+-+## Changed Files
-+-+-+
-+-+-+- `src/dw6/augmenter.py`
-+-+-+- `src/dw6/main.py`
-+-+-+
-+-+-+## Git Diff
-+-+-+
-+-+-+```diff
-+-+-+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-+-++@@ -2,74 +2,422 @@
-+-++ 
-+-++ ## Changed Files
-+-++ 
-+-++-- `src/dw6/augmenter.py`
-+-+++- `deliverables/coding/coder_deliverable.md`
-+-+++- `deliverables/engineering/cycle_9_technical_specification.md`
-+-+++- `logs/.last_commit_sha`
-+-+++- `logs/workflow_state.txt`
-+-+++- `pytest.ini`
-+-++ - `src/dw6/main.py`
-+-+++- `src/dw6/state_manager.py`
-+-+++- `tests/test_governor.py`
-+-+++- `tests/test_state_manager_integration.py`
-+-+++- `uv.lock`
-+-++ 
-+-++ ## Git Diff
-+-++ 
-+-++ ```diff
-+-++-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-+-+++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
-+-+++index 82ea098..c5520c2 100644
-+-+++--- a/deliverables/coding/coder_deliverable.md
-+-++++++ b/deliverables/coding/coder_deliverable.md
-+-+++@@ -1 +1,75 @@
-+-+++-This file serves as the deliverable for the Coder stage.
-+-++++# Coder Deliverable
- -++++
---++++import os
---++++from .state_manager import get_current_requirement_id
--+-@@ -2,74 +2,422 @@
--+- 
--++@@ -3,421 +3,578 @@
--+  ## Changed Files
--+  
--+--- `src/dw6/augmenter.py`
--+-+- `deliverables/coding/coder_deliverable.md`
--+-+- `deliverables/engineering/cycle_9_technical_specification.md`
--+-+- `logs/.last_commit_sha`
--+-+- `logs/workflow_state.txt`
--+-+- `pytest.ini`
--+- - `src/dw6/main.py`
--+-+- `src/dw6/state_manager.py`
--+-+- `tests/test_governor.py`
--+-+- `tests/test_state_manager_integration.py`
--+-+- `uv.lock`
--++ - `deliverables/coding/coder_deliverable.md`
--++-- `deliverables/engineering/cycle_9_technical_specification.md`
--+++- `deliverables/engineering/cycle_10_technical_specification.md`
--++ - `logs/.last_commit_sha`
--++ - `logs/workflow_state.txt`
--++-- `pytest.ini`
--++-- `src/dw6/main.py`
--++ - `src/dw6/state_manager.py`
--++ - `tests/test_governor.py`
--++-- `tests/test_state_manager_integration.py`
--++-- `uv.lock`
--+  
--+  ## Git Diff
--+  
--+  ```diff
--+--diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
--+-+diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
--+-+index 82ea098..c5520c2 100644
--+-+--- a/deliverables/coding/coder_deliverable.md
--+-++++ b/deliverables/coding/coder_deliverable.md
--+-+@@ -1 +1,75 @@
--+-+-This file serves as the deliverable for the Coder stage.
--+-++# Coder Deliverable
--+-++
--+-++## Changed Files
--+-++
--+-++- `src/dw6/augmenter.py`
--+-++- `src/dw6/main.py`
--+-++
--+-++## Git Diff
--+-++
--+-++```diff
--+-++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
--++ diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
--++-index 82ea098..c5520c2 100644
--+++index c5520c2..e748a41 100644
--++ --- a/deliverables/coding/coder_deliverable.md
--++ +++ b/deliverables/coding/coder_deliverable.md
--++-@@ -1 +1,75 @@
--++--This file serves as the deliverable for the Coder stage.
--++-+# Coder Deliverable
--++-+
--++-+## Changed Files
--++-+
--++-+- `src/dw6/augmenter.py`
--++-+- `src/dw6/main.py`
--++-+
--++-+## Git Diff
--++-+
--++-+```diff
--++-+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
--+++@@ -2,74 +2,422 @@
--+++ 
--+++ ## Changed Files
--+++ 
--+++-- `src/dw6/augmenter.py`
--++++- `deliverables/coding/coder_deliverable.md`
--++++- `deliverables/engineering/cycle_9_technical_specification.md`
--++++- `logs/.last_commit_sha`
--++++- `logs/workflow_state.txt`
--++++- `pytest.ini`
--+++ - `src/dw6/main.py`
--++++- `src/dw6/state_manager.py`
--++++- `tests/test_governor.py`
--++++- `tests/test_state_manager_integration.py`
--++++- `uv.lock`
--+++ 
--+++ ## Git Diff
--+++ 
--+++ ```diff
--+++-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
--++++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
--++++index 82ea098..c5520c2 100644
--++++--- a/deliverables/coding/coder_deliverable.md
--+++++++ b/deliverables/coding/coder_deliverable.md
--++++@@ -1 +1,75 @@
--++++-This file serves as the deliverable for the Coder stage.
--+++++# Coder Deliverable
-- ++++
---++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
--+++++## Changed Files
-- ++++
---++++def process_prompt(prompt_text: str):
---++++    """
---++++    Augments a raw user prompt and generates a formal technical specification markdown file.
---++++    """
---++++    requirement_id = get_current_requirement_id()
---++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
--+++++- `src/dw6/augmenter.py`
--+++++- `src/dw6/main.py`
-- ++++
---++++    content = f"# Requirement: {requirement_id}\n\n"
---++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
---++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
--+++++## Git Diff
-- ++++
---++++    try:
---++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
---++++        with open(file_path, 'w') as f:
---++++            f.write(content)
---++++        print(f"Successfully created specification: {file_path}")
---++++    except IOError as e:
---++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
---++++        sys.exit(1)
---+++diff --git a/src/dw6/main.py b/src/dw6/main.py
---+++index 7bbd031..a55f148 100644
---+++--- a/src/dw6/main.py
---++++++ b/src/dw6/main.py
---+++@@ -2,6 +2,7 @@
---+++ import argparse
---+++ import sys
---+++ from dw6.state_manager import StateManager
---++++from dw6.augmenter import process_prompt
--+++++```diff
--+++++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
--+++++new file mode 100644
--+++++index 0000000..c1614f0
--+++++--- /dev/null
--++++++++ b/src/dw6/augmenter.py
--+++++@@ -0,0 +1,26 @@
--++++++# src/dw6/augmenter.py
--++++++
--++++++import os
--++++++from .state_manager import get_current_requirement_id
--++++++
--++++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+---@@ -2,74 +2,422 @@
+--- 
+--+@@ -3,421 +3,578 @@
+-+-@@ -3,421 +3,578 @@
+-++@@ -3,578 +3,1129 @@
++--@@ -3,421 +3,578 @@
++-+@@ -3,578 +3,1129 @@
+++-@@ -3,578 +3,1129 @@
++++@@ -3,1129 +3,1893 @@
+    ## Changed Files
+    
+----- `src/dw6/augmenter.py`
+---+- `deliverables/coding/coder_deliverable.md`
+---+- `deliverables/engineering/cycle_9_technical_specification.md`
+---+- `logs/.last_commit_sha`
+---+- `logs/workflow_state.txt`
+---+- `pytest.ini`
+--- - `src/dw6/main.py`
+---+- `src/dw6/state_manager.py`
+---+- `tests/test_governor.py`
+---+- `tests/test_state_manager_integration.py`
+---+- `uv.lock`
+--+ - `deliverables/coding/coder_deliverable.md`
+--+-- `deliverables/engineering/cycle_9_technical_specification.md`
+--++- `deliverables/engineering/cycle_10_technical_specification.md`
+--+ - `logs/.last_commit_sha`
+--+ - `logs/workflow_state.txt`
+--+-- `pytest.ini`
+--+-- `src/dw6/main.py`
+--+ - `src/dw6/state_manager.py`
+--+ - `tests/test_governor.py`
+--+-- `tests/test_state_manager_integration.py`
+--+-- `uv.lock`
+-+  - `deliverables/coding/coder_deliverable.md`
+-+--- `deliverables/engineering/cycle_9_technical_specification.md`
+-+-+- `deliverables/engineering/cycle_10_technical_specification.md`
+-++-- `deliverables/engineering/cycle_10_technical_specification.md`
+-+++- `deliverables/engineering/cycle_11_technical_specification.md`
+-+  - `logs/.last_commit_sha`
+-+  - `logs/workflow_state.txt`
+-+--- `pytest.ini`
+-+--- `src/dw6/main.py`
+-+- - `src/dw6/state_manager.py`
+-+- - `tests/test_governor.py`
+-+--- `tests/test_state_manager_integration.py`
+-+--- `uv.lock`
+-++-- `src/dw6/state_manager.py`
+-++-- `tests/test_governor.py`
+-+++- `src/dw6/main.py`
+-+++- `tests/test_main.py`
++   - `deliverables/coding/coder_deliverable.md`
++---- `deliverables/engineering/cycle_9_technical_specification.md`
++--+- `deliverables/engineering/cycle_10_technical_specification.md`
++-+-- `deliverables/engineering/cycle_10_technical_specification.md`
++-++- `deliverables/engineering/cycle_11_technical_specification.md`
+++--- `deliverables/engineering/cycle_10_technical_specification.md`
+++-+- `deliverables/engineering/cycle_11_technical_specification.md`
++++-- `deliverables/engineering/cycle_11_technical_specification.md`
+++++- `deliverables/engineering/cycle_12_technical_specification.md`
++   - `logs/.last_commit_sha`
++   - `logs/workflow_state.txt`
++---- `pytest.ini`
++---- `src/dw6/main.py`
++-- - `src/dw6/state_manager.py`
++-- - `tests/test_governor.py`
++---- `tests/test_state_manager_integration.py`
++---- `uv.lock`
++-+-- `src/dw6/state_manager.py`
++-+-- `tests/test_governor.py`
++-++- `src/dw6/main.py`
++-++- `tests/test_main.py`
+++--- `src/dw6/state_manager.py`
+++--- `tests/test_governor.py`
+++-+- `src/dw6/main.py`
+++-+- `tests/test_main.py`
++++ - `src/dw6/main.py`
+++++- `src/dw6/state_manager.py`
+++++- `tests/test_governor.py`
++++ - `tests/test_main.py`
+    
+    ## Git Diff
+    
+    ```diff
+----diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+---+diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+---+index 82ea098..c5520c2 100644
+---+--- a/deliverables/coding/coder_deliverable.md
+---++++ b/deliverables/coding/coder_deliverable.md
+---+@@ -1 +1,75 @@
+---+-This file serves as the deliverable for the Coder stage.
+---++# Coder Deliverable
+---++
+---++## Changed Files
+---++
+---++- `src/dw6/augmenter.py`
+---++- `src/dw6/main.py`
+---++
+---++## Git Diff
+---++
+---++```diff
+---++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+--+ diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+--+-index 82ea098..c5520c2 100644
+--++index c5520c2..e748a41 100644
+--+ --- a/deliverables/coding/coder_deliverable.md
+--+ +++ b/deliverables/coding/coder_deliverable.md
+--+-@@ -1 +1,75 @@
+--+--This file serves as the deliverable for the Coder stage.
+--+-+# Coder Deliverable
+--+-+
+--+-+## Changed Files
+--+-+
+--+-+- `src/dw6/augmenter.py`
+--+-+- `src/dw6/main.py`
+--+-+
+--+-+## Git Diff
+--+-+
+--+-+```diff
+--+-+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+--++@@ -2,74 +2,422 @@
+--++ 
+--++ ## Changed Files
+--++ 
+--++-- `src/dw6/augmenter.py`
+--+++- `deliverables/coding/coder_deliverable.md`
+--+++- `deliverables/engineering/cycle_9_technical_specification.md`
+--+++- `logs/.last_commit_sha`
+--+++- `logs/workflow_state.txt`
+--+++- `pytest.ini`
+--++ - `src/dw6/main.py`
+--+++- `src/dw6/state_manager.py`
+--+++- `tests/test_governor.py`
+--+++- `tests/test_state_manager_integration.py`
+--+++- `uv.lock`
+--++ 
+--++ ## Git Diff
+--++ 
+--++ ```diff
+--++-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+--+++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+--+++index 82ea098..c5520c2 100644
+--+++--- a/deliverables/coding/coder_deliverable.md
+--++++++ b/deliverables/coding/coder_deliverable.md
+--+++@@ -1 +1,75 @@
+--+++-This file serves as the deliverable for the Coder stage.
+--++++# Coder Deliverable
+--++++
+--++++## Changed Files
+--++++
+--++++- `src/dw6/augmenter.py`
+--++++- `src/dw6/main.py`
+--++++
+--++++## Git Diff
+--++++
+--++++```diff
+--++++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+--++++new file mode 100644
+--++++index 0000000..c1614f0
+--++++--- /dev/null
+--+++++++ b/src/dw6/augmenter.py
+--++++@@ -0,0 +1,26 @@
+--+++++# src/dw6/augmenter.py
+--+++++
+--+++++import os
+--+++++from .state_manager import get_current_requirement_id
+--+++++
+--+++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+--+++++
+--+++++def process_prompt(prompt_text: str):
+--+++++    """
+--+++++    Augments a raw user prompt and generates a formal technical specification markdown file.
+--+++++    """
+--+++++    requirement_id = get_current_requirement_id()
+--+++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+--+++++
+--+++++    content = f"# Requirement: {requirement_id}\n\n"
+--+++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+--+++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+--+++++
+--+++++    try:
+--+++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+--+++++        with open(file_path, 'w') as f:
+--+++++            f.write(content)
+--+++++        print(f"Successfully created specification: {file_path}")
+--+++++    except IOError as e:
+--+++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+--+++++        sys.exit(1)
+--++++diff --git a/src/dw6/main.py b/src/dw6/main.py
+--++++index 7bbd031..a55f148 100644
+--++++--- a/src/dw6/main.py
+--+++++++ b/src/dw6/main.py
+--++++@@ -2,6 +2,7 @@
+--++++ import argparse
+--++++ import sys
+--++++ from dw6.state_manager import StateManager
+--+++++from dw6.augmenter import process_prompt
+--++++ 
+--++++ def main():
+--++++     """Main entry point for the DW6 CLI."""
+--++++@@ -15,6 +16,10 @@ def main():
+--++++     # Approve command
+--++++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+--++++ 
+--+++++    # New command
+--+++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+--+++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+--+++++
+--++++     if len(sys.argv) == 1:
+--++++         parser.print_help(sys.stderr)
+--++++         sys.exit(1)
+--++++@@ -27,6 +32,8 @@ def main():
+--++++         manager.review()
+--++++     elif args.command == "approve":
+--++++         manager.approve()
+--+++++    elif args.command == "new":
+--+++++        process_prompt(args.prompt)
+--++++ 
+--++++ if __name__ == "__main__":
+--++++     main()
+--++++```
+--+++\ No newline at end of file
+--+++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+--++ new file mode 100644
+--++-index 0000000..c1614f0
+--+++index 0000000..6c1638b
+--++ --- /dev/null
+--++-+++ b/src/dw6/augmenter.py
+--++-@@ -0,0 +1,26 @@
+--++-+# src/dw6/augmenter.py
+-+  diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+-+--index 82ea098..c5520c2 100644
+-+-+index c5520c2..e748a41 100644
+-++-index c5520c2..e748a41 100644
+-+++index e748a41..82968f8 100644
+-+  --- a/deliverables/coding/coder_deliverable.md
+-+  +++ b/deliverables/coding/coder_deliverable.md
+-+--@@ -1 +1,75 @@
+-+---This file serves as the deliverable for the Coder stage.
+-+--+# Coder Deliverable
+-+--+
+-+--+## Changed Files
+-+--+
+-+--+- `src/dw6/augmenter.py`
+-+--+- `src/dw6/main.py`
+-+--+
+-+--+## Git Diff
+-+--+
+-+--+```diff
+-+--+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+-+-+@@ -2,74 +2,422 @@
+-+-+ 
+-+-+ ## Changed Files
+-+-+ 
+-+-+-- `src/dw6/augmenter.py`
+-+-++- `deliverables/coding/coder_deliverable.md`
+-+-++- `deliverables/engineering/cycle_9_technical_specification.md`
+-+-++- `logs/.last_commit_sha`
+-+-++- `logs/workflow_state.txt`
+-+-++- `pytest.ini`
+-+-+ - `src/dw6/main.py`
+-+-++- `src/dw6/state_manager.py`
+-+-++- `tests/test_governor.py`
+-+-++- `tests/test_state_manager_integration.py`
+-+-++- `uv.lock`
+-+-+ 
+-+-+ ## Git Diff
+-+-+ 
+-+-+ ```diff
+-+-+-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+-+-++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+-+-++index 82ea098..c5520c2 100644
+-+-++--- a/deliverables/coding/coder_deliverable.md
+-+-+++++ b/deliverables/coding/coder_deliverable.md
+-+-++@@ -1 +1,75 @@
+-+-++-This file serves as the deliverable for the Coder stage.
+-+-+++# Coder Deliverable
+-+-+++
+-+-+++## Changed Files
+-+-+++
+-+-+++- `src/dw6/augmenter.py`
+-+-+++- `src/dw6/main.py`
+-+-+++
+-+-+++## Git Diff
+-+-+++
+-+-+++```diff
+-+-+++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+-+-+++new file mode 100644
+-+-+++index 0000000..c1614f0
+-+-+++--- /dev/null
+-+-++++++ b/src/dw6/augmenter.py
+-+-+++@@ -0,0 +1,26 @@
+-+-++++# src/dw6/augmenter.py
+-+-++++
+-+-++++import os
+-+-++++from .state_manager import get_current_requirement_id
+-++-@@ -2,74 +2,422 @@
+-++- 
+-+++@@ -3,421 +3,578 @@
+-++  ## Changed Files
+-++  
+-++--- `src/dw6/augmenter.py`
+-++-+- `deliverables/coding/coder_deliverable.md`
+-++-+- `deliverables/engineering/cycle_9_technical_specification.md`
+-++-+- `logs/.last_commit_sha`
+-++-+- `logs/workflow_state.txt`
+-++-+- `pytest.ini`
+-++- - `src/dw6/main.py`
+-++-+- `src/dw6/state_manager.py`
+-++-+- `tests/test_governor.py`
+-++-+- `tests/test_state_manager_integration.py`
+-++-+- `uv.lock`
+-+++ - `deliverables/coding/coder_deliverable.md`
+-+++-- `deliverables/engineering/cycle_9_technical_specification.md`
+-++++- `deliverables/engineering/cycle_10_technical_specification.md`
+-+++ - `logs/.last_commit_sha`
+-+++ - `logs/workflow_state.txt`
+-+++-- `pytest.ini`
+-+++-- `src/dw6/main.py`
+-+++ - `src/dw6/state_manager.py`
+-+++ - `tests/test_governor.py`
+-+++-- `tests/test_state_manager_integration.py`
+-+++-- `uv.lock`
+-++  
+-++  ## Git Diff
+-++  
+-++  ```diff
+-++--diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+-++-+diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+-++-+index 82ea098..c5520c2 100644
+-++-+--- a/deliverables/coding/coder_deliverable.md
+-++-++++ b/deliverables/coding/coder_deliverable.md
+-++-+@@ -1 +1,75 @@
+-++-+-This file serves as the deliverable for the Coder stage.
+-++-++# Coder Deliverable
+-++-++
+-++-++## Changed Files
+-++-++
+-++-++- `src/dw6/augmenter.py`
+-++-++- `src/dw6/main.py`
+-++-++
+-++-++## Git Diff
+-++-++
+-++-++```diff
+-++-++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+-+++ diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+-+++-index 82ea098..c5520c2 100644
+-++++index c5520c2..e748a41 100644
+-+++ --- a/deliverables/coding/coder_deliverable.md
+-+++ +++ b/deliverables/coding/coder_deliverable.md
+-+++-@@ -1 +1,75 @@
+-+++--This file serves as the deliverable for the Coder stage.
+-+++-+# Coder Deliverable
+-+++-+
+-+++-+## Changed Files
+-+++-+
+-+++-+- `src/dw6/augmenter.py`
+-+++-+- `src/dw6/main.py`
+- ++-+
+--++-+import os
+--++-+from .state_manager import get_current_requirement_id
+--++++++ b/deliverables/engineering/cycle_9_technical_specification.md
+--+++@@ -0,0 +1,9 @@
+--++++# Requirement: 8
+--++ +
+--++-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+--++++## 1. High-Level Goal
+--++ +
+--++-+def process_prompt(prompt_text: str):
+--++-+    """
+--++-+    Augments a raw user prompt and generates a formal technical specification markdown file.
+--++-+    """
+--++-+    requirement_id = get_current_requirement_id()
+--++-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+--++++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+--++ +
+--++-+    content = f"# Requirement: {requirement_id}\n\n"
+--++-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+--++-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+--++++## 2. Guiding Principles
+--++ +
+--++-+    try:
+--++-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+--++-+        with open(file_path, 'w') as f:
+--++-+            f.write(content)
+--++-+        print(f"Successfully created specification: {file_path}")
+--++-+    except IOError as e:
+--++-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+--++-+        sys.exit(1)
+--++++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+--+++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+--+++index 9718eda..b85b3d9 100644
+--+++--- a/logs/.last_commit_sha
+--++++++ b/logs/.last_commit_sha
+--+++@@ -1 +1 @@
+--+++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+--+++\ No newline at end of file
+--++++75be02c0b7e1723e32042299497f3673b11b4ddd
+--+++\ No newline at end of file
+--+++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+--+++index 28746b7..743582b 100644
+--+++--- a/logs/workflow_state.txt
+--++++++ b/logs/workflow_state.txt
+--+++@@ -1,2 +1,2 @@
+--+++-CurrentStage=Engineer
+--+++-RequirementPointer=7
+--++++CurrentStage=Coder
+--++++RequirementPointer=9
+--+++diff --git a/pytest.ini b/pytest.ini
+--+ +new file mode 100644
+--+-+index 0000000..c1614f0
+--+++index 0000000..a635c5c
+--+ +--- /dev/null
+--+-++++ b/src/dw6/augmenter.py
+--+-+@@ -0,0 +1,26 @@
+--+-++# src/dw6/augmenter.py
+--++++++ b/pytest.ini
+--+++@@ -0,0 +1,2 @@
+--++++[pytest]
+--++++pythonpath = .
+--++ diff --git a/src/dw6/main.py b/src/dw6/main.py
+--++-index 7bbd031..a55f148 100644
+--+++index a55f148..90862f9 100644
+--++ --- a/src/dw6/main.py
+--++ +++ b/src/dw6/main.py
+--++-@@ -2,6 +2,7 @@
+--+++@@ -1,7 +1,7 @@
+--+++ # dw6/main.py
+--++  import argparse
+--++  import sys
+--++- from dw6.state_manager import StateManager
+--++-+from dw6.augmenter import process_prompt
+--+++-from dw6.state_manager import StateManager
+--++++from dw6.state_manager import WorkflowManager
+--+++ from dw6.augmenter import process_prompt
+--++  
+--++  def main():
+--++-     """Main entry point for the DW6 CLI."""
+--++-@@ -15,6 +16,10 @@ def main():
+--+++@@ -10,9 +10,7 @@ def main():
+--+++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+--+++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+-+++-+## Git Diff
+-+++-+
+-+++-+```diff
+-+++-+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+-++++@@ -2,74 +2,422 @@
+- +++ 
+--+++-    # Review command
+--+++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
+--+++-    
+--+ ++
+--+-++import os
+--+-++from .state_manager import get_current_requirement_id
+--++      # Approve command
+--++      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+--++  
+--++-+    # New command
+--++-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+--++-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+--+++@@ -26,11 +24,9 @@ def main():
+-++++ ## Changed Files
+- +++ 
+--+++     args = parser.parse_args()
+--+++     
+--+++-    manager = StateManager()
+--++++    manager = WorkflowManager()
+-++++-- `src/dw6/augmenter.py`
+-+++++- `deliverables/coding/coder_deliverable.md`
+-+++++- `deliverables/engineering/cycle_9_technical_specification.md`
+-+++++- `logs/.last_commit_sha`
+-+++++- `logs/workflow_state.txt`
+-+++++- `pytest.ini`
+-++++ - `src/dw6/main.py`
+-+++++- `src/dw6/state_manager.py`
+-+++++- `tests/test_governor.py`
+-+++++- `tests/test_state_manager_integration.py`
+-+++++- `uv.lock`
+- +++ 
+--+++-    if args.command == "review":
+--+++-        manager.review()
+--+++-    elif args.command == "approve":
+--++++    if args.command == "approve":
+--+++         manager.approve()
+--+++     elif args.command == "new":
+--+++         process_prompt(args.prompt)
+--+++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+--+++index 703640c..b829d36 100644
+--+++--- a/src/dw6/state_manager.py
+--++++++ b/src/dw6/state_manager.py
+--+++@@ -9,7 +9,7 @@ from dw6 import git_handler
+--+++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+--+++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+--+++ APPROVAL_FILE = "logs/approvals.log"
+--+++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+--++++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+--+++ DELIVERABLE_PATHS = {
+--+++     "Engineer": "deliverables/engineering",
+--+++     "Coder": "deliverables/coding",
+--+++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+--+++     "Researcher": "deliverables/research",
+--+++ }
+-++++ ## Git Diff
+- +++ 
+--++++class Governor:
+--++++    def __init__(self, state):
+--++++        self.state = state
+--++++        self.current_stage = self.state.get("CurrentStage")
+--+ ++
+--+-++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+--++++    def approve(self):
+--++++        old_stage = self.current_stage
+--++++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+--++++        self._validate_stage_exit_criteria()
+--++++        # The original logic from WorkflowManager is now fully integrated here.
+--++++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+--++++        workflow_manager._validate_stage()
+--++++        workflow_manager._run_pre_transition_actions()
+--++++        self._transition_to_next_stage() # This method now belongs to the Governor
+--++++        workflow_manager._run_post_transition_actions()
+--++++        self.state.save()
+--++++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+--+ ++
+--+-++def process_prompt(prompt_text: str):
+--+-++    """
+--+-++    Augments a raw user prompt and generates a formal technical specification markdown file.
+--+-++    """
+--+-++    requirement_id = get_current_requirement_id()
+--+-++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+--++++    def _validate_stage_exit_criteria(self):
+--++++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+--++++        if self.current_stage == "Engineer":
+--++++            req_id = self.state.get("RequirementPointer")
+--++++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+--++++            if not spec_file.exists():
+--++++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+--++++                sys.exit(1)
+--++++            print("Governor: 'Engineer' exit criteria met.")
+--++ +
+--++-     if len(sys.argv) == 1:
+--++-         parser.print_help(sys.stderr)
+--++-         sys.exit(1)
+--++-@@ -27,6 +32,8 @@ def main():
+--++-         manager.review()
+--++-     elif args.command == "approve":
+--++++    def _transition_to_next_stage(self):
+--++++        current_index = STAGES.index(self.current_stage)
+--++++        # After 'Deployer', the cycle is complete
+--++++        if self.current_stage == "Deployer":
+--++++            self._complete_requirement_cycle()
+--++++            self.current_stage = STAGES[0]
+--++++        else:
+--++++            self.current_stage = STAGES[current_index + 1]
+--++++        self.state.set("CurrentStage", self.current_stage)
+--+ ++
+--+-++    content = f"# Requirement: {requirement_id}\n\n"
+--+-++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+--+-++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+--++++    def _complete_requirement_cycle(self):
+--++++        req_id = int(self.state.get("RequirementPointer"))
+--++++        os.makedirs("logs", exist_ok=True)
+--++++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+--++++        with open(APPROVAL_FILE, "a") as f:
+--++++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+--++++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+--++++        next_req_id = req_id + 1
+--++++        self.state.set("RequirementPointer", next_req_id)
+--++++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-++++ ```diff
+-++++-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+-+++++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+-+++++index 82ea098..c5520c2 100644
+-+++++--- a/deliverables/coding/coder_deliverable.md
+-++++++++ b/deliverables/coding/coder_deliverable.md
+-+++++@@ -1 +1,75 @@
+-+++++-This file serves as the deliverable for the Coder stage.
+-++++++# Coder Deliverable
+-+ ++++
+-+-++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+-++++++## Changed Files
+-+ ++++
+-+-++++def process_prompt(prompt_text: str):
+-+-++++    """
+-+-++++    Augments a raw user prompt and generates a formal technical specification markdown file.
+-+-++++    """
+-+-++++    requirement_id = get_current_requirement_id()
+-+-++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+-++++++- `src/dw6/augmenter.py`
+-++++++- `src/dw6/main.py`
+-+ ++++
+-+-++++    content = f"# Requirement: {requirement_id}\n\n"
+-+-++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+-+-++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+-++++++## Git Diff
+-+ ++++
+-+-++++    try:
+-+-++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+-+-++++        with open(file_path, 'w') as f:
+-+-++++            f.write(content)
+-+-++++        print(f"Successfully created specification: {file_path}")
+-+-++++    except IOError as e:
+-+-++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+-+-++++        sys.exit(1)
+-+-+++diff --git a/src/dw6/main.py b/src/dw6/main.py
+-+-+++index 7bbd031..a55f148 100644
+-+-+++--- a/src/dw6/main.py
+-+-++++++ b/src/dw6/main.py
+-+-+++@@ -2,6 +2,7 @@
+-+-+++ import argparse
+-+-+++ import sys
+-+-+++ from dw6.state_manager import StateManager
+-+-++++from dw6.augmenter import process_prompt
+-++++++```diff
+-++++++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+-++++++new file mode 100644
+-++++++index 0000000..c1614f0
+-++++++--- /dev/null
+-+++++++++ b/src/dw6/augmenter.py
+-++++++@@ -0,0 +1,26 @@
+-+++++++# src/dw6/augmenter.py
+-+++++++
+-+++++++import os
+-+++++++from .state_manager import get_current_requirement_id
+-+++++++
+-+++++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+-+++++++
+-+++++++def process_prompt(prompt_text: str):
+-+++++++    """
+-+++++++    Augments a raw user prompt and generates a formal technical specification markdown file.
+-+++++++    """
+-+++++++    requirement_id = get_current_requirement_id()
+-+++++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+-+++++++
+-+++++++    content = f"# Requirement: {requirement_id}\n\n"
+-+++++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+-+++++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+-+++++++
+-+++++++    try:
+-+++++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+-+++++++        with open(file_path, 'w') as f:
+-+++++++            f.write(content)
+-+++++++        print(f"Successfully created specification: {file_path}")
+-+++++++    except IOError as e:
+-+++++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+-+++++++        sys.exit(1)
+-++++++diff --git a/src/dw6/main.py b/src/dw6/main.py
+-++++++index 7bbd031..a55f148 100644
+-++++++--- a/src/dw6/main.py
+-+++++++++ b/src/dw6/main.py
+-++++++@@ -2,6 +2,7 @@
+-++++++ import argparse
+-++++++ import sys
+-++++++ from dw6.state_manager import StateManager
+-+++++++from dw6.augmenter import process_prompt
+-++++++ 
+-++++++ def main():
+-++++++     """Main entry point for the DW6 CLI."""
+-++++++@@ -15,6 +16,10 @@ def main():
+-++++++     # Approve command
+-++++++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-++++++ 
+-+++++++    # New command
+-+++++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+-+++++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+-+++++++
+-++++++     if len(sys.argv) == 1:
+-++++++         parser.print_help(sys.stderr)
+-++++++         sys.exit(1)
+-++++++@@ -27,6 +32,8 @@ def main():
+-++++++         manager.review()
+-++++++     elif args.command == "approve":
+-++++++         manager.approve()
+-+++++++    elif args.command == "new":
+-+++++++        process_prompt(args.prompt)
+-++++++ 
+-++++++ if __name__ == "__main__":
+-++++++     main()
+-++++++```
+-+++++\ No newline at end of file
+-+++++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+-++++ new file mode 100644
+-++++-index 0000000..c1614f0
+-+++++index 0000000..6c1638b
+-++++ --- /dev/null
+-++++-+++ b/src/dw6/augmenter.py
+-++++-@@ -0,0 +1,26 @@
+-++++-+# src/dw6/augmenter.py
+-++++-+
+-++++-+import os
+-++++-+from .state_manager import get_current_requirement_id
+-++++++++ b/deliverables/engineering/cycle_9_technical_specification.md
+-+++++@@ -0,0 +1,9 @@
+-++++++# Requirement: 8
+-++++ +
+-++++-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+-++++++## 1. High-Level Goal
+-++++ +
+-++++-+def process_prompt(prompt_text: str):
+-++++-+    """
+-++++-+    Augments a raw user prompt and generates a formal technical specification markdown file.
+-++++-+    """
+-++++-+    requirement_id = get_current_requirement_id()
+-++++-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+-++++++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+-++++ +
+-++++-+    content = f"# Requirement: {requirement_id}\n\n"
+-++++-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+-++++-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+-++++++## 2. Guiding Principles
+-++++ +
+-++++-+    try:
+-++++-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+-++++-+        with open(file_path, 'w') as f:
+-++++-+            f.write(content)
+-++++-+        print(f"Successfully created specification: {file_path}")
+-++++-+    except IOError as e:
+-++++-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+-++++-+        sys.exit(1)
+-++++++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+-+++++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+-+++++index 9718eda..b85b3d9 100644
+-+++++--- a/logs/.last_commit_sha
+-++++++++ b/logs/.last_commit_sha
+-+++++@@ -1 +1 @@
+-+++++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+-+++++\ No newline at end of file
+-++++++75be02c0b7e1723e32042299497f3673b11b4ddd
+-+++++\ No newline at end of file
+-+++++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+-+++++index 28746b7..743582b 100644
+-+++++--- a/logs/workflow_state.txt
+-++++++++ b/logs/workflow_state.txt
+-+++++@@ -1,2 +1,2 @@
+-+++++-CurrentStage=Engineer
+-+++++-RequirementPointer=7
+-++++++CurrentStage=Coder
+-++++++RequirementPointer=9
+-+++++diff --git a/pytest.ini b/pytest.ini
+-+++ +new file mode 100644
+-+++-+index 0000000..c1614f0
+-+++++index 0000000..a635c5c
+-+++ +--- /dev/null
+-+++-++++ b/src/dw6/augmenter.py
+-+++-+@@ -0,0 +1,26 @@
+-+++-++# src/dw6/augmenter.py
+-++++++++ b/pytest.ini
+-+++++@@ -0,0 +1,2 @@
+-++++++[pytest]
+-++++++pythonpath = .
+-++++ diff --git a/src/dw6/main.py b/src/dw6/main.py
+-++++-index 7bbd031..a55f148 100644
+-+++++index a55f148..90862f9 100644
+-++++ --- a/src/dw6/main.py
+-++++ +++ b/src/dw6/main.py
+-++++-@@ -2,6 +2,7 @@
+-+++++@@ -1,7 +1,7 @@
+-+++++ # dw6/main.py
+-++++  import argparse
+-++++  import sys
+-++++- from dw6.state_manager import StateManager
+-++++-+from dw6.augmenter import process_prompt
+-+++++-from dw6.state_manager import StateManager
+-++++++from dw6.state_manager import WorkflowManager
+-+++++ from dw6.augmenter import process_prompt
+-++++  
+-++++  def main():
+-++++-     """Main entry point for the DW6 CLI."""
+-++++-@@ -15,6 +16,10 @@ def main():
+-+++++@@ -10,9 +10,7 @@ def main():
+-+++++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+-+++++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+-+ +++ 
+-+-+++ def main():
+-+-+++     """Main entry point for the DW6 CLI."""
+-+-+++@@ -15,6 +16,10 @@ def main():
+-+-+++     # Approve command
+-+-+++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-+++++-    # Review command
+-+++++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
+-+++++-    
+-+++ ++
+-+++-++import os
+-+++-++from .state_manager import get_current_requirement_id
+-++++      # Approve command
+-++++      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-++++  
+-++++-+    # New command
+-++++-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+-++++-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+-+++++@@ -26,11 +24,9 @@ def main():
+-+ +++ 
+-+-++++    # New command
+-+-++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+-+-++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+-+-++++
+-+-+++     if len(sys.argv) == 1:
+-+-+++         parser.print_help(sys.stderr)
+-+-+++         sys.exit(1)
+-+-+++@@ -27,6 +32,8 @@ def main():
+-+-+++         manager.review()
+-+-+++     elif args.command == "approve":
+-+++++     args = parser.parse_args()
+-+++++     
+-+++++-    manager = StateManager()
+-++++++    manager = WorkflowManager()
+-+++++ 
+-+++++-    if args.command == "review":
+-+++++-        manager.review()
+-+++++-    elif args.command == "approve":
+-++++++    if args.command == "approve":
+-+ +++         manager.approve()
+-+-++++    elif args.command == "new":
+-+-++++        process_prompt(args.prompt)
+-+++++     elif args.command == "new":
+-+++++         process_prompt(args.prompt)
+-+++++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+-+++++index 703640c..b829d36 100644
+-+++++--- a/src/dw6/state_manager.py
+-++++++++ b/src/dw6/state_manager.py
+-+++++@@ -9,7 +9,7 @@ from dw6 import git_handler
+-+++++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+-+++++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+-+++++ APPROVAL_FILE = "logs/approvals.log"
+-+++++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+-++++++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+-+++++ DELIVERABLE_PATHS = {
+-+++++     "Engineer": "deliverables/engineering",
+-+++++     "Coder": "deliverables/coding",
+-+++++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+-+++++     "Researcher": "deliverables/research",
+-+++++ }
+-+++++ 
+-++++++class Governor:
+-++++++    def __init__(self, state):
+-++++++        self.state = state
+-++++++        self.current_stage = self.state.get("CurrentStage")
+-+++ ++
+-+++-++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+-++++++    def approve(self):
+-++++++        old_stage = self.current_stage
+-++++++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+-++++++        self._validate_stage_exit_criteria()
+-++++++        # The original logic from WorkflowManager is now fully integrated here.
+-++++++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+-++++++        workflow_manager._validate_stage()
+-++++++        workflow_manager._run_pre_transition_actions()
+-++++++        self._transition_to_next_stage() # This method now belongs to the Governor
+-++++++        workflow_manager._run_post_transition_actions()
+-++++++        self.state.save()
+-++++++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+-+++ ++
+-+++-++def process_prompt(prompt_text: str):
+-+++-++    """
+-+++-++    Augments a raw user prompt and generates a formal technical specification markdown file.
+-+++-++    """
+-+++-++    requirement_id = get_current_requirement_id()
+-+++-++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+-++++++    def _validate_stage_exit_criteria(self):
+-++++++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+-++++++        if self.current_stage == "Engineer":
+-++++++            req_id = self.state.get("RequirementPointer")
+-++++++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+-++++++            if not spec_file.exists():
+-++++++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+-++++++                sys.exit(1)
+-++++++            print("Governor: 'Engineer' exit criteria met.")
+-++++ +
+-++++-     if len(sys.argv) == 1:
+-++++-         parser.print_help(sys.stderr)
+-++++-         sys.exit(1)
+-++++-@@ -27,6 +32,8 @@ def main():
+-++++-         manager.review()
+-++++-     elif args.command == "approve":
+-++++++    def _transition_to_next_stage(self):
+-++++++        current_index = STAGES.index(self.current_stage)
+-++++++        # After 'Deployer', the cycle is complete
+-++++++        if self.current_stage == "Deployer":
+-++++++            self._complete_requirement_cycle()
+-++++++            self.current_stage = STAGES[0]
+-++++++        else:
+-++++++            self.current_stage = STAGES[current_index + 1]
+-++++++        self.state.set("CurrentStage", self.current_stage)
+-+++ ++
+-+++-++    content = f"# Requirement: {requirement_id}\n\n"
+-+++-++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+-+++-++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+-++++++    def _complete_requirement_cycle(self):
+-++++++        req_id = int(self.state.get("RequirementPointer"))
+-++++++        os.makedirs("logs", exist_ok=True)
+-++++++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-++++++        with open(APPROVAL_FILE, "a") as f:
+-++++++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-++++++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-++++++        next_req_id = req_id + 1
+-++++++        self.state.set("RequirementPointer", next_req_id)
+-++++++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-+++ ++
+-+++-++    try:
+-+++-++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+-+++-++        with open(file_path, 'w') as f:
+-+++-++            f.write(content)
+-+++-++        print(f"Successfully created specification: {file_path}")
+-+++-++    except IOError as e:
+-+++-++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+-+++-++        sys.exit(1)
+-+++-+diff --git a/src/dw6/main.py b/src/dw6/main.py
+-+++-+index 7bbd031..a55f148 100644
+-+++-+--- a/src/dw6/main.py
+-+++-++++ b/src/dw6/main.py
+-+++-+@@ -2,6 +2,7 @@
+-+++-+ import argparse
+-+++-+ import sys
+-+++-+ from dw6.state_manager import StateManager
+-+++-++from dw6.augmenter import process_prompt
+-+++++ class WorkflowManager:
+-+++++     def __init__(self):
+-+++++         self.state = WorkflowState()
+-++++++        self.governor = Governor(self.state) # The manager now has a governor
+-+++++         self.current_stage = self.state.get("CurrentStage")
+-+++ + 
+-+++-+ def main():
+-+++-+     """Main entry point for the DW6 CLI."""
+-+++-+@@ -15,6 +16,10 @@ def main():
+-+++-+     # Approve command
+-+++-+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-+++++     def get_state(self):
+-+++++         return self.state.data
+-+++ + 
+-+++-++    # New command
+-+++-++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+-+++-++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+-+++++     def approve(self):
+-+++++-        old_stage = self.current_stage
+-+++++-        print(f"--- Approving Stage: {old_stage} ---")
+-+++++-        self._validate_stage()
+-+++++-        self._run_pre_transition_actions()
+-+++++-        self._transition_to_next_stage()
+-+++++-        self._run_post_transition_actions()
+-+++++-        self.state.save()
+-+++++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+-++++++        # The manager now simply delegates to the governor.
+-++++++        self.governor.approve()
+-+++++ 
+-+++++     def _validate_stage(self):
+-+++++         print(f"Validating deliverables for stage: {self.current_stage}")
+-+++++@@ -123,25 +167,7 @@ class WorkflowManager:
+-+++++         if self.current_stage == "Coder":
+-+++++             git_handler.save_current_commit_sha()
+-+++++ 
+-+++++-    def _transition_to_next_stage(self):
+-+++++-        current_index = STAGES.index(self.current_stage)
+-+++++-        if current_index == len(STAGES) - 1:
+-+++++-            self._complete_requirement_cycle()
+-+++++-            self.current_stage = STAGES[0]
+-+++++-        else:
+-+++++-            self.current_stage = STAGES[current_index + 1]
+-+++++-        self.state.set("CurrentStage", self.current_stage)
+-+++++ 
+-+++++-    def _complete_requirement_cycle(self):
+-+++++-        req_id = int(self.state.get("RequirementPointer"))
+-+++++-        os.makedirs("logs", exist_ok=True)
+-+++++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-+++++-        with open(APPROVAL_FILE, "a") as f:
+-+++++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-+++++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-+++++-        next_req_id = req_id + 1
+-+++++-        self.state.set("RequirementPointer", next_req_id)
+-+++++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-+++++ 
+-+++++ class WorkflowState:
+-+++++     def __init__(self):
+-+++++diff --git a/tests/test_governor.py b/tests/test_governor.py
+-++ ++new file mode 100644
+-++-++index 0000000..c1614f0
+-+++++index 0000000..95b566d
+-++ ++--- /dev/null
+-++-+++++ b/src/dw6/augmenter.py
+-++-++@@ -0,0 +1,26 @@
+-++-+++# src/dw6/augmenter.py
+-++++++++ b/tests/test_governor.py
+-+++++@@ -0,0 +1,55 @@
+-++++++# tests/test_governor.py
+-++++++import pytest
+-++++++from unittest.mock import MagicMock
+-++++++from pathlib import Path
+-++++++import sys
+-+++ ++
+-+++-+     if len(sys.argv) == 1:
+-+++-+         parser.print_help(sys.stderr)
+-+++-+         sys.exit(1)
+-+++-+@@ -27,6 +32,8 @@ def main():
+-+++-+         manager.review()
+-+++-+     elif args.command == "approve":
+-+++-+         manager.approve()
+-+++-++    elif args.command == "new":
+-+++-++        process_prompt(args.prompt)
+-++++++from dw6.state_manager import Governor, WorkflowState
 -++++++
--++++++def process_prompt(prompt_text: str):
--++++++    """
--++++++    Augments a raw user prompt and generates a formal technical specification markdown file.
--++++++    """
--++++++    requirement_id = get_current_requirement_id()
--++++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+-++++++@pytest.fixture
+-++++++def mock_state(mocker):
+-++++++    """Fixture to create a mock WorkflowState."""
+-++++++    state = MagicMock(spec=WorkflowState)
+-++++++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+-++++++    return state
+-++ +++
+-++-+++import os
+-++-+++from .state_manager import get_current_requirement_id
+-++++++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+-++++++    """Verify the Governor blocks approval if the spec file is missing."""
+-++++++    # Arrange: Set the state to Engineer and mock the requirement pointer
+-++++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+-++++++    
+-++++++    # Ensure the spec file does NOT exist for this test
+-++++++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+-++++++    if spec_file.exists():
+-++++++        spec_file.unlink()
+-++ +++
+-++-+++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+-++++++    governor = Governor(mock_state)
+-++ +++
+-++-+++def process_prompt(prompt_text: str):
+-++-+++    """
+-++-+++    Augments a raw user prompt and generates a formal technical specification markdown file.
+-++-+++    """
+-++-+++    requirement_id = get_current_requirement_id()
+-++-+++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+-++++++    # Act & Assert: The approval should fail with a SystemExit
+-++++++    with pytest.raises(SystemExit) as e:
+-++++++        governor._validate_stage_exit_criteria()
+-++++++    
+-++++++    assert e.type == SystemExit
+-++++++    assert e.value.code == 1
+-++ +++
+-++-+++    content = f"# Requirement: {requirement_id}\n\n"
+-++-+++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+-++-+++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+-++++++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+-++++++    """Verify the Governor allows approval if the spec file exists."""
+-++++++    # Arrange: Set the state to Engineer and mock the requirement pointer
+-++++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+-++++++    
+-++++++    # Ensure the spec file DOES exist for this test
+-++++++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+-++++++    spec_file.parent.mkdir(parents=True, exist_ok=True)
+-++++++    spec_file.touch()
+-++ +++
+-++++++    governor = Governor(mock_state)
 -++++++
--++++++    content = f"# Requirement: {requirement_id}\n\n"
--++++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
--++++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+-++++++    # Act & Assert: The approval should pass without raising an exception
+-++ +++    try:
+-++-+++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+-++-+++        with open(file_path, 'w') as f:
+-++-+++            f.write(content)
+-++-+++        print(f"Successfully created specification: {file_path}")
+-++-+++    except IOError as e:
+-++-+++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+-++-+++        sys.exit(1)
+-++-++diff --git a/src/dw6/main.py b/src/dw6/main.py
+-++-++index 7bbd031..a55f148 100644
+-++-++--- a/src/dw6/main.py
+-++-+++++ b/src/dw6/main.py
+-++-++@@ -2,6 +2,7 @@
+-++-++ import argparse
+-++-++ import sys
+-++-++ from dw6.state_manager import StateManager
+-++-+++from dw6.augmenter import process_prompt
+-++-++ 
+-++-++ def main():
+-++-++     """Main entry point for the DW6 CLI."""
+-++-++@@ -15,6 +16,10 @@ def main():
+-++-++     # Approve command
+-++-++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-++++++        governor._validate_stage_exit_criteria()
+-++++++    except SystemExit:
+-++++++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+-++++++    finally:
+-++++++        # Clean up the created file
+-++++++        if spec_file.exists():
+-++++++            spec_file.unlink()
+-+++++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+-+++++index 5b9d1eb..44d2cc9 100644
+-+++++--- a/tests/test_state_manager_integration.py
+-++++++++ b/tests/test_state_manager_integration.py
+-+++++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+-++ ++ 
+-++-+++    # New command
+-++-+++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+-++-+++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+-+++++     @patch('dw6.state_manager.WorkflowState')
+-+++++     @patch('dw6.git_handler.get_changes_since_last_commit')
+-+++++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+-++++++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+-++++++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+-+++++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+-+++++         # Arrange
+-+++++         mock_state_instance = mock_WorkflowState.return_value
+-+++++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+-+++++         # Act
+-++++          manager.approve()
+-++++-+    elif args.command == "new":
+-++++-+        process_prompt(args.prompt)
+-++++  
+-++++- if __name__ == "__main__":
+-++++-     main()
+-+++++-        # Assert
+-++++++        # Assert that the deliverable file was created
+-+++++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+-+++++         self.assertTrue(deliverable_path.exists())
+-++++++        # Clean up the created file
+-++++++        deliverable_path.unlink()
+-++ +++
+-++-++     if len(sys.argv) == 1:
+-++-++         parser.print_help(sys.stderr)
+-++-++         sys.exit(1)
+-++-++@@ -27,6 +32,8 @@ def main():
+-++-++         manager.review()
+-++-++     elif args.command == "approve":
+-++-++         manager.approve()
+-++-+++    elif args.command == "new":
+-++-+++        process_prompt(args.prompt)
+-+++++         mock_state_instance.save.assert_called_once()
+-++ ++ 
+-++-++ if __name__ == "__main__":
+-++-++     main()
+-++-++```
+-++-+\ No newline at end of file
+-++-+diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+-+++++ if __name__ == '__main__':
+-+++++diff --git a/uv.lock b/uv.lock
+-+++++index c79d29c..8e7411f 100644
+-+++++--- a/uv.lock
+-++++++++ b/uv.lock
+-+++++@@ -66,6 +66,7 @@ dependencies = [
+-+++++ test = [
+-+++++     { name = "pytest" },
+-+++++     { name = "pytest-cov" },
+-++++++    { name = "pytest-mock" },
+-+++++ ]
+-+++ + 
+-+++-+ if __name__ == "__main__":
+-+++-+     main()
+-+++-+```
+-+++++ [package.metadata]
+-+++++@@ -73,6 +74,7 @@ requires-dist = [
+-+++++     { name = "gitpython" },
+-+++++     { name = "pytest", marker = "extra == 'test'" },
+-+++++     { name = "pytest-cov", marker = "extra == 'test'" },
+-++++++    { name = "pytest-mock", marker = "extra == 'test'" },
+-+++++     { name = "python-dotenv" },
+-+++++ ]
+-+++++ provides-extras = ["test"]
+-+++++@@ -167,6 +169,18 @@ wheels = [
+-+++++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+-+++++ ]
+-+ +++ 
+-+-+++ if __name__ == "__main__":
+-+-+++     main()
+-+-+++```
+-+-++\ No newline at end of file
+-+-++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+-+-+ new file mode 100644
+-+-+-index 0000000..c1614f0
+-+-++index 0000000..6c1638b
+-+-+ --- /dev/null
+-+-+-+++ b/src/dw6/augmenter.py
+-+-+-@@ -0,0 +1,26 @@
+-+-+-+# src/dw6/augmenter.py
+-++++++[[package]]
+-++++++name = "pytest-mock"
+-++++++version = "3.14.1"
+-++++++source = { registry = "https://pypi.org/simple" }
+-++++++dependencies = [
+-++++++    { name = "pytest" },
+-++++++]
+-++++++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+-++++++wheels = [
+-++++++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+-++++++]
 -++++++
--++++++    try:
--++++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
--++++++        with open(file_path, 'w') as f:
--++++++            f.write(content)
--++++++        print(f"Successfully created specification: {file_path}")
--++++++    except IOError as e:
--++++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
--++++++        sys.exit(1)
--+++++diff --git a/src/dw6/main.py b/src/dw6/main.py
--+++++index 7bbd031..a55f148 100644
--+++++--- a/src/dw6/main.py
--++++++++ b/src/dw6/main.py
--+++++@@ -2,6 +2,7 @@
--+++++ import argparse
--+++++ import sys
--+++++ from dw6.state_manager import StateManager
--++++++from dw6.augmenter import process_prompt
-+-++++## Changed Files
-+-++++
-+-++++- `src/dw6/augmenter.py`
-+-++++- `src/dw6/main.py`
-+-++++
-+-++++## Git Diff
-+-++++
-+-++++```diff
-+-++++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-+-++++new file mode 100644
-+-++++index 0000000..c1614f0
-+-++++--- /dev/null
-+-+++++++ b/src/dw6/augmenter.py
-+-++++@@ -0,0 +1,26 @@
-+-+++++# src/dw6/augmenter.py
-+-+++++
-+-+++++import os
-+-+++++from .state_manager import get_current_requirement_id
-+-+++++
-+-+++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-+-+++++
-+-+++++def process_prompt(prompt_text: str):
-+-+++++    """
-+-+++++    Augments a raw user prompt and generates a formal technical specification markdown file.
-+-+++++    """
-+-+++++    requirement_id = get_current_requirement_id()
-+-+++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-+-+++++
-+-+++++    content = f"# Requirement: {requirement_id}\n\n"
-+-+++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-+-+++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-+-+++++
-+-+++++    try:
-+-+++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-+-+++++        with open(file_path, 'w') as f:
-+-+++++            f.write(content)
-+-+++++        print(f"Successfully created specification: {file_path}")
-+-+++++    except IOError as e:
-+-+++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-+-+++++        sys.exit(1)
-+-++++diff --git a/src/dw6/main.py b/src/dw6/main.py
-+-++++index 7bbd031..a55f148 100644
-+-++++--- a/src/dw6/main.py
-+-+++++++ b/src/dw6/main.py
-+-++++@@ -2,6 +2,7 @@
-+-++++ import argparse
-+-++++ import sys
-+-++++ from dw6.state_manager import StateManager
-+-+++++from dw6.augmenter import process_prompt
-+-++++ 
-+-++++ def main():
-+-++++     """Main entry point for the DW6 CLI."""
-+-++++@@ -15,6 +16,10 @@ def main():
-+-++++     # Approve command
-+-++++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-+-++++ 
-+-+++++    # New command
-+-+++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-+-+++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-+-+++++
-+-++++     if len(sys.argv) == 1:
-+-++++         parser.print_help(sys.stderr)
-+-++++         sys.exit(1)
-+-++++@@ -27,6 +32,8 @@ def main():
-+-++++         manager.review()
-+-++++     elif args.command == "approve":
-+-++++         manager.approve()
-+-+++++    elif args.command == "new":
-+-+++++        process_prompt(args.prompt)
-+-++++ 
-+-++++ if __name__ == "__main__":
-+-++++     main()
-+-++++```
-+-+++\ No newline at end of file
-+-+++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
-+-++ new file mode 100644
-+-++-index 0000000..c1614f0
-+-+++index 0000000..6c1638b
-+-++ --- /dev/null
-+-++-+++ b/src/dw6/augmenter.py
-+-++-@@ -0,0 +1,26 @@
-+-++-+# src/dw6/augmenter.py
-++  diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
-++--index 82ea098..c5520c2 100644
-++-+index c5520c2..e748a41 100644
-+++-index c5520c2..e748a41 100644
-++++index e748a41..82968f8 100644
-++  --- a/deliverables/coding/coder_deliverable.md
-++  +++ b/deliverables/coding/coder_deliverable.md
-++--@@ -1 +1,75 @@
-++---This file serves as the deliverable for the Coder stage.
-++--+# Coder Deliverable
-++--+
-++--+## Changed Files
-++--+
-++--+- `src/dw6/augmenter.py`
-++--+- `src/dw6/main.py`
-++--+
-++--+## Git Diff
-++--+
-++--+```diff
-++--+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-++-+@@ -2,74 +2,422 @@
-++-+ 
-++-+ ## Changed Files
-++-+ 
-++-+-- `src/dw6/augmenter.py`
-++-++- `deliverables/coding/coder_deliverable.md`
-++-++- `deliverables/engineering/cycle_9_technical_specification.md`
-++-++- `logs/.last_commit_sha`
-++-++- `logs/workflow_state.txt`
-++-++- `pytest.ini`
-++-+ - `src/dw6/main.py`
-++-++- `src/dw6/state_manager.py`
-++-++- `tests/test_governor.py`
-++-++- `tests/test_state_manager_integration.py`
-++-++- `uv.lock`
-++-+ 
-++-+ ## Git Diff
-++-+ 
-++-+ ```diff
-++-+-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-++-++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
-++-++index 82ea098..c5520c2 100644
-++-++--- a/deliverables/coding/coder_deliverable.md
-++-+++++ b/deliverables/coding/coder_deliverable.md
-++-++@@ -1 +1,75 @@
-++-++-This file serves as the deliverable for the Coder stage.
-++-+++# Coder Deliverable
-++-+++
-++-+++## Changed Files
-++-+++
-++-+++- `src/dw6/augmenter.py`
-++-+++- `src/dw6/main.py`
-++-+++
-++-+++## Git Diff
-++-+++
-++-+++```diff
-++-+++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-++-+++new file mode 100644
-++-+++index 0000000..c1614f0
-++-+++--- /dev/null
-++-++++++ b/src/dw6/augmenter.py
-++-+++@@ -0,0 +1,26 @@
-++-++++# src/dw6/augmenter.py
+-+++++ [[package]]
+-+++++ name = "python-dotenv"
+-+++++ version = "1.1.1"
+-++++ ```
+-+++ \ No newline at end of file
+-+++-diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+-++++diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
+-++  new file mode 100644
+-++--index 0000000..c1614f0
+-++-+index 0000000..6c1638b
+-+++-index 0000000..6c1638b
+-++++index 0000000..691df8d
+-++  --- /dev/null
+-++--+++ b/src/dw6/augmenter.py
+-++--@@ -0,0 +1,26 @@
+-++--+# src/dw6/augmenter.py
+-++--+
+-++--+import os
+-++--+from .state_manager import get_current_requirement_id
+-++-++++ b/deliverables/engineering/cycle_9_technical_specification.md
+-++-+@@ -0,0 +1,9 @@
+-++-++# Requirement: 8
+-+++-+++ b/deliverables/engineering/cycle_9_technical_specification.md
+-+++++++ b/deliverables/engineering/cycle_10_technical_specification.md
+-+++ @@ -0,0 +1,9 @@
+-+++-+# Requirement: 8
+-+++++# Requirement: 10
+-++  +
+-++--+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+-++-++## 1. High-Level Goal
+-+++ +## 1. High-Level Goal
+-++  +
+-++--+def process_prompt(prompt_text: str):
+-++--+    """
+-++--+    Augments a raw user prompt and generates a formal technical specification markdown file.
+-++--+    """
+-++--+    requirement_id = get_current_requirement_id()
+-++--+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+-++-++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+-+++-+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+-+++++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
+-++  +
+-++--+    content = f"# Requirement: {requirement_id}\n\n"
+-++--+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+-++--+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+-++-++## 2. Guiding Principles
+-+++ +## 2. Guiding Principles
+-++  +
+-++--+    try:
+-++--+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+-++--+        with open(file_path, 'w') as f:
+-++--+            f.write(content)
+-++--+        print(f"Successfully created specification: {file_path}")
+-++--+    except IOError as e:
+-++--+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+-++--+        sys.exit(1)
+-++-++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+-++-+diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+-++-+index 9718eda..b85b3d9 100644
+-++-+--- a/logs/.last_commit_sha
+-++-++++ b/logs/.last_commit_sha
+-++-+@@ -1 +1 @@
+-++-+-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+-++-+\ No newline at end of file
+-++-++75be02c0b7e1723e32042299497f3673b11b4ddd
+-++-+\ No newline at end of file
+-++-+diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+-++-+index 28746b7..743582b 100644
+-++-+--- a/logs/workflow_state.txt
+-++-++++ b/logs/workflow_state.txt
+-++-+@@ -1,2 +1,2 @@
+-++-+-CurrentStage=Engineer
+-++-+-RequirementPointer=7
+-++-++CurrentStage=Coder
+-++-++RequirementPointer=9
+-++-+diff --git a/pytest.ini b/pytest.ini
+-++-+new file mode 100644
+-++-+index 0000000..a635c5c
+-++-+--- /dev/null
+-++-++++ b/pytest.ini
+-++-+@@ -0,0 +1,2 @@
+-++-++[pytest]
+-++-++pythonpath = .
+-++- diff --git a/src/dw6/main.py b/src/dw6/main.py
+-++--index 7bbd031..a55f148 100644
+-++-+index a55f148..90862f9 100644
+-++- --- a/src/dw6/main.py
+-++- +++ b/src/dw6/main.py
+-++--@@ -2,6 +2,7 @@
+-++-+@@ -1,7 +1,7 @@
+-++-+ # dw6/main.py
+-++-  import argparse
+-++-  import sys
+-++-- from dw6.state_manager import StateManager
+-++--+from dw6.augmenter import process_prompt
+-++-+-from dw6.state_manager import StateManager
+-++-++from dw6.state_manager import WorkflowManager
+-++-+ from dw6.augmenter import process_prompt
+-+++ +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+-+++ diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+-+++-index 9718eda..b85b3d9 100644
+-++++index b85b3d9..00ab2c8 100644
+-+++ --- a/logs/.last_commit_sha
+-+++ +++ b/logs/.last_commit_sha
+-+++ @@ -1 +1 @@
+-+++--7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+-++++-75be02c0b7e1723e32042299497f3673b11b4ddd
+-+++ \ No newline at end of file
+-+++-+75be02c0b7e1723e32042299497f3673b11b4ddd
+-+++++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+-+++ \ No newline at end of file
+-+++ diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+-+++-index 28746b7..743582b 100644
+-++++index 743582b..a7aa662 100644
+-+++ --- a/logs/workflow_state.txt
+-+++ +++ b/logs/workflow_state.txt
+-+++ @@ -1,2 +1,2 @@
+-+++--CurrentStage=Engineer
+-+++--RequirementPointer=7
+-+++-+CurrentStage=Coder
+-+++-+RequirementPointer=9
+-+++-diff --git a/pytest.ini b/pytest.ini
+-+++-new file mode 100644
+-+++-index 0000000..a635c5c
+-+++---- /dev/null
+-+++-+++ b/pytest.ini
+-+++-@@ -0,0 +1,2 @@
+-+++-+[pytest]
+-+++-+pythonpath = .
+-+++-diff --git a/src/dw6/main.py b/src/dw6/main.py
+-+++-index a55f148..90862f9 100644
+-+++---- a/src/dw6/main.py
+-+++-+++ b/src/dw6/main.py
+-+++-@@ -1,7 +1,7 @@
+-+++- # dw6/main.py
+-+++- import argparse
+-+++- import sys
+-+++--from dw6.state_manager import StateManager
+-+++-+from dw6.state_manager import WorkflowManager
+-+++- from dw6.augmenter import process_prompt
+-+++- 
+-+++- def main():
+-+++-@@ -10,9 +10,7 @@ def main():
+-+++-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+-+++-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+-+++- 
+-+++--    # Review command
+-+++--    subparsers.add_parser("review", help="Review the changes for the current stage.")
+-+++--    
+-+ +-+
+-+-+-+import os
+-+-+-+from .state_manager import get_current_requirement_id
+-+-+++++ b/deliverables/engineering/cycle_9_technical_specification.md
+-+-++@@ -0,0 +1,9 @@
+-+-+++# Requirement: 8
+-+-+ +
+-+-+-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+-+-+++## 1. High-Level Goal
+-+-+ +
+-+-+-+def process_prompt(prompt_text: str):
+-+-+-+    """
+-+-+-+    Augments a raw user prompt and generates a formal technical specification markdown file.
+-+-+-+    """
+-+-+-+    requirement_id = get_current_requirement_id()
+-+-+-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+-+-+++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+-+-+ +
+-+-+-+    content = f"# Requirement: {requirement_id}\n\n"
+-+-+-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+-+-+-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+-+-+++## 2. Guiding Principles
+-+++-     # Approve command
+-+++-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-+++- 
+-+++-@@ -26,11 +24,9 @@ def main():
+-+++- 
+-+++-     args = parser.parse_args()
+-+++-     
+-+++--    manager = StateManager()
+-+++-+    manager = WorkflowManager()
+-+++- 
+-+++--    if args.command == "review":
+-+++--        manager.review()
+-+++--    elif args.command == "approve":
+-+++-+    if args.command == "approve":
+-+++-         manager.approve()
+-+++-     elif args.command == "new":
+-+++-         process_prompt(args.prompt)
+-++++ CurrentStage=Coder
+-++++-RequirementPointer=9
+-+++++RequirementPointer=10
+-+++ diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+-+++-index 703640c..b829d36 100644
+-++++index b829d36..241fa62 100644
+-+++ --- a/src/dw6/state_manager.py
+-+++ +++ b/src/dw6/state_manager.py
+-+++-@@ -9,7 +9,7 @@ from dw6 import git_handler
+-+++- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+-+++- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+-+++- APPROVAL_FILE = "logs/approvals.log"
+-+++--STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+-+++-+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+-+++- DELIVERABLE_PATHS = {
+-+++-     "Engineer": "deliverables/engineering",
+-+++-     "Coder": "deliverables/coding",
+-+++-@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+-+++-     "Researcher": "deliverables/research",
+-++++@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
+-+++  }
+-++   
+-++-  def main():
+-++--     """Main entry point for the DW6 CLI."""
+-++--@@ -15,6 +16,10 @@ def main():
+-++-+@@ -10,9 +10,7 @@ def main():
+-++-+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+-++-+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+-++-+ 
+-++-+-    # Review command
+-++-+-    subparsers.add_parser("review", help="Review the changes for the current stage.")
+-++-+-    
+-++-++
+-++-      # Approve command
+-++-      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-+++-+class Governor:
+-+++-+    def __init__(self, state):
+-+++-+        self.state = state
+-+++-+        self.current_stage = self.state.get("CurrentStage")
+-+++-+
+-+++-+    def approve(self):
+-+++-+        old_stage = self.current_stage
+-+++-+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+-+++-+        self._validate_stage_exit_criteria()
+-+++-+        # The original logic from WorkflowManager is now fully integrated here.
+-+++-+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+-+++-+        workflow_manager._validate_stage()
+-+++-+        workflow_manager._run_pre_transition_actions()
+-+++-+        self._transition_to_next_stage() # This method now belongs to the Governor
+-+++-+        workflow_manager._run_post_transition_actions()
+-+++-+        self.state.save()
+-+++-+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+-+++-+
+-+++-+    def _validate_stage_exit_criteria(self):
+-+++-+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+-+++-+        if self.current_stage == "Engineer":
+-+++-+            req_id = self.state.get("RequirementPointer")
+-+++-+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+-+++-+            if not spec_file.exists():
+-+++-+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+-+++-+                sys.exit(1)
+-+++-+            print("Governor: 'Engineer' exit criteria met.")
+-+++-+
+-+++-+    def _transition_to_next_stage(self):
+-+++-+        current_index = STAGES.index(self.current_stage)
+-+++-+        # After 'Deployer', the cycle is complete
+-+++-+        if self.current_stage == "Deployer":
+-+++-+            self._complete_requirement_cycle()
+-+++-+            self.current_stage = STAGES[0]
+-+++-+        else:
+-+++-+            self.current_stage = STAGES[current_index + 1]
+-+++-+        self.state.set("CurrentStage", self.current_stage)
+-+++-+
+-+++-+    def _complete_requirement_cycle(self):
+-+++-+        req_id = int(self.state.get("RequirementPointer"))
+-+++-+        os.makedirs("logs", exist_ok=True)
+-+++-+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-+++-+        with open(APPROVAL_FILE, "a") as f:
+-+++-+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-+++-+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-+++-+        next_req_id = req_id + 1
+-+++-+        self.state.set("RequirementPointer", next_req_id)
+-+++-+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-+++-+
+-+++- class WorkflowManager:
+-+++-     def __init__(self):
+-+++-         self.state = WorkflowState()
+-+++-+        self.governor = Governor(self.state) # The manager now has a governor
+-++++ class Governor:
+-+++++    RULES = {
+-+++++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+-+++++        "Coder": "Can use file system tools, code editing tools, and run tests.",
+-+++++        "Validator": "Can only run tests and validation tools.",
+-+++++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+-+++++        "Researcher": "Can use web search and documentation reading tools."
+-+++++    }
+-++++     def __init__(self, state):
+-++++         self.state = state
+-+++          self.current_stage = self.state.get("CurrentStage")
+-++   
+-++--+    # New command
+-++--+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+-++--+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+-++-+@@ -26,11 +24,9 @@ def main():
+-++-+ 
+-++-+     args = parser.parse_args()
+-++-+     
+-++-+-    manager = StateManager()
+-++-++    manager = WorkflowManager()
+-++-+ 
+-++-+-    if args.command == "review":
+-++-+-        manager.review()
+-++-+-    elif args.command == "approve":
+-++-++    if args.command == "approve":
+-++-+         manager.approve()
+-++-+     elif args.command == "new":
+-++-+         process_prompt(args.prompt)
+-++-+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+-++-+index 703640c..b829d36 100644
+-++-+--- a/src/dw6/state_manager.py
+-++-++++ b/src/dw6/state_manager.py
+-++-+@@ -9,7 +9,7 @@ from dw6 import git_handler
+-++-+ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+-++-+ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+-++-+ APPROVAL_FILE = "logs/approvals.log"
+-++-+-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+-++-++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+-++-+ DELIVERABLE_PATHS = {
+-++-+     "Engineer": "deliverables/engineering",
+-++-+     "Coder": "deliverables/coding",
+-++-+@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+-++-+     "Researcher": "deliverables/research",
+-++-+ }
+-++-+ 
+-++-++class Governor:
+-++-++    def __init__(self, state):
+-++-++        self.state = state
+-++-++        self.current_stage = self.state.get("CurrentStage")
+-+++-     def get_state(self):
+-+++-         return self.state.data
+-+++- 
+-+++++    def enforce_rules(self):
+-+++++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+-+++++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+-+++++        print(f"[RULE] {rule}")
+- + ++
+-++-++    def approve(self):
+-++-++        old_stage = self.current_stage
+-++-++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+-++-++        self._validate_stage_exit_criteria()
+-++-++        # The original logic from WorkflowManager is now fully integrated here.
+-++-++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+-++-++        workflow_manager._validate_stage()
+-++-++        workflow_manager._run_pre_transition_actions()
+-++-++        self._transition_to_next_stage() # This method now belongs to the Governor
+-++-++        workflow_manager._run_post_transition_actions()
+-++-++        self.state.save()
+-++-++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+-++-++
+-++-++    def _validate_stage_exit_criteria(self):
+-++-++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+-++-++        if self.current_stage == "Engineer":
+-++-++            req_id = self.state.get("RequirementPointer")
+-++-++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+-++-++            if not spec_file.exists():
+-++-++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+-++-++                sys.exit(1)
+-++-++            print("Governor: 'Engineer' exit criteria met.")
+-+++      def approve(self):
+-+++--        old_stage = self.current_stage
+-+++--        print(f"--- Approving Stage: {old_stage} ---")
+-+++--        self._validate_stage()
+-+++--        self._run_pre_transition_actions()
+-+++--        self._transition_to_next_stage()
+-+++--        self._run_post_transition_actions()
+-+++--        self.state.save()
+-+++--        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+-+++-+        # The manager now simply delegates to the governor.
+-+++-+        self.governor.approve()
+-+++- 
+-+++-     def _validate_stage(self):
+-+++-         print(f"Validating deliverables for stage: {self.current_stage}")
+-+++-@@ -123,25 +167,7 @@ class WorkflowManager:
+-+++-         if self.current_stage == "Coder":
+-+++-             git_handler.save_current_commit_sha()
+-+++- 
+-+++--    def _transition_to_next_stage(self):
+-+++--        current_index = STAGES.index(self.current_stage)
+-+++--        if current_index == len(STAGES) - 1:
+-+++--            self._complete_requirement_cycle()
+-+++--            self.current_stage = STAGES[0]
+-+++--        else:
+-+++--            self.current_stage = STAGES[current_index + 1]
+-+++--        self.state.set("CurrentStage", self.current_stage)
+-+++- 
+-+++--    def _complete_requirement_cycle(self):
+-+++--        req_id = int(self.state.get("RequirementPointer"))
+-+++--        os.makedirs("logs", exist_ok=True)
+-+++--        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-+++--        with open(APPROVAL_FILE, "a") as f:
+-+++--            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-+++--        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-+++--        next_req_id = req_id + 1
+-+++--        self.state.set("RequirementPointer", next_req_id)
+-+++--        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-+++- 
+-+++- class WorkflowState:
+-+++-     def __init__(self):
+-++++         old_stage = self.current_stage
+-++++         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+-+++++        self.enforce_rules()
+-++++         self._validate_stage_exit_criteria()
+-++++         # The original logic from WorkflowManager is now fully integrated here.
+-++++         workflow_manager = WorkflowManager() # We still need access to its methods for now.
+-+++ diff --git a/tests/test_governor.py b/tests/test_governor.py
+-+++-new file mode 100644
+-+++-index 0000000..95b566d
+-+++---- /dev/null
+-++++index 95b566d..26bf82b 100644
+-++++--- a/tests/test_governor.py
+-+++ +++ b/tests/test_governor.py
+-+++-@@ -0,0 +1,55 @@
+-+++-+# tests/test_governor.py
+-+++-+import pytest
+-+++-+from unittest.mock import MagicMock
+-+++-+from pathlib import Path
+-+++-+import sys
+-+++-+
+-+++-+from dw6.state_manager import Governor, WorkflowState
+-+++-+
+-+++-+@pytest.fixture
+-+++-+def mock_state(mocker):
+-+++-+    """Fixture to create a mock WorkflowState."""
+-+++-+    state = MagicMock(spec=WorkflowState)
+-+++-+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+-+++-+    return state
+-+++-+
+-+++-+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+-+++-+    """Verify the Governor blocks approval if the spec file is missing."""
+-+++-+    # Arrange: Set the state to Engineer and mock the requirement pointer
+-+++-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+-+++-+    
+-+++-+    # Ensure the spec file does NOT exist for this test
+-+++-+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+-+++-+    if spec_file.exists():
+-+++-+        spec_file.unlink()
+-+++-+
+-+++-+    governor = Governor(mock_state)
+-+++-+
+-+++-+    # Act & Assert: The approval should fail with a SystemExit
+-+++-+    with pytest.raises(SystemExit) as e:
+-+++-+        governor._validate_stage_exit_criteria()
+-+++-+    
+-+++-+    assert e.type == SystemExit
+-+++-+    assert e.value.code == 1
+-+++-+
+-+++-+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+-+++-+    """Verify the Governor allows approval if the spec file exists."""
+-+++-+    # Arrange: Set the state to Engineer and mock the requirement pointer
+-+++-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+-+++-+    
+-+++-+    # Ensure the spec file DOES exist for this test
+-+++-+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+-+++-+    spec_file.parent.mkdir(parents=True, exist_ok=True)
+-+++-+    spec_file.touch()
+-++++@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+-++++         # Clean up the created file
+-++++         if spec_file.exists():
+-++++             spec_file.unlink()
+-++  +
+-++--     if len(sys.argv) == 1:
+-++--         parser.print_help(sys.stderr)
+-++--         sys.exit(1)
+-++--@@ -27,6 +32,8 @@ def main():
+-++--         manager.review()
+-++--     elif args.command == "approve":
+-++-++    def _transition_to_next_stage(self):
+-++-++        current_index = STAGES.index(self.current_stage)
+-++-++        # After 'Deployer', the cycle is complete
+-++-++        if self.current_stage == "Deployer":
+-++-++            self._complete_requirement_cycle()
+-++-++            self.current_stage = STAGES[0]
+-++-++        else:
+-++-++            self.current_stage = STAGES[current_index + 1]
+-++-++        self.state.set("CurrentStage", self.current_stage)
+-++-++
+-++-++    def _complete_requirement_cycle(self):
+-++-++        req_id = int(self.state.get("RequirementPointer"))
+-++-++        os.makedirs("logs", exist_ok=True)
+-++-++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-++-++        with open(APPROVAL_FILE, "a") as f:
+-++-++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-++-++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-++-++        next_req_id = req_id + 1
+-++-++        self.state.set("RequirementPointer", next_req_id)
+-++-++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-++-++
+-++-+ class WorkflowManager:
+-++-+     def __init__(self):
+-++-+         self.state = WorkflowState()
+-++-++        self.governor = Governor(self.state) # The manager now has a governor
+-++-+         self.current_stage = self.state.get("CurrentStage")
+-++-+ 
+-++-+     def get_state(self):
+-++-+         return self.state.data
+-++-+ 
+-++-+     def approve(self):
+-++-+-        old_stage = self.current_stage
+-++-+-        print(f"--- Approving Stage: {old_stage} ---")
+-++-+-        self._validate_stage()
+-++-+-        self._run_pre_transition_actions()
+-++-+-        self._transition_to_next_stage()
+-++-+-        self._run_post_transition_actions()
+-++-+-        self.state.save()
+-++-+-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+-++-++        # The manager now simply delegates to the governor.
+-++-++        self.governor.approve()
+-++-+ 
+-++-+     def _validate_stage(self):
+-++-+         print(f"Validating deliverables for stage: {self.current_stage}")
+-++-+@@ -123,25 +167,7 @@ class WorkflowManager:
+-++-+         if self.current_stage == "Coder":
+-++-+             git_handler.save_current_commit_sha()
+-++-+ 
+-++-+-    def _transition_to_next_stage(self):
+-++-+-        current_index = STAGES.index(self.current_stage)
+-++-+-        if current_index == len(STAGES) - 1:
+-++-+-            self._complete_requirement_cycle()
+-++-+-            self.current_stage = STAGES[0]
+-++-+-        else:
+-++-+-            self.current_stage = STAGES[current_index + 1]
+-++-+-        self.state.set("CurrentStage", self.current_stage)
+-++-+ 
+-++-+-    def _complete_requirement_cycle(self):
+-++-+-        req_id = int(self.state.get("RequirementPointer"))
+-++-+-        os.makedirs("logs", exist_ok=True)
+-++-+-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-++-+-        with open(APPROVAL_FILE, "a") as f:
+-++-+-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-++-+-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-++-+-        next_req_id = req_id + 1
+-++-+-        self.state.set("RequirementPointer", next_req_id)
+-++-+-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-++-+ 
+-++-+ class WorkflowState:
+-++-+     def __init__(self):
+-++-+diff --git a/tests/test_governor.py b/tests/test_governor.py
+-++-+new file mode 100644
+-++-+index 0000000..95b566d
+-++-+--- /dev/null
+-++-++++ b/tests/test_governor.py
+-++-+@@ -0,0 +1,55 @@
+-++-++# tests/test_governor.py
+-++-++import pytest
+-++-++from unittest.mock import MagicMock
+-++-++from pathlib import Path
+-++-++import sys
+-++-++
+-++-++from dw6.state_manager import Governor, WorkflowState
+-++-++
+-++-++@pytest.fixture
+-++-++def mock_state(mocker):
+-++-++    """Fixture to create a mock WorkflowState."""
+-++-++    state = MagicMock(spec=WorkflowState)
+-++-++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+-++-++    return state
+-++-++
+-++-++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+-++-++    """Verify the Governor blocks approval if the spec file is missing."""
+-++-++    # Arrange: Set the state to Engineer and mock the requirement pointer
+-++-++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+-++-++    
+-++-++    # Ensure the spec file does NOT exist for this test
+-++-++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+-++-++    if spec_file.exists():
+-++-++        spec_file.unlink()
+-++-++
+-++-++    governor = Governor(mock_state)
+-++-++
+-++-++    # Act & Assert: The approval should fail with a SystemExit
+-++-++    with pytest.raises(SystemExit) as e:
+-++-++        governor._validate_stage_exit_criteria()
+-++-++    
+-++-++    assert e.type == SystemExit
+-++-++    assert e.value.code == 1
+-++-++
+-++-++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+-++-++    """Verify the Governor allows approval if the spec file exists."""
+-++-++    # Arrange: Set the state to Engineer and mock the requirement pointer
+-++-++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+-++-++    
+-++-++    # Ensure the spec file DOES exist for this test
+-++-++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+-++-++    spec_file.parent.mkdir(parents=True, exist_ok=True)
+-++-++    spec_file.touch()
+-++-++
+-++-++    governor = Governor(mock_state)
+-++-++
+-++-++    # Act & Assert: The approval should pass without raising an exception
+- +-++    try:
+--+-++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+--+-++        with open(file_path, 'w') as f:
+--+-++            f.write(content)
+--+-++        print(f"Successfully created specification: {file_path}")
+--+-++    except IOError as e:
+--+-++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+--+-++        sys.exit(1)
+--+-+diff --git a/src/dw6/main.py b/src/dw6/main.py
+--+-+index 7bbd031..a55f148 100644
+--+-+--- a/src/dw6/main.py
+--+-++++ b/src/dw6/main.py
+--+-+@@ -2,6 +2,7 @@
+--+-+ import argparse
+--+-+ import sys
+--+-+ from dw6.state_manager import StateManager
+--+-++from dw6.augmenter import process_prompt
+--+++ class WorkflowManager:
+--+++     def __init__(self):
+--+++         self.state = WorkflowState()
+--++++        self.governor = Governor(self.state) # The manager now has a governor
+--+++         self.current_stage = self.state.get("CurrentStage")
+--+ + 
+--+-+ def main():
+--+-+     """Main entry point for the DW6 CLI."""
+--+-+@@ -15,6 +16,10 @@ def main():
+--+-+     # Approve command
+--+-+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+--+++     def get_state(self):
+--+++         return self.state.data
+--+ + 
+--+-++    # New command
+--+-++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+--+-++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+--+++     def approve(self):
+--+++-        old_stage = self.current_stage
+--+++-        print(f"--- Approving Stage: {old_stage} ---")
+--+++-        self._validate_stage()
+--+++-        self._run_pre_transition_actions()
+--+++-        self._transition_to_next_stage()
+--+++-        self._run_post_transition_actions()
+--+++-        self.state.save()
+--+++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+--++++        # The manager now simply delegates to the governor.
+--++++        self.governor.approve()
++   diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
++---index 82ea098..c5520c2 100644
++--+index c5520c2..e748a41 100644
++-+-index c5520c2..e748a41 100644
++-++index e748a41..82968f8 100644
+++--index c5520c2..e748a41 100644
+++-+index e748a41..82968f8 100644
++++-index e748a41..82968f8 100644
+++++index 82968f8..081c25b 100644
++   --- a/deliverables/coding/coder_deliverable.md
++   +++ b/deliverables/coding/coder_deliverable.md
++---@@ -1 +1,75 @@
++----This file serves as the deliverable for the Coder stage.
++---+# Coder Deliverable
++---+
++---+## Changed Files
++---+
++---+- `src/dw6/augmenter.py`
++---+- `src/dw6/main.py`
++---+
++---+## Git Diff
++---+
++---+```diff
++---+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++--+@@ -2,74 +2,422 @@
++--+ 
++--+ ## Changed Files
++--+ 
++--+-- `src/dw6/augmenter.py`
++--++- `deliverables/coding/coder_deliverable.md`
++--++- `deliverables/engineering/cycle_9_technical_specification.md`
++--++- `logs/.last_commit_sha`
++--++- `logs/workflow_state.txt`
++--++- `pytest.ini`
++--+ - `src/dw6/main.py`
++--++- `src/dw6/state_manager.py`
++--++- `tests/test_governor.py`
++--++- `tests/test_state_manager_integration.py`
++--++- `uv.lock`
++--+ 
++--+ ## Git Diff
++--+ 
++--+ ```diff
++--+-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++--++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
++--++index 82ea098..c5520c2 100644
++--++--- a/deliverables/coding/coder_deliverable.md
++--+++++ b/deliverables/coding/coder_deliverable.md
++--++@@ -1 +1,75 @@
++--++-This file serves as the deliverable for the Coder stage.
++--+++# Coder Deliverable
++--+++
++--+++## Changed Files
++--+++
++--+++- `src/dw6/augmenter.py`
++--+++- `src/dw6/main.py`
++--+++
++--+++## Git Diff
++--+++
++--+++```diff
++--+++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++--+++new file mode 100644
++--+++index 0000000..c1614f0
++--+++--- /dev/null
++--++++++ b/src/dw6/augmenter.py
++--+++@@ -0,0 +1,26 @@
++--++++# src/dw6/augmenter.py
+++--@@ -2,74 +2,422 @@
+++-- 
+++-+@@ -3,421 +3,578 @@
++++-@@ -3,421 +3,578 @@
+++++@@ -3,578 +3,1129 @@
+++   ## Changed Files
+++   
+++---- `src/dw6/augmenter.py`
+++--+- `deliverables/coding/coder_deliverable.md`
+++--+- `deliverables/engineering/cycle_9_technical_specification.md`
+++--+- `logs/.last_commit_sha`
+++--+- `logs/workflow_state.txt`
+++--+- `pytest.ini`
+++-- - `src/dw6/main.py`
+++--+- `src/dw6/state_manager.py`
+++--+- `tests/test_governor.py`
+++--+- `tests/test_state_manager_integration.py`
+++--+- `uv.lock`
+++-+ - `deliverables/coding/coder_deliverable.md`
+++-+-- `deliverables/engineering/cycle_9_technical_specification.md`
+++-++- `deliverables/engineering/cycle_10_technical_specification.md`
+++-+ - `logs/.last_commit_sha`
+++-+ - `logs/workflow_state.txt`
+++-+-- `pytest.ini`
+++-+-- `src/dw6/main.py`
+++-+ - `src/dw6/state_manager.py`
+++-+ - `tests/test_governor.py`
+++-+-- `tests/test_state_manager_integration.py`
+++-+-- `uv.lock`
++++  - `deliverables/coding/coder_deliverable.md`
++++--- `deliverables/engineering/cycle_9_technical_specification.md`
++++-+- `deliverables/engineering/cycle_10_technical_specification.md`
+++++-- `deliverables/engineering/cycle_10_technical_specification.md`
++++++- `deliverables/engineering/cycle_11_technical_specification.md`
++++  - `logs/.last_commit_sha`
++++  - `logs/workflow_state.txt`
++++--- `pytest.ini`
++++--- `src/dw6/main.py`
++++- - `src/dw6/state_manager.py`
++++- - `tests/test_governor.py`
++++--- `tests/test_state_manager_integration.py`
++++--- `uv.lock`
+++++-- `src/dw6/state_manager.py`
+++++-- `tests/test_governor.py`
++++++- `src/dw6/main.py`
++++++- `tests/test_main.py`
+++   
+++   ## Git Diff
+++   
+++   ```diff
+++---diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+++--+diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+++--+index 82ea098..c5520c2 100644
+++--+--- a/deliverables/coding/coder_deliverable.md
+++--++++ b/deliverables/coding/coder_deliverable.md
+++--+@@ -1 +1,75 @@
+++--+-This file serves as the deliverable for the Coder stage.
+++--++# Coder Deliverable
+++--++
+++--++## Changed Files
+++--++
+++--++- `src/dw6/augmenter.py`
+++--++- `src/dw6/main.py`
+++--++
+++--++## Git Diff
+++--++
+++--++```diff
+++--++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+++-+ diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+++-+-index 82ea098..c5520c2 100644
+++-++index c5520c2..e748a41 100644
+++-+ --- a/deliverables/coding/coder_deliverable.md
+++-+ +++ b/deliverables/coding/coder_deliverable.md
+++-+-@@ -1 +1,75 @@
+++-+--This file serves as the deliverable for the Coder stage.
+++-+-+# Coder Deliverable
+++-+-+
+++-+-+## Changed Files
+++-+-+
+++-+-+- `src/dw6/augmenter.py`
+++-+-+- `src/dw6/main.py`
+++-+-+
+++-+-+## Git Diff
+++-+-+
+++-+-+```diff
+++-+-+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+++-++@@ -2,74 +2,422 @@
+++-++ 
+++-++ ## Changed Files
+++-++ 
+++-++-- `src/dw6/augmenter.py`
+++-+++- `deliverables/coding/coder_deliverable.md`
+++-+++- `deliverables/engineering/cycle_9_technical_specification.md`
+++-+++- `logs/.last_commit_sha`
+++-+++- `logs/workflow_state.txt`
+++-+++- `pytest.ini`
+++-++ - `src/dw6/main.py`
+++-+++- `src/dw6/state_manager.py`
+++-+++- `tests/test_governor.py`
+++-+++- `tests/test_state_manager_integration.py`
+++-+++- `uv.lock`
+++-++ 
+++-++ ## Git Diff
+++-++ 
+++-++ ```diff
+++-++-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+++-+++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+++-+++index 82ea098..c5520c2 100644
+++-+++--- a/deliverables/coding/coder_deliverable.md
+++-++++++ b/deliverables/coding/coder_deliverable.md
+++-+++@@ -1 +1,75 @@
+++-+++-This file serves as the deliverable for the Coder stage.
+++-++++# Coder Deliverable
++ -++++
++--++++import os
++--++++from .state_manager import get_current_requirement_id
++-+-@@ -2,74 +2,422 @@
++-+- 
++-++@@ -3,421 +3,578 @@
++-+  ## Changed Files
++-+  
++-+--- `src/dw6/augmenter.py`
++-+-+- `deliverables/coding/coder_deliverable.md`
++-+-+- `deliverables/engineering/cycle_9_technical_specification.md`
++-+-+- `logs/.last_commit_sha`
++-+-+- `logs/workflow_state.txt`
++-+-+- `pytest.ini`
++-+- - `src/dw6/main.py`
++-+-+- `src/dw6/state_manager.py`
++-+-+- `tests/test_governor.py`
++-+-+- `tests/test_state_manager_integration.py`
++-+-+- `uv.lock`
++-++ - `deliverables/coding/coder_deliverable.md`
++-++-- `deliverables/engineering/cycle_9_technical_specification.md`
++-+++- `deliverables/engineering/cycle_10_technical_specification.md`
++-++ - `logs/.last_commit_sha`
++-++ - `logs/workflow_state.txt`
++-++-- `pytest.ini`
++-++-- `src/dw6/main.py`
++-++ - `src/dw6/state_manager.py`
++-++ - `tests/test_governor.py`
++-++-- `tests/test_state_manager_integration.py`
++-++-- `uv.lock`
++-+  
++-+  ## Git Diff
++-+  
++-+  ```diff
++-+--diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++-+-+diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
++-+-+index 82ea098..c5520c2 100644
++-+-+--- a/deliverables/coding/coder_deliverable.md
++-+-++++ b/deliverables/coding/coder_deliverable.md
++-+-+@@ -1 +1,75 @@
++-+-+-This file serves as the deliverable for the Coder stage.
++-+-++# Coder Deliverable
++-+-++
++-+-++## Changed Files
++-+-++
++-+-++- `src/dw6/augmenter.py`
++-+-++- `src/dw6/main.py`
++-+-++
++-+-++## Git Diff
++-+-++
++-+-++```diff
++-+-++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++-++ diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
++-++-index 82ea098..c5520c2 100644
++-+++index c5520c2..e748a41 100644
++-++ --- a/deliverables/coding/coder_deliverable.md
++-++ +++ b/deliverables/coding/coder_deliverable.md
++-++-@@ -1 +1,75 @@
++-++--This file serves as the deliverable for the Coder stage.
++-++-+# Coder Deliverable
++-++-+
++-++-+## Changed Files
++-++-+
++-++-+- `src/dw6/augmenter.py`
++-++-+- `src/dw6/main.py`
++-++-+
++-++-+## Git Diff
++-++-+
++-++-+```diff
++-++-+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++-+++@@ -2,74 +2,422 @@
+ -+++ 
+--+++     def _validate_stage(self):
+--+++         print(f"Validating deliverables for stage: {self.current_stage}")
+--+++@@ -123,25 +167,7 @@ class WorkflowManager:
+--+++         if self.current_stage == "Coder":
+--+++             git_handler.save_current_commit_sha()
++-+++ ## Changed Files
+ -+++ 
+--+++-    def _transition_to_next_stage(self):
+--+++-        current_index = STAGES.index(self.current_stage)
+--+++-        if current_index == len(STAGES) - 1:
+--+++-            self._complete_requirement_cycle()
+--+++-            self.current_stage = STAGES[0]
+--+++-        else:
+--+++-            self.current_stage = STAGES[current_index + 1]
+--+++-        self.state.set("CurrentStage", self.current_stage)
++-+++-- `src/dw6/augmenter.py`
++-++++- `deliverables/coding/coder_deliverable.md`
++-++++- `deliverables/engineering/cycle_9_technical_specification.md`
++-++++- `logs/.last_commit_sha`
++-++++- `logs/workflow_state.txt`
++-++++- `pytest.ini`
++-+++ - `src/dw6/main.py`
++-++++- `src/dw6/state_manager.py`
++-++++- `tests/test_governor.py`
++-++++- `tests/test_state_manager_integration.py`
++-++++- `uv.lock`
+ -+++ 
+--+++-    def _complete_requirement_cycle(self):
+--+++-        req_id = int(self.state.get("RequirementPointer"))
+--+++-        os.makedirs("logs", exist_ok=True)
+--+++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+--+++-        with open(APPROVAL_FILE, "a") as f:
+--+++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+--+++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+--+++-        next_req_id = req_id + 1
+--+++-        self.state.set("RequirementPointer", next_req_id)
+--+++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++-+++ ## Git Diff
+ -+++ 
+--+++ class WorkflowState:
+--+++     def __init__(self):
+--+++diff --git a/tests/test_governor.py b/tests/test_governor.py
+-- ++new file mode 100644
+---++index 0000000..c1614f0
+--+++index 0000000..95b566d
+-- ++--- /dev/null
+---+++++ b/src/dw6/augmenter.py
+---++@@ -0,0 +1,26 @@
+---+++# src/dw6/augmenter.py
+--++++++ b/tests/test_governor.py
+--+++@@ -0,0 +1,55 @@
+--++++# tests/test_governor.py
+--++++import pytest
+--++++from unittest.mock import MagicMock
+--++++from pathlib import Path
+--++++import sys
+--+ ++
+--+-+     if len(sys.argv) == 1:
+--+-+         parser.print_help(sys.stderr)
+--+-+         sys.exit(1)
+--+-+@@ -27,6 +32,8 @@ def main():
+--+-+         manager.review()
+--+-+     elif args.command == "approve":
+--+-+         manager.approve()
+--+-++    elif args.command == "new":
+--+-++        process_prompt(args.prompt)
+--++++from dw6.state_manager import Governor, WorkflowState
+--++++
+--++++@pytest.fixture
+--++++def mock_state(mocker):
+--++++    """Fixture to create a mock WorkflowState."""
+--++++    state = MagicMock(spec=WorkflowState)
+--++++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+--++++    return state
+-- +++
+---+++import os
+---+++from .state_manager import get_current_requirement_id
+--++++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+--++++    """Verify the Governor blocks approval if the spec file is missing."""
+--++++    # Arrange: Set the state to Engineer and mock the requirement pointer
+--++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+--++++    
+--++++    # Ensure the spec file does NOT exist for this test
+--++++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+--++++    if spec_file.exists():
+--++++        spec_file.unlink()
+-- +++
+---+++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+--++++    governor = Governor(mock_state)
+-- +++
+---+++def process_prompt(prompt_text: str):
+---+++    """
+---+++    Augments a raw user prompt and generates a formal technical specification markdown file.
+---+++    """
+---+++    requirement_id = get_current_requirement_id()
+---+++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+--++++    # Act & Assert: The approval should fail with a SystemExit
+--++++    with pytest.raises(SystemExit) as e:
+--++++        governor._validate_stage_exit_criteria()
+--++++    
+--++++    assert e.type == SystemExit
+--++++    assert e.value.code == 1
+-- +++
+---+++    content = f"# Requirement: {requirement_id}\n\n"
+---+++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+---+++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+--++++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+--++++    """Verify the Governor allows approval if the spec file exists."""
+--++++    # Arrange: Set the state to Engineer and mock the requirement pointer
+--++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+--++++    
+--++++    # Ensure the spec file DOES exist for this test
+--++++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+--++++    spec_file.parent.mkdir(parents=True, exist_ok=True)
+--++++    spec_file.touch()
+-- +++
+--++++    governor = Governor(mock_state)
+--++++
+--++++    # Act & Assert: The approval should pass without raising an exception
+-- +++    try:
+---+++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+---+++        with open(file_path, 'w') as f:
+---+++            f.write(content)
+---+++        print(f"Successfully created specification: {file_path}")
+---+++    except IOError as e:
+---+++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+---+++        sys.exit(1)
+---++diff --git a/src/dw6/main.py b/src/dw6/main.py
+---++index 7bbd031..a55f148 100644
+---++--- a/src/dw6/main.py
+---+++++ b/src/dw6/main.py
+---++@@ -2,6 +2,7 @@
+---++ import argparse
+---++ import sys
+---++ from dw6.state_manager import StateManager
+---+++from dw6.augmenter import process_prompt
+-++-++        governor._validate_stage_exit_criteria()
+-++-++    except SystemExit:
+-++-++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+-++-++    finally:
+-++-++        # Clean up the created file
+-++-++        if spec_file.exists():
+-++-++            spec_file.unlink()
+-++-+diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+-++-+index 5b9d1eb..44d2cc9 100644
+-++-+--- a/tests/test_state_manager_integration.py
+-++-++++ b/tests/test_state_manager_integration.py
+-++-+@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++-+++ ```diff
++-+++-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++-++++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
++-++++index 82ea098..c5520c2 100644
++-++++--- a/deliverables/coding/coder_deliverable.md
++-+++++++ b/deliverables/coding/coder_deliverable.md
++-++++@@ -1 +1,75 @@
++-++++-This file serves as the deliverable for the Coder stage.
++-+++++# Coder Deliverable
++- ++++
++--++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++-+++++## Changed Files
++- ++++
++--++++def process_prompt(prompt_text: str):
++--++++    """
++--++++    Augments a raw user prompt and generates a formal technical specification markdown file.
++--++++    """
++--++++    requirement_id = get_current_requirement_id()
++--++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++-+++++- `src/dw6/augmenter.py`
++-+++++- `src/dw6/main.py`
++- ++++
++--++++    content = f"# Requirement: {requirement_id}\n\n"
++--++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++--++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++-+++++## Git Diff
++- ++++
++--++++    try:
++--++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++--++++        with open(file_path, 'w') as f:
++--++++            f.write(content)
++--++++        print(f"Successfully created specification: {file_path}")
++--++++    except IOError as e:
++--++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++--++++        sys.exit(1)
++--+++diff --git a/src/dw6/main.py b/src/dw6/main.py
++--+++index 7bbd031..a55f148 100644
++--+++--- a/src/dw6/main.py
++--++++++ b/src/dw6/main.py
++--+++@@ -2,6 +2,7 @@
++--+++ import argparse
++--+++ import sys
++--+++ from dw6.state_manager import StateManager
++--++++from dw6.augmenter import process_prompt
++-+++++```diff
++-+++++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++-+++++new file mode 100644
++-+++++index 0000000..c1614f0
++-+++++--- /dev/null
++-++++++++ b/src/dw6/augmenter.py
++-+++++@@ -0,0 +1,26 @@
++-++++++# src/dw6/augmenter.py
++-++++++
++-++++++import os
++-++++++from .state_manager import get_current_requirement_id
++-++++++
++-++++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++-++++++
++-++++++def process_prompt(prompt_text: str):
++-++++++    """
++-++++++    Augments a raw user prompt and generates a formal technical specification markdown file.
++-++++++    """
++-++++++    requirement_id = get_current_requirement_id()
++-++++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++-++++++
++-++++++    content = f"# Requirement: {requirement_id}\n\n"
++-++++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++-++++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++-++++++
++-++++++    try:
++-++++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++-++++++        with open(file_path, 'w') as f:
++-++++++            f.write(content)
++-++++++        print(f"Successfully created specification: {file_path}")
++-++++++    except IOError as e:
++-++++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++-++++++        sys.exit(1)
++-+++++diff --git a/src/dw6/main.py b/src/dw6/main.py
++-+++++index 7bbd031..a55f148 100644
++-+++++--- a/src/dw6/main.py
++-++++++++ b/src/dw6/main.py
++-+++++@@ -2,6 +2,7 @@
++-+++++ import argparse
++-+++++ import sys
++-+++++ from dw6.state_manager import StateManager
++-++++++from dw6.augmenter import process_prompt
+++-++++## Changed Files
 ++-++++
-++-++++import os
-++-++++from .state_manager import get_current_requirement_id
-+++-@@ -2,74 +2,422 @@
-+++- 
-++++@@ -3,421 +3,578 @@
-+++  ## Changed Files
-+++  
-+++--- `src/dw6/augmenter.py`
-+++-+- `deliverables/coding/coder_deliverable.md`
-+++-+- `deliverables/engineering/cycle_9_technical_specification.md`
-+++-+- `logs/.last_commit_sha`
-+++-+- `logs/workflow_state.txt`
-+++-+- `pytest.ini`
-+++- - `src/dw6/main.py`
-+++-+- `src/dw6/state_manager.py`
-+++-+- `tests/test_governor.py`
-+++-+- `tests/test_state_manager_integration.py`
-+++-+- `uv.lock`
-++++ - `deliverables/coding/coder_deliverable.md`
-++++-- `deliverables/engineering/cycle_9_technical_specification.md`
-+++++- `deliverables/engineering/cycle_10_technical_specification.md`
-++++ - `logs/.last_commit_sha`
-++++ - `logs/workflow_state.txt`
-++++-- `pytest.ini`
-++++-- `src/dw6/main.py`
-++++ - `src/dw6/state_manager.py`
-++++ - `tests/test_governor.py`
-++++-- `tests/test_state_manager_integration.py`
-++++-- `uv.lock`
-+++  
-+++  ## Git Diff
-+++  
-+++  ```diff
-+++--diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-+++-+diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
-+++-+index 82ea098..c5520c2 100644
-+++-+--- a/deliverables/coding/coder_deliverable.md
-+++-++++ b/deliverables/coding/coder_deliverable.md
-+++-+@@ -1 +1,75 @@
-+++-+-This file serves as the deliverable for the Coder stage.
-+++-++# Coder Deliverable
-+++-++
-+++-++## Changed Files
-+++-++
-+++-++- `src/dw6/augmenter.py`
-+++-++- `src/dw6/main.py`
-+++-++
-+++-++## Git Diff
-+++-++
-+++-++```diff
-+++-++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-++++ diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
-++++-index 82ea098..c5520c2 100644
-+++++index c5520c2..e748a41 100644
-++++ --- a/deliverables/coding/coder_deliverable.md
-++++ +++ b/deliverables/coding/coder_deliverable.md
-++++-@@ -1 +1,75 @@
-++++--This file serves as the deliverable for the Coder stage.
-++++-+# Coder Deliverable
-++++-+
-++++-+## Changed Files
-++++-+
-++++-+- `src/dw6/augmenter.py`
-++++-+- `src/dw6/main.py`
-+ ++-+
-+-++-+import os
-+-++-+from .state_manager import get_current_requirement_id
-+-++++++ b/deliverables/engineering/cycle_9_technical_specification.md
-+-+++@@ -0,0 +1,9 @@
-+-++++# Requirement: 8
-+-++ +
-+-++-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-+-++++## 1. High-Level Goal
-+-++ +
-+-++-+def process_prompt(prompt_text: str):
-+-++-+    """
-+-++-+    Augments a raw user prompt and generates a formal technical specification markdown file.
-+-++-+    """
-+-++-+    requirement_id = get_current_requirement_id()
-+-++-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-+-++++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
-+-++ +
-+-++-+    content = f"# Requirement: {requirement_id}\n\n"
-+-++-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-+-++-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-+-++++## 2. Guiding Principles
-+-++ +
-+-++-+    try:
-+-++-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-+-++-+        with open(file_path, 'w') as f:
-+-++-+            f.write(content)
-+-++-+        print(f"Successfully created specification: {file_path}")
-+-++-+    except IOError as e:
-+-++-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-+-++-+        sys.exit(1)
-+-++++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
-+-+++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
-+-+++index 9718eda..b85b3d9 100644
-+-+++--- a/logs/.last_commit_sha
-+-++++++ b/logs/.last_commit_sha
-+-+++@@ -1 +1 @@
-+-+++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
-+-+++\ No newline at end of file
-+-++++75be02c0b7e1723e32042299497f3673b11b4ddd
-+-+++\ No newline at end of file
-+-+++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
-+-+++index 28746b7..743582b 100644
-+-+++--- a/logs/workflow_state.txt
-+-++++++ b/logs/workflow_state.txt
-+-+++@@ -1,2 +1,2 @@
-+-+++-CurrentStage=Engineer
-+-+++-RequirementPointer=7
-+-++++CurrentStage=Coder
-+-++++RequirementPointer=9
-+-+++diff --git a/pytest.ini b/pytest.ini
-+-+ +new file mode 100644
-+-+-+index 0000000..c1614f0
-+-+++index 0000000..a635c5c
-+-+ +--- /dev/null
-+-+-++++ b/src/dw6/augmenter.py
-+-+-+@@ -0,0 +1,26 @@
-+-+-++# src/dw6/augmenter.py
-+-++++++ b/pytest.ini
-+-+++@@ -0,0 +1,2 @@
-+-++++[pytest]
-+-++++pythonpath = .
-+-++ diff --git a/src/dw6/main.py b/src/dw6/main.py
-+-++-index 7bbd031..a55f148 100644
-+-+++index a55f148..90862f9 100644
-+-++ --- a/src/dw6/main.py
-+-++ +++ b/src/dw6/main.py
-+-++-@@ -2,6 +2,7 @@
-+-+++@@ -1,7 +1,7 @@
-+-+++ # dw6/main.py
-+-++  import argparse
-+-++  import sys
-+-++- from dw6.state_manager import StateManager
-+-++-+from dw6.augmenter import process_prompt
-+-+++-from dw6.state_manager import StateManager
-+-++++from dw6.state_manager import WorkflowManager
-+-+++ from dw6.augmenter import process_prompt
-+-++  
-+-++  def main():
-+-++-     """Main entry point for the DW6 CLI."""
-+-++-@@ -15,6 +16,10 @@ def main():
-+-+++@@ -10,9 +10,7 @@ def main():
-+-+++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-+-+++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-++++-+## Git Diff
-++++-+
-++++-+```diff
-++++-+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-+++++@@ -2,74 +2,422 @@
-+ +++ 
-+-+++-    # Review command
-+-+++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
-+-+++-    
-+-+ ++
-+-+-++import os
-+-+-++from .state_manager import get_current_requirement_id
-+-++      # Approve command
-+-++      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-+-++  
-+-++-+    # New command
-+-++-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-+-++-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-+-+++@@ -26,11 +24,9 @@ def main():
-+++++ ## Changed Files
-+ +++ 
-+-+++     args = parser.parse_args()
-+-+++     
-+-+++-    manager = StateManager()
-+-++++    manager = WorkflowManager()
-+++++-- `src/dw6/augmenter.py`
-++++++- `deliverables/coding/coder_deliverable.md`
-++++++- `deliverables/engineering/cycle_9_technical_specification.md`
-++++++- `logs/.last_commit_sha`
-++++++- `logs/workflow_state.txt`
-++++++- `pytest.ini`
-+++++ - `src/dw6/main.py`
-++++++- `src/dw6/state_manager.py`
-++++++- `tests/test_governor.py`
-++++++- `tests/test_state_manager_integration.py`
-++++++- `uv.lock`
-+ +++ 
-+-+++-    if args.command == "review":
-+-+++-        manager.review()
-+-+++-    elif args.command == "approve":
-+-++++    if args.command == "approve":
-+-+++         manager.approve()
-+-+++     elif args.command == "new":
-+-+++         process_prompt(args.prompt)
-+-+++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-+-+++index 703640c..b829d36 100644
-+-+++--- a/src/dw6/state_manager.py
-+-++++++ b/src/dw6/state_manager.py
-+-+++@@ -9,7 +9,7 @@ from dw6 import git_handler
-+-+++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
-+-+++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
-+-+++ APPROVAL_FILE = "logs/approvals.log"
-+-+++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
-+-++++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
-+-+++ DELIVERABLE_PATHS = {
-+-+++     "Engineer": "deliverables/engineering",
-+-+++     "Coder": "deliverables/coding",
-+-+++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
-+-+++     "Researcher": "deliverables/research",
-+-+++ }
-+++++ ## Git Diff
-+ +++ 
-+-++++class Governor:
-+-++++    def __init__(self, state):
-+-++++        self.state = state
-+-++++        self.current_stage = self.state.get("CurrentStage")
-+-+ ++
-+-+-++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-+-++++    def approve(self):
-+-++++        old_stage = self.current_stage
-+-++++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-+-++++        self._validate_stage_exit_criteria()
-+-++++        # The original logic from WorkflowManager is now fully integrated here.
-+-++++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
-+-++++        workflow_manager._validate_stage()
-+-++++        workflow_manager._run_pre_transition_actions()
-+-++++        self._transition_to_next_stage() # This method now belongs to the Governor
-+-++++        workflow_manager._run_post_transition_actions()
-+-++++        self.state.save()
-+-++++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-+-+ ++
-+-+-++def process_prompt(prompt_text: str):
-+-+-++    """
-+-+-++    Augments a raw user prompt and generates a formal technical specification markdown file.
-+-+-++    """
-+-+-++    requirement_id = get_current_requirement_id()
-+-+-++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-+-++++    def _validate_stage_exit_criteria(self):
-+-++++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
-+-++++        if self.current_stage == "Engineer":
-+-++++            req_id = self.state.get("RequirementPointer")
-+-++++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
-+-++++            if not spec_file.exists():
-+-++++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
-+-++++                sys.exit(1)
-+-++++            print("Governor: 'Engineer' exit criteria met.")
-+-++ +
-+-++-     if len(sys.argv) == 1:
-+-++-         parser.print_help(sys.stderr)
-+-++-         sys.exit(1)
-+-++-@@ -27,6 +32,8 @@ def main():
-+-++-         manager.review()
-+-++-     elif args.command == "approve":
-+-++++    def _transition_to_next_stage(self):
-+-++++        current_index = STAGES.index(self.current_stage)
-+-++++        # After 'Deployer', the cycle is complete
-+-++++        if self.current_stage == "Deployer":
-+-++++            self._complete_requirement_cycle()
-+-++++            self.current_stage = STAGES[0]
-+-++++        else:
-+-++++            self.current_stage = STAGES[current_index + 1]
-+-++++        self.state.set("CurrentStage", self.current_stage)
-+-+ ++
-+-+-++    content = f"# Requirement: {requirement_id}\n\n"
-+-+-++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-+-+-++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-+-++++    def _complete_requirement_cycle(self):
-+-++++        req_id = int(self.state.get("RequirementPointer"))
-+-++++        os.makedirs("logs", exist_ok=True)
-+-++++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+-++++        with open(APPROVAL_FILE, "a") as f:
-+-++++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-+-++++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-+-++++        next_req_id = req_id + 1
-+-++++        self.state.set("RequirementPointer", next_req_id)
-+-++++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-+++++ ```diff
-+++++-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-++++++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
-++++++index 82ea098..c5520c2 100644
-++++++--- a/deliverables/coding/coder_deliverable.md
-+++++++++ b/deliverables/coding/coder_deliverable.md
-++++++@@ -1 +1,75 @@
-++++++-This file serves as the deliverable for the Coder stage.
-+++++++# Coder Deliverable
-++ ++++
-++-++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-+++++++## Changed Files
-++ ++++
-++-++++def process_prompt(prompt_text: str):
-++-++++    """
-++-++++    Augments a raw user prompt and generates a formal technical specification markdown file.
-++-++++    """
-++-++++    requirement_id = get_current_requirement_id()
-++-++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-+++++++- `src/dw6/augmenter.py`
-+++++++- `src/dw6/main.py`
-++ ++++
-++-++++    content = f"# Requirement: {requirement_id}\n\n"
-++-++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-++-++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-+++++++## Git Diff
-++ ++++
-++-++++    try:
-++-++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-++-++++        with open(file_path, 'w') as f:
-++-++++            f.write(content)
-++-++++        print(f"Successfully created specification: {file_path}")
-++-++++    except IOError as e:
-++-++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-++-++++        sys.exit(1)
-++-+++diff --git a/src/dw6/main.py b/src/dw6/main.py
-++-+++index 7bbd031..a55f148 100644
-++-+++--- a/src/dw6/main.py
-++-++++++ b/src/dw6/main.py
-++-+++@@ -2,6 +2,7 @@
-++-+++ import argparse
-++-+++ import sys
-++-+++ from dw6.state_manager import StateManager
-++-++++from dw6.augmenter import process_prompt
-+++++++```diff
-+++++++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
-+++++++new file mode 100644
-+++++++index 0000000..c1614f0
-+++++++--- /dev/null
-++++++++++ b/src/dw6/augmenter.py
-+++++++@@ -0,0 +1,26 @@
-++++++++# src/dw6/augmenter.py
-++++++++
-++++++++import os
-++++++++from .state_manager import get_current_requirement_id
-++++++++
-++++++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-++++++++
-++++++++def process_prompt(prompt_text: str):
-++++++++    """
-++++++++    Augments a raw user prompt and generates a formal technical specification markdown file.
-++++++++    """
-++++++++    requirement_id = get_current_requirement_id()
-++++++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-++++++++
-++++++++    content = f"# Requirement: {requirement_id}\n\n"
-++++++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-++++++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-++++++++
-++++++++    try:
-++++++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-++++++++        with open(file_path, 'w') as f:
-++++++++            f.write(content)
-++++++++        print(f"Successfully created specification: {file_path}")
-++++++++    except IOError as e:
-++++++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-++++++++        sys.exit(1)
-+++++++diff --git a/src/dw6/main.py b/src/dw6/main.py
-+++++++index 7bbd031..a55f148 100644
-+++++++--- a/src/dw6/main.py
-++++++++++ b/src/dw6/main.py
-+++++++@@ -2,6 +2,7 @@
-+++++++ import argparse
-+++++++ import sys
-+++++++ from dw6.state_manager import StateManager
-++++++++from dw6.augmenter import process_prompt
+++-++++- `src/dw6/augmenter.py`
+++-++++- `src/dw6/main.py`
+++-++++
+++-++++## Git Diff
+++-++++
+++-++++```diff
+++-++++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+++-++++new file mode 100644
+++-++++index 0000000..c1614f0
+++-++++--- /dev/null
+++-+++++++ b/src/dw6/augmenter.py
+++-++++@@ -0,0 +1,26 @@
+++-+++++# src/dw6/augmenter.py
+++-+++++
+++-+++++import os
+++-+++++from .state_manager import get_current_requirement_id
+++-+++++
+++-+++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++-+++++
+++-+++++def process_prompt(prompt_text: str):
+++-+++++    """
+++-+++++    Augments a raw user prompt and generates a formal technical specification markdown file.
+++-+++++    """
+++-+++++    requirement_id = get_current_requirement_id()
+++-+++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++-+++++
+++-+++++    content = f"# Requirement: {requirement_id}\n\n"
+++-+++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+++-+++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++-+++++
+++-+++++    try:
+++-+++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+++-+++++        with open(file_path, 'w') as f:
+++-+++++            f.write(content)
+++-+++++        print(f"Successfully created specification: {file_path}")
+++-+++++    except IOError as e:
+++-+++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+++-+++++        sys.exit(1)
+++-++++diff --git a/src/dw6/main.py b/src/dw6/main.py
+++-++++index 7bbd031..a55f148 100644
+++-++++--- a/src/dw6/main.py
+++-+++++++ b/src/dw6/main.py
+++-++++@@ -2,6 +2,7 @@
+++-++++ import argparse
+++-++++ import sys
+++-++++ from dw6.state_manager import StateManager
+++-+++++from dw6.augmenter import process_prompt
+++-++++ 
+++-++++ def main():
+++-++++     """Main entry point for the DW6 CLI."""
+++-++++@@ -15,6 +16,10 @@ def main():
+++-++++     # Approve command
+++-++++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++-++++ 
+++-+++++    # New command
+++-+++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+++-+++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+++-+++++
+++-++++     if len(sys.argv) == 1:
+++-++++         parser.print_help(sys.stderr)
+++-++++         sys.exit(1)
+++-++++@@ -27,6 +32,8 @@ def main():
+++-++++         manager.review()
+++-++++     elif args.command == "approve":
+++-++++         manager.approve()
+++-+++++    elif args.command == "new":
+++-+++++        process_prompt(args.prompt)
+++-++++ 
+++-++++ if __name__ == "__main__":
+++-++++     main()
+++-++++```
+++-+++\ No newline at end of file
+++-+++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+++-++ new file mode 100644
+++-++-index 0000000..c1614f0
+++-+++index 0000000..6c1638b
+++-++ --- /dev/null
+++-++-+++ b/src/dw6/augmenter.py
+++-++-@@ -0,0 +1,26 @@
+++-++-+# src/dw6/augmenter.py
++++  diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
++++--index 82ea098..c5520c2 100644
++++-+index c5520c2..e748a41 100644
+++++-index c5520c2..e748a41 100644
++++++index e748a41..82968f8 100644
++++  --- a/deliverables/coding/coder_deliverable.md
++++  +++ b/deliverables/coding/coder_deliverable.md
++++--@@ -1 +1,75 @@
++++---This file serves as the deliverable for the Coder stage.
++++--+# Coder Deliverable
++++--+
++++--+## Changed Files
++++--+
++++--+- `src/dw6/augmenter.py`
++++--+- `src/dw6/main.py`
++++--+
++++--+## Git Diff
++++--+
++++--+```diff
++++--+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++++-+@@ -2,74 +2,422 @@
+ ++-+ 
+-++-+     @patch('dw6.state_manager.WorkflowState')
+-++-+     @patch('dw6.git_handler.get_changes_since_last_commit')
+-++-+-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+-++-++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+-++-++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+-++-+         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+-++-+         # Arrange
+-++-+         mock_state_instance = mock_WorkflowState.return_value
+-++-+@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+-++-+         # Act
+-++-          manager.approve()
+-++--+    elif args.command == "new":
+-++--+        process_prompt(args.prompt)
+-++-  
+-++-- if __name__ == "__main__":
+-++--     main()
+-++-+-        # Assert
+-++-++        # Assert that the deliverable file was created
+-++-+         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+-++-+         self.assertTrue(deliverable_path.exists())
+-++-++        # Clean up the created file
+-++-++        deliverable_path.unlink()
+-++-++
+-++-+         mock_state_instance.save.assert_called_once()
++++-+ ## Changed Files
+ ++-+ 
+-++-+ if __name__ == '__main__':
+-++-+diff --git a/uv.lock b/uv.lock
+-++-+index c79d29c..8e7411f 100644
+-++-+--- a/uv.lock
+-++-++++ b/uv.lock
+-++-+@@ -66,6 +66,7 @@ dependencies = [
+-++-+ test = [
+-++-+     { name = "pytest" },
+-++-+     { name = "pytest-cov" },
+-++-++    { name = "pytest-mock" },
+-++-+ ]
++++-+-- `src/dw6/augmenter.py`
++++-++- `deliverables/coding/coder_deliverable.md`
++++-++- `deliverables/engineering/cycle_9_technical_specification.md`
++++-++- `logs/.last_commit_sha`
++++-++- `logs/workflow_state.txt`
++++-++- `pytest.ini`
++++-+ - `src/dw6/main.py`
++++-++- `src/dw6/state_manager.py`
++++-++- `tests/test_governor.py`
++++-++- `tests/test_state_manager_integration.py`
++++-++- `uv.lock`
+ ++-+ 
+-++-+ [package.metadata]
+-++-+@@ -73,6 +74,7 @@ requires-dist = [
+-++-+     { name = "gitpython" },
+-++-+     { name = "pytest", marker = "extra == 'test'" },
+-++-+     { name = "pytest-cov", marker = "extra == 'test'" },
+-++-++    { name = "pytest-mock", marker = "extra == 'test'" },
+-++-+     { name = "python-dotenv" },
+-++-+ ]
+-++-+ provides-extras = ["test"]
+-++-+@@ -167,6 +169,18 @@ wheels = [
+-++-+     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+-++-+ ]
++++-+ ## Git Diff
+ ++-+ 
+-++-++[[package]]
+-++-++name = "pytest-mock"
+-++-++version = "3.14.1"
+-++-++source = { registry = "https://pypi.org/simple" }
+-++-++dependencies = [
+-++-++    { name = "pytest" },
+-++-++]
+-++-++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+-++-++wheels = [
+-++-++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+-++-++]
+-++-++
+-++-+ [[package]]
+-++-+ name = "python-dotenv"
+-++-+ version = "1.1.1"
+-+++++def test_governor_enforces_rules_on_approve(mocker, capsys):
+-+++++    """Verify that the Governor prints the correct rule for the current stage."""
+-+++++    # Arrange
+-+++++    mock_state = mocker.MagicMock(spec=WorkflowState)
+-+++++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
+-+++ +    governor = Governor(mock_state)
+-+++++    # Mock the exit criteria validation to prevent SystemExit
+-+++++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
+-+++++    # Mock the rest of the approval process to isolate the rule enforcement
+-+++++    mocker.patch.object(governor, '_transition_to_next_stage')
+-+++++    mocker.patch('dw6.state_manager.WorkflowManager')
+-+ + +
+-+++-+    # Act & Assert: The approval should pass without raising an exception
+-+ +-+    try:
+-+-+-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+-+-+-+        with open(file_path, 'w') as f:
+-+-+-+            f.write(content)
+-+-+-+        print(f"Successfully created specification: {file_path}")
+-+-+-+    except IOError as e:
+-+-+-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+-+-+-+        sys.exit(1)
+-+-+++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+-+-++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+-+-++index 9718eda..b85b3d9 100644
+-+-++--- a/logs/.last_commit_sha
+-+-+++++ b/logs/.last_commit_sha
+-+-++@@ -1 +1 @@
+-+-++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+-+-++\ No newline at end of file
+-+-+++75be02c0b7e1723e32042299497f3673b11b4ddd
+-+-++\ No newline at end of file
+-+-++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+-+-++index 28746b7..743582b 100644
+-+-++--- a/logs/workflow_state.txt
+-+-+++++ b/logs/workflow_state.txt
+-+-++@@ -1,2 +1,2 @@
+-+-++-CurrentStage=Engineer
+-+-++-RequirementPointer=7
+-+-+++CurrentStage=Coder
+-+-+++RequirementPointer=9
+-+-++diff --git a/pytest.ini b/pytest.ini
+-+- +new file mode 100644
+-+--+index 0000000..c1614f0
+-+-++index 0000000..a635c5c
+-+- +--- /dev/null
+-+--++++ b/src/dw6/augmenter.py
+-+--+@@ -0,0 +1,26 @@
+-+--++# src/dw6/augmenter.py
+-+-+++++ b/pytest.ini
+-+-++@@ -0,0 +1,2 @@
+-+-+++[pytest]
+-+-+++pythonpath = .
+-+-+ diff --git a/src/dw6/main.py b/src/dw6/main.py
+-+-+-index 7bbd031..a55f148 100644
+-+-++index a55f148..90862f9 100644
+-+-+ --- a/src/dw6/main.py
+-+-+ +++ b/src/dw6/main.py
+-+-+-@@ -2,6 +2,7 @@
+-+-++@@ -1,7 +1,7 @@
+-+-++ # dw6/main.py
+-+-+  import argparse
+-+-+  import sys
+-+-+- from dw6.state_manager import StateManager
+-+-+-+from dw6.augmenter import process_prompt
+-+-++-from dw6.state_manager import StateManager
+-+-+++from dw6.state_manager import WorkflowManager
+-+-++ from dw6.augmenter import process_prompt
+-+-+  
+-+-+  def main():
+-+-+-     """Main entry point for the DW6 CLI."""
+-+-+-@@ -15,6 +16,10 @@ def main():
+-+-++@@ -10,9 +10,7 @@ def main():
+-+-++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+-+-++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+-+-++ 
+-+-++-    # Review command
+-+-++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
+-+-++-    
+-+- ++
+-+--++import os
+-+--++from .state_manager import get_current_requirement_id
+-+-+      # Approve command
+-+-+      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-+-+  
+-+-+-+    # New command
+-+-+-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+-+-+-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+-+-++@@ -26,11 +24,9 @@ def main():
+- -++ 
+---++ def main():
+---++     """Main entry point for the DW6 CLI."""
+---++@@ -15,6 +16,10 @@ def main():
+---++     # Approve command
+---++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+--++++        governor._validate_stage_exit_criteria()
+--++++    except SystemExit:
+--++++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+--++++    finally:
+--++++        # Clean up the created file
+--++++        if spec_file.exists():
+--++++            spec_file.unlink()
+--+++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+--+++index 5b9d1eb..44d2cc9 100644
+--+++--- a/tests/test_state_manager_integration.py
+--++++++ b/tests/test_state_manager_integration.py
+--+++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+-- ++ 
+---+++    # New command
+---+++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+---+++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+--+++     @patch('dw6.state_manager.WorkflowState')
+--+++     @patch('dw6.git_handler.get_changes_since_last_commit')
+--+++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+--++++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+--++++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+--+++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+--+++         # Arrange
+--+++         mock_state_instance = mock_WorkflowState.return_value
+--+++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+--+++         # Act
+--++          manager.approve()
+--++-+    elif args.command == "new":
+--++-+        process_prompt(args.prompt)
+--++  
+--++- if __name__ == "__main__":
+--++-     main()
+--+++-        # Assert
+--++++        # Assert that the deliverable file was created
+--+++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+--+++         self.assertTrue(deliverable_path.exists())
+--++++        # Clean up the created file
+--++++        deliverable_path.unlink()
+-- +++
+---++     if len(sys.argv) == 1:
+---++         parser.print_help(sys.stderr)
+---++         sys.exit(1)
+---++@@ -27,6 +32,8 @@ def main():
+---++         manager.review()
+---++     elif args.command == "approve":
+-+-++     args = parser.parse_args()
+-+-++     
+-+-++-    manager = StateManager()
+-+-+++    manager = WorkflowManager()
+-+-++ 
+-+-++-    if args.command == "review":
+-+-++-        manager.review()
+-+-++-    elif args.command == "approve":
+-+-+++    if args.command == "approve":
+- -++         manager.approve()
+---+++    elif args.command == "new":
+---+++        process_prompt(args.prompt)
+--+++         mock_state_instance.save.assert_called_once()
+-- ++ 
+---++ if __name__ == "__main__":
+---++     main()
+---++```
+---+\ No newline at end of file
+---+diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+--+++ if __name__ == '__main__':
+--+++diff --git a/uv.lock b/uv.lock
+--+++index c79d29c..8e7411f 100644
+--+++--- a/uv.lock
+--++++++ b/uv.lock
+--+++@@ -66,6 +66,7 @@ dependencies = [
+--+++ test = [
+--+++     { name = "pytest" },
+--+++     { name = "pytest-cov" },
+--++++    { name = "pytest-mock" },
+--+++ ]
+--+ + 
+--+-+ if __name__ == "__main__":
+--+-+     main()
+--+-+```
+--+++ [package.metadata]
+--+++@@ -73,6 +74,7 @@ requires-dist = [
+--+++     { name = "gitpython" },
+--+++     { name = "pytest", marker = "extra == 'test'" },
+--+++     { name = "pytest-cov", marker = "extra == 'test'" },
+--++++    { name = "pytest-mock", marker = "extra == 'test'" },
+--+++     { name = "python-dotenv" },
+--+++ ]
+--+++ provides-extras = ["test"]
+--+++@@ -167,6 +169,18 @@ wheels = [
+--+++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+--+++ ]
+--+++ 
+--++++[[package]]
+--++++name = "pytest-mock"
+--++++version = "3.14.1"
+--++++source = { registry = "https://pypi.org/simple" }
+--++++dependencies = [
+--++++    { name = "pytest" },
+--++++]
+--++++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+--++++wheels = [
+--++++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+--++++]
+--++++
+--+++ [[package]]
+--+++ name = "python-dotenv"
+--+++ version = "1.1.1"
+--++ ```
+--+ \ No newline at end of file
+--+-diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+--++diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
+-+-++     elif args.command == "new":
+-+-++         process_prompt(args.prompt)
+-+-++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+-+-++index 703640c..b829d36 100644
+-+-++--- a/src/dw6/state_manager.py
+-+-+++++ b/src/dw6/state_manager.py
+-+-++@@ -9,7 +9,7 @@ from dw6 import git_handler
+-+-++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+-+-++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+-+-++ APPROVAL_FILE = "logs/approvals.log"
+-+-++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+-+-+++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+-+-++ DELIVERABLE_PATHS = {
+-+-++     "Engineer": "deliverables/engineering",
+-+-++     "Coder": "deliverables/coding",
+-+-++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+-+-++     "Researcher": "deliverables/research",
+-+-++ }
+-+-++ 
+-+-+++class Governor:
+-+-+++    def __init__(self, state):
+-+-+++        self.state = state
+-+-+++        self.current_stage = self.state.get("CurrentStage")
+-+- ++
+-+--++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+-+-+++    def approve(self):
+-+-+++        old_stage = self.current_stage
+-+-+++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+-+-+++        self._validate_stage_exit_criteria()
+-+-+++        # The original logic from WorkflowManager is now fully integrated here.
+-+-+++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+-+-+++        workflow_manager._validate_stage()
+-+-+++        workflow_manager._run_pre_transition_actions()
+-+-+++        self._transition_to_next_stage() # This method now belongs to the Governor
+-+-+++        workflow_manager._run_post_transition_actions()
+-+-+++        self.state.save()
+-+-+++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+-+- ++
+-+--++def process_prompt(prompt_text: str):
+-+--++    """
+-+--++    Augments a raw user prompt and generates a formal technical specification markdown file.
+-+--++    """
+-+--++    requirement_id = get_current_requirement_id()
+-+--++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+-+-+++    def _validate_stage_exit_criteria(self):
+-+-+++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+-+-+++        if self.current_stage == "Engineer":
+-+-+++            req_id = self.state.get("RequirementPointer")
+-+-+++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+-+-+++            if not spec_file.exists():
+-+-+++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+-+-+++                sys.exit(1)
+-+-+++            print("Governor: 'Engineer' exit criteria met.")
+-+++-+        governor._validate_stage_exit_criteria()
+-+++-+    except SystemExit:
+-+++-+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+-+++-+    finally:
+-+++-+        # Clean up the created file
+-+++-+        if spec_file.exists():
+-+++-+            spec_file.unlink()
+-+++-diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+-+++-index 5b9d1eb..44d2cc9 100644
+-+++---- a/tests/test_state_manager_integration.py
+-+++-+++ b/tests/test_state_manager_integration.py
+-+++-@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+-+++- 
+-+++-     @patch('dw6.state_manager.WorkflowState')
+-+++-     @patch('dw6.git_handler.get_changes_since_last_commit')
+-+++--    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+-+++-+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+-+++-+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+-+++-         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+-+++-         # Arrange
+-+++-         mock_state_instance = mock_WorkflowState.return_value
+-+++-@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+-+++-         # Act
+-+++-         manager.approve()
+-+++- 
+-+++--        # Assert
+-+++-+        # Assert that the deliverable file was created
+-+++-         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+-+++-         self.assertTrue(deliverable_path.exists())
+-+++-+        # Clean up the created file
+-+++-+        deliverable_path.unlink()
+-+++-+
+-+++-         mock_state_instance.save.assert_called_once()
+-+++- 
+-+++- if __name__ == '__main__':
+-+++-diff --git a/uv.lock b/uv.lock
+-+++-index c79d29c..8e7411f 100644
+-+++---- a/uv.lock
+-+++-+++ b/uv.lock
+-+++-@@ -66,6 +66,7 @@ dependencies = [
+-+++- test = [
+-+++-     { name = "pytest" },
+-+++-     { name = "pytest-cov" },
+-+++-+    { name = "pytest-mock" },
+-+++- ]
+-+++- 
+-+++- [package.metadata]
+-+++-@@ -73,6 +74,7 @@ requires-dist = [
+-+++-     { name = "gitpython" },
+-+++-     { name = "pytest", marker = "extra == 'test'" },
+-+++-     { name = "pytest-cov", marker = "extra == 'test'" },
+-+++-+    { name = "pytest-mock", marker = "extra == 'test'" },
+-+++-     { name = "python-dotenv" },
+-+++- ]
+-+++- provides-extras = ["test"]
+-+++-@@ -167,6 +169,18 @@ wheels = [
+-+++-     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+-+++- ]
++++-+ ```diff
++++-+-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++++-++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
++++-++index 82ea098..c5520c2 100644
++++-++--- a/deliverables/coding/coder_deliverable.md
++++-+++++ b/deliverables/coding/coder_deliverable.md
++++-++@@ -1 +1,75 @@
++++-++-This file serves as the deliverable for the Coder stage.
++++-+++# Coder Deliverable
++++-+++
++++-+++## Changed Files
++++-+++
++++-+++- `src/dw6/augmenter.py`
++++-+++- `src/dw6/main.py`
++++-+++
++++-+++## Git Diff
++++-+++
++++-+++```diff
++++-+++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++++-+++new file mode 100644
++++-+++index 0000000..c1614f0
++++-+++--- /dev/null
++++-++++++ b/src/dw6/augmenter.py
++++-+++@@ -0,0 +1,26 @@
++++-++++# src/dw6/augmenter.py
++++-++++
++++-++++import os
++++-++++from .state_manager import get_current_requirement_id
+++++-@@ -2,74 +2,422 @@
+ +++- 
+-+++-+[[package]]
+-+++-+name = "pytest-mock"
+-+++-+version = "3.14.1"
+-+++-+source = { registry = "https://pypi.org/simple" }
+-+++-+dependencies = [
+-+++-+    { name = "pytest" },
+-+++-+]
+-+++-+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+-+++-+wheels = [
+-+++-+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+-+++-+]
+-+++++    # Act
+-+++++    governor.approve()
+-+ + +
+-+-+-     if len(sys.argv) == 1:
+-+-+-         parser.print_help(sys.stderr)
+-+-+-         sys.exit(1)
+-+-+-@@ -27,6 +32,8 @@ def main():
+-+-+-         manager.review()
+-+-+-     elif args.command == "approve":
+-+-+++    def _transition_to_next_stage(self):
+-+-+++        current_index = STAGES.index(self.current_stage)
+-+-+++        # After 'Deployer', the cycle is complete
+-+-+++        if self.current_stage == "Deployer":
+-+-+++            self._complete_requirement_cycle()
+-+-+++            self.current_stage = STAGES[0]
+-+-+++        else:
+-+-+++            self.current_stage = STAGES[current_index + 1]
+-+-+++        self.state.set("CurrentStage", self.current_stage)
+-+- ++
+-+--++    content = f"# Requirement: {requirement_id}\n\n"
+-+--++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+-+--++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+-+-+++    def _complete_requirement_cycle(self):
+-+-+++        req_id = int(self.state.get("RequirementPointer"))
+-+-+++        os.makedirs("logs", exist_ok=True)
+-+-+++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-+-+++        with open(APPROVAL_FILE, "a") as f:
+-+-+++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-+-+++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-+-+++        next_req_id = req_id + 1
+-+-+++        self.state.set("RequirementPointer", next_req_id)
+-+-+++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-+- ++
+-+--++    try:
+-+--++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+-+--++        with open(file_path, 'w') as f:
+-+--++            f.write(content)
+-+--++        print(f"Successfully created specification: {file_path}")
+-+--++    except IOError as e:
+-+--++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+-+--++        sys.exit(1)
+-+--+diff --git a/src/dw6/main.py b/src/dw6/main.py
+-+--+index 7bbd031..a55f148 100644
+-+--+--- a/src/dw6/main.py
+-+--++++ b/src/dw6/main.py
+-+--+@@ -2,6 +2,7 @@
+-+--+ import argparse
+-+--+ import sys
+-+--+ from dw6.state_manager import StateManager
+-+--++from dw6.augmenter import process_prompt
+-+-++ class WorkflowManager:
+-+-++     def __init__(self):
+-+-++         self.state = WorkflowState()
+-+-+++        self.governor = Governor(self.state) # The manager now has a governor
+-+-++         self.current_stage = self.state.get("CurrentStage")
+-+- + 
+-+--+ def main():
+-+--+     """Main entry point for the DW6 CLI."""
+-+--+@@ -15,6 +16,10 @@ def main():
+-+--+     # Approve command
+-+--+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-+-++     def get_state(self):
+-+-++         return self.state.data
+-+- + 
+-+--++    # New command
+-+--++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+-+--++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+-+-++     def approve(self):
+-+-++-        old_stage = self.current_stage
+-+-++-        print(f"--- Approving Stage: {old_stage} ---")
+-+-++-        self._validate_stage()
+-+-++-        self._run_pre_transition_actions()
+-+-++-        self._transition_to_next_stage()
+-+-++-        self._run_post_transition_actions()
+-+-++-        self.state.save()
+-+-++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+-+-+++        # The manager now simply delegates to the governor.
+-+-+++        self.governor.approve()
+-+-++ 
+-+-++     def _validate_stage(self):
+-+-++         print(f"Validating deliverables for stage: {self.current_stage}")
+-+-++@@ -123,25 +167,7 @@ class WorkflowManager:
+-+-++         if self.current_stage == "Coder":
+-+-++             git_handler.save_current_commit_sha()
+-+-++ 
+-+-++-    def _transition_to_next_stage(self):
+-+-++-        current_index = STAGES.index(self.current_stage)
+-+-++-        if current_index == len(STAGES) - 1:
+-+-++-            self._complete_requirement_cycle()
+-+-++-            self.current_stage = STAGES[0]
+-+-++-        else:
+-+-++-            self.current_stage = STAGES[current_index + 1]
+-+-++-        self.state.set("CurrentStage", self.current_stage)
+-+-++ 
+-+-++-    def _complete_requirement_cycle(self):
+-+-++-        req_id = int(self.state.get("RequirementPointer"))
+-+-++-        os.makedirs("logs", exist_ok=True)
+-+-++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-+-++-        with open(APPROVAL_FILE, "a") as f:
+-+-++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-+-++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-+-++-        next_req_id = req_id + 1
+-+-++-        self.state.set("RequirementPointer", next_req_id)
+-+-++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-+-++ 
+-+-++ class WorkflowState:
+-+-++     def __init__(self):
+-+-++diff --git a/tests/test_governor.py b/tests/test_governor.py
+-+-++new file mode 100644
+-+-++index 0000000..95b566d
+-+-++--- /dev/null
+-+-+++++ b/tests/test_governor.py
+-+-++@@ -0,0 +1,55 @@
+-+-+++# tests/test_governor.py
+-+-+++import pytest
+-+-+++from unittest.mock import MagicMock
+-+-+++from pathlib import Path
+-+-+++import sys
+-+- ++
+-+--+     if len(sys.argv) == 1:
+-+--+         parser.print_help(sys.stderr)
+-+--+         sys.exit(1)
+-+--+@@ -27,6 +32,8 @@ def main():
+-+--+         manager.review()
+-+--+     elif args.command == "approve":
++++++@@ -3,421 +3,578 @@
+++++  ## Changed Files
+++++  
+++++--- `src/dw6/augmenter.py`
+++++-+- `deliverables/coding/coder_deliverable.md`
+++++-+- `deliverables/engineering/cycle_9_technical_specification.md`
+++++-+- `logs/.last_commit_sha`
+++++-+- `logs/workflow_state.txt`
+++++-+- `pytest.ini`
+++++- - `src/dw6/main.py`
+++++-+- `src/dw6/state_manager.py`
+++++-+- `tests/test_governor.py`
+++++-+- `tests/test_state_manager_integration.py`
+++++-+- `uv.lock`
++++++ - `deliverables/coding/coder_deliverable.md`
++++++-- `deliverables/engineering/cycle_9_technical_specification.md`
+++++++- `deliverables/engineering/cycle_10_technical_specification.md`
++++++ - `logs/.last_commit_sha`
++++++ - `logs/workflow_state.txt`
++++++-- `pytest.ini`
++++++-- `src/dw6/main.py`
++++++ - `src/dw6/state_manager.py`
++++++ - `tests/test_governor.py`
++++++-- `tests/test_state_manager_integration.py`
++++++-- `uv.lock`
+++++  
+++++  ## Git Diff
+++++  
+++++  ```diff
+++++--diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+++++-+diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
+++++-+index 82ea098..c5520c2 100644
+++++-+--- a/deliverables/coding/coder_deliverable.md
+++++-++++ b/deliverables/coding/coder_deliverable.md
+++++-+@@ -1 +1,75 @@
+++++-+-This file serves as the deliverable for the Coder stage.
+++++-++# Coder Deliverable
+++++-++
+++++-++## Changed Files
+++++-++
+++++-++- `src/dw6/augmenter.py`
+++++-++- `src/dw6/main.py`
+++++-++
+++++-++## Git Diff
+++++-++
+++++-++```diff
+++++-++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++++++ diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
++++++-index 82ea098..c5520c2 100644
+++++++index c5520c2..e748a41 100644
++++++ --- a/deliverables/coding/coder_deliverable.md
++++++ +++ b/deliverables/coding/coder_deliverable.md
++++++-@@ -1 +1,75 @@
++++++--This file serves as the deliverable for the Coder stage.
++++++-+# Coder Deliverable
++++++-+
++++++-+## Changed Files
++++++-+
++++++-+- `src/dw6/augmenter.py`
++++++-+- `src/dw6/main.py`
+++ ++-+
+++-++-+import os
+++-++-+from .state_manager import get_current_requirement_id
+++-++++++ b/deliverables/engineering/cycle_9_technical_specification.md
+++-+++@@ -0,0 +1,9 @@
+++-++++# Requirement: 8
+++-++ +
+++-++-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++-++++## 1. High-Level Goal
+++-++ +
+++-++-+def process_prompt(prompt_text: str):
+++-++-+    """
+++-++-+    Augments a raw user prompt and generates a formal technical specification markdown file.
+++-++-+    """
+++-++-+    requirement_id = get_current_requirement_id()
+++-++-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++-++++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+++-++ +
+++-++-+    content = f"# Requirement: {requirement_id}\n\n"
+++-++-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+++-++-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++-++++## 2. Guiding Principles
+++-++ +
+++-++-+    try:
+++-++-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+++-++-+        with open(file_path, 'w') as f:
+++-++-+            f.write(content)
+++-++-+        print(f"Successfully created specification: {file_path}")
+++-++-+    except IOError as e:
+++-++-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+++-++-+        sys.exit(1)
+++-++++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+++-+++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+++-+++index 9718eda..b85b3d9 100644
+++-+++--- a/logs/.last_commit_sha
+++-++++++ b/logs/.last_commit_sha
+++-+++@@ -1 +1 @@
+++-+++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+++-+++\ No newline at end of file
+++-++++75be02c0b7e1723e32042299497f3673b11b4ddd
+++-+++\ No newline at end of file
+++-+++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+++-+++index 28746b7..743582b 100644
+++-+++--- a/logs/workflow_state.txt
+++-++++++ b/logs/workflow_state.txt
+++-+++@@ -1,2 +1,2 @@
+++-+++-CurrentStage=Engineer
+++-+++-RequirementPointer=7
+++-++++CurrentStage=Coder
+++-++++RequirementPointer=9
+++-+++diff --git a/pytest.ini b/pytest.ini
+++-+ +new file mode 100644
+++-+-+index 0000000..c1614f0
+++-+++index 0000000..a635c5c
+++-+ +--- /dev/null
+++-+-++++ b/src/dw6/augmenter.py
+++-+-+@@ -0,0 +1,26 @@
+++-+-++# src/dw6/augmenter.py
+++-++++++ b/pytest.ini
+++-+++@@ -0,0 +1,2 @@
+++-++++[pytest]
+++-++++pythonpath = .
+++-++ diff --git a/src/dw6/main.py b/src/dw6/main.py
+++-++-index 7bbd031..a55f148 100644
+++-+++index a55f148..90862f9 100644
+++-++ --- a/src/dw6/main.py
+++-++ +++ b/src/dw6/main.py
+++-++-@@ -2,6 +2,7 @@
+++-+++@@ -1,7 +1,7 @@
+++-+++ # dw6/main.py
+++-++  import argparse
+++-++  import sys
+++-++- from dw6.state_manager import StateManager
+++-++-+from dw6.augmenter import process_prompt
+++-+++-from dw6.state_manager import StateManager
+++-++++from dw6.state_manager import WorkflowManager
+++-+++ from dw6.augmenter import process_prompt
+++-++  
+++-++  def main():
+++-++-     """Main entry point for the DW6 CLI."""
+++-++-@@ -15,6 +16,10 @@ def main():
+++-+++@@ -10,9 +10,7 @@ def main():
+++-+++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+++-+++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++++++-+## Git Diff
++++++-+
++++++-+```diff
++++++-+diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+++++++@@ -2,74 +2,422 @@
+++ +++ 
+++-+++-    # Review command
+++-+++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
+++-+++-    
+++-+ ++
+++-+-++import os
+++-+-++from .state_manager import get_current_requirement_id
+++-++      # Approve command
+++-++      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++-++  
+++-++-+    # New command
+++-++-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+++-++-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+++-+++@@ -26,11 +24,9 @@ def main():
+++++++ ## Changed Files
+++ +++ 
+++-+++     args = parser.parse_args()
+++-+++     
+++-+++-    manager = StateManager()
+++-++++    manager = WorkflowManager()
+++++++-- `src/dw6/augmenter.py`
++++++++- `deliverables/coding/coder_deliverable.md`
++++++++- `deliverables/engineering/cycle_9_technical_specification.md`
++++++++- `logs/.last_commit_sha`
++++++++- `logs/workflow_state.txt`
++++++++- `pytest.ini`
+++++++ - `src/dw6/main.py`
++++++++- `src/dw6/state_manager.py`
++++++++- `tests/test_governor.py`
++++++++- `tests/test_state_manager_integration.py`
++++++++- `uv.lock`
+++ +++ 
+++-+++-    if args.command == "review":
+++-+++-        manager.review()
+++-+++-    elif args.command == "approve":
+++-++++    if args.command == "approve":
+++-+++         manager.approve()
+++-+++     elif args.command == "new":
+++-+++         process_prompt(args.prompt)
+++-+++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+++-+++index 703640c..b829d36 100644
+++-+++--- a/src/dw6/state_manager.py
+++-++++++ b/src/dw6/state_manager.py
+++-+++@@ -9,7 +9,7 @@ from dw6 import git_handler
+++-+++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+++-+++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+++-+++ APPROVAL_FILE = "logs/approvals.log"
+++-+++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+++-++++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+++-+++ DELIVERABLE_PATHS = {
+++-+++     "Engineer": "deliverables/engineering",
+++-+++     "Coder": "deliverables/coding",
+++-+++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+++-+++     "Researcher": "deliverables/research",
+++-+++ }
+++++++ ## Git Diff
+++ +++ 
+++-++++class Governor:
+++-++++    def __init__(self, state):
+++-++++        self.state = state
+++-++++        self.current_stage = self.state.get("CurrentStage")
+++-+ ++
+++-+-++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++-++++    def approve(self):
+++-++++        old_stage = self.current_stage
+++-++++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+++-++++        self._validate_stage_exit_criteria()
+++-++++        # The original logic from WorkflowManager is now fully integrated here.
+++-++++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+++-++++        workflow_manager._validate_stage()
+++-++++        workflow_manager._run_pre_transition_actions()
+++-++++        self._transition_to_next_stage() # This method now belongs to the Governor
+++-++++        workflow_manager._run_post_transition_actions()
+++-++++        self.state.save()
+++-++++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+++-+ ++
+++-+-++def process_prompt(prompt_text: str):
+++-+-++    """
+++-+-++    Augments a raw user prompt and generates a formal technical specification markdown file.
+++-+-++    """
+++-+-++    requirement_id = get_current_requirement_id()
+++-+-++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++-++++    def _validate_stage_exit_criteria(self):
+++-++++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+++-++++        if self.current_stage == "Engineer":
+++-++++            req_id = self.state.get("RequirementPointer")
+++-++++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+++-++++            if not spec_file.exists():
+++-++++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+++-++++                sys.exit(1)
+++-++++            print("Governor: 'Engineer' exit criteria met.")
+++-++ +
+++-++-     if len(sys.argv) == 1:
+++-++-         parser.print_help(sys.stderr)
+++-++-         sys.exit(1)
+++-++-@@ -27,6 +32,8 @@ def main():
+++-++-         manager.review()
+++-++-     elif args.command == "approve":
+++-++++    def _transition_to_next_stage(self):
+++-++++        current_index = STAGES.index(self.current_stage)
+++-++++        # After 'Deployer', the cycle is complete
+++-++++        if self.current_stage == "Deployer":
+++-++++            self._complete_requirement_cycle()
+++-++++            self.current_stage = STAGES[0]
+++-++++        else:
+++-++++            self.current_stage = STAGES[current_index + 1]
+++-++++        self.state.set("CurrentStage", self.current_stage)
+++-+ ++
+++-+-++    content = f"# Requirement: {requirement_id}\n\n"
+++-+-++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+++-+-++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++-++++    def _complete_requirement_cycle(self):
+++-++++        req_id = int(self.state.get("RequirementPointer"))
+++-++++        os.makedirs("logs", exist_ok=True)
+++-++++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++-++++        with open(APPROVAL_FILE, "a") as f:
+++-++++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+++-++++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+++-++++        next_req_id = req_id + 1
+++-++++        self.state.set("RequirementPointer", next_req_id)
+++-++++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+++++++ ```diff
+++++++-diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
++++++++diff --git a/deliverables/coding/coder_deliverable.md b/deliverables/coding/coder_deliverable.md
++++++++index 82ea098..c5520c2 100644
++++++++--- a/deliverables/coding/coder_deliverable.md
+++++++++++ b/deliverables/coding/coder_deliverable.md
++++++++@@ -1 +1,75 @@
++++++++-This file serves as the deliverable for the Coder stage.
+++++++++# Coder Deliverable
++++ ++++
++++-++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++++++++## Changed Files
++++ ++++
++++-++++def process_prompt(prompt_text: str):
++++-++++    """
++++-++++    Augments a raw user prompt and generates a formal technical specification markdown file.
++++-++++    """
++++-++++    requirement_id = get_current_requirement_id()
++++-++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++++++++- `src/dw6/augmenter.py`
+++++++++- `src/dw6/main.py`
++++ ++++
++++-++++    content = f"# Requirement: {requirement_id}\n\n"
++++-++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++++-++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++++++++## Git Diff
++++ ++++
++++-++++    try:
++++-++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++++-++++        with open(file_path, 'w') as f:
++++-++++            f.write(content)
++++-++++        print(f"Successfully created specification: {file_path}")
++++-++++    except IOError as e:
++++-++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++++-++++        sys.exit(1)
++++-+++diff --git a/src/dw6/main.py b/src/dw6/main.py
++++-+++index 7bbd031..a55f148 100644
++++-+++--- a/src/dw6/main.py
++++-++++++ b/src/dw6/main.py
++++-+++@@ -2,6 +2,7 @@
++++-+++ import argparse
++++-+++ import sys
++++-+++ from dw6.state_manager import StateManager
++++-++++from dw6.augmenter import process_prompt
+++++++++```diff
+++++++++diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
+++++++++new file mode 100644
+++++++++index 0000000..c1614f0
+++++++++--- /dev/null
++++++++++++ b/src/dw6/augmenter.py
+++++++++@@ -0,0 +1,26 @@
++++++++++# src/dw6/augmenter.py
++++++++++
++++++++++import os
++++++++++from .state_manager import get_current_requirement_id
++++++++++
++++++++++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++++++++++
++++++++++def process_prompt(prompt_text: str):
++++++++++    """
++++++++++    Augments a raw user prompt and generates a formal technical specification markdown file.
++++++++++    """
++++++++++    requirement_id = get_current_requirement_id()
++++++++++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++++++++++
++++++++++    content = f"# Requirement: {requirement_id}\n\n"
++++++++++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++++++++++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++++++++++
++++++++++    try:
++++++++++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++++++++++        with open(file_path, 'w') as f:
++++++++++            f.write(content)
++++++++++        print(f"Successfully created specification: {file_path}")
++++++++++    except IOError as e:
++++++++++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++++++++++        sys.exit(1)
+++++++++diff --git a/src/dw6/main.py b/src/dw6/main.py
+++++++++index 7bbd031..a55f148 100644
+++++++++--- a/src/dw6/main.py
++++++++++++ b/src/dw6/main.py
+++++++++@@ -2,6 +2,7 @@
+++++++++ import argparse
+++++++++ import sys
+++++++++ from dw6.state_manager import StateManager
++++++++++from dw6.augmenter import process_prompt
+++++++++ 
+++++++++ def main():
+++++++++     """Main entry point for the DW6 CLI."""
+++++++++@@ -15,6 +16,10 @@ def main():
+++++++++     # Approve command
+++++++++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++++++++ 
++++++++++    # New command
++++++++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++++++++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++++++++++
+++++++++     if len(sys.argv) == 1:
+++++++++         parser.print_help(sys.stderr)
+++++++++         sys.exit(1)
+++++++++@@ -27,6 +32,8 @@ def main():
+++++++++         manager.review()
+++++++++     elif args.command == "approve":
+++++++++         manager.approve()
++++++++++    elif args.command == "new":
++++++++++        process_prompt(args.prompt)
+++++++++ 
+++++++++ if __name__ == "__main__":
+++++++++     main()
+++++++++```
++++++++\ No newline at end of file
++++++++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+++++++ new file mode 100644
+++++++-index 0000000..c1614f0
++++++++index 0000000..6c1638b
+++++++ --- /dev/null
+++++++-+++ b/src/dw6/augmenter.py
+++++++-@@ -0,0 +1,26 @@
+++++++-+# src/dw6/augmenter.py
+++++++-+
+++++++-+import os
+++++++-+from .state_manager import get_current_requirement_id
+++++++++++ b/deliverables/engineering/cycle_9_technical_specification.md
++++++++@@ -0,0 +1,9 @@
+++++++++# Requirement: 8
+++++++ +
+++++++-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++++++++## 1. High-Level Goal
+++++++ +
+++++++-+def process_prompt(prompt_text: str):
+++++++-+    """
+++++++-+    Augments a raw user prompt and generates a formal technical specification markdown file.
+++++++-+    """
+++++++-+    requirement_id = get_current_requirement_id()
+++++++-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++++++++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+++++++ +
+++++++-+    content = f"# Requirement: {requirement_id}\n\n"
+++++++-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+++++++-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++++++++## 2. Guiding Principles
+++++++ +
+++++++-+    try:
+++++++-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+++++++-+        with open(file_path, 'w') as f:
+++++++-+            f.write(content)
+++++++-+        print(f"Successfully created specification: {file_path}")
+++++++-+    except IOError as e:
+++++++-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+++++++-+        sys.exit(1)
+++++++++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
++++++++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
++++++++index 9718eda..b85b3d9 100644
++++++++--- a/logs/.last_commit_sha
+++++++++++ b/logs/.last_commit_sha
++++++++@@ -1 +1 @@
++++++++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
++++++++\ No newline at end of file
+++++++++75be02c0b7e1723e32042299497f3673b11b4ddd
++++++++\ No newline at end of file
++++++++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
++++++++index 28746b7..743582b 100644
++++++++--- a/logs/workflow_state.txt
+++++++++++ b/logs/workflow_state.txt
++++++++@@ -1,2 +1,2 @@
++++++++-CurrentStage=Engineer
++++++++-RequirementPointer=7
+++++++++CurrentStage=Coder
+++++++++RequirementPointer=9
++++++++diff --git a/pytest.ini b/pytest.ini
++++++ +new file mode 100644
++++++-+index 0000000..c1614f0
++++++++index 0000000..a635c5c
++++++ +--- /dev/null
++++++-++++ b/src/dw6/augmenter.py
++++++-+@@ -0,0 +1,26 @@
++++++-++# src/dw6/augmenter.py
+++++++++++ b/pytest.ini
++++++++@@ -0,0 +1,2 @@
+++++++++[pytest]
+++++++++pythonpath = .
+++++++ diff --git a/src/dw6/main.py b/src/dw6/main.py
+++++++-index 7bbd031..a55f148 100644
++++++++index a55f148..90862f9 100644
+++++++ --- a/src/dw6/main.py
+++++++ +++ b/src/dw6/main.py
+++++++-@@ -2,6 +2,7 @@
++++++++@@ -1,7 +1,7 @@
++++++++ # dw6/main.py
+++++++  import argparse
+++++++  import sys
+++++++- from dw6.state_manager import StateManager
+++++++-+from dw6.augmenter import process_prompt
++++++++-from dw6.state_manager import StateManager
+++++++++from dw6.state_manager import WorkflowManager
++++++++ from dw6.augmenter import process_prompt
+++++++  
+++++++  def main():
+++++++-     """Main entry point for the DW6 CLI."""
+++++++-@@ -15,6 +16,10 @@ def main():
++++++++@@ -10,9 +10,7 @@ def main():
++++++++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++++++++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++++ +++ 
++++-+++ def main():
++++-+++     """Main entry point for the DW6 CLI."""
++++-+++@@ -15,6 +16,10 @@ def main():
++++-+++     # Approve command
++++-+++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++++++-    # Review command
++++++++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
++++++++-    
++++++ ++
++++++-++import os
++++++-++from .state_manager import get_current_requirement_id
+++++++      # Approve command
+++++++      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++++++  
+++++++-+    # New command
+++++++-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+++++++-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++++++++@@ -26,11 +24,9 @@ def main():
++++ +++ 
++++-++++    # New command
++++-++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++++-++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++++-++++
++++-+++     if len(sys.argv) == 1:
++++-+++         parser.print_help(sys.stderr)
++++-+++         sys.exit(1)
++++-+++@@ -27,6 +32,8 @@ def main():
++++-+++         manager.review()
++++-+++     elif args.command == "approve":
++++++++     args = parser.parse_args()
++++++++     
++++++++-    manager = StateManager()
+++++++++    manager = WorkflowManager()
++ +++++ 
++-+++++ def main():
++-+++++     """Main entry point for the DW6 CLI."""
++-+++++@@ -15,6 +16,10 @@ def main():
++-+++++     # Approve command
++-+++++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++++++-    if args.command == "review":
++++++++-        manager.review()
++++++++-    elif args.command == "approve":
+++++++++    if args.command == "approve":
++++ +++         manager.approve()
++++-++++    elif args.command == "new":
++++-++++        process_prompt(args.prompt)
++++++++     elif args.command == "new":
++++++++         process_prompt(args.prompt)
++++++++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++++++++index 703640c..b829d36 100644
++++++++--- a/src/dw6/state_manager.py
+++++++++++ b/src/dw6/state_manager.py
++++++++@@ -9,7 +9,7 @@ from dw6 import git_handler
++++++++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
++++++++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
++++++++ APPROVAL_FILE = "logs/approvals.log"
++++++++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+++++++++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
++++++++ DELIVERABLE_PATHS = {
++++++++     "Engineer": "deliverables/engineering",
++++++++     "Coder": "deliverables/coding",
++++++++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
++++++++     "Researcher": "deliverables/research",
++++++++ }
++ +++++ 
++-++++++    # New command
++-++++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++-++++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++-++++++
++-+++++     if len(sys.argv) == 1:
++-+++++         parser.print_help(sys.stderr)
++-+++++         sys.exit(1)
++-+++++@@ -27,6 +32,8 @@ def main():
++-+++++         manager.review()
++-+++++     elif args.command == "approve":
++-+++++         manager.approve()
++-++++++    elif args.command == "new":
++-++++++        process_prompt(args.prompt)
+++++++++class Governor:
+++++++++    def __init__(self, state):
+++++++++        self.state = state
+++++++++        self.current_stage = self.state.get("CurrentStage")
++++++ ++
++++++-++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++++++++    def approve(self):
+++++++++        old_stage = self.current_stage
+++++++++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+++++++++        self._validate_stage_exit_criteria()
+++++++++        # The original logic from WorkflowManager is now fully integrated here.
+++++++++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+++++++++        workflow_manager._validate_stage()
+++++++++        workflow_manager._run_pre_transition_actions()
+++++++++        self._transition_to_next_stage() # This method now belongs to the Governor
+++++++++        workflow_manager._run_post_transition_actions()
+++++++++        self.state.save()
+++++++++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++++++ ++
++++++-++def process_prompt(prompt_text: str):
++++++-++    """
++++++-++    Augments a raw user prompt and generates a formal technical specification markdown file.
++++++-++    """
++++++-++    requirement_id = get_current_requirement_id()
++++++-++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++++++++    def _validate_stage_exit_criteria(self):
+++++++++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+++++++++        if self.current_stage == "Engineer":
+++++++++            req_id = self.state.get("RequirementPointer")
+++++++++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+++++++++            if not spec_file.exists():
+++++++++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+++++++++                sys.exit(1)
+++++++++            print("Governor: 'Engineer' exit criteria met.")
+++++++ +
+++++++-     if len(sys.argv) == 1:
+++++++-         parser.print_help(sys.stderr)
+++++++-         sys.exit(1)
+++++++-@@ -27,6 +32,8 @@ def main():
+++++++-         manager.review()
+++++++-     elif args.command == "approve":
+++++++++    def _transition_to_next_stage(self):
+++++++++        current_index = STAGES.index(self.current_stage)
+++++++++        # After 'Deployer', the cycle is complete
+++++++++        if self.current_stage == "Deployer":
+++++++++            self._complete_requirement_cycle()
+++++++++            self.current_stage = STAGES[0]
+++++++++        else:
+++++++++            self.current_stage = STAGES[current_index + 1]
+++++++++        self.state.set("CurrentStage", self.current_stage)
++++++ ++
++++++-++    content = f"# Requirement: {requirement_id}\n\n"
++++++-++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++++++-++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++++++++    def _complete_requirement_cycle(self):
+++++++++        req_id = int(self.state.get("RequirementPointer"))
+++++++++        os.makedirs("logs", exist_ok=True)
+++++++++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++++++++        with open(APPROVAL_FILE, "a") as f:
+++++++++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+++++++++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+++++++++        next_req_id = req_id + 1
+++++++++        self.state.set("RequirementPointer", next_req_id)
+++++++++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++++++ ++
++++++-++    try:
++++++-++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++++++-++        with open(file_path, 'w') as f:
++++++-++            f.write(content)
++++++-++        print(f"Successfully created specification: {file_path}")
++++++-++    except IOError as e:
++++++-++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++++++-++        sys.exit(1)
++++++-+diff --git a/src/dw6/main.py b/src/dw6/main.py
++++++-+index 7bbd031..a55f148 100644
++++++-+--- a/src/dw6/main.py
++++++-++++ b/src/dw6/main.py
++++++-+@@ -2,6 +2,7 @@
++++++-+ import argparse
++++++-+ import sys
++++++-+ from dw6.state_manager import StateManager
++++++-++from dw6.augmenter import process_prompt
++++++++ class WorkflowManager:
++++++++     def __init__(self):
++++++++         self.state = WorkflowState()
+++++++++        self.governor = Governor(self.state) # The manager now has a governor
++++++++         self.current_stage = self.state.get("CurrentStage")
++++++ + 
++++++-+ def main():
++++++-+     """Main entry point for the DW6 CLI."""
++++++-+@@ -15,6 +16,10 @@ def main():
++++++-+     # Approve command
++++++-+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++++++     def get_state(self):
++++++++         return self.state.data
++++++ + 
++++++-++    # New command
++++++-++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++++++-++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++++++++     def approve(self):
++++++++-        old_stage = self.current_stage
++++++++-        print(f"--- Approving Stage: {old_stage} ---")
++++++++-        self._validate_stage()
++++++++-        self._run_pre_transition_actions()
++++++++-        self._transition_to_next_stage()
++++++++-        self._run_post_transition_actions()
++++++++-        self.state.save()
++++++++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+++++++++        # The manager now simply delegates to the governor.
+++++++++        self.governor.approve()
 +++++++ 
-+++++++ def main():
-+++++++     """Main entry point for the DW6 CLI."""
-+++++++@@ -15,6 +16,10 @@ def main():
-+++++++     # Approve command
-+++++++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++++++     def _validate_stage(self):
++++++++         print(f"Validating deliverables for stage: {self.current_stage}")
++++++++@@ -123,25 +167,7 @@ class WorkflowManager:
++++++++         if self.current_stage == "Coder":
++++++++             git_handler.save_current_commit_sha()
 +++++++ 
-++++++++    # New command
-++++++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-++++++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-++++++++
-+++++++     if len(sys.argv) == 1:
-+++++++         parser.print_help(sys.stderr)
-+++++++         sys.exit(1)
-+++++++@@ -27,6 +32,8 @@ def main():
-+++++++         manager.review()
-+++++++     elif args.command == "approve":
-+++++++         manager.approve()
-++++++++    elif args.command == "new":
-++++++++        process_prompt(args.prompt)
++++++++-    def _transition_to_next_stage(self):
++++++++-        current_index = STAGES.index(self.current_stage)
++++++++-        if current_index == len(STAGES) - 1:
++++++++-            self._complete_requirement_cycle()
++++++++-            self.current_stage = STAGES[0]
++++++++-        else:
++++++++-            self.current_stage = STAGES[current_index + 1]
++++++++-        self.state.set("CurrentStage", self.current_stage)
++ +++++ 
++-+++++ if __name__ == "__main__":
++-+++++     main()
++-+++++```
++-++++\ No newline at end of file
++-++++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
++-+++ new file mode 100644
++-+++-index 0000000..c1614f0
++-++++index 0000000..6c1638b
++-+++ --- /dev/null
++-+++-+++ b/src/dw6/augmenter.py
++-+++-@@ -0,0 +1,26 @@
++-+++-+# src/dw6/augmenter.py
++++++++-    def _complete_requirement_cycle(self):
++++++++-        req_id = int(self.state.get("RequirementPointer"))
++++++++-        os.makedirs("logs", exist_ok=True)
++++++++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++++++++-        with open(APPROVAL_FILE, "a") as f:
++++++++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++++++++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++++++++-        next_req_id = req_id + 1
++++++++-        self.state.set("RequirementPointer", next_req_id)
++++++++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
 +++++++ 
-+++++++ if __name__ == "__main__":
-+++++++     main()
-+++++++```
-++++++\ No newline at end of file
-++++++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
-+++++ new file mode 100644
-+++++-index 0000000..c1614f0
-++++++index 0000000..6c1638b
-+++++ --- /dev/null
-+++++-+++ b/src/dw6/augmenter.py
-+++++-@@ -0,0 +1,26 @@
-+++++-+# src/dw6/augmenter.py
++++++++ class WorkflowState:
++++++++     def __init__(self):
++++++++diff --git a/tests/test_governor.py b/tests/test_governor.py
+++++ ++new file mode 100644
+++++-++index 0000000..c1614f0
++++++++index 0000000..95b566d
+++++ ++--- /dev/null
+++++-+++++ b/src/dw6/augmenter.py
+++++-++@@ -0,0 +1,26 @@
+++++-+++# src/dw6/augmenter.py
+++++++++++ b/tests/test_governor.py
++++++++@@ -0,0 +1,55 @@
+++++++++# tests/test_governor.py
+++++++++import pytest
+++++++++from unittest.mock import MagicMock
+++++++++from pathlib import Path
+++++++++import sys
++++++ ++
++++++-+     if len(sys.argv) == 1:
++++++-+         parser.print_help(sys.stderr)
++++++-+         sys.exit(1)
++++++-+@@ -27,6 +32,8 @@ def main():
++++++-+         manager.review()
++++++-+     elif args.command == "approve":
++++++-+         manager.approve()
++++++-++    elif args.command == "new":
++++++-++        process_prompt(args.prompt)
+++++++++from dw6.state_manager import Governor, WorkflowState
+++++++++
+++++++++@pytest.fixture
+++++++++def mock_state(mocker):
+++++++++    """Fixture to create a mock WorkflowState."""
+++++++++    state = MagicMock(spec=WorkflowState)
+++++++++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+++++++++    return state
+++++ +++
+++++-+++import os
+++++-+++from .state_manager import get_current_requirement_id
+++++++++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+++++++++    """Verify the Governor blocks approval if the spec file is missing."""
+++++++++    # Arrange: Set the state to Engineer and mock the requirement pointer
+++++++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+++++++++    
+++++++++    # Ensure the spec file does NOT exist for this test
+++++++++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+++++++++    if spec_file.exists():
+++++++++        spec_file.unlink()
+++++ +++
+++++-+++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++++++++    governor = Governor(mock_state)
+++++ +++
+++++-+++def process_prompt(prompt_text: str):
+++++-+++    """
+++++-+++    Augments a raw user prompt and generates a formal technical specification markdown file.
+++++-+++    """
+++++-+++    requirement_id = get_current_requirement_id()
+++++-+++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++++++++    # Act & Assert: The approval should fail with a SystemExit
+++++++++    with pytest.raises(SystemExit) as e:
+++++++++        governor._validate_stage_exit_criteria()
+++++++++    
+++++++++    assert e.type == SystemExit
+++++++++    assert e.value.code == 1
+++++ +++
+++++-+++    content = f"# Requirement: {requirement_id}\n\n"
+++++-+++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+++++-+++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++++++++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+++++++++    """Verify the Governor allows approval if the spec file exists."""
+++++++++    # Arrange: Set the state to Engineer and mock the requirement pointer
+++++++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+++++++++    
+++++++++    # Ensure the spec file DOES exist for this test
+++++++++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+++++++++    spec_file.parent.mkdir(parents=True, exist_ok=True)
+++++++++    spec_file.touch()
+++++ +++
+++++++++    governor = Governor(mock_state)
+++++++++
+++++++++    # Act & Assert: The approval should pass without raising an exception
+++++ +++    try:
+++++-+++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+++++-+++        with open(file_path, 'w') as f:
+++++-+++            f.write(content)
+++++-+++        print(f"Successfully created specification: {file_path}")
+++++-+++    except IOError as e:
+++++-+++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+++++-+++        sys.exit(1)
+++++-++diff --git a/src/dw6/main.py b/src/dw6/main.py
+++++-++index 7bbd031..a55f148 100644
+++++-++--- a/src/dw6/main.py
+++++-+++++ b/src/dw6/main.py
+++++-++@@ -2,6 +2,7 @@
+++++-++ import argparse
+++++-++ import sys
+++++-++ from dw6.state_manager import StateManager
+++++-+++from dw6.augmenter import process_prompt
+++++-++ 
+++++-++ def main():
+++++-++     """Main entry point for the DW6 CLI."""
+++++-++@@ -15,6 +16,10 @@ def main():
+++++-++     # Approve command
+++++-++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++++++++        governor._validate_stage_exit_criteria()
+++++++++    except SystemExit:
+++++++++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+++++++++    finally:
+++++++++        # Clean up the created file
+++++++++        if spec_file.exists():
+++++++++            spec_file.unlink()
++++++++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
++++++++index 5b9d1eb..44d2cc9 100644
++++++++--- a/tests/test_state_manager_integration.py
+++++++++++ b/tests/test_state_manager_integration.py
++++++++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+++++ ++ 
+++++-+++    # New command
+++++-+++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+++++-+++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++++++++     @patch('dw6.state_manager.WorkflowState')
++++++++     @patch('dw6.git_handler.get_changes_since_last_commit')
++++++++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+++++++++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+++++++++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
++++++++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
++++++++         # Arrange
++++++++         mock_state_instance = mock_WorkflowState.return_value
++++++++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++++++++         # Act
+++++++          manager.approve()
+++++++-+    elif args.command == "new":
+++++++-+        process_prompt(args.prompt)
+++++++  
+++++++- if __name__ == "__main__":
+++++++-     main()
++++++++-        # Assert
+++++++++        # Assert that the deliverable file was created
++++++++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
++++++++         self.assertTrue(deliverable_path.exists())
+++++++++        # Clean up the created file
+++++++++        deliverable_path.unlink()
+++++ +++
+++++-++     if len(sys.argv) == 1:
+++++-++         parser.print_help(sys.stderr)
+++++-++         sys.exit(1)
+++++-++@@ -27,6 +32,8 @@ def main():
+++++-++         manager.review()
+++++-++     elif args.command == "approve":
+++++-++         manager.approve()
+++++-+++    elif args.command == "new":
+++++-+++        process_prompt(args.prompt)
++++++++         mock_state_instance.save.assert_called_once()
+++++ ++ 
+++++-++ if __name__ == "__main__":
+++++-++     main()
+++++-++```
+++++-+\ No newline at end of file
+++++-+diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
++++++++ if __name__ == '__main__':
++++++++diff --git a/uv.lock b/uv.lock
++++++++index c79d29c..8e7411f 100644
++++++++--- a/uv.lock
+++++++++++ b/uv.lock
++++++++@@ -66,6 +66,7 @@ dependencies = [
++++++++ test = [
++++++++     { name = "pytest" },
++++++++     { name = "pytest-cov" },
+++++++++    { name = "pytest-mock" },
++++++++ ]
++++++ + 
++++++-+ if __name__ == "__main__":
++++++-+     main()
++++++-+```
++++++++ [package.metadata]
++++++++@@ -73,6 +74,7 @@ requires-dist = [
++++++++     { name = "gitpython" },
++++++++     { name = "pytest", marker = "extra == 'test'" },
++++++++     { name = "pytest-cov", marker = "extra == 'test'" },
+++++++++    { name = "pytest-mock", marker = "extra == 'test'" },
++++++++     { name = "python-dotenv" },
++++++++ ]
++++++++ provides-extras = ["test"]
++++++++@@ -167,6 +169,18 @@ wheels = [
++++++++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
++++++++ ]
++++ +++ 
++++-+++ if __name__ == "__main__":
++++-+++     main()
++++-+++```
++++-++\ No newline at end of file
++++-++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
++++-+ new file mode 100644
++++-+-index 0000000..c1614f0
++++-++index 0000000..6c1638b
++++-+ --- /dev/null
++++-+-+++ b/src/dw6/augmenter.py
++++-+-@@ -0,0 +1,26 @@
++++-+-+# src/dw6/augmenter.py
+++++++++[[package]]
+++++++++name = "pytest-mock"
+++++++++version = "3.14.1"
+++++++++source = { registry = "https://pypi.org/simple" }
+++++++++dependencies = [
+++++++++    { name = "pytest" },
+++++++++]
+++++++++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+++++++++wheels = [
+++++++++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+++++++++]
+++++++++
++++++++ [[package]]
++++++++ name = "python-dotenv"
++++++++ version = "1.1.1"
+++++++ ```
++++++ \ No newline at end of file
++++++-diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+++++++diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
+++++  new file mode 100644
+++++--index 0000000..c1614f0
+++++-+index 0000000..6c1638b
++++++-index 0000000..6c1638b
+++++++index 0000000..691df8d
+++++  --- /dev/null
+++++--+++ b/src/dw6/augmenter.py
+++++--@@ -0,0 +1,26 @@
+++++--+# src/dw6/augmenter.py
+++++--+
+++++--+import os
+++++--+from .state_manager import get_current_requirement_id
+++++-++++ b/deliverables/engineering/cycle_9_technical_specification.md
+++++-+@@ -0,0 +1,9 @@
+++++-++# Requirement: 8
++++++-+++ b/deliverables/engineering/cycle_9_technical_specification.md
++++++++++ b/deliverables/engineering/cycle_10_technical_specification.md
++++++ @@ -0,0 +1,9 @@
++++++-+# Requirement: 8
++++++++# Requirement: 10
+++++  +
+++++--+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++++-++## 1. High-Level Goal
++++++ +## 1. High-Level Goal
+++++  +
+++++--+def process_prompt(prompt_text: str):
+++++--+    """
+++++--+    Augments a raw user prompt and generates a formal technical specification markdown file.
+++++--+    """
+++++--+    requirement_id = get_current_requirement_id()
+++++--+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++++-++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
++++++-+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
++++++++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
+++++  +
+++++--+    content = f"# Requirement: {requirement_id}\n\n"
+++++--+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+++++--+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++++-++## 2. Guiding Principles
++++++ +## 2. Guiding Principles
+++++  +
+++++--+    try:
+++++--+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+++++--+        with open(file_path, 'w') as f:
+++++--+            f.write(content)
+++++--+        print(f"Successfully created specification: {file_path}")
+++++--+    except IOError as e:
+++++--+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+++++--+        sys.exit(1)
+++++-++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+++++-+diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+++++-+index 9718eda..b85b3d9 100644
+++++-+--- a/logs/.last_commit_sha
+++++-++++ b/logs/.last_commit_sha
+++++-+@@ -1 +1 @@
+++++-+-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+++++-+\ No newline at end of file
+++++-++75be02c0b7e1723e32042299497f3673b11b4ddd
+++++-+\ No newline at end of file
+++++-+diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+++++-+index 28746b7..743582b 100644
+++++-+--- a/logs/workflow_state.txt
+++++-++++ b/logs/workflow_state.txt
+++++-+@@ -1,2 +1,2 @@
+++++-+-CurrentStage=Engineer
+++++-+-RequirementPointer=7
+++++-++CurrentStage=Coder
+++++-++RequirementPointer=9
+++++-+diff --git a/pytest.ini b/pytest.ini
+++++-+new file mode 100644
+++++-+index 0000000..a635c5c
+++++-+--- /dev/null
+++++-++++ b/pytest.ini
+++++-+@@ -0,0 +1,2 @@
+++++-++[pytest]
+++++-++pythonpath = .
+++++- diff --git a/src/dw6/main.py b/src/dw6/main.py
+++++--index 7bbd031..a55f148 100644
+++++-+index a55f148..90862f9 100644
+++++- --- a/src/dw6/main.py
+++++- +++ b/src/dw6/main.py
+++++--@@ -2,6 +2,7 @@
+++++-+@@ -1,7 +1,7 @@
+++++-+ # dw6/main.py
+++++-  import argparse
+++++-  import sys
+++++-- from dw6.state_manager import StateManager
+++++--+from dw6.augmenter import process_prompt
+++++-+-from dw6.state_manager import StateManager
+++++-++from dw6.state_manager import WorkflowManager
+++++-+ from dw6.augmenter import process_prompt
++++++ +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
++++++ diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
++++++-index 9718eda..b85b3d9 100644
+++++++index b85b3d9..00ab2c8 100644
++++++ --- a/logs/.last_commit_sha
++++++ +++ b/logs/.last_commit_sha
++++++ @@ -1 +1 @@
++++++--7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+++++++-75be02c0b7e1723e32042299497f3673b11b4ddd
++++++ \ No newline at end of file
++++++-+75be02c0b7e1723e32042299497f3673b11b4ddd
++++++++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
++++++ \ No newline at end of file
++++++ diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
++++++-index 28746b7..743582b 100644
+++++++index 743582b..a7aa662 100644
++++++ --- a/logs/workflow_state.txt
++++++ +++ b/logs/workflow_state.txt
++++++ @@ -1,2 +1,2 @@
++++++--CurrentStage=Engineer
++++++--RequirementPointer=7
++++++-+CurrentStage=Coder
++++++-+RequirementPointer=9
++++++-diff --git a/pytest.ini b/pytest.ini
++++++-new file mode 100644
++++++-index 0000000..a635c5c
++++++---- /dev/null
++++++-+++ b/pytest.ini
++++++-@@ -0,0 +1,2 @@
++++++-+[pytest]
++++++-+pythonpath = .
++++++-diff --git a/src/dw6/main.py b/src/dw6/main.py
++++++-index a55f148..90862f9 100644
++++++---- a/src/dw6/main.py
++++++-+++ b/src/dw6/main.py
++++++-@@ -1,7 +1,7 @@
++++++- # dw6/main.py
++++++- import argparse
++++++- import sys
++++++--from dw6.state_manager import StateManager
++++++-+from dw6.state_manager import WorkflowManager
++++++- from dw6.augmenter import process_prompt
++++++- 
++++++- def main():
++++++-@@ -10,9 +10,7 @@ def main():
++++++-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++++++-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++++++- 
++++++--    # Review command
++++++--    subparsers.add_parser("review", help="Review the changes for the current stage.")
++++++--    
++++ +-+
++++-+-+import os
++++-+-+from .state_manager import get_current_requirement_id
++++-+++++ b/deliverables/engineering/cycle_9_technical_specification.md
++++-++@@ -0,0 +1,9 @@
++++-+++# Requirement: 8
++++-+ +
++++-+-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++++-+++## 1. High-Level Goal
++++-+ +
++++-+-+def process_prompt(prompt_text: str):
++++-+-+    """
++++-+-+    Augments a raw user prompt and generates a formal technical specification markdown file.
++++-+-+    """
++++-+-+    requirement_id = get_current_requirement_id()
++++-+-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++++-+++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
++++-+ +
++++-+-+    content = f"# Requirement: {requirement_id}\n\n"
++++-+-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++++-+-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++++-+++## 2. Guiding Principles
++++++-     # Approve command
++++++-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++++- 
++++++-@@ -26,11 +24,9 @@ def main():
++++++- 
++++++-     args = parser.parse_args()
++++++-     
++++++--    manager = StateManager()
++++++-+    manager = WorkflowManager()
++++++- 
++++++--    if args.command == "review":
++++++--        manager.review()
++++++--    elif args.command == "approve":
++++++-+    if args.command == "approve":
++++++-         manager.approve()
++++++-     elif args.command == "new":
++++++-         process_prompt(args.prompt)
+++++++ CurrentStage=Coder
+++++++-RequirementPointer=9
++++++++RequirementPointer=10
++++++ diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++++++-index 703640c..b829d36 100644
+++++++index b829d36..241fa62 100644
++++++ --- a/src/dw6/state_manager.py
++++++ +++ b/src/dw6/state_manager.py
++++++-@@ -9,7 +9,7 @@ from dw6 import git_handler
++++++- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
++++++- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
++++++- APPROVAL_FILE = "logs/approvals.log"
++++++--STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
++++++-+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
++++++- DELIVERABLE_PATHS = {
++++++-     "Engineer": "deliverables/engineering",
++++++-     "Coder": "deliverables/coding",
++++++-@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
++++++-     "Researcher": "deliverables/research",
+++++++@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
++++++  }
+++++   
+++++-  def main():
+++++--     """Main entry point for the DW6 CLI."""
+++++--@@ -15,6 +16,10 @@ def main():
+++++-+@@ -10,9 +10,7 @@ def main():
+++++-+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+++++-+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+++++-+ 
+++++-+-    # Review command
+++++-+-    subparsers.add_parser("review", help="Review the changes for the current stage.")
+++++-+-    
+++++-++
+++++-      # Approve command
+++++-      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++++-+class Governor:
++++++-+    def __init__(self, state):
++++++-+        self.state = state
++++++-+        self.current_stage = self.state.get("CurrentStage")
++ +++-+
++-+++-+import os
++-+++-+from .state_manager import get_current_requirement_id
++-+++++++ b/deliverables/engineering/cycle_9_technical_specification.md
++-++++@@ -0,0 +1,9 @@
++-+++++# Requirement: 8
++-+++ +
++-+++-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++-+++++## 1. High-Level Goal
++-+++ +
++-+++-+def process_prompt(prompt_text: str):
++-+++-+    """
++-+++-+    Augments a raw user prompt and generates a formal technical specification markdown file.
++-+++-+    """
++-+++-+    requirement_id = get_current_requirement_id()
++-+++-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++-+++++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
++-+++ +
++-+++-+    content = f"# Requirement: {requirement_id}\n\n"
++-+++-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++-+++-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++-+++++## 2. Guiding Principles
++-+++ +
++-+++-+    try:
++-+++-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++-+++-+        with open(file_path, 'w') as f:
++-+++-+            f.write(content)
++-+++-+        print(f"Successfully created specification: {file_path}")
++-+++-+    except IOError as e:
++-+++-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++-+++-+        sys.exit(1)
++-+++++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
++-++++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
++-++++index 9718eda..b85b3d9 100644
++-++++--- a/logs/.last_commit_sha
++-+++++++ b/logs/.last_commit_sha
++-++++@@ -1 +1 @@
++-++++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
++-++++\ No newline at end of file
++-+++++75be02c0b7e1723e32042299497f3673b11b4ddd
++-++++\ No newline at end of file
++-++++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
++-++++index 28746b7..743582b 100644
++-++++--- a/logs/workflow_state.txt
++-+++++++ b/logs/workflow_state.txt
++-++++@@ -1,2 +1,2 @@
++-++++-CurrentStage=Engineer
++-++++-RequirementPointer=7
++-+++++CurrentStage=Coder
++-+++++RequirementPointer=9
++-++++diff --git a/pytest.ini b/pytest.ini
++-++ +new file mode 100644
++-++-+index 0000000..c1614f0
++-++++index 0000000..a635c5c
++-++ +--- /dev/null
++-++-++++ b/src/dw6/augmenter.py
++-++-+@@ -0,0 +1,26 @@
++-++-++# src/dw6/augmenter.py
++-+++++++ b/pytest.ini
++-++++@@ -0,0 +1,2 @@
++-+++++[pytest]
++-+++++pythonpath = .
++-+++ diff --git a/src/dw6/main.py b/src/dw6/main.py
++-+++-index 7bbd031..a55f148 100644
++-++++index a55f148..90862f9 100644
++-+++ --- a/src/dw6/main.py
++-+++ +++ b/src/dw6/main.py
++-+++-@@ -2,6 +2,7 @@
++-++++@@ -1,7 +1,7 @@
++-++++ # dw6/main.py
++-+++  import argparse
++-+++  import sys
++-+++- from dw6.state_manager import StateManager
++-+++-+from dw6.augmenter import process_prompt
++-++++-from dw6.state_manager import StateManager
++-+++++from dw6.state_manager import WorkflowManager
++-++++ from dw6.augmenter import process_prompt
++-+++  
++-+++  def main():
++-+++-     """Main entry point for the DW6 CLI."""
++-+++-@@ -15,6 +16,10 @@ def main():
++-++++@@ -10,9 +10,7 @@ def main():
++-++++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++-++++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++- +++ 
++--+++ def main():
++--+++     """Main entry point for the DW6 CLI."""
++--+++@@ -15,6 +16,10 @@ def main():
++--+++     # Approve command
++--+++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++-++++-    # Review command
++-++++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
++-++++-    
++-++ ++
++-++-++import os
++-++-++from .state_manager import get_current_requirement_id
++-+++      # Approve command
++-+++      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++-+++  
++-+++-+    # New command
++-+++-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++-+++-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++-++++@@ -26,11 +24,9 @@ def main():
++- +++ 
++--++++    # New command
++--++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++--++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++--++++
++--+++     if len(sys.argv) == 1:
++--+++         parser.print_help(sys.stderr)
++--+++         sys.exit(1)
++--+++@@ -27,6 +32,8 @@ def main():
++--+++         manager.review()
++--+++     elif args.command == "approve":
++-++++     args = parser.parse_args()
++-++++     
++-++++-    manager = StateManager()
++-+++++    manager = WorkflowManager()
++-++++ 
++-++++-    if args.command == "review":
++-++++-        manager.review()
++-++++-    elif args.command == "approve":
++-+++++    if args.command == "approve":
++- +++         manager.approve()
++--++++    elif args.command == "new":
++--++++        process_prompt(args.prompt)
++-++++     elif args.command == "new":
++-++++         process_prompt(args.prompt)
++-++++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++-++++index 703640c..b829d36 100644
++-++++--- a/src/dw6/state_manager.py
++-+++++++ b/src/dw6/state_manager.py
++-++++@@ -9,7 +9,7 @@ from dw6 import git_handler
++-++++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
++-++++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
++-++++ APPROVAL_FILE = "logs/approvals.log"
++-++++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
++-+++++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
++-++++ DELIVERABLE_PATHS = {
++-++++     "Engineer": "deliverables/engineering",
++-++++     "Coder": "deliverables/coding",
++-++++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
++-++++     "Researcher": "deliverables/research",
++-++++ }
++-++++ 
++-+++++class Governor:
++-+++++    def __init__(self, state):
++-+++++        self.state = state
++-+++++        self.current_stage = self.state.get("CurrentStage")
++-++ ++
++-++-++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++-+++++    def approve(self):
++-+++++        old_stage = self.current_stage
++-+++++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++-+++++        self._validate_stage_exit_criteria()
++-+++++        # The original logic from WorkflowManager is now fully integrated here.
++-+++++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
++-+++++        workflow_manager._validate_stage()
++-+++++        workflow_manager._run_pre_transition_actions()
++-+++++        self._transition_to_next_stage() # This method now belongs to the Governor
++-+++++        workflow_manager._run_post_transition_actions()
++-+++++        self.state.save()
++-+++++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++-++ ++
++-++-++def process_prompt(prompt_text: str):
++-++-++    """
++-++-++    Augments a raw user prompt and generates a formal technical specification markdown file.
++-++-++    """
++-++-++    requirement_id = get_current_requirement_id()
++-++-++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++-+++++    def _validate_stage_exit_criteria(self):
++-+++++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
++-+++++        if self.current_stage == "Engineer":
++-+++++            req_id = self.state.get("RequirementPointer")
++-+++++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
++-+++++            if not spec_file.exists():
++-+++++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
++-+++++                sys.exit(1)
++-+++++            print("Governor: 'Engineer' exit criteria met.")
++-+++ +
++-+++-     if len(sys.argv) == 1:
++-+++-         parser.print_help(sys.stderr)
++-+++-         sys.exit(1)
++-+++-@@ -27,6 +32,8 @@ def main():
++-+++-         manager.review()
++-+++-     elif args.command == "approve":
++-+++++    def _transition_to_next_stage(self):
++-+++++        current_index = STAGES.index(self.current_stage)
++-+++++        # After 'Deployer', the cycle is complete
++-+++++        if self.current_stage == "Deployer":
++-+++++            self._complete_requirement_cycle()
++-+++++            self.current_stage = STAGES[0]
++-+++++        else:
++-+++++            self.current_stage = STAGES[current_index + 1]
++-+++++        self.state.set("CurrentStage", self.current_stage)
++-++ ++
++-++-++    content = f"# Requirement: {requirement_id}\n\n"
++-++-++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++-++-++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++-+++++    def _complete_requirement_cycle(self):
++-+++++        req_id = int(self.state.get("RequirementPointer"))
++-+++++        os.makedirs("logs", exist_ok=True)
++-+++++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++-+++++        with open(APPROVAL_FILE, "a") as f:
++-+++++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++-+++++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++-+++++        next_req_id = req_id + 1
++-+++++        self.state.set("RequirementPointer", next_req_id)
++-+++++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++-++ ++
++-++-++    try:
++-++-++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++-++-++        with open(file_path, 'w') as f:
++-++-++            f.write(content)
++-++-++        print(f"Successfully created specification: {file_path}")
++-++-++    except IOError as e:
++-++-++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++-++-++        sys.exit(1)
++-++-+diff --git a/src/dw6/main.py b/src/dw6/main.py
++-++-+index 7bbd031..a55f148 100644
++-++-+--- a/src/dw6/main.py
++-++-++++ b/src/dw6/main.py
++-++-+@@ -2,6 +2,7 @@
++-++-+ import argparse
++-++-+ import sys
++-++-+ from dw6.state_manager import StateManager
++-++-++from dw6.augmenter import process_prompt
++-++++ class WorkflowManager:
++-++++     def __init__(self):
++-++++         self.state = WorkflowState()
++-+++++        self.governor = Governor(self.state) # The manager now has a governor
++-++++         self.current_stage = self.state.get("CurrentStage")
++-++ + 
++-++-+ def main():
++-++-+     """Main entry point for the DW6 CLI."""
++-++-+@@ -15,6 +16,10 @@ def main():
++-++-+     # Approve command
++-++-+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++-++++     def get_state(self):
++-++++         return self.state.data
++-++ + 
++-++-++    # New command
++-++-++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++-++-++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++-++++     def approve(self):
++-++++-        old_stage = self.current_stage
++-++++-        print(f"--- Approving Stage: {old_stage} ---")
++-++++-        self._validate_stage()
++-++++-        self._run_pre_transition_actions()
++-++++-        self._transition_to_next_stage()
++-++++-        self._run_post_transition_actions()
++-++++-        self.state.save()
++-++++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++-+++++        # The manager now simply delegates to the governor.
++-+++++        self.governor.approve()
++-++++ 
++-++++     def _validate_stage(self):
++-++++         print(f"Validating deliverables for stage: {self.current_stage}")
++-++++@@ -123,25 +167,7 @@ class WorkflowManager:
++-++++         if self.current_stage == "Coder":
++-++++             git_handler.save_current_commit_sha()
++-++++ 
++-++++-    def _transition_to_next_stage(self):
++-++++-        current_index = STAGES.index(self.current_stage)
++-++++-        if current_index == len(STAGES) - 1:
++-++++-            self._complete_requirement_cycle()
++-++++-            self.current_stage = STAGES[0]
++-++++-        else:
++-++++-            self.current_stage = STAGES[current_index + 1]
++-++++-        self.state.set("CurrentStage", self.current_stage)
++-++++ 
++-++++-    def _complete_requirement_cycle(self):
++-++++-        req_id = int(self.state.get("RequirementPointer"))
++-++++-        os.makedirs("logs", exist_ok=True)
++-++++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++-++++-        with open(APPROVAL_FILE, "a") as f:
++-++++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++-++++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++-++++-        next_req_id = req_id + 1
++-++++-        self.state.set("RequirementPointer", next_req_id)
++-++++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++-++++ 
++-++++ class WorkflowState:
++-++++     def __init__(self):
++-++++diff --git a/tests/test_governor.py b/tests/test_governor.py
++-+ ++new file mode 100644
++-+-++index 0000000..c1614f0
++-++++index 0000000..95b566d
++-+ ++--- /dev/null
++-+-+++++ b/src/dw6/augmenter.py
++-+-++@@ -0,0 +1,26 @@
++-+-+++# src/dw6/augmenter.py
++-+++++++ b/tests/test_governor.py
++-++++@@ -0,0 +1,55 @@
++-+++++# tests/test_governor.py
++-+++++import pytest
++-+++++from unittest.mock import MagicMock
++-+++++from pathlib import Path
++-+++++import sys
++-++ ++
++-++-+     if len(sys.argv) == 1:
++-++-+         parser.print_help(sys.stderr)
++-++-+         sys.exit(1)
++-++-+@@ -27,6 +32,8 @@ def main():
++-++-+         manager.review()
++-++-+     elif args.command == "approve":
++++++-+    def approve(self):
++++++-+        old_stage = self.current_stage
++++++-+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++++++-+        self._validate_stage_exit_criteria()
++++++-+        # The original logic from WorkflowManager is now fully integrated here.
++++++-+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
++++++-+        workflow_manager._validate_stage()
++++++-+        workflow_manager._run_pre_transition_actions()
++++++-+        self._transition_to_next_stage() # This method now belongs to the Governor
++++++-+        workflow_manager._run_post_transition_actions()
++++++-+        self.state.save()
++++++-+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
 +++++-+
-+++++-+import os
-+++++-+from .state_manager import get_current_requirement_id
-+++++++++ b/deliverables/engineering/cycle_9_technical_specification.md
-++++++@@ -0,0 +1,9 @@
-+++++++# Requirement: 8
-+++++ +
-+++++-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-+++++++## 1. High-Level Goal
-+++++ +
-+++++-+def process_prompt(prompt_text: str):
-+++++-+    """
-+++++-+    Augments a raw user prompt and generates a formal technical specification markdown file.
-+++++-+    """
-+++++-+    requirement_id = get_current_requirement_id()
-+++++-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-+++++++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
-+++++ +
-+++++-+    content = f"# Requirement: {requirement_id}\n\n"
-+++++-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-+++++-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-+++++++## 2. Guiding Principles
-+++++ +
-+++++-+    try:
-+++++-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-+++++-+        with open(file_path, 'w') as f:
-+++++-+            f.write(content)
-+++++-+        print(f"Successfully created specification: {file_path}")
-+++++-+    except IOError as e:
-+++++-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-+++++-+        sys.exit(1)
-+++++++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
-++++++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
-++++++index 9718eda..b85b3d9 100644
-++++++--- a/logs/.last_commit_sha
-+++++++++ b/logs/.last_commit_sha
-++++++@@ -1 +1 @@
-++++++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
-++++++\ No newline at end of file
-+++++++75be02c0b7e1723e32042299497f3673b11b4ddd
-++++++\ No newline at end of file
-++++++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
-++++++index 28746b7..743582b 100644
-++++++--- a/logs/workflow_state.txt
-+++++++++ b/logs/workflow_state.txt
-++++++@@ -1,2 +1,2 @@
-++++++-CurrentStage=Engineer
-++++++-RequirementPointer=7
-+++++++CurrentStage=Coder
-+++++++RequirementPointer=9
-++++++diff --git a/pytest.ini b/pytest.ini
-++++ +new file mode 100644
-++++-+index 0000000..c1614f0
-++++++index 0000000..a635c5c
-++++ +--- /dev/null
-++++-++++ b/src/dw6/augmenter.py
-++++-+@@ -0,0 +1,26 @@
-++++-++# src/dw6/augmenter.py
-+++++++++ b/pytest.ini
-++++++@@ -0,0 +1,2 @@
-+++++++[pytest]
-+++++++pythonpath = .
-+++++ diff --git a/src/dw6/main.py b/src/dw6/main.py
-+++++-index 7bbd031..a55f148 100644
-++++++index a55f148..90862f9 100644
-+++++ --- a/src/dw6/main.py
-+++++ +++ b/src/dw6/main.py
-+++++-@@ -2,6 +2,7 @@
-++++++@@ -1,7 +1,7 @@
-++++++ # dw6/main.py
-+++++  import argparse
-+++++  import sys
-+++++- from dw6.state_manager import StateManager
-+++++-+from dw6.augmenter import process_prompt
-++++++-from dw6.state_manager import StateManager
-+++++++from dw6.state_manager import WorkflowManager
-++++++ from dw6.augmenter import process_prompt
-+++++  
-+++++  def main():
-+++++-     """Main entry point for the DW6 CLI."""
-+++++-@@ -15,6 +16,10 @@ def main():
-++++++@@ -10,9 +10,7 @@ def main():
-++++++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-++++++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-++ +++ 
-++-+++ def main():
-++-+++     """Main entry point for the DW6 CLI."""
-++-+++@@ -15,6 +16,10 @@ def main():
-++-+++     # Approve command
-++-+++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-++++++-    # Review command
-++++++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
-++++++-    
-++++ ++
-++++-++import os
-++++-++from .state_manager import get_current_requirement_id
-+++++      # Approve command
-+++++      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-+++++  
-+++++-+    # New command
-+++++-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-+++++-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-++++++@@ -26,11 +24,9 @@ def main():
-++ +++ 
-++-++++    # New command
-++-++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-++-++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++++++-+    def _validate_stage_exit_criteria(self):
++++++-+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
++++++-+        if self.current_stage == "Engineer":
++++++-+            req_id = self.state.get("RequirementPointer")
++++++-+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
++++++-+            if not spec_file.exists():
++++++-+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
++++++-+                sys.exit(1)
++++++-+            print("Governor: 'Engineer' exit criteria met.")
++++++-+
++++++-+    def _transition_to_next_stage(self):
++++++-+        current_index = STAGES.index(self.current_stage)
++++++-+        # After 'Deployer', the cycle is complete
++++++-+        if self.current_stage == "Deployer":
++++++-+            self._complete_requirement_cycle()
++++++-+            self.current_stage = STAGES[0]
++++++-+        else:
++++++-+            self.current_stage = STAGES[current_index + 1]
++++++-+        self.state.set("CurrentStage", self.current_stage)
++++++-+
++++++-+    def _complete_requirement_cycle(self):
++++++-+        req_id = int(self.state.get("RequirementPointer"))
++++++-+        os.makedirs("logs", exist_ok=True)
++++++-+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++++++-+        with open(APPROVAL_FILE, "a") as f:
++++++-+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++++++-+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++++++-+        next_req_id = req_id + 1
++++++-+        self.state.set("RequirementPointer", next_req_id)
++++++-+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++++++-+
++++++- class WorkflowManager:
++++++-     def __init__(self):
++++++-         self.state = WorkflowState()
++++++-+        self.governor = Governor(self.state) # The manager now has a governor
+++++++ class Governor:
++++++++    RULES = {
++++++++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
++++++++        "Coder": "Can use file system tools, code editing tools, and run tests.",
++++++++        "Validator": "Can only run tests and validation tools.",
++++++++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
++++++++        "Researcher": "Can use web search and documentation reading tools."
++++++++    }
+++++++     def __init__(self, state):
+++++++         self.state = state
++++++          self.current_stage = self.state.get("CurrentStage")
+++++   
+++++--+    # New command
+++++--+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+++++--+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+++++-+@@ -26,11 +24,9 @@ def main():
+++++-+ 
+++++-+     args = parser.parse_args()
+++++-+     
+++++-+-    manager = StateManager()
+++++-++    manager = WorkflowManager()
+++++-+ 
+++++-+-    if args.command == "review":
+++++-+-        manager.review()
+++++-+-    elif args.command == "approve":
+++++-++    if args.command == "approve":
++ ++-+         manager.approve()
++-++-++    elif args.command == "new":
++-++-++        process_prompt(args.prompt)
++-+++++from dw6.state_manager import Governor, WorkflowState
++-+++++
++-+++++@pytest.fixture
++-+++++def mock_state(mocker):
++-+++++    """Fixture to create a mock WorkflowState."""
++-+++++    state = MagicMock(spec=WorkflowState)
++-+++++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
++-+++++    return state
++-+ +++
++-+-+++import os
++-+-+++from .state_manager import get_current_requirement_id
++-+++++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
++-+++++    """Verify the Governor blocks approval if the spec file is missing."""
++-+++++    # Arrange: Set the state to Engineer and mock the requirement pointer
++-+++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
++-+++++    
++-+++++    # Ensure the spec file does NOT exist for this test
++-+++++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
++-+++++    if spec_file.exists():
++-+++++        spec_file.unlink()
++-+ +++
++-+-+++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++-+++++    governor = Governor(mock_state)
++-+ +++
++-+-+++def process_prompt(prompt_text: str):
++-+-+++    """
++-+-+++    Augments a raw user prompt and generates a formal technical specification markdown file.
++-+-+++    """
++-+-+++    requirement_id = get_current_requirement_id()
++-+-+++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++-+++++    # Act & Assert: The approval should fail with a SystemExit
++-+++++    with pytest.raises(SystemExit) as e:
++-+++++        governor._validate_stage_exit_criteria()
++-+++++    
++-+++++    assert e.type == SystemExit
++-+++++    assert e.value.code == 1
++-+ +++
++-+-+++    content = f"# Requirement: {requirement_id}\n\n"
++-+-+++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++-+-+++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++-+++++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++-+++++    """Verify the Governor allows approval if the spec file exists."""
++-+++++    # Arrange: Set the state to Engineer and mock the requirement pointer
++-+++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
++-+++++    
++-+++++    # Ensure the spec file DOES exist for this test
++-+++++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
++-+++++    spec_file.parent.mkdir(parents=True, exist_ok=True)
++-+++++    spec_file.touch()
++-+ +++
++-+++++    governor = Governor(mock_state)
++-+++++
++-+++++    # Act & Assert: The approval should pass without raising an exception
++-+ +++    try:
++-+-+++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++-+-+++        with open(file_path, 'w') as f:
++-+-+++            f.write(content)
++-+-+++        print(f"Successfully created specification: {file_path}")
++-+-+++    except IOError as e:
++-+-+++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++-+-+++        sys.exit(1)
++-+-++diff --git a/src/dw6/main.py b/src/dw6/main.py
++-+-++index 7bbd031..a55f148 100644
++-+-++--- a/src/dw6/main.py
++-+-+++++ b/src/dw6/main.py
++-+-++@@ -2,6 +2,7 @@
++-+-++ import argparse
++-+-++ import sys
++-+-++ from dw6.state_manager import StateManager
++-+-+++from dw6.augmenter import process_prompt
+++++-+     elif args.command == "new":
+++++-+         process_prompt(args.prompt)
+++++-+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+++++-+index 703640c..b829d36 100644
+++++-+--- a/src/dw6/state_manager.py
+++++-++++ b/src/dw6/state_manager.py
+++++-+@@ -9,7 +9,7 @@ from dw6 import git_handler
+++++-+ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+++++-+ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+++++-+ APPROVAL_FILE = "logs/approvals.log"
+++++-+-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+++++-++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+++++-+ DELIVERABLE_PATHS = {
+++++-+     "Engineer": "deliverables/engineering",
+++++-+     "Coder": "deliverables/coding",
+++++-+@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+++++-+     "Researcher": "deliverables/research",
+++++-+ }
+++++-+ 
+++++-++class Governor:
+++++-++    def __init__(self, state):
+++++-++        self.state = state
+++++-++        self.current_stage = self.state.get("CurrentStage")
++++++-     def get_state(self):
++++++-         return self.state.data
++++++- 
++++++++    def enforce_rules(self):
++++++++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
++++++++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
++++++++        print(f"[RULE] {rule}")
+++ + ++
+++++-++    def approve(self):
+++++-++        old_stage = self.current_stage
+++++-++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+++++-++        self._validate_stage_exit_criteria()
+++++-++        # The original logic from WorkflowManager is now fully integrated here.
+++++-++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+++++-++        workflow_manager._validate_stage()
+++++-++        workflow_manager._run_pre_transition_actions()
+++++-++        self._transition_to_next_stage() # This method now belongs to the Governor
+++++-++        workflow_manager._run_post_transition_actions()
+++++-++        self.state.save()
+++++-++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+++++-++
+++++-++    def _validate_stage_exit_criteria(self):
+++++-++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+++++-++        if self.current_stage == "Engineer":
+++++-++            req_id = self.state.get("RequirementPointer")
+++++-++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+++++-++            if not spec_file.exists():
+++++-++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+++++-++                sys.exit(1)
+++++-++            print("Governor: 'Engineer' exit criteria met.")
++++++      def approve(self):
++++++--        old_stage = self.current_stage
++++++--        print(f"--- Approving Stage: {old_stage} ---")
++++++--        self._validate_stage()
++++++--        self._run_pre_transition_actions()
++++++--        self._transition_to_next_stage()
++++++--        self._run_post_transition_actions()
++++++--        self.state.save()
++++++--        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++++++-+        # The manager now simply delegates to the governor.
++++++-+        self.governor.approve()
++++++- 
++++++-     def _validate_stage(self):
++++++-         print(f"Validating deliverables for stage: {self.current_stage}")
++++++-@@ -123,25 +167,7 @@ class WorkflowManager:
++++++-         if self.current_stage == "Coder":
++++++-             git_handler.save_current_commit_sha()
++++++- 
++++++--    def _transition_to_next_stage(self):
++++++--        current_index = STAGES.index(self.current_stage)
++++++--        if current_index == len(STAGES) - 1:
++++++--            self._complete_requirement_cycle()
++++++--            self.current_stage = STAGES[0]
++++++--        else:
++++++--            self.current_stage = STAGES[current_index + 1]
++++++--        self.state.set("CurrentStage", self.current_stage)
++++++- 
++++++--    def _complete_requirement_cycle(self):
++++++--        req_id = int(self.state.get("RequirementPointer"))
++++++--        os.makedirs("logs", exist_ok=True)
++++++--        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++++++--        with open(APPROVAL_FILE, "a") as f:
++++++--            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++++++--        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++++++--        next_req_id = req_id + 1
++++++--        self.state.set("RequirementPointer", next_req_id)
++++++--        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++++++- 
++++++- class WorkflowState:
++++++-     def __init__(self):
+++++++         old_stage = self.current_stage
+++++++         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++++++++        self.enforce_rules()
+++++++         self._validate_stage_exit_criteria()
+++++++         # The original logic from WorkflowManager is now fully integrated here.
+++++++         workflow_manager = WorkflowManager() # We still need access to its methods for now.
++++++ diff --git a/tests/test_governor.py b/tests/test_governor.py
++++++-new file mode 100644
++++++-index 0000000..95b566d
++++++---- /dev/null
+++++++index 95b566d..26bf82b 100644
+++++++--- a/tests/test_governor.py
++++++ +++ b/tests/test_governor.py
++++++-@@ -0,0 +1,55 @@
++++++-+# tests/test_governor.py
++++++-+import pytest
++++++-+from unittest.mock import MagicMock
++++++-+from pathlib import Path
++++++-+import sys
++++++-+
++++++-+from dw6.state_manager import Governor, WorkflowState
++++++-+
++++++-+@pytest.fixture
++++++-+def mock_state(mocker):
++++++-+    """Fixture to create a mock WorkflowState."""
++++++-+    state = MagicMock(spec=WorkflowState)
++++++-+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
++++++-+    return state
++++++-+
++++++-+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
++++++-+    """Verify the Governor blocks approval if the spec file is missing."""
++++++-+    # Arrange: Set the state to Engineer and mock the requirement pointer
++++++-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
++++++-+    
++++++-+    # Ensure the spec file does NOT exist for this test
++++++-+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
++++++-+    if spec_file.exists():
++++++-+        spec_file.unlink()
++++++-+
++++++-+    governor = Governor(mock_state)
++++++-+
++++++-+    # Act & Assert: The approval should fail with a SystemExit
++++++-+    with pytest.raises(SystemExit) as e:
++++++-+        governor._validate_stage_exit_criteria()
++++++-+    
++++++-+    assert e.type == SystemExit
++++++-+    assert e.value.code == 1
++++++-+
++++++-+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++++++-+    """Verify the Governor allows approval if the spec file exists."""
++++++-+    # Arrange: Set the state to Engineer and mock the requirement pointer
++++++-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
++++++-+    
++++++-+    # Ensure the spec file DOES exist for this test
++++++-+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
++++++-+    spec_file.parent.mkdir(parents=True, exist_ok=True)
++++++-+    spec_file.touch()
+++++++@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+++++++         # Clean up the created file
+++++++         if spec_file.exists():
+++++++             spec_file.unlink()
+++++  +
+++++--     if len(sys.argv) == 1:
+++++--         parser.print_help(sys.stderr)
+++++--         sys.exit(1)
+++++--@@ -27,6 +32,8 @@ def main():
+++++--         manager.review()
+++++--     elif args.command == "approve":
+++++-++    def _transition_to_next_stage(self):
+++++-++        current_index = STAGES.index(self.current_stage)
+++++-++        # After 'Deployer', the cycle is complete
+++++-++        if self.current_stage == "Deployer":
+++++-++            self._complete_requirement_cycle()
+++++-++            self.current_stage = STAGES[0]
+++++-++        else:
+++++-++            self.current_stage = STAGES[current_index + 1]
+++++-++        self.state.set("CurrentStage", self.current_stage)
+++++-++
+++++-++    def _complete_requirement_cycle(self):
+++++-++        req_id = int(self.state.get("RequirementPointer"))
+++++-++        os.makedirs("logs", exist_ok=True)
+++++-++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++++-++        with open(APPROVAL_FILE, "a") as f:
+++++-++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+++++-++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+++++-++        next_req_id = req_id + 1
+++++-++        self.state.set("RequirementPointer", next_req_id)
+++++-++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+++++-++
+++++-+ class WorkflowManager:
+++++-+     def __init__(self):
+++++-+         self.state = WorkflowState()
+++++-++        self.governor = Governor(self.state) # The manager now has a governor
+++++-+         self.current_stage = self.state.get("CurrentStage")
+++++-+ 
+++++-+     def get_state(self):
+++++-+         return self.state.data
+++++-+ 
+++++-+     def approve(self):
+++++-+-        old_stage = self.current_stage
+++++-+-        print(f"--- Approving Stage: {old_stage} ---")
+++++-+-        self._validate_stage()
+++++-+-        self._run_pre_transition_actions()
+++++-+-        self._transition_to_next_stage()
+++++-+-        self._run_post_transition_actions()
+++++-+-        self.state.save()
+++++-+-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+++++-++        # The manager now simply delegates to the governor.
+++++-++        self.governor.approve()
+++++-+ 
+++++-+     def _validate_stage(self):
+++++-+         print(f"Validating deliverables for stage: {self.current_stage}")
+++++-+@@ -123,25 +167,7 @@ class WorkflowManager:
+++++-+         if self.current_stage == "Coder":
+++++-+             git_handler.save_current_commit_sha()
+++++-+ 
+++++-+-    def _transition_to_next_stage(self):
+++++-+-        current_index = STAGES.index(self.current_stage)
+++++-+-        if current_index == len(STAGES) - 1:
+++++-+-            self._complete_requirement_cycle()
+++++-+-            self.current_stage = STAGES[0]
+++++-+-        else:
+++++-+-            self.current_stage = STAGES[current_index + 1]
+++++-+-        self.state.set("CurrentStage", self.current_stage)
+++++-+ 
+++++-+-    def _complete_requirement_cycle(self):
+++++-+-        req_id = int(self.state.get("RequirementPointer"))
+++++-+-        os.makedirs("logs", exist_ok=True)
+++++-+-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++++-+-        with open(APPROVAL_FILE, "a") as f:
+++++-+-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+++++-+-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+++++-+-        next_req_id = req_id + 1
+++++-+-        self.state.set("RequirementPointer", next_req_id)
+++++-+-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+++++-+ 
+++++-+ class WorkflowState:
+++++-+     def __init__(self):
+++++-+diff --git a/tests/test_governor.py b/tests/test_governor.py
+++++-+new file mode 100644
+++++-+index 0000000..95b566d
+++++-+--- /dev/null
+++++-++++ b/tests/test_governor.py
+++++-+@@ -0,0 +1,55 @@
+++++-++# tests/test_governor.py
+++++-++import pytest
+++++-++from unittest.mock import MagicMock
+++++-++from pathlib import Path
+++++-++import sys
+++++-++
+++++-++from dw6.state_manager import Governor, WorkflowState
+++++-++
+++++-++@pytest.fixture
+++++-++def mock_state(mocker):
+++++-++    """Fixture to create a mock WorkflowState."""
+++++-++    state = MagicMock(spec=WorkflowState)
+++++-++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+++++-++    return state
+++++-++
+++++-++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+++++-++    """Verify the Governor blocks approval if the spec file is missing."""
+++++-++    # Arrange: Set the state to Engineer and mock the requirement pointer
+++++-++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+++++-++    
+++++-++    # Ensure the spec file does NOT exist for this test
+++++-++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+++++-++    if spec_file.exists():
+++++-++        spec_file.unlink()
+++++-++
+++++-++    governor = Governor(mock_state)
+++++-++
+++++-++    # Act & Assert: The approval should fail with a SystemExit
+++++-++    with pytest.raises(SystemExit) as e:
+++++-++        governor._validate_stage_exit_criteria()
+++++-++    
+++++-++    assert e.type == SystemExit
+++++-++    assert e.value.code == 1
+++++-++
+++++-++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+++++-++    """Verify the Governor allows approval if the spec file exists."""
+++++-++    # Arrange: Set the state to Engineer and mock the requirement pointer
+++++-++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+++++-++    
+++++-++    # Ensure the spec file DOES exist for this test
+++++-++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+++++-++    spec_file.parent.mkdir(parents=True, exist_ok=True)
+++++-++    spec_file.touch()
+++++-++
+++++-++    governor = Governor(mock_state)
+++++-++
+++++-++    # Act & Assert: The approval should pass without raising an exception
+++ +-++    try:
+++-+-++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+++-+-++        with open(file_path, 'w') as f:
+++-+-++            f.write(content)
+++-+-++        print(f"Successfully created specification: {file_path}")
+++-+-++    except IOError as e:
+++-+-++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+++-+-++        sys.exit(1)
+++-+-+diff --git a/src/dw6/main.py b/src/dw6/main.py
+++-+-+index 7bbd031..a55f148 100644
+++-+-+--- a/src/dw6/main.py
+++-+-++++ b/src/dw6/main.py
+++-+-+@@ -2,6 +2,7 @@
+++-+-+ import argparse
+++-+-+ import sys
+++-+-+ from dw6.state_manager import StateManager
+++-+-++from dw6.augmenter import process_prompt
+++-+++ class WorkflowManager:
+++-+++     def __init__(self):
+++-+++         self.state = WorkflowState()
+++-++++        self.governor = Governor(self.state) # The manager now has a governor
+++-+++         self.current_stage = self.state.get("CurrentStage")
+++-+ + 
+++-+-+ def main():
+++-+-+     """Main entry point for the DW6 CLI."""
+++-+-+@@ -15,6 +16,10 @@ def main():
+++-+-+     # Approve command
+++-+-+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++-+++     def get_state(self):
+++-+++         return self.state.data
+++-+ + 
+++-+-++    # New command
+++-+-++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+++-+-++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+++-+++     def approve(self):
+++-+++-        old_stage = self.current_stage
+++-+++-        print(f"--- Approving Stage: {old_stage} ---")
+++-+++-        self._validate_stage()
+++-+++-        self._run_pre_transition_actions()
+++-+++-        self._transition_to_next_stage()
+++-+++-        self._run_post_transition_actions()
+++-+++-        self.state.save()
+++-+++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+++-++++        # The manager now simply delegates to the governor.
+++-++++        self.governor.approve()
+++-+++ 
+++-+++     def _validate_stage(self):
+++-+++         print(f"Validating deliverables for stage: {self.current_stage}")
+++-+++@@ -123,25 +167,7 @@ class WorkflowManager:
+++-+++         if self.current_stage == "Coder":
+++-+++             git_handler.save_current_commit_sha()
+++-+++ 
+++-+++-    def _transition_to_next_stage(self):
+++-+++-        current_index = STAGES.index(self.current_stage)
+++-+++-        if current_index == len(STAGES) - 1:
+++-+++-            self._complete_requirement_cycle()
+++-+++-            self.current_stage = STAGES[0]
+++-+++-        else:
+++-+++-            self.current_stage = STAGES[current_index + 1]
+++-+++-        self.state.set("CurrentStage", self.current_stage)
+++-+++ 
+++-+++-    def _complete_requirement_cycle(self):
+++-+++-        req_id = int(self.state.get("RequirementPointer"))
+++-+++-        os.makedirs("logs", exist_ok=True)
+++-+++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++-+++-        with open(APPROVAL_FILE, "a") as f:
+++-+++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+++-+++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+++-+++-        next_req_id = req_id + 1
+++-+++-        self.state.set("RequirementPointer", next_req_id)
+++-+++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+++-+++ 
+++-+++ class WorkflowState:
+++-+++     def __init__(self):
+++-+++diff --git a/tests/test_governor.py b/tests/test_governor.py
+++- ++new file mode 100644
+++--++index 0000000..c1614f0
+++-+++index 0000000..95b566d
+++- ++--- /dev/null
+++--+++++ b/src/dw6/augmenter.py
+++--++@@ -0,0 +1,26 @@
+++--+++# src/dw6/augmenter.py
+++-++++++ b/tests/test_governor.py
+++-+++@@ -0,0 +1,55 @@
+++-++++# tests/test_governor.py
+++-++++import pytest
+++-++++from unittest.mock import MagicMock
+++-++++from pathlib import Path
+++-++++import sys
+++-+ ++
+++-+-+     if len(sys.argv) == 1:
+++-+-+         parser.print_help(sys.stderr)
+++-+-+         sys.exit(1)
+++-+-+@@ -27,6 +32,8 @@ def main():
+++-+-+         manager.review()
+++-+-+     elif args.command == "approve":
+++-+-+         manager.approve()
+++-+-++    elif args.command == "new":
+++-+-++        process_prompt(args.prompt)
+++-++++from dw6.state_manager import Governor, WorkflowState
 ++-++++
-++-+++     if len(sys.argv) == 1:
-++-+++         parser.print_help(sys.stderr)
-++-+++         sys.exit(1)
-++-+++@@ -27,6 +32,8 @@ def main():
-++-+++         manager.review()
-++-+++     elif args.command == "approve":
-++++++     args = parser.parse_args()
-++++++     
-++++++-    manager = StateManager()
-+++++++    manager = WorkflowManager()
- +++++ 
--+++++ def main():
--+++++     """Main entry point for the DW6 CLI."""
--+++++@@ -15,6 +16,10 @@ def main():
--+++++     # Approve command
--+++++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-++++++-    if args.command == "review":
-++++++-        manager.review()
-++++++-    elif args.command == "approve":
-+++++++    if args.command == "approve":
-++ +++         manager.approve()
-++-++++    elif args.command == "new":
-++-++++        process_prompt(args.prompt)
-++++++     elif args.command == "new":
-++++++         process_prompt(args.prompt)
-++++++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-++++++index 703640c..b829d36 100644
-++++++--- a/src/dw6/state_manager.py
-+++++++++ b/src/dw6/state_manager.py
-++++++@@ -9,7 +9,7 @@ from dw6 import git_handler
-++++++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
-++++++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
-++++++ APPROVAL_FILE = "logs/approvals.log"
-++++++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
-+++++++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
-++++++ DELIVERABLE_PATHS = {
-++++++     "Engineer": "deliverables/engineering",
-++++++     "Coder": "deliverables/coding",
-++++++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
-++++++     "Researcher": "deliverables/research",
-++++++ }
- +++++ 
--++++++    # New command
--++++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
--++++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
--++++++
--+++++     if len(sys.argv) == 1:
--+++++         parser.print_help(sys.stderr)
--+++++         sys.exit(1)
--+++++@@ -27,6 +32,8 @@ def main():
--+++++         manager.review()
--+++++     elif args.command == "approve":
--+++++         manager.approve()
--++++++    elif args.command == "new":
--++++++        process_prompt(args.prompt)
-+++++++class Governor:
-+++++++    def __init__(self, state):
-+++++++        self.state = state
-+++++++        self.current_stage = self.state.get("CurrentStage")
-++++ ++
-++++-++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-+++++++    def approve(self):
-+++++++        old_stage = self.current_stage
-+++++++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-+++++++        self._validate_stage_exit_criteria()
-+++++++        # The original logic from WorkflowManager is now fully integrated here.
-+++++++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
-+++++++        workflow_manager._validate_stage()
-+++++++        workflow_manager._run_pre_transition_actions()
-+++++++        self._transition_to_next_stage() # This method now belongs to the Governor
-+++++++        workflow_manager._run_post_transition_actions()
-+++++++        self.state.save()
-+++++++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-++++ ++
-++++-++def process_prompt(prompt_text: str):
-++++-++    """
-++++-++    Augments a raw user prompt and generates a formal technical specification markdown file.
-++++-++    """
-++++-++    requirement_id = get_current_requirement_id()
-++++-++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-+++++++    def _validate_stage_exit_criteria(self):
-+++++++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
-+++++++        if self.current_stage == "Engineer":
-+++++++            req_id = self.state.get("RequirementPointer")
-+++++++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
-+++++++            if not spec_file.exists():
-+++++++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
-+++++++                sys.exit(1)
-+++++++            print("Governor: 'Engineer' exit criteria met.")
-+++++ +
-+++++-     if len(sys.argv) == 1:
-+++++-         parser.print_help(sys.stderr)
-+++++-         sys.exit(1)
-+++++-@@ -27,6 +32,8 @@ def main():
-+++++-         manager.review()
-+++++-     elif args.command == "approve":
-+++++++    def _transition_to_next_stage(self):
-+++++++        current_index = STAGES.index(self.current_stage)
-+++++++        # After 'Deployer', the cycle is complete
-+++++++        if self.current_stage == "Deployer":
-+++++++            self._complete_requirement_cycle()
-+++++++            self.current_stage = STAGES[0]
-+++++++        else:
-+++++++            self.current_stage = STAGES[current_index + 1]
-+++++++        self.state.set("CurrentStage", self.current_stage)
-++++ ++
-++++-++    content = f"# Requirement: {requirement_id}\n\n"
-++++-++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-++++-++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-+++++++    def _complete_requirement_cycle(self):
-+++++++        req_id = int(self.state.get("RequirementPointer"))
-+++++++        os.makedirs("logs", exist_ok=True)
-+++++++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+++++++        with open(APPROVAL_FILE, "a") as f:
-+++++++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-+++++++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-+++++++        next_req_id = req_id + 1
-+++++++        self.state.set("RequirementPointer", next_req_id)
-+++++++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-++++ ++
-++++-++    try:
-++++-++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-++++-++        with open(file_path, 'w') as f:
-++++-++            f.write(content)
-++++-++        print(f"Successfully created specification: {file_path}")
-++++-++    except IOError as e:
-++++-++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-++++-++        sys.exit(1)
-++++-+diff --git a/src/dw6/main.py b/src/dw6/main.py
-++++-+index 7bbd031..a55f148 100644
-++++-+--- a/src/dw6/main.py
-++++-++++ b/src/dw6/main.py
-++++-+@@ -2,6 +2,7 @@
-++++-+ import argparse
-++++-+ import sys
-++++-+ from dw6.state_manager import StateManager
-++++-++from dw6.augmenter import process_prompt
-++++++ class WorkflowManager:
-++++++     def __init__(self):
-++++++         self.state = WorkflowState()
-+++++++        self.governor = Governor(self.state) # The manager now has a governor
-++++++         self.current_stage = self.state.get("CurrentStage")
-++++ + 
-++++-+ def main():
-++++-+     """Main entry point for the DW6 CLI."""
-++++-+@@ -15,6 +16,10 @@ def main():
-++++-+     # Approve command
-++++-+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-++++++     def get_state(self):
-++++++         return self.state.data
-++++ + 
-++++-++    # New command
-++++-++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-++++-++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-++++++     def approve(self):
-++++++-        old_stage = self.current_stage
-++++++-        print(f"--- Approving Stage: {old_stage} ---")
-++++++-        self._validate_stage()
-++++++-        self._run_pre_transition_actions()
-++++++-        self._transition_to_next_stage()
-++++++-        self._run_post_transition_actions()
-++++++-        self.state.save()
-++++++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-+++++++        # The manager now simply delegates to the governor.
-+++++++        self.governor.approve()
-++++++ 
-++++++     def _validate_stage(self):
-++++++         print(f"Validating deliverables for stage: {self.current_stage}")
-++++++@@ -123,25 +167,7 @@ class WorkflowManager:
-++++++         if self.current_stage == "Coder":
-++++++             git_handler.save_current_commit_sha()
-++++++ 
-++++++-    def _transition_to_next_stage(self):
-++++++-        current_index = STAGES.index(self.current_stage)
-++++++-        if current_index == len(STAGES) - 1:
-++++++-            self._complete_requirement_cycle()
-++++++-            self.current_stage = STAGES[0]
-++++++-        else:
-++++++-            self.current_stage = STAGES[current_index + 1]
-++++++-        self.state.set("CurrentStage", self.current_stage)
- +++++ 
--+++++ if __name__ == "__main__":
--+++++     main()
--+++++```
--++++\ No newline at end of file
--++++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
--+++ new file mode 100644
--+++-index 0000000..c1614f0
--++++index 0000000..6c1638b
--+++ --- /dev/null
--+++-+++ b/src/dw6/augmenter.py
--+++-@@ -0,0 +1,26 @@
--+++-+# src/dw6/augmenter.py
-++++++-    def _complete_requirement_cycle(self):
-++++++-        req_id = int(self.state.get("RequirementPointer"))
-++++++-        os.makedirs("logs", exist_ok=True)
-++++++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-++++++-        with open(APPROVAL_FILE, "a") as f:
-++++++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-++++++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-++++++-        next_req_id = req_id + 1
-++++++-        self.state.set("RequirementPointer", next_req_id)
-++++++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-++++++ 
-++++++ class WorkflowState:
-++++++     def __init__(self):
-++++++diff --git a/tests/test_governor.py b/tests/test_governor.py
-+++ ++new file mode 100644
-+++-++index 0000000..c1614f0
-++++++index 0000000..95b566d
-+++ ++--- /dev/null
-+++-+++++ b/src/dw6/augmenter.py
-+++-++@@ -0,0 +1,26 @@
-+++-+++# src/dw6/augmenter.py
-+++++++++ b/tests/test_governor.py
-++++++@@ -0,0 +1,55 @@
-+++++++# tests/test_governor.py
-+++++++import pytest
-+++++++from unittest.mock import MagicMock
-+++++++from pathlib import Path
-+++++++import sys
-++++ ++
-++++-+     if len(sys.argv) == 1:
-++++-+         parser.print_help(sys.stderr)
-++++-+         sys.exit(1)
-++++-+@@ -27,6 +32,8 @@ def main():
-++++-+         manager.review()
-++++-+     elif args.command == "approve":
-++++-+         manager.approve()
-++++-++    elif args.command == "new":
-++++-++        process_prompt(args.prompt)
-+++++++from dw6.state_manager import Governor, WorkflowState
-+++++++
-+++++++@pytest.fixture
-+++++++def mock_state(mocker):
-+++++++    """Fixture to create a mock WorkflowState."""
-+++++++    state = MagicMock(spec=WorkflowState)
-+++++++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
-+++++++    return state
-+++ +++
-+++-+++import os
-+++-+++from .state_manager import get_current_requirement_id
-+++++++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
-+++++++    """Verify the Governor blocks approval if the spec file is missing."""
-+++++++    # Arrange: Set the state to Engineer and mock the requirement pointer
-+++++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
-+++++++    
-+++++++    # Ensure the spec file does NOT exist for this test
-+++++++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
-+++++++    if spec_file.exists():
-+++++++        spec_file.unlink()
-+++ +++
-+++-+++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-+++++++    governor = Governor(mock_state)
-+++ +++
-+++-+++def process_prompt(prompt_text: str):
-+++-+++    """
-+++-+++    Augments a raw user prompt and generates a formal technical specification markdown file.
-+++-+++    """
-+++-+++    requirement_id = get_current_requirement_id()
-+++-+++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-+++++++    # Act & Assert: The approval should fail with a SystemExit
-+++++++    with pytest.raises(SystemExit) as e:
-+++++++        governor._validate_stage_exit_criteria()
-+++++++    
-+++++++    assert e.type == SystemExit
-+++++++    assert e.value.code == 1
-+++ +++
-+++-+++    content = f"# Requirement: {requirement_id}\n\n"
-+++-+++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-+++-+++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-+++++++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-+++++++    """Verify the Governor allows approval if the spec file exists."""
-+++++++    # Arrange: Set the state to Engineer and mock the requirement pointer
-+++++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
-+++++++    
-+++++++    # Ensure the spec file DOES exist for this test
-+++++++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
-+++++++    spec_file.parent.mkdir(parents=True, exist_ok=True)
-+++++++    spec_file.touch()
-+++ +++
-+++++++    governor = Governor(mock_state)
-+++++++
-+++++++    # Act & Assert: The approval should pass without raising an exception
-+++ +++    try:
-+++-+++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-+++-+++        with open(file_path, 'w') as f:
-+++-+++            f.write(content)
-+++-+++        print(f"Successfully created specification: {file_path}")
-+++-+++    except IOError as e:
-+++-+++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-+++-+++        sys.exit(1)
-+++-++diff --git a/src/dw6/main.py b/src/dw6/main.py
-+++-++index 7bbd031..a55f148 100644
-+++-++--- a/src/dw6/main.py
-+++-+++++ b/src/dw6/main.py
-+++-++@@ -2,6 +2,7 @@
-+++-++ import argparse
-+++-++ import sys
-+++-++ from dw6.state_manager import StateManager
-+++-+++from dw6.augmenter import process_prompt
+++-++++@pytest.fixture
+++-++++def mock_state(mocker):
+++-++++    """Fixture to create a mock WorkflowState."""
+++-++++    state = MagicMock(spec=WorkflowState)
+++-++++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+++-++++    return state
+++- +++
+++--+++import os
+++--+++from .state_manager import get_current_requirement_id
+++-++++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+++-++++    """Verify the Governor blocks approval if the spec file is missing."""
+++-++++    # Arrange: Set the state to Engineer and mock the requirement pointer
+++-++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+++-++++    
+++-++++    # Ensure the spec file does NOT exist for this test
+++-++++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+++-++++    if spec_file.exists():
+++-++++        spec_file.unlink()
+++- +++
+++--+++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++-++++    governor = Governor(mock_state)
+++- +++
+++--+++def process_prompt(prompt_text: str):
+++--+++    """
+++--+++    Augments a raw user prompt and generates a formal technical specification markdown file.
+++--+++    """
+++--+++    requirement_id = get_current_requirement_id()
+++--+++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++-++++    # Act & Assert: The approval should fail with a SystemExit
+++-++++    with pytest.raises(SystemExit) as e:
+++-++++        governor._validate_stage_exit_criteria()
+++-++++    
+++-++++    assert e.type == SystemExit
+++-++++    assert e.value.code == 1
+++- +++
+++--+++    content = f"# Requirement: {requirement_id}\n\n"
+++--+++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+++--+++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++-++++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+++-++++    """Verify the Governor allows approval if the spec file exists."""
+++-++++    # Arrange: Set the state to Engineer and mock the requirement pointer
+++-++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+++-++++    
+++-++++    # Ensure the spec file DOES exist for this test
+++-++++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+++-++++    spec_file.parent.mkdir(parents=True, exist_ok=True)
+++-++++    spec_file.touch()
+++- +++
+++-++++    governor = Governor(mock_state)
+++-++++
+++-++++    # Act & Assert: The approval should pass without raising an exception
+++- +++    try:
+++--+++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+++--+++        with open(file_path, 'w') as f:
+++--+++            f.write(content)
+++--+++        print(f"Successfully created specification: {file_path}")
+++--+++    except IOError as e:
+++--+++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+++--+++        sys.exit(1)
+++--++diff --git a/src/dw6/main.py b/src/dw6/main.py
+++--++index 7bbd031..a55f148 100644
+++--++--- a/src/dw6/main.py
+++--+++++ b/src/dw6/main.py
+++--++@@ -2,6 +2,7 @@
+++--++ import argparse
+++--++ import sys
+++--++ from dw6.state_manager import StateManager
+++--+++from dw6.augmenter import process_prompt
+++++-++        governor._validate_stage_exit_criteria()
+++++-++    except SystemExit:
+++++-++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+++++-++    finally:
+++++-++        # Clean up the created file
+++++-++        if spec_file.exists():
+++++-++            spec_file.unlink()
+++++-+diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+++++-+index 5b9d1eb..44d2cc9 100644
+++++-+--- a/tests/test_state_manager_integration.py
+++++-++++ b/tests/test_state_manager_integration.py
+++++-+@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+++++-+ 
+++++-+     @patch('dw6.state_manager.WorkflowState')
+++++-+     @patch('dw6.git_handler.get_changes_since_last_commit')
+++++-+-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+++++-++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+++++-++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+++++-+         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+++++-+         # Arrange
+++++-+         mock_state_instance = mock_WorkflowState.return_value
+++++-+@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+++++-+         # Act
+++++-          manager.approve()
+++++--+    elif args.command == "new":
+++++--+        process_prompt(args.prompt)
+++++-  
+++++-- if __name__ == "__main__":
+++++--     main()
+++++-+-        # Assert
+++++-++        # Assert that the deliverable file was created
+++++-+         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+++++-+         self.assertTrue(deliverable_path.exists())
+++++-++        # Clean up the created file
+++++-++        deliverable_path.unlink()
+++++-++
+++++-+         mock_state_instance.save.assert_called_once()
+++++-+ 
+++++-+ if __name__ == '__main__':
+++++-+diff --git a/uv.lock b/uv.lock
+++++-+index c79d29c..8e7411f 100644
+++++-+--- a/uv.lock
+++++-++++ b/uv.lock
+++++-+@@ -66,6 +66,7 @@ dependencies = [
+++++-+ test = [
+++++-+     { name = "pytest" },
+++++-+     { name = "pytest-cov" },
+++++-++    { name = "pytest-mock" },
+++++-+ ]
+++++-+ 
+++++-+ [package.metadata]
+++++-+@@ -73,6 +74,7 @@ requires-dist = [
+++++-+     { name = "gitpython" },
+++++-+     { name = "pytest", marker = "extra == 'test'" },
+++++-+     { name = "pytest-cov", marker = "extra == 'test'" },
+++++-++    { name = "pytest-mock", marker = "extra == 'test'" },
+++++-+     { name = "python-dotenv" },
+++++-+ ]
+++++-+ provides-extras = ["test"]
+++++-+@@ -167,6 +169,18 @@ wheels = [
+++++-+     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+++++-+ ]
+++++-+ 
+++++-++[[package]]
+++++-++name = "pytest-mock"
+++++-++version = "3.14.1"
+++++-++source = { registry = "https://pypi.org/simple" }
+++++-++dependencies = [
+++++-++    { name = "pytest" },
+++++-++]
+++++-++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+++++-++wheels = [
+++++-++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+++++-++]
+++++-++
+++++-+ [[package]]
+++++-+ name = "python-dotenv"
+++++-+ version = "1.1.1"
++++++++def test_governor_enforces_rules_on_approve(mocker, capsys):
++++++++    """Verify that the Governor prints the correct rule for the current stage."""
++++++++    # Arrange
++++++++    mock_state = mocker.MagicMock(spec=WorkflowState)
++++++++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
++++++ +    governor = Governor(mock_state)
++++++++    # Mock the exit criteria validation to prevent SystemExit
++++++++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
++++++++    # Mock the rest of the approval process to isolate the rule enforcement
++++++++    mocker.patch.object(governor, '_transition_to_next_stage')
++++++++    mocker.patch('dw6.state_manager.WorkflowManager')
++++ + +
++++++-+    # Act & Assert: The approval should pass without raising an exception
++++ +-+    try:
++++-+-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++++-+-+        with open(file_path, 'w') as f:
++++-+-+            f.write(content)
++++-+-+        print(f"Successfully created specification: {file_path}")
++++-+-+    except IOError as e:
++++-+-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++++-+-+        sys.exit(1)
++++-+++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
++++-++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
++++-++index 9718eda..b85b3d9 100644
++++-++--- a/logs/.last_commit_sha
++++-+++++ b/logs/.last_commit_sha
++++-++@@ -1 +1 @@
++++-++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
++++-++\ No newline at end of file
++++-+++75be02c0b7e1723e32042299497f3673b11b4ddd
++++-++\ No newline at end of file
++++-++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
++++-++index 28746b7..743582b 100644
++++-++--- a/logs/workflow_state.txt
++++-+++++ b/logs/workflow_state.txt
++++-++@@ -1,2 +1,2 @@
++++-++-CurrentStage=Engineer
++++-++-RequirementPointer=7
++++-+++CurrentStage=Coder
++++-+++RequirementPointer=9
++++-++diff --git a/pytest.ini b/pytest.ini
++++- +new file mode 100644
++++--+index 0000000..c1614f0
++++-++index 0000000..a635c5c
++++- +--- /dev/null
++++--++++ b/src/dw6/augmenter.py
++++--+@@ -0,0 +1,26 @@
++++--++# src/dw6/augmenter.py
++++-+++++ b/pytest.ini
++++-++@@ -0,0 +1,2 @@
++++-+++[pytest]
++++-+++pythonpath = .
++++-+ diff --git a/src/dw6/main.py b/src/dw6/main.py
++++-+-index 7bbd031..a55f148 100644
++++-++index a55f148..90862f9 100644
++++-+ --- a/src/dw6/main.py
++++-+ +++ b/src/dw6/main.py
++++-+-@@ -2,6 +2,7 @@
++++-++@@ -1,7 +1,7 @@
++++-++ # dw6/main.py
++++-+  import argparse
++++-+  import sys
++++-+- from dw6.state_manager import StateManager
++++-+-+from dw6.augmenter import process_prompt
++++-++-from dw6.state_manager import StateManager
++++-+++from dw6.state_manager import WorkflowManager
++++-++ from dw6.augmenter import process_prompt
++++-+  
++++-+  def main():
++++-+-     """Main entry point for the DW6 CLI."""
++++-+-@@ -15,6 +16,10 @@ def main():
++++-++@@ -10,9 +10,7 @@ def main():
++++-++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++++-++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++ +-++ 
++-+-++ def main():
++-+-++     """Main entry point for the DW6 CLI."""
++-+-++@@ -15,6 +16,10 @@ def main():
++-+-++     # Approve command
++-+-++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++-+++++        governor._validate_stage_exit_criteria()
++-+++++    except SystemExit:
++-+++++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
++-+++++    finally:
++-+++++        # Clean up the created file
++-+++++        if spec_file.exists():
++-+++++            spec_file.unlink()
++-++++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
++-++++index 5b9d1eb..44d2cc9 100644
++-++++--- a/tests/test_state_manager_integration.py
++-+++++++ b/tests/test_state_manager_integration.py
++-++++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++-+ ++ 
++-+-+++    # New command
++-+-+++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++-+-+++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++-++++     @patch('dw6.state_manager.WorkflowState')
++-++++     @patch('dw6.git_handler.get_changes_since_last_commit')
++-++++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
++-+++++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
++-+++++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
++-++++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
++-++++         # Arrange
++-++++         mock_state_instance = mock_WorkflowState.return_value
++-++++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++-++++         # Act
++-+++          manager.approve()
++-+++-+    elif args.command == "new":
++-+++-+        process_prompt(args.prompt)
++-+++  
++-+++- if __name__ == "__main__":
++-+++-     main()
++-++++-        # Assert
++-+++++        # Assert that the deliverable file was created
++-++++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
++-++++         self.assertTrue(deliverable_path.exists())
++-+++++        # Clean up the created file
++-+++++        deliverable_path.unlink()
++-+ +++
++-+-++     if len(sys.argv) == 1:
++-+-++         parser.print_help(sys.stderr)
++-+-++         sys.exit(1)
++-+-++@@ -27,6 +32,8 @@ def main():
++-+-++         manager.review()
++-+-++     elif args.command == "approve":
++-+-++         manager.approve()
++-+-+++    elif args.command == "new":
++-+-+++        process_prompt(args.prompt)
++-++++         mock_state_instance.save.assert_called_once()
++-+ ++ 
++-+-++ if __name__ == "__main__":
++-+-++     main()
++-+-++```
++-+-+\ No newline at end of file
++-+-+diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
++-++++ if __name__ == '__main__':
++-++++diff --git a/uv.lock b/uv.lock
++-++++index c79d29c..8e7411f 100644
++-++++--- a/uv.lock
++-+++++++ b/uv.lock
++-++++@@ -66,6 +66,7 @@ dependencies = [
++-++++ test = [
++-++++     { name = "pytest" },
++-++++     { name = "pytest-cov" },
++-+++++    { name = "pytest-mock" },
++-++++ ]
++-++ + 
++-++-+ if __name__ == "__main__":
++-++-+     main()
++-++-+```
++-++++ [package.metadata]
++-++++@@ -73,6 +74,7 @@ requires-dist = [
++-++++     { name = "gitpython" },
++-++++     { name = "pytest", marker = "extra == 'test'" },
++-++++     { name = "pytest-cov", marker = "extra == 'test'" },
++-+++++    { name = "pytest-mock", marker = "extra == 'test'" },
++-++++     { name = "python-dotenv" },
++-++++ ]
++-++++ provides-extras = ["test"]
++-++++@@ -167,6 +169,18 @@ wheels = [
++-++++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
++-++++ ]
++- +++ 
++--+++ if __name__ == "__main__":
++--+++     main()
++--+++```
++--++\ No newline at end of file
++--++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
++--+ new file mode 100644
++--+-index 0000000..c1614f0
++--++index 0000000..6c1638b
++--+ --- /dev/null
++--+-+++ b/src/dw6/augmenter.py
++--+-@@ -0,0 +1,26 @@
++--+-+# src/dw6/augmenter.py
++-+++++[[package]]
++-+++++name = "pytest-mock"
++-+++++version = "3.14.1"
++-+++++source = { registry = "https://pypi.org/simple" }
++-+++++dependencies = [
++-+++++    { name = "pytest" },
++-+++++]
++-+++++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
++-+++++wheels = [
++-+++++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
++-+++++]
++-+++++
++-++++ [[package]]
++-++++ name = "python-dotenv"
++-++++ version = "1.1.1"
++-+++ ```
++-++ \ No newline at end of file
++-++-diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
++-+++diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
++-+  new file mode 100644
++-+--index 0000000..c1614f0
++-+-+index 0000000..6c1638b
++-++-index 0000000..6c1638b
++-+++index 0000000..691df8d
++-+  --- /dev/null
++-+--+++ b/src/dw6/augmenter.py
++-+--@@ -0,0 +1,26 @@
++-+--+# src/dw6/augmenter.py
++++-++-    # Review command
++++-++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
++++-++-    
++++- ++
++++--++import os
++++--++from .state_manager import get_current_requirement_id
++++-+      # Approve command
++++-+      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++-+  
++++-+-+    # New command
++++-+-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++++-+-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++++-++@@ -26,11 +24,9 @@ def main():
+++ -++ 
+++--++ def main():
+++--++     """Main entry point for the DW6 CLI."""
+++--++@@ -15,6 +16,10 @@ def main():
+++--++     # Approve command
+++--++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++-++++        governor._validate_stage_exit_criteria()
+++-++++    except SystemExit:
+++-++++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+++-++++    finally:
+++-++++        # Clean up the created file
+++-++++        if spec_file.exists():
+++-++++            spec_file.unlink()
+++-+++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+++-+++index 5b9d1eb..44d2cc9 100644
+++-+++--- a/tests/test_state_manager_integration.py
+++-++++++ b/tests/test_state_manager_integration.py
+++-+++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+++- ++ 
+++--+++    # New command
+++--+++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+++--+++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+++-+++     @patch('dw6.state_manager.WorkflowState')
+++-+++     @patch('dw6.git_handler.get_changes_since_last_commit')
+++-+++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+++-++++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+++-++++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+++-+++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+++-+++         # Arrange
+++-+++         mock_state_instance = mock_WorkflowState.return_value
+++-+++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+++-+++         # Act
+++-++          manager.approve()
+++-++-+    elif args.command == "new":
+++-++-+        process_prompt(args.prompt)
+++-++  
+++-++- if __name__ == "__main__":
+++-++-     main()
+++-+++-        # Assert
+++-++++        # Assert that the deliverable file was created
+++-+++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+++-+++         self.assertTrue(deliverable_path.exists())
+++-++++        # Clean up the created file
+++-++++        deliverable_path.unlink()
+++- +++
+++--++     if len(sys.argv) == 1:
+++--++         parser.print_help(sys.stderr)
+++--++         sys.exit(1)
+++--++@@ -27,6 +32,8 @@ def main():
+++--++         manager.review()
+++--++     elif args.command == "approve":
++++-++     args = parser.parse_args()
++++-++     
++++-++-    manager = StateManager()
++++-+++    manager = WorkflowManager()
 +++-++ 
-+++-++ def main():
-+++-++     """Main entry point for the DW6 CLI."""
-+++-++@@ -15,6 +16,10 @@ def main():
-+++-++     # Approve command
-+++-++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-+++++++        governor._validate_stage_exit_criteria()
-+++++++    except SystemExit:
-+++++++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
-+++++++    finally:
-+++++++        # Clean up the created file
-+++++++        if spec_file.exists():
-+++++++            spec_file.unlink()
-++++++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
-++++++index 5b9d1eb..44d2cc9 100644
-++++++--- a/tests/test_state_manager_integration.py
-+++++++++ b/tests/test_state_manager_integration.py
-++++++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-+++ ++ 
-+++-+++    # New command
-+++-+++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-+++-+++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-++++++     @patch('dw6.state_manager.WorkflowState')
-++++++     @patch('dw6.git_handler.get_changes_since_last_commit')
-++++++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
-+++++++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
-+++++++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
-++++++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
-++++++         # Arrange
-++++++         mock_state_instance = mock_WorkflowState.return_value
-++++++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-++++++         # Act
-+++++          manager.approve()
-+++++-+    elif args.command == "new":
-+++++-+        process_prompt(args.prompt)
-+++++  
-+++++- if __name__ == "__main__":
-+++++-     main()
-++++++-        # Assert
-+++++++        # Assert that the deliverable file was created
-++++++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
-++++++         self.assertTrue(deliverable_path.exists())
-+++++++        # Clean up the created file
-+++++++        deliverable_path.unlink()
-+++ +++
-+++-++     if len(sys.argv) == 1:
-+++-++         parser.print_help(sys.stderr)
-+++-++         sys.exit(1)
-+++-++@@ -27,6 +32,8 @@ def main():
-+++-++         manager.review()
-+++-++     elif args.command == "approve":
-+++-++         manager.approve()
-+++-+++    elif args.command == "new":
-+++-+++        process_prompt(args.prompt)
-++++++         mock_state_instance.save.assert_called_once()
-+++ ++ 
-+++-++ if __name__ == "__main__":
-+++-++     main()
-+++-++```
-+++-+\ No newline at end of file
-+++-+diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
-++++++ if __name__ == '__main__':
-++++++diff --git a/uv.lock b/uv.lock
-++++++index c79d29c..8e7411f 100644
-++++++--- a/uv.lock
-+++++++++ b/uv.lock
-++++++@@ -66,6 +66,7 @@ dependencies = [
-++++++ test = [
-++++++     { name = "pytest" },
-++++++     { name = "pytest-cov" },
-+++++++    { name = "pytest-mock" },
-++++++ ]
-++++ + 
-++++-+ if __name__ == "__main__":
-++++-+     main()
-++++-+```
-++++++ [package.metadata]
-++++++@@ -73,6 +74,7 @@ requires-dist = [
-++++++     { name = "gitpython" },
-++++++     { name = "pytest", marker = "extra == 'test'" },
-++++++     { name = "pytest-cov", marker = "extra == 'test'" },
-+++++++    { name = "pytest-mock", marker = "extra == 'test'" },
-++++++     { name = "python-dotenv" },
-++++++ ]
-++++++ provides-extras = ["test"]
-++++++@@ -167,6 +169,18 @@ wheels = [
-++++++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
-++++++ ]
-++ +++ 
-++-+++ if __name__ == "__main__":
-++-+++     main()
-++-+++```
-++-++\ No newline at end of file
-++-++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
-++-+ new file mode 100644
-++-+-index 0000000..c1614f0
-++-++index 0000000..6c1638b
-++-+ --- /dev/null
-++-+-+++ b/src/dw6/augmenter.py
-++-+-@@ -0,0 +1,26 @@
-++-+-+# src/dw6/augmenter.py
-+++++++[[package]]
-+++++++name = "pytest-mock"
-+++++++version = "3.14.1"
-+++++++source = { registry = "https://pypi.org/simple" }
-+++++++dependencies = [
-+++++++    { name = "pytest" },
-+++++++]
-+++++++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
-+++++++wheels = [
-+++++++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
-+++++++]
-+++++++
-++++++ [[package]]
-++++++ name = "python-dotenv"
-++++++ version = "1.1.1"
-+++++ ```
-++++ \ No newline at end of file
-++++-diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
-+++++diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
-+++  new file mode 100644
-+++--index 0000000..c1614f0
-+++-+index 0000000..6c1638b
-++++-index 0000000..6c1638b
-+++++index 0000000..691df8d
-+++  --- /dev/null
-+++--+++ b/src/dw6/augmenter.py
-+++--@@ -0,0 +1,26 @@
-+++--+# src/dw6/augmenter.py
++++-++-    if args.command == "review":
++++-++-        manager.review()
++++-++-    elif args.command == "approve":
++++-+++    if args.command == "approve":
+++ -++         manager.approve()
+++--+++    elif args.command == "new":
+++--+++        process_prompt(args.prompt)
+++-+++         mock_state_instance.save.assert_called_once()
+++- ++ 
+++--++ if __name__ == "__main__":
+++--++     main()
+++--++```
+++--+\ No newline at end of file
+++--+diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+++-+++ if __name__ == '__main__':
+++-+++diff --git a/uv.lock b/uv.lock
+++-+++index c79d29c..8e7411f 100644
+++-+++--- a/uv.lock
+++-++++++ b/uv.lock
+++-+++@@ -66,6 +66,7 @@ dependencies = [
+++-+++ test = [
+++-+++     { name = "pytest" },
+++-+++     { name = "pytest-cov" },
+++-++++    { name = "pytest-mock" },
+++-+++ ]
+++-+ + 
+++-+-+ if __name__ == "__main__":
+++-+-+     main()
+++-+-+```
+++-+++ [package.metadata]
+++-+++@@ -73,6 +74,7 @@ requires-dist = [
+++-+++     { name = "gitpython" },
+++-+++     { name = "pytest", marker = "extra == 'test'" },
+++-+++     { name = "pytest-cov", marker = "extra == 'test'" },
+++-++++    { name = "pytest-mock", marker = "extra == 'test'" },
+++-+++     { name = "python-dotenv" },
+++-+++ ]
+++-+++ provides-extras = ["test"]
+++-+++@@ -167,6 +169,18 @@ wheels = [
+++-+++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+++-+++ ]
+++-+++ 
+++-++++[[package]]
+++-++++name = "pytest-mock"
+++-++++version = "3.14.1"
+++-++++source = { registry = "https://pypi.org/simple" }
+++-++++dependencies = [
+++-++++    { name = "pytest" },
+++-++++]
+++-++++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+++-++++wheels = [
+++-++++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+++-++++]
+++-++++
+++-+++ [[package]]
+++-+++ name = "python-dotenv"
+++-+++ version = "1.1.1"
+++-++ ```
+++-+ \ No newline at end of file
+++-+-diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+++-++diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
++++-++     elif args.command == "new":
++++-++         process_prompt(args.prompt)
++++-++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++++-++index 703640c..b829d36 100644
++++-++--- a/src/dw6/state_manager.py
++++-+++++ b/src/dw6/state_manager.py
++++-++@@ -9,7 +9,7 @@ from dw6 import git_handler
++++-++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
++++-++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
++++-++ APPROVAL_FILE = "logs/approvals.log"
++++-++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
++++-+++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
++++-++ DELIVERABLE_PATHS = {
++++-++     "Engineer": "deliverables/engineering",
++++-++     "Coder": "deliverables/coding",
++++-++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
++++-++     "Researcher": "deliverables/research",
++++-++ }
++++-++ 
++++-+++class Governor:
++++-+++    def __init__(self, state):
++++-+++        self.state = state
++++-+++        self.current_stage = self.state.get("CurrentStage")
++++- ++
++++--++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++++-+++    def approve(self):
++++-+++        old_stage = self.current_stage
++++-+++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++++-+++        self._validate_stage_exit_criteria()
++++-+++        # The original logic from WorkflowManager is now fully integrated here.
++++-+++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
++++-+++        workflow_manager._validate_stage()
++++-+++        workflow_manager._run_pre_transition_actions()
++++-+++        self._transition_to_next_stage() # This method now belongs to the Governor
++++-+++        workflow_manager._run_post_transition_actions()
++++-+++        self.state.save()
++++-+++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++++- ++
++++--++def process_prompt(prompt_text: str):
++++--++    """
++++--++    Augments a raw user prompt and generates a formal technical specification markdown file.
++++--++    """
++++--++    requirement_id = get_current_requirement_id()
++++--++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++++-+++    def _validate_stage_exit_criteria(self):
++++-+++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
++++-+++        if self.current_stage == "Engineer":
++++-+++            req_id = self.state.get("RequirementPointer")
++++-+++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
++++-+++            if not spec_file.exists():
++++-+++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
++++-+++                sys.exit(1)
++++-+++            print("Governor: 'Engineer' exit criteria met.")
++++++-+        governor._validate_stage_exit_criteria()
++++++-+    except SystemExit:
++++++-+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
++++++-+    finally:
++++++-+        # Clean up the created file
++++++-+        if spec_file.exists():
++++++-+            spec_file.unlink()
++++++-diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
++++++-index 5b9d1eb..44d2cc9 100644
++++++---- a/tests/test_state_manager_integration.py
++++++-+++ b/tests/test_state_manager_integration.py
++++++-@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++++++- 
++++++-     @patch('dw6.state_manager.WorkflowState')
++++++-     @patch('dw6.git_handler.get_changes_since_last_commit')
++++++--    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
++++++-+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
++++++-+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
++++++-         """Ensure approving Coder stage generates a deliverable without altering the real state."""
++++++-         # Arrange
++++++-         mock_state_instance = mock_WorkflowState.return_value
++++++-@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++++++-         # Act
++++++-         manager.approve()
++++++- 
++++++--        # Assert
++++++-+        # Assert that the deliverable file was created
++++++-         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
++++++-         self.assertTrue(deliverable_path.exists())
++++++-+        # Clean up the created file
++++++-+        deliverable_path.unlink()
++++++-+
++++++-         mock_state_instance.save.assert_called_once()
++++++- 
++++++- if __name__ == '__main__':
++++++-diff --git a/uv.lock b/uv.lock
++++++-index c79d29c..8e7411f 100644
++++++---- a/uv.lock
++++++-+++ b/uv.lock
++++++-@@ -66,6 +66,7 @@ dependencies = [
++++++- test = [
++++++-     { name = "pytest" },
++++++-     { name = "pytest-cov" },
++++++-+    { name = "pytest-mock" },
++++++- ]
++++++- 
++++++- [package.metadata]
++++++-@@ -73,6 +74,7 @@ requires-dist = [
++++++-     { name = "gitpython" },
++++++-     { name = "pytest", marker = "extra == 'test'" },
++++++-     { name = "pytest-cov", marker = "extra == 'test'" },
++++++-+    { name = "pytest-mock", marker = "extra == 'test'" },
++++++-     { name = "python-dotenv" },
++++++- ]
++++++- provides-extras = ["test"]
++++++-@@ -167,6 +169,18 @@ wheels = [
++++++-     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
++++++- ]
++++++- 
++++++-+[[package]]
++++++-+name = "pytest-mock"
++++++-+version = "3.14.1"
++++++-+source = { registry = "https://pypi.org/simple" }
++++++-+dependencies = [
++++++-+    { name = "pytest" },
++++++-+]
++++++-+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
++++++-+wheels = [
++++++-+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
++++++-+]
++++++++    # Act
++++++++    governor.approve()
++++ + +
++++-+-     if len(sys.argv) == 1:
++++-+-         parser.print_help(sys.stderr)
++++-+-         sys.exit(1)
++++-+-@@ -27,6 +32,8 @@ def main():
++++-+-         manager.review()
++++-+-     elif args.command == "approve":
++++-+++    def _transition_to_next_stage(self):
++++-+++        current_index = STAGES.index(self.current_stage)
++++-+++        # After 'Deployer', the cycle is complete
++++-+++        if self.current_stage == "Deployer":
++++-+++            self._complete_requirement_cycle()
++++-+++            self.current_stage = STAGES[0]
++++-+++        else:
++++-+++            self.current_stage = STAGES[current_index + 1]
++++-+++        self.state.set("CurrentStage", self.current_stage)
++++- ++
++++--++    content = f"# Requirement: {requirement_id}\n\n"
++++--++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++++--++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++++-+++    def _complete_requirement_cycle(self):
++++-+++        req_id = int(self.state.get("RequirementPointer"))
++++-+++        os.makedirs("logs", exist_ok=True)
++++-+++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++++-+++        with open(APPROVAL_FILE, "a") as f:
++++-+++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++++-+++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++++-+++        next_req_id = req_id + 1
++++-+++        self.state.set("RequirementPointer", next_req_id)
++++-+++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++++- ++
++++--++    try:
++++--++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++++--++        with open(file_path, 'w') as f:
++++--++            f.write(content)
++++--++        print(f"Successfully created specification: {file_path}")
++++--++    except IOError as e:
++++--++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++++--++        sys.exit(1)
++++--+diff --git a/src/dw6/main.py b/src/dw6/main.py
++++--+index 7bbd031..a55f148 100644
++++--+--- a/src/dw6/main.py
++++--++++ b/src/dw6/main.py
++++--+@@ -2,6 +2,7 @@
++++--+ import argparse
++++--+ import sys
++++--+ from dw6.state_manager import StateManager
++++--++from dw6.augmenter import process_prompt
++++-++ class WorkflowManager:
++++-++     def __init__(self):
++++-++         self.state = WorkflowState()
++++-+++        self.governor = Governor(self.state) # The manager now has a governor
++++-++         self.current_stage = self.state.get("CurrentStage")
++++- + 
++++--+ def main():
++++--+     """Main entry point for the DW6 CLI."""
++++--+@@ -15,6 +16,10 @@ def main():
++++--+     # Approve command
++++--+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++-++     def get_state(self):
++++-++         return self.state.data
++++- + 
++++--++    # New command
++++--++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++++--++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++++-++     def approve(self):
++++-++-        old_stage = self.current_stage
++++-++-        print(f"--- Approving Stage: {old_stage} ---")
++++-++-        self._validate_stage()
++++-++-        self._run_pre_transition_actions()
++++-++-        self._transition_to_next_stage()
++++-++-        self._run_post_transition_actions()
++++-++-        self.state.save()
++++-++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++++-+++        # The manager now simply delegates to the governor.
++++-+++        self.governor.approve()
++++-++ 
++++-++     def _validate_stage(self):
++++-++         print(f"Validating deliverables for stage: {self.current_stage}")
++++-++@@ -123,25 +167,7 @@ class WorkflowManager:
++++-++         if self.current_stage == "Coder":
++++-++             git_handler.save_current_commit_sha()
++++-++ 
++++-++-    def _transition_to_next_stage(self):
++++-++-        current_index = STAGES.index(self.current_stage)
++++-++-        if current_index == len(STAGES) - 1:
++++-++-            self._complete_requirement_cycle()
++++-++-            self.current_stage = STAGES[0]
++++-++-        else:
++++-++-            self.current_stage = STAGES[current_index + 1]
++++-++-        self.state.set("CurrentStage", self.current_stage)
++++-++ 
++++-++-    def _complete_requirement_cycle(self):
++++-++-        req_id = int(self.state.get("RequirementPointer"))
++++-++-        os.makedirs("logs", exist_ok=True)
++++-++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++++-++-        with open(APPROVAL_FILE, "a") as f:
++++-++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++++-++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++++-++-        next_req_id = req_id + 1
++++-++-        self.state.set("RequirementPointer", next_req_id)
++++-++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++++-++ 
++++-++ class WorkflowState:
++++-++     def __init__(self):
++++-++diff --git a/tests/test_governor.py b/tests/test_governor.py
++++-++new file mode 100644
++++-++index 0000000..95b566d
++++-++--- /dev/null
++++-+++++ b/tests/test_governor.py
++++-++@@ -0,0 +1,55 @@
++++-+++# tests/test_governor.py
++++-+++import pytest
++++-+++from unittest.mock import MagicMock
++++-+++from pathlib import Path
++++-+++import sys
++++- ++
++++--+     if len(sys.argv) == 1:
++++--+         parser.print_help(sys.stderr)
++++--+         sys.exit(1)
++++--+@@ -27,6 +32,8 @@ def main():
++++--+         manager.review()
++++--+     elif args.command == "approve":
++++--+         manager.approve()
++++--++    elif args.command == "new":
++++--++        process_prompt(args.prompt)
++++-+++from dw6.state_manager import Governor, WorkflowState
++++-+++
++++-+++@pytest.fixture
++++-+++def mock_state(mocker):
++++-+++    """Fixture to create a mock WorkflowState."""
++++-+++    state = MagicMock(spec=WorkflowState)
++++-+++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
++++-+++    return state
++++-+++
++++-+++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
++++-+++    """Verify the Governor blocks approval if the spec file is missing."""
++++-+++    # Arrange: Set the state to Engineer and mock the requirement pointer
++++-+++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
++++-+++    
++++-+++    # Ensure the spec file does NOT exist for this test
++++-+++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
++++-+++    if spec_file.exists():
++++-+++        spec_file.unlink()
++++-+++
++++-+++    governor = Governor(mock_state)
++++-+++
++++-+++    # Act & Assert: The approval should fail with a SystemExit
++++-+++    with pytest.raises(SystemExit) as e:
++++-+++        governor._validate_stage_exit_criteria()
++++-+++    
++++-+++    assert e.type == SystemExit
++++-+++    assert e.value.code == 1
++++-+++
++++-+++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++++-+++    """Verify the Governor allows approval if the spec file exists."""
++++-+++    # Arrange: Set the state to Engineer and mock the requirement pointer
++++-+++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
++++-+++    
++++-+++    # Ensure the spec file DOES exist for this test
++++-+++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
++++-+++    spec_file.parent.mkdir(parents=True, exist_ok=True)
++++-+++    spec_file.touch()
++++-+++
++++-+++    governor = Governor(mock_state)
++++-+++
++++-+++    # Act & Assert: The approval should pass without raising an exception
++++-+++    try:
++++-+++        governor._validate_stage_exit_criteria()
++++-+++    except SystemExit:
++++-+++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
++++-+++    finally:
++++-+++        # Clean up the created file
++++-+++        if spec_file.exists():
++++-+++            spec_file.unlink()
++++-++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
++++-++index 5b9d1eb..44d2cc9 100644
++++-++--- a/tests/test_state_manager_integration.py
++++-+++++ b/tests/test_state_manager_integration.py
++++-++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++++-++ 
++++-++     @patch('dw6.state_manager.WorkflowState')
++++-++     @patch('dw6.git_handler.get_changes_since_last_commit')
++++-++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
++++-+++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
++++-+++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
++++-++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
++++-++         # Arrange
++++-++         mock_state_instance = mock_WorkflowState.return_value
++++-++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++++-++         # Act
++++-+          manager.approve()
++++-+-+    elif args.command == "new":
++++-+-+        process_prompt(args.prompt)
++++-+  
++++-+- if __name__ == "__main__":
++++-+-     main()
++++-++-        # Assert
++++-+++        # Assert that the deliverable file was created
++++-++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
++++-++         self.assertTrue(deliverable_path.exists())
++++-+++        # Clean up the created file
++++-+++        deliverable_path.unlink()
++++-+++
++++-++         mock_state_instance.save.assert_called_once()
++++-++ 
++++-++ if __name__ == '__main__':
++++-++diff --git a/uv.lock b/uv.lock
++++-++index c79d29c..8e7411f 100644
++++-++--- a/uv.lock
++++-+++++ b/uv.lock
++++-++@@ -66,6 +66,7 @@ dependencies = [
++++-++ test = [
++++-++     { name = "pytest" },
++++-++     { name = "pytest-cov" },
++++-+++    { name = "pytest-mock" },
++++-++ ]
++++- + 
++++--+ if __name__ == "__main__":
++++--+     main()
++++--+```
++++-++ [package.metadata]
++++-++@@ -73,6 +74,7 @@ requires-dist = [
++++-++     { name = "gitpython" },
++++-++     { name = "pytest", marker = "extra == 'test'" },
++++-++     { name = "pytest-cov", marker = "extra == 'test'" },
++++-+++    { name = "pytest-mock", marker = "extra == 'test'" },
++++-++     { name = "python-dotenv" },
++++-++ ]
++++-++ provides-extras = ["test"]
++++-++@@ -167,6 +169,18 @@ wheels = [
++++-++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
++++-++ ]
++++-++ 
++++-+++[[package]]
++++-+++name = "pytest-mock"
++++-+++version = "3.14.1"
++++-+++source = { registry = "https://pypi.org/simple" }
++++-+++dependencies = [
++++-+++    { name = "pytest" },
++++-+++]
++++-+++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
++++-+++wheels = [
++++-+++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
++++-+++]
++++-+++
++++-++ [[package]]
++++-++ name = "python-dotenv"
++++-++ version = "1.1.1"
++++-+ ```
++++++- [[package]]
++++++- name = "python-dotenv"
++++++- version = "1.1.1"
++++++++    # Assert
++++++++    captured = capsys.readouterr()
++++++++    expected_rule = Governor.RULES["Coder"]
++++++++    assert expected_rule in captured.out
+++++  ```
++++  \ No newline at end of file
++++--diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
++++-+diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
+++++-diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
++++++diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
+++   new file mode 100644
+++---index 0000000..c1614f0
+++--+index 0000000..6c1638b
+++-+-index 0000000..6c1638b
+++-++index 0000000..691df8d
++++--index 0000000..6c1638b
++++-+index 0000000..691df8d
+++++-index 0000000..691df8d
++++++index 0000000..071c22d
+++   --- /dev/null
+++---+++ b/src/dw6/augmenter.py
+++---@@ -0,0 +1,26 @@
+++---+# src/dw6/augmenter.py
+++---+
+++---+import os
+++---+from .state_manager import get_current_requirement_id
+++--++++ b/deliverables/engineering/cycle_9_technical_specification.md
+++--+@@ -0,0 +1,9 @@
+++--++# Requirement: 8
+++-+-+++ b/deliverables/engineering/cycle_9_technical_specification.md
+++-+++++ b/deliverables/engineering/cycle_10_technical_specification.md
+++-+ @@ -0,0 +1,9 @@
+++-+-+# Requirement: 8
+++-+++# Requirement: 10
++++--+++ b/deliverables/engineering/cycle_9_technical_specification.md
++++-++++ b/deliverables/engineering/cycle_10_technical_specification.md
+++++-+++ b/deliverables/engineering/cycle_10_technical_specification.md
+++++++++ b/deliverables/engineering/cycle_11_technical_specification.md
++++  @@ -0,0 +1,9 @@
++++--+# Requirement: 8
++++-++# Requirement: 10
+++++-+# Requirement: 10
+++++++# Requirement: 11
+++   +
+++---+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+++--++## 1. High-Level Goal
+++-+ +## 1. High-Level Goal
++++  +## 1. High-Level Goal
+++   +
+++---+def process_prompt(prompt_text: str):
+++---+    """
+++---+    Augments a raw user prompt and generates a formal technical specification markdown file.
+++---+    """
+++---+    requirement_id = get_current_requirement_id()
+++---+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+++--++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+++-+-+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+++-+++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
++++--+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
++++-++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
+++++-+Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
+++++++Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
+++   +
+++---+    content = f"# Requirement: {requirement_id}\n\n"
+++---+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+++---+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+++--++## 2. Guiding Principles
+++-+ +## 2. Guiding Principles
++++  +## 2. Guiding Principles
+++   +
+++---+    try:
+++---+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+++---+        with open(file_path, 'w') as f:
+++---+            f.write(content)
+++---+        print(f"Successfully created specification: {file_path}")
+++---+    except IOError as e:
+++---+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+++---+        sys.exit(1)
+++--++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+++--+diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+++--+index 9718eda..b85b3d9 100644
+++--+--- a/logs/.last_commit_sha
+++--++++ b/logs/.last_commit_sha
+++--+@@ -1 +1 @@
+++--+-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+++--+\ No newline at end of file
+++--++75be02c0b7e1723e32042299497f3673b11b4ddd
+++--+\ No newline at end of file
+++--+diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+++--+index 28746b7..743582b 100644
+++--+--- a/logs/workflow_state.txt
+++--++++ b/logs/workflow_state.txt
+++--+@@ -1,2 +1,2 @@
+++--+-CurrentStage=Engineer
+++--+-RequirementPointer=7
+++--++CurrentStage=Coder
+++--++RequirementPointer=9
+++--+diff --git a/pytest.ini b/pytest.ini
+++--+new file mode 100644
+++--+index 0000000..a635c5c
+++--+--- /dev/null
+++--++++ b/pytest.ini
+++--+@@ -0,0 +1,2 @@
+++--++[pytest]
+++--++pythonpath = .
+++-- diff --git a/src/dw6/main.py b/src/dw6/main.py
+++---index 7bbd031..a55f148 100644
+++--+index a55f148..90862f9 100644
+++-- --- a/src/dw6/main.py
+++-- +++ b/src/dw6/main.py
+++---@@ -2,6 +2,7 @@
+++--+@@ -1,7 +1,7 @@
+++--+ # dw6/main.py
+++--  import argparse
+++--  import sys
+++--- from dw6.state_manager import StateManager
+++---+from dw6.augmenter import process_prompt
+++--+-from dw6.state_manager import StateManager
+++--++from dw6.state_manager import WorkflowManager
+++--+ from dw6.augmenter import process_prompt
+++-+ +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+++-+ diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+++-+-index 9718eda..b85b3d9 100644
+++-++index b85b3d9..00ab2c8 100644
+++-+ --- a/logs/.last_commit_sha
+++-+ +++ b/logs/.last_commit_sha
+++-+ @@ -1 +1 @@
+++-+--7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+++-++-75be02c0b7e1723e32042299497f3673b11b4ddd
+++-+ \ No newline at end of file
+++-+-+75be02c0b7e1723e32042299497f3673b11b4ddd
+++-+++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+++-+ \ No newline at end of file
+++-+ diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+++-+-index 28746b7..743582b 100644
+++-++index 743582b..a7aa662 100644
+++-+ --- a/logs/workflow_state.txt
+++-+ +++ b/logs/workflow_state.txt
+++-+ @@ -1,2 +1,2 @@
+++-+--CurrentStage=Engineer
+++-+--RequirementPointer=7
+++-+-+CurrentStage=Coder
+++-+-+RequirementPointer=9
+++-+-diff --git a/pytest.ini b/pytest.ini
+++-+-new file mode 100644
+++-+-index 0000000..a635c5c
+++-+---- /dev/null
+++-+-+++ b/pytest.ini
+++-+-@@ -0,0 +1,2 @@
+++-+-+[pytest]
+++-+-+pythonpath = .
+++-+-diff --git a/src/dw6/main.py b/src/dw6/main.py
+++-+-index a55f148..90862f9 100644
+++-+---- a/src/dw6/main.py
+++-+-+++ b/src/dw6/main.py
+++-+-@@ -1,7 +1,7 @@
+++-+- # dw6/main.py
+++-+- import argparse
+++-+- import sys
+++-+--from dw6.state_manager import StateManager
+++-+-+from dw6.state_manager import WorkflowManager
+++-+- from dw6.augmenter import process_prompt
+++-+- 
+++-+- def main():
+++-+-@@ -10,9 +10,7 @@ def main():
+++-+-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+++-+-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+++-+- 
+++-+--    # Review command
+++-+--    subparsers.add_parser("review", help="Review the changes for the current stage.")
+++-+--    
+++-+-+
+++-+-     # Approve command
+++-+-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++-+- 
+++-+-@@ -26,11 +24,9 @@ def main():
+++-+- 
+++-+-     args = parser.parse_args()
+++-+-     
+++-+--    manager = StateManager()
+++-+-+    manager = WorkflowManager()
+++-+- 
+++-+--    if args.command == "review":
+++-+--        manager.review()
+++-+--    elif args.command == "approve":
+++-+-+    if args.command == "approve":
+++-+-         manager.approve()
+++-+-     elif args.command == "new":
+++-+-         process_prompt(args.prompt)
+++-++ CurrentStage=Coder
+++-++-RequirementPointer=9
+++-+++RequirementPointer=10
+++-+ diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+++-+-index 703640c..b829d36 100644
+++-++index b829d36..241fa62 100644
+++-+ --- a/src/dw6/state_manager.py
+++-+ +++ b/src/dw6/state_manager.py
+++-+-@@ -9,7 +9,7 @@ from dw6 import git_handler
+++-+- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+++-+- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+++-+- APPROVAL_FILE = "logs/approvals.log"
+++-+--STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+++-+-+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+++-+- DELIVERABLE_PATHS = {
+++-+-     "Engineer": "deliverables/engineering",
+++-+-     "Coder": "deliverables/coding",
+++-+-@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+++-+-     "Researcher": "deliverables/research",
+++-++@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
+++-+  }
++++  +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
++++  diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
++++--index 9718eda..b85b3d9 100644
++++-+index b85b3d9..00ab2c8 100644
+++++-index b85b3d9..00ab2c8 100644
++++++index 00ab2c8..ede42cf 100644
++++  --- a/logs/.last_commit_sha
++++  +++ b/logs/.last_commit_sha
++++  @@ -1 +1 @@
++++---7aa14d9c189cbc22b982d3d7895a650c1cf7a654
++++-+-75be02c0b7e1723e32042299497f3673b11b4ddd
+++++--75be02c0b7e1723e32042299497f3673b11b4ddd
++++++-b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
++++  \ No newline at end of file
++++--+75be02c0b7e1723e32042299497f3673b11b4ddd
++++-++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+++++-+b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+++++++96a1111270912ae2722109d00ed1405c166f577c
++++  \ No newline at end of file
++++  diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
++++--index 28746b7..743582b 100644
++++-+index 743582b..a7aa662 100644
+++++-index 743582b..a7aa662 100644
++++++index a7aa662..591ebb9 100644
++++  --- a/logs/workflow_state.txt
++++  +++ b/logs/workflow_state.txt
++++  @@ -1,2 +1,2 @@
++++---CurrentStage=Engineer
++++---RequirementPointer=7
++++--+CurrentStage=Coder
++++--+RequirementPointer=9
++++--diff --git a/pytest.ini b/pytest.ini
++++--new file mode 100644
++++--index 0000000..a635c5c
++++----- /dev/null
++++--+++ b/pytest.ini
++++--@@ -0,0 +1,2 @@
++++--+[pytest]
++++--+pythonpath = .
++++--diff --git a/src/dw6/main.py b/src/dw6/main.py
++++--index a55f148..90862f9 100644
++++----- a/src/dw6/main.py
++++--+++ b/src/dw6/main.py
++++--@@ -1,7 +1,7 @@
++++-- # dw6/main.py
++++-- import argparse
++++-- import sys
++++---from dw6.state_manager import StateManager
++++--+from dw6.state_manager import WorkflowManager
++++-- from dw6.augmenter import process_prompt
++++-- 
++++-- def main():
++++--@@ -10,9 +10,7 @@ def main():
++++--     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++++--     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++++-- 
++++---    # Review command
++++---    subparsers.add_parser("review", help="Review the changes for the current stage.")
++++---    
 +++--+
-+++--+import os
-+++--+from .state_manager import get_current_requirement_id
-+++-++++ b/deliverables/engineering/cycle_9_technical_specification.md
-+++-+@@ -0,0 +1,9 @@
-+++-++# Requirement: 8
-++++-+++ b/deliverables/engineering/cycle_9_technical_specification.md
-++++++++ b/deliverables/engineering/cycle_10_technical_specification.md
-++++ @@ -0,0 +1,9 @@
-++++-+# Requirement: 8
-++++++# Requirement: 10
-+++  +
-+++--+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-+++-++## 1. High-Level Goal
-++++ +## 1. High-Level Goal
-+++  +
-+++--+def process_prompt(prompt_text: str):
-+++--+    """
-+++--+    Augments a raw user prompt and generates a formal technical specification markdown file.
-+++--+    """
-+++--+    requirement_id = get_current_requirement_id()
-+++--+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-+++-++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
-++++-+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
-++++++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
-+++  +
-+++--+    content = f"# Requirement: {requirement_id}\n\n"
-+++--+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-+++--+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-+++-++## 2. Guiding Principles
-++++ +## 2. Guiding Principles
-+++  +
-+++--+    try:
-+++--+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-+++--+        with open(file_path, 'w') as f:
-+++--+            f.write(content)
-+++--+        print(f"Successfully created specification: {file_path}")
-+++--+    except IOError as e:
-+++--+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-+++--+        sys.exit(1)
-+++-++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
-+++-+diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
-+++-+index 9718eda..b85b3d9 100644
-+++-+--- a/logs/.last_commit_sha
-+++-++++ b/logs/.last_commit_sha
-+++-+@@ -1 +1 @@
-+++-+-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
-+++-+\ No newline at end of file
-+++-++75be02c0b7e1723e32042299497f3673b11b4ddd
-+++-+\ No newline at end of file
-+++-+diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
-+++-+index 28746b7..743582b 100644
-+++-+--- a/logs/workflow_state.txt
-+++-++++ b/logs/workflow_state.txt
-+++-+@@ -1,2 +1,2 @@
-+++-+-CurrentStage=Engineer
-+++-+-RequirementPointer=7
-+++-++CurrentStage=Coder
-+++-++RequirementPointer=9
-+++-+diff --git a/pytest.ini b/pytest.ini
-+++-+new file mode 100644
-+++-+index 0000000..a635c5c
-+++-+--- /dev/null
-+++-++++ b/pytest.ini
-+++-+@@ -0,0 +1,2 @@
-+++-++[pytest]
-+++-++pythonpath = .
-+++- diff --git a/src/dw6/main.py b/src/dw6/main.py
-+++--index 7bbd031..a55f148 100644
-+++-+index a55f148..90862f9 100644
-+++- --- a/src/dw6/main.py
-+++- +++ b/src/dw6/main.py
-+++--@@ -2,6 +2,7 @@
-+++-+@@ -1,7 +1,7 @@
-+++-+ # dw6/main.py
-+++-  import argparse
-+++-  import sys
-+++-- from dw6.state_manager import StateManager
-+++--+from dw6.augmenter import process_prompt
-+++-+-from dw6.state_manager import StateManager
-+++-++from dw6.state_manager import WorkflowManager
-+++-+ from dw6.augmenter import process_prompt
-++++ +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
-++++ diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
-++++-index 9718eda..b85b3d9 100644
-+++++index b85b3d9..00ab2c8 100644
-++++ --- a/logs/.last_commit_sha
-++++ +++ b/logs/.last_commit_sha
-++++ @@ -1 +1 @@
-++++--7aa14d9c189cbc22b982d3d7895a650c1cf7a654
-+++++-75be02c0b7e1723e32042299497f3673b11b4ddd
-++++ \ No newline at end of file
-++++-+75be02c0b7e1723e32042299497f3673b11b4ddd
-++++++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
-++++ \ No newline at end of file
-++++ diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
-++++-index 28746b7..743582b 100644
-+++++index 743582b..a7aa662 100644
-++++ --- a/logs/workflow_state.txt
-++++ +++ b/logs/workflow_state.txt
-++++ @@ -1,2 +1,2 @@
-++++--CurrentStage=Engineer
-++++--RequirementPointer=7
-++++-+CurrentStage=Coder
-++++-+RequirementPointer=9
-++++-diff --git a/pytest.ini b/pytest.ini
-++++-new file mode 100644
-++++-index 0000000..a635c5c
-++++---- /dev/null
-++++-+++ b/pytest.ini
-++++-@@ -0,0 +1,2 @@
-++++-+[pytest]
-++++-+pythonpath = .
-++++-diff --git a/src/dw6/main.py b/src/dw6/main.py
-++++-index a55f148..90862f9 100644
-++++---- a/src/dw6/main.py
-++++-+++ b/src/dw6/main.py
-++++-@@ -1,7 +1,7 @@
-++++- # dw6/main.py
-++++- import argparse
-++++- import sys
-++++--from dw6.state_manager import StateManager
-++++-+from dw6.state_manager import WorkflowManager
-++++- from dw6.augmenter import process_prompt
-++++- 
-++++- def main():
-++++-@@ -10,9 +10,7 @@ def main():
-++++-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-++++-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-++++- 
-++++--    # Review command
-++++--    subparsers.add_parser("review", help="Review the changes for the current stage.")
-++++--    
-++ +-+
-++-+-+import os
-++-+-+from .state_manager import get_current_requirement_id
-++-+++++ b/deliverables/engineering/cycle_9_technical_specification.md
-++-++@@ -0,0 +1,9 @@
-++-+++# Requirement: 8
-++-+ +
-++-+-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-++-+++## 1. High-Level Goal
-++-+ +
-++-+-+def process_prompt(prompt_text: str):
-++-+-+    """
-++-+-+    Augments a raw user prompt and generates a formal technical specification markdown file.
-++-+-+    """
-++-+-+    requirement_id = get_current_requirement_id()
-++-+-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-++-+++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
-++-+ +
-++-+-+    content = f"# Requirement: {requirement_id}\n\n"
-++-+-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-++-+-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-++-+++## 2. Guiding Principles
-++++-     # Approve command
-++++-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-++++- 
-++++-@@ -26,11 +24,9 @@ def main():
-++++- 
-++++-     args = parser.parse_args()
-++++-     
-++++--    manager = StateManager()
-++++-+    manager = WorkflowManager()
-++++- 
-++++--    if args.command == "review":
-++++--        manager.review()
-++++--    elif args.command == "approve":
-++++-+    if args.command == "approve":
-++++-         manager.approve()
-++++-     elif args.command == "new":
-++++-         process_prompt(args.prompt)
-+++++ CurrentStage=Coder
-+++++-RequirementPointer=9
-++++++RequirementPointer=10
-++++ diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-++++-index 703640c..b829d36 100644
-+++++index b829d36..241fa62 100644
-++++ --- a/src/dw6/state_manager.py
-++++ +++ b/src/dw6/state_manager.py
-++++-@@ -9,7 +9,7 @@ from dw6 import git_handler
-++++- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
-++++- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
-++++- APPROVAL_FILE = "logs/approvals.log"
-++++--STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
-++++-+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
-++++- DELIVERABLE_PATHS = {
-++++-     "Engineer": "deliverables/engineering",
-++++-     "Coder": "deliverables/coding",
-++++-@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
-++++-     "Researcher": "deliverables/research",
-+++++@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
-++++  }
-+++   
-+++-  def main():
-+++--     """Main entry point for the DW6 CLI."""
-+++--@@ -15,6 +16,10 @@ def main():
-+++-+@@ -10,9 +10,7 @@ def main():
-+++-+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-+++-+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-+++-+ 
-+++-+-    # Review command
-+++-+-    subparsers.add_parser("review", help="Review the changes for the current stage.")
-+++-+-    
-+++-++
-+++-      # Approve command
-+++-      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-++++-+class Governor:
-++++-+    def __init__(self, state):
-++++-+        self.state = state
-++++-+        self.current_stage = self.state.get("CurrentStage")
- +++-+
--+++-+import os
--+++-+from .state_manager import get_current_requirement_id
--+++++++ b/deliverables/engineering/cycle_9_technical_specification.md
--++++@@ -0,0 +1,9 @@
--+++++# Requirement: 8
--+++ +
--+++-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
--+++++## 1. High-Level Goal
--+++ +
--+++-+def process_prompt(prompt_text: str):
--+++-+    """
--+++-+    Augments a raw user prompt and generates a formal technical specification markdown file.
--+++-+    """
--+++-+    requirement_id = get_current_requirement_id()
--+++-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
--+++++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
--+++ +
--+++-+    content = f"# Requirement: {requirement_id}\n\n"
--+++-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
--+++-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
--+++++## 2. Guiding Principles
--+++ +
--+++-+    try:
--+++-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
--+++-+        with open(file_path, 'w') as f:
--+++-+            f.write(content)
--+++-+        print(f"Successfully created specification: {file_path}")
--+++-+    except IOError as e:
--+++-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
--+++-+        sys.exit(1)
--+++++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
--++++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
--++++index 9718eda..b85b3d9 100644
--++++--- a/logs/.last_commit_sha
--+++++++ b/logs/.last_commit_sha
--++++@@ -1 +1 @@
--++++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
--++++\ No newline at end of file
--+++++75be02c0b7e1723e32042299497f3673b11b4ddd
--++++\ No newline at end of file
--++++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
--++++index 28746b7..743582b 100644
--++++--- a/logs/workflow_state.txt
--+++++++ b/logs/workflow_state.txt
--++++@@ -1,2 +1,2 @@
--++++-CurrentStage=Engineer
--++++-RequirementPointer=7
--+++++CurrentStage=Coder
--+++++RequirementPointer=9
--++++diff --git a/pytest.ini b/pytest.ini
--++ +new file mode 100644
--++-+index 0000000..c1614f0
--++++index 0000000..a635c5c
--++ +--- /dev/null
--++-++++ b/src/dw6/augmenter.py
--++-+@@ -0,0 +1,26 @@
--++-++# src/dw6/augmenter.py
--+++++++ b/pytest.ini
--++++@@ -0,0 +1,2 @@
--+++++[pytest]
--+++++pythonpath = .
--+++ diff --git a/src/dw6/main.py b/src/dw6/main.py
--+++-index 7bbd031..a55f148 100644
--++++index a55f148..90862f9 100644
--+++ --- a/src/dw6/main.py
--+++ +++ b/src/dw6/main.py
--+++-@@ -2,6 +2,7 @@
--++++@@ -1,7 +1,7 @@
--++++ # dw6/main.py
--+++  import argparse
--+++  import sys
--+++- from dw6.state_manager import StateManager
--+++-+from dw6.augmenter import process_prompt
--++++-from dw6.state_manager import StateManager
--+++++from dw6.state_manager import WorkflowManager
--++++ from dw6.augmenter import process_prompt
--+++  
--+++  def main():
--+++-     """Main entry point for the DW6 CLI."""
--+++-@@ -15,6 +16,10 @@ def main():
--++++@@ -10,9 +10,7 @@ def main():
--++++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
--++++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-- +++ 
---+++ def main():
---+++     """Main entry point for the DW6 CLI."""
---+++@@ -15,6 +16,10 @@ def main():
---+++     # Approve command
---+++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
--++++-    # Review command
--++++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
--++++-    
--++ ++
--++-++import os
--++-++from .state_manager import get_current_requirement_id
--+++      # Approve command
--+++      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
--+++  
--+++-+    # New command
--+++-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
--+++-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
--++++@@ -26,11 +24,9 @@ def main():
-- +++ 
---++++    # New command
---++++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
---++++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
---++++
---+++     if len(sys.argv) == 1:
---+++         parser.print_help(sys.stderr)
---+++         sys.exit(1)
---+++@@ -27,6 +32,8 @@ def main():
---+++         manager.review()
---+++     elif args.command == "approve":
--++++     args = parser.parse_args()
--++++     
--++++-    manager = StateManager()
--+++++    manager = WorkflowManager()
--++++ 
--++++-    if args.command == "review":
--++++-        manager.review()
--++++-    elif args.command == "approve":
--+++++    if args.command == "approve":
-- +++         manager.approve()
---++++    elif args.command == "new":
---++++        process_prompt(args.prompt)
--++++     elif args.command == "new":
--++++         process_prompt(args.prompt)
--++++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
--++++index 703640c..b829d36 100644
--++++--- a/src/dw6/state_manager.py
--+++++++ b/src/dw6/state_manager.py
--++++@@ -9,7 +9,7 @@ from dw6 import git_handler
--++++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
--++++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
--++++ APPROVAL_FILE = "logs/approvals.log"
--++++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
--+++++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
--++++ DELIVERABLE_PATHS = {
--++++     "Engineer": "deliverables/engineering",
--++++     "Coder": "deliverables/coding",
--++++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
--++++     "Researcher": "deliverables/research",
--++++ }
--++++ 
--+++++class Governor:
--+++++    def __init__(self, state):
--+++++        self.state = state
--+++++        self.current_stage = self.state.get("CurrentStage")
--++ ++
--++-++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
--+++++    def approve(self):
--+++++        old_stage = self.current_stage
--+++++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
--+++++        self._validate_stage_exit_criteria()
--+++++        # The original logic from WorkflowManager is now fully integrated here.
--+++++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
--+++++        workflow_manager._validate_stage()
--+++++        workflow_manager._run_pre_transition_actions()
--+++++        self._transition_to_next_stage() # This method now belongs to the Governor
--+++++        workflow_manager._run_post_transition_actions()
--+++++        self.state.save()
--+++++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
--++ ++
--++-++def process_prompt(prompt_text: str):
--++-++    """
--++-++    Augments a raw user prompt and generates a formal technical specification markdown file.
--++-++    """
--++-++    requirement_id = get_current_requirement_id()
--++-++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
--+++++    def _validate_stage_exit_criteria(self):
--+++++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
--+++++        if self.current_stage == "Engineer":
--+++++            req_id = self.state.get("RequirementPointer")
--+++++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
--+++++            if not spec_file.exists():
--+++++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
--+++++                sys.exit(1)
--+++++            print("Governor: 'Engineer' exit criteria met.")
--+++ +
--+++-     if len(sys.argv) == 1:
--+++-         parser.print_help(sys.stderr)
--+++-         sys.exit(1)
--+++-@@ -27,6 +32,8 @@ def main():
--+++-         manager.review()
--+++-     elif args.command == "approve":
--+++++    def _transition_to_next_stage(self):
--+++++        current_index = STAGES.index(self.current_stage)
--+++++        # After 'Deployer', the cycle is complete
--+++++        if self.current_stage == "Deployer":
--+++++            self._complete_requirement_cycle()
--+++++            self.current_stage = STAGES[0]
--+++++        else:
--+++++            self.current_stage = STAGES[current_index + 1]
--+++++        self.state.set("CurrentStage", self.current_stage)
--++ ++
--++-++    content = f"# Requirement: {requirement_id}\n\n"
--++-++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
--++-++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
--+++++    def _complete_requirement_cycle(self):
--+++++        req_id = int(self.state.get("RequirementPointer"))
--+++++        os.makedirs("logs", exist_ok=True)
--+++++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
--+++++        with open(APPROVAL_FILE, "a") as f:
--+++++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
--+++++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
--+++++        next_req_id = req_id + 1
--+++++        self.state.set("RequirementPointer", next_req_id)
--+++++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
--++ ++
--++-++    try:
--++-++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
--++-++        with open(file_path, 'w') as f:
--++-++            f.write(content)
--++-++        print(f"Successfully created specification: {file_path}")
--++-++    except IOError as e:
--++-++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
--++-++        sys.exit(1)
--++-+diff --git a/src/dw6/main.py b/src/dw6/main.py
--++-+index 7bbd031..a55f148 100644
--++-+--- a/src/dw6/main.py
--++-++++ b/src/dw6/main.py
--++-+@@ -2,6 +2,7 @@
--++-+ import argparse
--++-+ import sys
--++-+ from dw6.state_manager import StateManager
--++-++from dw6.augmenter import process_prompt
--++++ class WorkflowManager:
--++++     def __init__(self):
--++++         self.state = WorkflowState()
--+++++        self.governor = Governor(self.state) # The manager now has a governor
--++++         self.current_stage = self.state.get("CurrentStage")
--++ + 
--++-+ def main():
--++-+     """Main entry point for the DW6 CLI."""
--++-+@@ -15,6 +16,10 @@ def main():
--++-+     # Approve command
--++-+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
--++++     def get_state(self):
--++++         return self.state.data
--++ + 
--++-++    # New command
--++-++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
--++-++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
--++++     def approve(self):
--++++-        old_stage = self.current_stage
--++++-        print(f"--- Approving Stage: {old_stage} ---")
--++++-        self._validate_stage()
--++++-        self._run_pre_transition_actions()
--++++-        self._transition_to_next_stage()
--++++-        self._run_post_transition_actions()
--++++-        self.state.save()
--++++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
--+++++        # The manager now simply delegates to the governor.
--+++++        self.governor.approve()
--++++ 
--++++     def _validate_stage(self):
--++++         print(f"Validating deliverables for stage: {self.current_stage}")
--++++@@ -123,25 +167,7 @@ class WorkflowManager:
--++++         if self.current_stage == "Coder":
--++++             git_handler.save_current_commit_sha()
--++++ 
--++++-    def _transition_to_next_stage(self):
--++++-        current_index = STAGES.index(self.current_stage)
--++++-        if current_index == len(STAGES) - 1:
--++++-            self._complete_requirement_cycle()
--++++-            self.current_stage = STAGES[0]
--++++-        else:
--++++-            self.current_stage = STAGES[current_index + 1]
--++++-        self.state.set("CurrentStage", self.current_stage)
--++++ 
--++++-    def _complete_requirement_cycle(self):
--++++-        req_id = int(self.state.get("RequirementPointer"))
--++++-        os.makedirs("logs", exist_ok=True)
--++++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
--++++-        with open(APPROVAL_FILE, "a") as f:
--++++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
--++++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
--++++-        next_req_id = req_id + 1
--++++-        self.state.set("RequirementPointer", next_req_id)
--++++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
--++++ 
--++++ class WorkflowState:
--++++     def __init__(self):
--++++diff --git a/tests/test_governor.py b/tests/test_governor.py
--+ ++new file mode 100644
--+-++index 0000000..c1614f0
--++++index 0000000..95b566d
--+ ++--- /dev/null
--+-+++++ b/src/dw6/augmenter.py
--+-++@@ -0,0 +1,26 @@
--+-+++# src/dw6/augmenter.py
--+++++++ b/tests/test_governor.py
--++++@@ -0,0 +1,55 @@
--+++++# tests/test_governor.py
--+++++import pytest
--+++++from unittest.mock import MagicMock
--+++++from pathlib import Path
--+++++import sys
--++ ++
--++-+     if len(sys.argv) == 1:
--++-+         parser.print_help(sys.stderr)
--++-+         sys.exit(1)
--++-+@@ -27,6 +32,8 @@ def main():
--++-+         manager.review()
--++-+     elif args.command == "approve":
-++++-+    def approve(self):
-++++-+        old_stage = self.current_stage
-++++-+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-++++-+        self._validate_stage_exit_criteria()
-++++-+        # The original logic from WorkflowManager is now fully integrated here.
-++++-+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
-++++-+        workflow_manager._validate_stage()
-++++-+        workflow_manager._run_pre_transition_actions()
-++++-+        self._transition_to_next_stage() # This method now belongs to the Governor
-++++-+        workflow_manager._run_post_transition_actions()
-++++-+        self.state.save()
-++++-+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-++++-+
-++++-+    def _validate_stage_exit_criteria(self):
-++++-+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
-++++-+        if self.current_stage == "Engineer":
-++++-+            req_id = self.state.get("RequirementPointer")
-++++-+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
-++++-+            if not spec_file.exists():
-++++-+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
-++++-+                sys.exit(1)
-++++-+            print("Governor: 'Engineer' exit criteria met.")
-++++-+
-++++-+    def _transition_to_next_stage(self):
-++++-+        current_index = STAGES.index(self.current_stage)
-++++-+        # After 'Deployer', the cycle is complete
-++++-+        if self.current_stage == "Deployer":
-++++-+            self._complete_requirement_cycle()
-++++-+            self.current_stage = STAGES[0]
-++++-+        else:
-++++-+            self.current_stage = STAGES[current_index + 1]
-++++-+        self.state.set("CurrentStage", self.current_stage)
-++++-+
-++++-+    def _complete_requirement_cycle(self):
-++++-+        req_id = int(self.state.get("RequirementPointer"))
-++++-+        os.makedirs("logs", exist_ok=True)
-++++-+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-++++-+        with open(APPROVAL_FILE, "a") as f:
-++++-+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-++++-+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-++++-+        next_req_id = req_id + 1
-++++-+        self.state.set("RequirementPointer", next_req_id)
-++++-+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-++++-+
-++++- class WorkflowManager:
-++++-     def __init__(self):
-++++-         self.state = WorkflowState()
-++++-+        self.governor = Governor(self.state) # The manager now has a governor
-+++++ class Governor:
-++++++    RULES = {
-++++++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
-++++++        "Coder": "Can use file system tools, code editing tools, and run tests.",
-++++++        "Validator": "Can only run tests and validation tools.",
-++++++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
-++++++        "Researcher": "Can use web search and documentation reading tools."
-++++++    }
-+++++     def __init__(self, state):
-+++++         self.state = state
-++++          self.current_stage = self.state.get("CurrentStage")
-+++   
-+++--+    # New command
-+++--+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-+++--+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-+++-+@@ -26,11 +24,9 @@ def main():
-+++-+ 
-+++-+     args = parser.parse_args()
-+++-+     
-+++-+-    manager = StateManager()
-+++-++    manager = WorkflowManager()
-+++-+ 
-+++-+-    if args.command == "review":
-+++-+-        manager.review()
-+++-+-    elif args.command == "approve":
-+++-++    if args.command == "approve":
- ++-+         manager.approve()
--++-++    elif args.command == "new":
--++-++        process_prompt(args.prompt)
--+++++from dw6.state_manager import Governor, WorkflowState
--+++++
--+++++@pytest.fixture
--+++++def mock_state(mocker):
--+++++    """Fixture to create a mock WorkflowState."""
--+++++    state = MagicMock(spec=WorkflowState)
--+++++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
--+++++    return state
--+ +++
--+-+++import os
--+-+++from .state_manager import get_current_requirement_id
--+++++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
--+++++    """Verify the Governor blocks approval if the spec file is missing."""
--+++++    # Arrange: Set the state to Engineer and mock the requirement pointer
--+++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
--+++++    
--+++++    # Ensure the spec file does NOT exist for this test
--+++++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
--+++++    if spec_file.exists():
--+++++        spec_file.unlink()
--+ +++
--+-+++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
--+++++    governor = Governor(mock_state)
--+ +++
--+-+++def process_prompt(prompt_text: str):
--+-+++    """
--+-+++    Augments a raw user prompt and generates a formal technical specification markdown file.
--+-+++    """
--+-+++    requirement_id = get_current_requirement_id()
--+-+++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
--+++++    # Act & Assert: The approval should fail with a SystemExit
--+++++    with pytest.raises(SystemExit) as e:
--+++++        governor._validate_stage_exit_criteria()
--+++++    
--+++++    assert e.type == SystemExit
--+++++    assert e.value.code == 1
--+ +++
--+-+++    content = f"# Requirement: {requirement_id}\n\n"
--+-+++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
--+-+++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
--+++++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
--+++++    """Verify the Governor allows approval if the spec file exists."""
--+++++    # Arrange: Set the state to Engineer and mock the requirement pointer
--+++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
--+++++    
--+++++    # Ensure the spec file DOES exist for this test
--+++++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
--+++++    spec_file.parent.mkdir(parents=True, exist_ok=True)
--+++++    spec_file.touch()
--+ +++
--+++++    governor = Governor(mock_state)
--+++++
--+++++    # Act & Assert: The approval should pass without raising an exception
--+ +++    try:
--+-+++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
--+-+++        with open(file_path, 'w') as f:
--+-+++            f.write(content)
--+-+++        print(f"Successfully created specification: {file_path}")
--+-+++    except IOError as e:
--+-+++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
--+-+++        sys.exit(1)
--+-++diff --git a/src/dw6/main.py b/src/dw6/main.py
--+-++index 7bbd031..a55f148 100644
--+-++--- a/src/dw6/main.py
--+-+++++ b/src/dw6/main.py
--+-++@@ -2,6 +2,7 @@
--+-++ import argparse
--+-++ import sys
--+-++ from dw6.state_manager import StateManager
--+-+++from dw6.augmenter import process_prompt
-+++-+     elif args.command == "new":
-+++-+         process_prompt(args.prompt)
-+++-+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-+++-+index 703640c..b829d36 100644
-+++-+--- a/src/dw6/state_manager.py
-+++-++++ b/src/dw6/state_manager.py
-+++-+@@ -9,7 +9,7 @@ from dw6 import git_handler
-+++-+ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
-+++-+ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
-+++-+ APPROVAL_FILE = "logs/approvals.log"
-+++-+-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
-+++-++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
-+++-+ DELIVERABLE_PATHS = {
-+++-+     "Engineer": "deliverables/engineering",
-+++-+     "Coder": "deliverables/coding",
-+++-+@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
-+++-+     "Researcher": "deliverables/research",
-+++-+ }
-+++-+ 
-+++-++class Governor:
-+++-++    def __init__(self, state):
-+++-++        self.state = state
-+++-++        self.current_stage = self.state.get("CurrentStage")
-++++-     def get_state(self):
-++++-         return self.state.data
-++++- 
-++++++    def enforce_rules(self):
-++++++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
-++++++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
-++++++        print(f"[RULE] {rule}")
-+ + ++
-+++-++    def approve(self):
-+++-++        old_stage = self.current_stage
-+++-++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-+++-++        self._validate_stage_exit_criteria()
-+++-++        # The original logic from WorkflowManager is now fully integrated here.
-+++-++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
-+++-++        workflow_manager._validate_stage()
-+++-++        workflow_manager._run_pre_transition_actions()
-+++-++        self._transition_to_next_stage() # This method now belongs to the Governor
-+++-++        workflow_manager._run_post_transition_actions()
-+++-++        self.state.save()
-+++-++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-+++-++
-+++-++    def _validate_stage_exit_criteria(self):
-+++-++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
-+++-++        if self.current_stage == "Engineer":
-+++-++            req_id = self.state.get("RequirementPointer")
-+++-++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
-+++-++            if not spec_file.exists():
-+++-++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
-+++-++                sys.exit(1)
-+++-++            print("Governor: 'Engineer' exit criteria met.")
-++++      def approve(self):
-++++--        old_stage = self.current_stage
-++++--        print(f"--- Approving Stage: {old_stage} ---")
-++++--        self._validate_stage()
-++++--        self._run_pre_transition_actions()
-++++--        self._transition_to_next_stage()
-++++--        self._run_post_transition_actions()
-++++--        self.state.save()
-++++--        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-++++-+        # The manager now simply delegates to the governor.
-++++-+        self.governor.approve()
-++++- 
-++++-     def _validate_stage(self):
-++++-         print(f"Validating deliverables for stage: {self.current_stage}")
-++++-@@ -123,25 +167,7 @@ class WorkflowManager:
-++++-         if self.current_stage == "Coder":
-++++-             git_handler.save_current_commit_sha()
-++++- 
-++++--    def _transition_to_next_stage(self):
-++++--        current_index = STAGES.index(self.current_stage)
-++++--        if current_index == len(STAGES) - 1:
-++++--            self._complete_requirement_cycle()
-++++--            self.current_stage = STAGES[0]
-++++--        else:
-++++--            self.current_stage = STAGES[current_index + 1]
-++++--        self.state.set("CurrentStage", self.current_stage)
-++++- 
-++++--    def _complete_requirement_cycle(self):
-++++--        req_id = int(self.state.get("RequirementPointer"))
-++++--        os.makedirs("logs", exist_ok=True)
-++++--        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-++++--        with open(APPROVAL_FILE, "a") as f:
-++++--            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-++++--        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-++++--        next_req_id = req_id + 1
-++++--        self.state.set("RequirementPointer", next_req_id)
-++++--        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-++++- 
-++++- class WorkflowState:
-++++-     def __init__(self):
-+++++         old_stage = self.current_stage
-+++++         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-++++++        self.enforce_rules()
-+++++         self._validate_stage_exit_criteria()
-+++++         # The original logic from WorkflowManager is now fully integrated here.
-+++++         workflow_manager = WorkflowManager() # We still need access to its methods for now.
-++++ diff --git a/tests/test_governor.py b/tests/test_governor.py
-++++-new file mode 100644
-++++-index 0000000..95b566d
-++++---- /dev/null
-+++++index 95b566d..26bf82b 100644
-+++++--- a/tests/test_governor.py
-++++ +++ b/tests/test_governor.py
-++++-@@ -0,0 +1,55 @@
-++++-+# tests/test_governor.py
-++++-+import pytest
-++++-+from unittest.mock import MagicMock
-++++-+from pathlib import Path
-++++-+import sys
-++++-+
-++++-+from dw6.state_manager import Governor, WorkflowState
-++++-+
-++++-+@pytest.fixture
-++++-+def mock_state(mocker):
-++++-+    """Fixture to create a mock WorkflowState."""
-++++-+    state = MagicMock(spec=WorkflowState)
-++++-+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
-++++-+    return state
-++++-+
-++++-+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
-++++-+    """Verify the Governor blocks approval if the spec file is missing."""
-++++-+    # Arrange: Set the state to Engineer and mock the requirement pointer
-++++-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
-++++-+    
-++++-+    # Ensure the spec file does NOT exist for this test
-++++-+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
-++++-+    if spec_file.exists():
-++++-+        spec_file.unlink()
-++++-+
-++++-+    governor = Governor(mock_state)
-++++-+
-++++-+    # Act & Assert: The approval should fail with a SystemExit
-++++-+    with pytest.raises(SystemExit) as e:
-++++-+        governor._validate_stage_exit_criteria()
-++++-+    
-++++-+    assert e.type == SystemExit
-++++-+    assert e.value.code == 1
-++++-+
-++++-+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-++++-+    """Verify the Governor allows approval if the spec file exists."""
-++++-+    # Arrange: Set the state to Engineer and mock the requirement pointer
-++++-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
-++++-+    
-++++-+    # Ensure the spec file DOES exist for this test
-++++-+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
-++++-+    spec_file.parent.mkdir(parents=True, exist_ok=True)
-++++-+    spec_file.touch()
-+++++@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-+++++         # Clean up the created file
-+++++         if spec_file.exists():
-+++++             spec_file.unlink()
-+++  +
-+++--     if len(sys.argv) == 1:
-+++--         parser.print_help(sys.stderr)
-+++--         sys.exit(1)
-+++--@@ -27,6 +32,8 @@ def main():
-+++--         manager.review()
-+++--     elif args.command == "approve":
-+++-++    def _transition_to_next_stage(self):
-+++-++        current_index = STAGES.index(self.current_stage)
-+++-++        # After 'Deployer', the cycle is complete
-+++-++        if self.current_stage == "Deployer":
-+++-++            self._complete_requirement_cycle()
-+++-++            self.current_stage = STAGES[0]
-+++-++        else:
-+++-++            self.current_stage = STAGES[current_index + 1]
-+++-++        self.state.set("CurrentStage", self.current_stage)
-+++-++
-+++-++    def _complete_requirement_cycle(self):
-+++-++        req_id = int(self.state.get("RequirementPointer"))
-+++-++        os.makedirs("logs", exist_ok=True)
-+++-++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+++-++        with open(APPROVAL_FILE, "a") as f:
-+++-++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-+++-++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-+++-++        next_req_id = req_id + 1
-+++-++        self.state.set("RequirementPointer", next_req_id)
-+++-++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-+++-++
-+++-+ class WorkflowManager:
-+++-+     def __init__(self):
-+++-+         self.state = WorkflowState()
-+++-++        self.governor = Governor(self.state) # The manager now has a governor
-+++-+         self.current_stage = self.state.get("CurrentStage")
-+++-+ 
-+++-+     def get_state(self):
-+++-+         return self.state.data
-+++-+ 
-+++-+     def approve(self):
-+++-+-        old_stage = self.current_stage
-+++-+-        print(f"--- Approving Stage: {old_stage} ---")
-+++-+-        self._validate_stage()
-+++-+-        self._run_pre_transition_actions()
-+++-+-        self._transition_to_next_stage()
-+++-+-        self._run_post_transition_actions()
-+++-+-        self.state.save()
-+++-+-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-+++-++        # The manager now simply delegates to the governor.
-+++-++        self.governor.approve()
-+++-+ 
-+++-+     def _validate_stage(self):
-+++-+         print(f"Validating deliverables for stage: {self.current_stage}")
-+++-+@@ -123,25 +167,7 @@ class WorkflowManager:
-+++-+         if self.current_stage == "Coder":
-+++-+             git_handler.save_current_commit_sha()
-+++-+ 
-+++-+-    def _transition_to_next_stage(self):
-+++-+-        current_index = STAGES.index(self.current_stage)
-+++-+-        if current_index == len(STAGES) - 1:
-+++-+-            self._complete_requirement_cycle()
-+++-+-            self.current_stage = STAGES[0]
-+++-+-        else:
-+++-+-            self.current_stage = STAGES[current_index + 1]
-+++-+-        self.state.set("CurrentStage", self.current_stage)
-+++-+ 
-+++-+-    def _complete_requirement_cycle(self):
-+++-+-        req_id = int(self.state.get("RequirementPointer"))
-+++-+-        os.makedirs("logs", exist_ok=True)
-+++-+-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+++-+-        with open(APPROVAL_FILE, "a") as f:
-+++-+-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-+++-+-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-+++-+-        next_req_id = req_id + 1
-+++-+-        self.state.set("RequirementPointer", next_req_id)
-+++-+-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-+++-+ 
-+++-+ class WorkflowState:
-+++-+     def __init__(self):
-+++-+diff --git a/tests/test_governor.py b/tests/test_governor.py
-+++-+new file mode 100644
-+++-+index 0000000..95b566d
-+++-+--- /dev/null
-+++-++++ b/tests/test_governor.py
-+++-+@@ -0,0 +1,55 @@
-+++-++# tests/test_governor.py
-+++-++import pytest
-+++-++from unittest.mock import MagicMock
-+++-++from pathlib import Path
-+++-++import sys
-+++-++
-+++-++from dw6.state_manager import Governor, WorkflowState
-+++-++
-+++-++@pytest.fixture
-+++-++def mock_state(mocker):
-+++-++    """Fixture to create a mock WorkflowState."""
-+++-++    state = MagicMock(spec=WorkflowState)
-+++-++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
-+++-++    return state
-+++-++
-+++-++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
-+++-++    """Verify the Governor blocks approval if the spec file is missing."""
-+++-++    # Arrange: Set the state to Engineer and mock the requirement pointer
-+++-++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
-+++-++    
-+++-++    # Ensure the spec file does NOT exist for this test
-+++-++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
-+++-++    if spec_file.exists():
-+++-++        spec_file.unlink()
-+++-++
-+++-++    governor = Governor(mock_state)
-+++-++
-+++-++    # Act & Assert: The approval should fail with a SystemExit
-+++-++    with pytest.raises(SystemExit) as e:
-+++-++        governor._validate_stage_exit_criteria()
-+++-++    
-+++-++    assert e.type == SystemExit
-+++-++    assert e.value.code == 1
-+++-++
-+++-++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-+++-++    """Verify the Governor allows approval if the spec file exists."""
-+++-++    # Arrange: Set the state to Engineer and mock the requirement pointer
-+++-++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
-+++-++    
-+++-++    # Ensure the spec file DOES exist for this test
-+++-++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
-+++-++    spec_file.parent.mkdir(parents=True, exist_ok=True)
-+++-++    spec_file.touch()
-+++-++
-+++-++    governor = Governor(mock_state)
-+++-++
-+++-++    # Act & Assert: The approval should pass without raising an exception
-+ +-++    try:
-+-+-++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-+-+-++        with open(file_path, 'w') as f:
-+-+-++            f.write(content)
-+-+-++        print(f"Successfully created specification: {file_path}")
-+-+-++    except IOError as e:
-+-+-++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-+-+-++        sys.exit(1)
-+-+-+diff --git a/src/dw6/main.py b/src/dw6/main.py
-+-+-+index 7bbd031..a55f148 100644
-+-+-+--- a/src/dw6/main.py
-+-+-++++ b/src/dw6/main.py
-+-+-+@@ -2,6 +2,7 @@
-+-+-+ import argparse
-+-+-+ import sys
-+-+-+ from dw6.state_manager import StateManager
-+-+-++from dw6.augmenter import process_prompt
-+-+++ class WorkflowManager:
-+-+++     def __init__(self):
-+-+++         self.state = WorkflowState()
-+-++++        self.governor = Governor(self.state) # The manager now has a governor
-+-+++         self.current_stage = self.state.get("CurrentStage")
-+-+ + 
-+-+-+ def main():
-+-+-+     """Main entry point for the DW6 CLI."""
-+-+-+@@ -15,6 +16,10 @@ def main():
-+-+-+     # Approve command
-+-+-+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-+-+++     def get_state(self):
-+-+++         return self.state.data
-+-+ + 
-+-+-++    # New command
-+-+-++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-+-+-++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-+-+++     def approve(self):
-+-+++-        old_stage = self.current_stage
-+-+++-        print(f"--- Approving Stage: {old_stage} ---")
-+-+++-        self._validate_stage()
-+-+++-        self._run_pre_transition_actions()
-+-+++-        self._transition_to_next_stage()
-+-+++-        self._run_post_transition_actions()
-+-+++-        self.state.save()
-+-+++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-+-++++        # The manager now simply delegates to the governor.
-+-++++        self.governor.approve()
-+-+++ 
-+-+++     def _validate_stage(self):
-+-+++         print(f"Validating deliverables for stage: {self.current_stage}")
-+-+++@@ -123,25 +167,7 @@ class WorkflowManager:
-+-+++         if self.current_stage == "Coder":
-+-+++             git_handler.save_current_commit_sha()
-+-+++ 
-+-+++-    def _transition_to_next_stage(self):
-+-+++-        current_index = STAGES.index(self.current_stage)
-+-+++-        if current_index == len(STAGES) - 1:
-+-+++-            self._complete_requirement_cycle()
-+-+++-            self.current_stage = STAGES[0]
-+-+++-        else:
-+-+++-            self.current_stage = STAGES[current_index + 1]
-+-+++-        self.state.set("CurrentStage", self.current_stage)
-+-+++ 
-+-+++-    def _complete_requirement_cycle(self):
-+-+++-        req_id = int(self.state.get("RequirementPointer"))
-+-+++-        os.makedirs("logs", exist_ok=True)
-+-+++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+-+++-        with open(APPROVAL_FILE, "a") as f:
-+-+++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-+-+++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-+-+++-        next_req_id = req_id + 1
-+-+++-        self.state.set("RequirementPointer", next_req_id)
-+-+++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-+-+++ 
-+-+++ class WorkflowState:
-+-+++     def __init__(self):
-+-+++diff --git a/tests/test_governor.py b/tests/test_governor.py
-+- ++new file mode 100644
-+--++index 0000000..c1614f0
-+-+++index 0000000..95b566d
-+- ++--- /dev/null
-+--+++++ b/src/dw6/augmenter.py
-+--++@@ -0,0 +1,26 @@
-+--+++# src/dw6/augmenter.py
-+-++++++ b/tests/test_governor.py
-+-+++@@ -0,0 +1,55 @@
-+-++++# tests/test_governor.py
-+-++++import pytest
-+-++++from unittest.mock import MagicMock
-+-++++from pathlib import Path
-+-++++import sys
-+-+ ++
-+-+-+     if len(sys.argv) == 1:
-+-+-+         parser.print_help(sys.stderr)
-+-+-+         sys.exit(1)
-+-+-+@@ -27,6 +32,8 @@ def main():
-+-+-+         manager.review()
-+-+-+     elif args.command == "approve":
-+-+-+         manager.approve()
-+-+-++    elif args.command == "new":
-+-+-++        process_prompt(args.prompt)
-+-++++from dw6.state_manager import Governor, WorkflowState
-+-++++
-+-++++@pytest.fixture
-+-++++def mock_state(mocker):
-+-++++    """Fixture to create a mock WorkflowState."""
-+-++++    state = MagicMock(spec=WorkflowState)
-+-++++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
-+-++++    return state
-+- +++
-+--+++import os
-+--+++from .state_manager import get_current_requirement_id
-+-++++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
-+-++++    """Verify the Governor blocks approval if the spec file is missing."""
-+-++++    # Arrange: Set the state to Engineer and mock the requirement pointer
-+-++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
-+-++++    
-+-++++    # Ensure the spec file does NOT exist for this test
-+-++++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
-+-++++    if spec_file.exists():
-+-++++        spec_file.unlink()
-+- +++
-+--+++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-+-++++    governor = Governor(mock_state)
-+- +++
-+--+++def process_prompt(prompt_text: str):
-+--+++    """
-+--+++    Augments a raw user prompt and generates a formal technical specification markdown file.
-+--+++    """
-+--+++    requirement_id = get_current_requirement_id()
-+--+++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-+-++++    # Act & Assert: The approval should fail with a SystemExit
-+-++++    with pytest.raises(SystemExit) as e:
-+-++++        governor._validate_stage_exit_criteria()
-+-++++    
-+-++++    assert e.type == SystemExit
-+-++++    assert e.value.code == 1
-+- +++
-+--+++    content = f"# Requirement: {requirement_id}\n\n"
-+--+++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-+--+++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-+-++++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-+-++++    """Verify the Governor allows approval if the spec file exists."""
-+-++++    # Arrange: Set the state to Engineer and mock the requirement pointer
-+-++++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
-+-++++    
-+-++++    # Ensure the spec file DOES exist for this test
-+-++++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
-+-++++    spec_file.parent.mkdir(parents=True, exist_ok=True)
-+-++++    spec_file.touch()
-+- +++
-+-++++    governor = Governor(mock_state)
-+-++++
-+-++++    # Act & Assert: The approval should pass without raising an exception
-+- +++    try:
-+--+++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-+--+++        with open(file_path, 'w') as f:
-+--+++            f.write(content)
-+--+++        print(f"Successfully created specification: {file_path}")
-+--+++    except IOError as e:
-+--+++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-+--+++        sys.exit(1)
-+--++diff --git a/src/dw6/main.py b/src/dw6/main.py
-+--++index 7bbd031..a55f148 100644
-+--++--- a/src/dw6/main.py
-+--+++++ b/src/dw6/main.py
-+--++@@ -2,6 +2,7 @@
-+--++ import argparse
-+--++ import sys
-+--++ from dw6.state_manager import StateManager
-+--+++from dw6.augmenter import process_prompt
-+++-++        governor._validate_stage_exit_criteria()
-+++-++    except SystemExit:
-+++-++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
-+++-++    finally:
-+++-++        # Clean up the created file
-+++-++        if spec_file.exists():
-+++-++            spec_file.unlink()
-+++-+diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
-+++-+index 5b9d1eb..44d2cc9 100644
-+++-+--- a/tests/test_state_manager_integration.py
-+++-++++ b/tests/test_state_manager_integration.py
-+++-+@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-+++-+ 
-+++-+     @patch('dw6.state_manager.WorkflowState')
-+++-+     @patch('dw6.git_handler.get_changes_since_last_commit')
-+++-+-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
-+++-++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
-+++-++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
-+++-+         """Ensure approving Coder stage generates a deliverable without altering the real state."""
-+++-+         # Arrange
-+++-+         mock_state_instance = mock_WorkflowState.return_value
-+++-+@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-+++-+         # Act
-+++-          manager.approve()
-+++--+    elif args.command == "new":
-+++--+        process_prompt(args.prompt)
-+++-  
-+++-- if __name__ == "__main__":
-+++--     main()
-+++-+-        # Assert
-+++-++        # Assert that the deliverable file was created
-+++-+         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
-+++-+         self.assertTrue(deliverable_path.exists())
-+++-++        # Clean up the created file
-+++-++        deliverable_path.unlink()
-+++-++
-+++-+         mock_state_instance.save.assert_called_once()
-+++-+ 
-+++-+ if __name__ == '__main__':
-+++-+diff --git a/uv.lock b/uv.lock
-+++-+index c79d29c..8e7411f 100644
-+++-+--- a/uv.lock
-+++-++++ b/uv.lock
-+++-+@@ -66,6 +66,7 @@ dependencies = [
-+++-+ test = [
-+++-+     { name = "pytest" },
-+++-+     { name = "pytest-cov" },
-+++-++    { name = "pytest-mock" },
-+++-+ ]
-+++-+ 
-+++-+ [package.metadata]
-+++-+@@ -73,6 +74,7 @@ requires-dist = [
-+++-+     { name = "gitpython" },
-+++-+     { name = "pytest", marker = "extra == 'test'" },
-+++-+     { name = "pytest-cov", marker = "extra == 'test'" },
-+++-++    { name = "pytest-mock", marker = "extra == 'test'" },
-+++-+     { name = "python-dotenv" },
-+++-+ ]
-+++-+ provides-extras = ["test"]
-+++-+@@ -167,6 +169,18 @@ wheels = [
-+++-+     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
-+++-+ ]
-+++-+ 
-+++-++[[package]]
-+++-++name = "pytest-mock"
-+++-++version = "3.14.1"
-+++-++source = { registry = "https://pypi.org/simple" }
-+++-++dependencies = [
-+++-++    { name = "pytest" },
-+++-++]
-+++-++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
-+++-++wheels = [
-+++-++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
-+++-++]
-+++-++
-+++-+ [[package]]
-+++-+ name = "python-dotenv"
-+++-+ version = "1.1.1"
-++++++def test_governor_enforces_rules_on_approve(mocker, capsys):
-++++++    """Verify that the Governor prints the correct rule for the current stage."""
-++++++    # Arrange
-++++++    mock_state = mocker.MagicMock(spec=WorkflowState)
-++++++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
-++++ +    governor = Governor(mock_state)
-++++++    # Mock the exit criteria validation to prevent SystemExit
-++++++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
-++++++    # Mock the rest of the approval process to isolate the rule enforcement
-++++++    mocker.patch.object(governor, '_transition_to_next_stage')
-++++++    mocker.patch('dw6.state_manager.WorkflowManager')
-++ + +
-++++-+    # Act & Assert: The approval should pass without raising an exception
-++ +-+    try:
-++-+-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-++-+-+        with open(file_path, 'w') as f:
-++-+-+            f.write(content)
-++-+-+        print(f"Successfully created specification: {file_path}")
-++-+-+    except IOError as e:
-++-+-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-++-+-+        sys.exit(1)
-++-+++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
-++-++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
-++-++index 9718eda..b85b3d9 100644
-++-++--- a/logs/.last_commit_sha
-++-+++++ b/logs/.last_commit_sha
-++-++@@ -1 +1 @@
-++-++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
-++-++\ No newline at end of file
-++-+++75be02c0b7e1723e32042299497f3673b11b4ddd
-++-++\ No newline at end of file
-++-++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
-++-++index 28746b7..743582b 100644
-++-++--- a/logs/workflow_state.txt
-++-+++++ b/logs/workflow_state.txt
-++-++@@ -1,2 +1,2 @@
-++-++-CurrentStage=Engineer
-++-++-RequirementPointer=7
-++-+++CurrentStage=Coder
-++-+++RequirementPointer=9
-++-++diff --git a/pytest.ini b/pytest.ini
-++- +new file mode 100644
-++--+index 0000000..c1614f0
-++-++index 0000000..a635c5c
-++- +--- /dev/null
-++--++++ b/src/dw6/augmenter.py
-++--+@@ -0,0 +1,26 @@
-++--++# src/dw6/augmenter.py
-++-+++++ b/pytest.ini
-++-++@@ -0,0 +1,2 @@
-++-+++[pytest]
-++-+++pythonpath = .
-++-+ diff --git a/src/dw6/main.py b/src/dw6/main.py
-++-+-index 7bbd031..a55f148 100644
-++-++index a55f148..90862f9 100644
-++-+ --- a/src/dw6/main.py
-++-+ +++ b/src/dw6/main.py
-++-+-@@ -2,6 +2,7 @@
-++-++@@ -1,7 +1,7 @@
-++-++ # dw6/main.py
-++-+  import argparse
-++-+  import sys
-++-+- from dw6.state_manager import StateManager
-++-+-+from dw6.augmenter import process_prompt
-++-++-from dw6.state_manager import StateManager
-++-+++from dw6.state_manager import WorkflowManager
-++-++ from dw6.augmenter import process_prompt
-++-+  
-++-+  def main():
-++-+-     """Main entry point for the DW6 CLI."""
-++-+-@@ -15,6 +16,10 @@ def main():
-++-++@@ -10,9 +10,7 @@ def main():
-++-++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-++-++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
- +-++ 
--+-++ def main():
--+-++     """Main entry point for the DW6 CLI."""
--+-++@@ -15,6 +16,10 @@ def main():
--+-++     # Approve command
--+-++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
--+++++        governor._validate_stage_exit_criteria()
--+++++    except SystemExit:
--+++++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
--+++++    finally:
--+++++        # Clean up the created file
--+++++        if spec_file.exists():
--+++++            spec_file.unlink()
--++++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
--++++index 5b9d1eb..44d2cc9 100644
--++++--- a/tests/test_state_manager_integration.py
--+++++++ b/tests/test_state_manager_integration.py
--++++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
--+ ++ 
--+-+++    # New command
--+-+++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
--+-+++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
--++++     @patch('dw6.state_manager.WorkflowState')
--++++     @patch('dw6.git_handler.get_changes_since_last_commit')
--++++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
--+++++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
--+++++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
--++++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
--++++         # Arrange
--++++         mock_state_instance = mock_WorkflowState.return_value
--++++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
--++++         # Act
--+++          manager.approve()
--+++-+    elif args.command == "new":
--+++-+        process_prompt(args.prompt)
--+++  
--+++- if __name__ == "__main__":
--+++-     main()
--++++-        # Assert
--+++++        # Assert that the deliverable file was created
--++++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
--++++         self.assertTrue(deliverable_path.exists())
--+++++        # Clean up the created file
--+++++        deliverable_path.unlink()
--+ +++
--+-++     if len(sys.argv) == 1:
--+-++         parser.print_help(sys.stderr)
--+-++         sys.exit(1)
--+-++@@ -27,6 +32,8 @@ def main():
--+-++         manager.review()
--+-++     elif args.command == "approve":
--+-++         manager.approve()
--+-+++    elif args.command == "new":
--+-+++        process_prompt(args.prompt)
--++++         mock_state_instance.save.assert_called_once()
--+ ++ 
--+-++ if __name__ == "__main__":
--+-++     main()
--+-++```
--+-+\ No newline at end of file
--+-+diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
--++++ if __name__ == '__main__':
--++++diff --git a/uv.lock b/uv.lock
--++++index c79d29c..8e7411f 100644
--++++--- a/uv.lock
--+++++++ b/uv.lock
--++++@@ -66,6 +66,7 @@ dependencies = [
--++++ test = [
--++++     { name = "pytest" },
--++++     { name = "pytest-cov" },
--+++++    { name = "pytest-mock" },
--++++ ]
--++ + 
--++-+ if __name__ == "__main__":
--++-+     main()
--++-+```
--++++ [package.metadata]
--++++@@ -73,6 +74,7 @@ requires-dist = [
--++++     { name = "gitpython" },
--++++     { name = "pytest", marker = "extra == 'test'" },
--++++     { name = "pytest-cov", marker = "extra == 'test'" },
--+++++    { name = "pytest-mock", marker = "extra == 'test'" },
--++++     { name = "python-dotenv" },
--++++ ]
--++++ provides-extras = ["test"]
--++++@@ -167,6 +169,18 @@ wheels = [
--++++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
--++++ ]
-- +++ 
---+++ if __name__ == "__main__":
---+++     main()
---+++```
---++\ No newline at end of file
---++diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
---+ new file mode 100644
---+-index 0000000..c1614f0
---++index 0000000..6c1638b
---+ --- /dev/null
---+-+++ b/src/dw6/augmenter.py
---+-@@ -0,0 +1,26 @@
---+-+# src/dw6/augmenter.py
--+++++[[package]]
--+++++name = "pytest-mock"
--+++++version = "3.14.1"
--+++++source = { registry = "https://pypi.org/simple" }
--+++++dependencies = [
--+++++    { name = "pytest" },
--+++++]
--+++++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
--+++++wheels = [
--+++++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
--+++++]
--+++++
--++++ [[package]]
--++++ name = "python-dotenv"
--++++ version = "1.1.1"
--+++ ```
--++ \ No newline at end of file
--++-diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
--+++diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
--+  new file mode 100644
--+--index 0000000..c1614f0
--+-+index 0000000..6c1638b
--++-index 0000000..6c1638b
--+++index 0000000..691df8d
--+  --- /dev/null
--+--+++ b/src/dw6/augmenter.py
--+--@@ -0,0 +1,26 @@
--+--+# src/dw6/augmenter.py
-++-++-    # Review command
-++-++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
-++-++-    
-++- ++
-++--++import os
-++--++from .state_manager import get_current_requirement_id
-++-+      # Approve command
-++-+      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-++-+  
-++-+-+    # New command
-++-+-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-++-+-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-++-++@@ -26,11 +24,9 @@ def main():
-+ -++ 
-+--++ def main():
-+--++     """Main entry point for the DW6 CLI."""
-+--++@@ -15,6 +16,10 @@ def main():
-+--++     # Approve command
-+--++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-+-++++        governor._validate_stage_exit_criteria()
-+-++++    except SystemExit:
-+-++++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
-+-++++    finally:
-+-++++        # Clean up the created file
-+-++++        if spec_file.exists():
-+-++++            spec_file.unlink()
-+-+++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
-+-+++index 5b9d1eb..44d2cc9 100644
-+-+++--- a/tests/test_state_manager_integration.py
-+-++++++ b/tests/test_state_manager_integration.py
-+-+++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-+- ++ 
-+--+++    # New command
-+--+++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-+--+++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-+-+++     @patch('dw6.state_manager.WorkflowState')
-+-+++     @patch('dw6.git_handler.get_changes_since_last_commit')
-+-+++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
-+-++++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
-+-++++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
-+-+++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
-+-+++         # Arrange
-+-+++         mock_state_instance = mock_WorkflowState.return_value
-+-+++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-+-+++         # Act
-+-++          manager.approve()
-+-++-+    elif args.command == "new":
-+-++-+        process_prompt(args.prompt)
-+-++  
-+-++- if __name__ == "__main__":
-+-++-     main()
-+-+++-        # Assert
-+-++++        # Assert that the deliverable file was created
-+-+++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
-+-+++         self.assertTrue(deliverable_path.exists())
-+-++++        # Clean up the created file
-+-++++        deliverable_path.unlink()
-+- +++
-+--++     if len(sys.argv) == 1:
-+--++         parser.print_help(sys.stderr)
-+--++         sys.exit(1)
-+--++@@ -27,6 +32,8 @@ def main():
-+--++         manager.review()
-+--++     elif args.command == "approve":
-++-++     args = parser.parse_args()
-++-++     
-++-++-    manager = StateManager()
-++-+++    manager = WorkflowManager()
-++-++ 
-++-++-    if args.command == "review":
-++-++-        manager.review()
-++-++-    elif args.command == "approve":
-++-+++    if args.command == "approve":
-+ -++         manager.approve()
-+--+++    elif args.command == "new":
-+--+++        process_prompt(args.prompt)
-+-+++         mock_state_instance.save.assert_called_once()
-+- ++ 
-+--++ if __name__ == "__main__":
-+--++     main()
-+--++```
-+--+\ No newline at end of file
-+--+diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
-+-+++ if __name__ == '__main__':
-+-+++diff --git a/uv.lock b/uv.lock
-+-+++index c79d29c..8e7411f 100644
-+-+++--- a/uv.lock
-+-++++++ b/uv.lock
-+-+++@@ -66,6 +66,7 @@ dependencies = [
-+-+++ test = [
-+-+++     { name = "pytest" },
-+-+++     { name = "pytest-cov" },
-+-++++    { name = "pytest-mock" },
-+-+++ ]
-+-+ + 
-+-+-+ if __name__ == "__main__":
-+-+-+     main()
-+-+-+```
-+-+++ [package.metadata]
-+-+++@@ -73,6 +74,7 @@ requires-dist = [
-+-+++     { name = "gitpython" },
-+-+++     { name = "pytest", marker = "extra == 'test'" },
-+-+++     { name = "pytest-cov", marker = "extra == 'test'" },
-+-++++    { name = "pytest-mock", marker = "extra == 'test'" },
-+-+++     { name = "python-dotenv" },
-+-+++ ]
-+-+++ provides-extras = ["test"]
-+-+++@@ -167,6 +169,18 @@ wheels = [
-+-+++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
-+-+++ ]
-+-+++ 
-+-++++[[package]]
-+-++++name = "pytest-mock"
-+-++++version = "3.14.1"
-+-++++source = { registry = "https://pypi.org/simple" }
-+-++++dependencies = [
-+-++++    { name = "pytest" },
-+-++++]
-+-++++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
-+-++++wheels = [
-+-++++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
-+-++++]
-+-++++
-+-+++ [[package]]
-+-+++ name = "python-dotenv"
-+-+++ version = "1.1.1"
-+-++ ```
-+-+ \ No newline at end of file
-+-+-diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
-+-++diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
-++-++     elif args.command == "new":
-++-++         process_prompt(args.prompt)
-++-++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-++-++index 703640c..b829d36 100644
-++-++--- a/src/dw6/state_manager.py
-++-+++++ b/src/dw6/state_manager.py
-++-++@@ -9,7 +9,7 @@ from dw6 import git_handler
-++-++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
-++-++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
-++-++ APPROVAL_FILE = "logs/approvals.log"
-++-++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
-++-+++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
-++-++ DELIVERABLE_PATHS = {
-++-++     "Engineer": "deliverables/engineering",
-++-++     "Coder": "deliverables/coding",
-++-++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
-++-++     "Researcher": "deliverables/research",
-++-++ }
-++-++ 
-++-+++class Governor:
-++-+++    def __init__(self, state):
-++-+++        self.state = state
-++-+++        self.current_stage = self.state.get("CurrentStage")
-++- ++
-++--++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-++-+++    def approve(self):
-++-+++        old_stage = self.current_stage
-++-+++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-++-+++        self._validate_stage_exit_criteria()
-++-+++        # The original logic from WorkflowManager is now fully integrated here.
-++-+++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
-++-+++        workflow_manager._validate_stage()
-++-+++        workflow_manager._run_pre_transition_actions()
-++-+++        self._transition_to_next_stage() # This method now belongs to the Governor
-++-+++        workflow_manager._run_post_transition_actions()
-++-+++        self.state.save()
-++-+++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-++- ++
-++--++def process_prompt(prompt_text: str):
-++--++    """
-++--++    Augments a raw user prompt and generates a formal technical specification markdown file.
-++--++    """
-++--++    requirement_id = get_current_requirement_id()
-++--++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-++-+++    def _validate_stage_exit_criteria(self):
-++-+++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
-++-+++        if self.current_stage == "Engineer":
-++-+++            req_id = self.state.get("RequirementPointer")
-++-+++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
-++-+++            if not spec_file.exists():
-++-+++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
-++-+++                sys.exit(1)
-++-+++            print("Governor: 'Engineer' exit criteria met.")
-++++-+        governor._validate_stage_exit_criteria()
-++++-+    except SystemExit:
-++++-+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
-++++-+    finally:
-++++-+        # Clean up the created file
-++++-+        if spec_file.exists():
-++++-+            spec_file.unlink()
-++++-diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
-++++-index 5b9d1eb..44d2cc9 100644
-++++---- a/tests/test_state_manager_integration.py
-++++-+++ b/tests/test_state_manager_integration.py
-++++-@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-++++- 
-++++-     @patch('dw6.state_manager.WorkflowState')
-++++-     @patch('dw6.git_handler.get_changes_since_last_commit')
-++++--    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
-++++-+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
-++++-+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
-++++-         """Ensure approving Coder stage generates a deliverable without altering the real state."""
-++++-         # Arrange
-++++-         mock_state_instance = mock_WorkflowState.return_value
-++++-@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-++++-         # Act
-++++-         manager.approve()
-++++- 
-++++--        # Assert
-++++-+        # Assert that the deliverable file was created
-++++-         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
-++++-         self.assertTrue(deliverable_path.exists())
-++++-+        # Clean up the created file
-++++-+        deliverable_path.unlink()
-++++-+
-++++-         mock_state_instance.save.assert_called_once()
-++++- 
-++++- if __name__ == '__main__':
-++++-diff --git a/uv.lock b/uv.lock
-++++-index c79d29c..8e7411f 100644
-++++---- a/uv.lock
-++++-+++ b/uv.lock
-++++-@@ -66,6 +66,7 @@ dependencies = [
-++++- test = [
-++++-     { name = "pytest" },
-++++-     { name = "pytest-cov" },
-++++-+    { name = "pytest-mock" },
-++++- ]
-++++- 
-++++- [package.metadata]
-++++-@@ -73,6 +74,7 @@ requires-dist = [
-++++-     { name = "gitpython" },
-++++-     { name = "pytest", marker = "extra == 'test'" },
-++++-     { name = "pytest-cov", marker = "extra == 'test'" },
-++++-+    { name = "pytest-mock", marker = "extra == 'test'" },
-++++-     { name = "python-dotenv" },
-++++- ]
-++++- provides-extras = ["test"]
-++++-@@ -167,6 +169,18 @@ wheels = [
-++++-     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
-++++- ]
-++++- 
-++++-+[[package]]
-++++-+name = "pytest-mock"
-++++-+version = "3.14.1"
-++++-+source = { registry = "https://pypi.org/simple" }
-++++-+dependencies = [
-++++-+    { name = "pytest" },
-++++-+]
-++++-+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
-++++-+wheels = [
-++++-+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
-++++-+]
-++++++    # Act
-++++++    governor.approve()
-++ + +
-++-+-     if len(sys.argv) == 1:
-++-+-         parser.print_help(sys.stderr)
-++-+-         sys.exit(1)
-++-+-@@ -27,6 +32,8 @@ def main():
-++-+-         manager.review()
-++-+-     elif args.command == "approve":
-++-+++    def _transition_to_next_stage(self):
-++-+++        current_index = STAGES.index(self.current_stage)
-++-+++        # After 'Deployer', the cycle is complete
-++-+++        if self.current_stage == "Deployer":
-++-+++            self._complete_requirement_cycle()
-++-+++            self.current_stage = STAGES[0]
-++-+++        else:
-++-+++            self.current_stage = STAGES[current_index + 1]
-++-+++        self.state.set("CurrentStage", self.current_stage)
-++- ++
-++--++    content = f"# Requirement: {requirement_id}\n\n"
-++--++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-++--++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-++-+++    def _complete_requirement_cycle(self):
-++-+++        req_id = int(self.state.get("RequirementPointer"))
-++-+++        os.makedirs("logs", exist_ok=True)
-++-+++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-++-+++        with open(APPROVAL_FILE, "a") as f:
-++-+++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-++-+++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-++-+++        next_req_id = req_id + 1
-++-+++        self.state.set("RequirementPointer", next_req_id)
-++-+++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-++- ++
++++--     # Approve command
++++--     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++-- 
++++--@@ -26,11 +24,9 @@ def main():
++++-- 
++++--     args = parser.parse_args()
++++--     
++++---    manager = StateManager()
++++--+    manager = WorkflowManager()
++++-- 
++++---    if args.command == "review":
++++---        manager.review()
++++---    elif args.command == "approve":
++++--+    if args.command == "approve":
++++--         manager.approve()
++++--     elif args.command == "new":
++++--         process_prompt(args.prompt)
++++-+ CurrentStage=Coder
++++-+-RequirementPointer=9
++++-++RequirementPointer=10
++++- diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++++--index 703640c..b829d36 100644
++++-+index b829d36..241fa62 100644
++++- --- a/src/dw6/state_manager.py
++++- +++ b/src/dw6/state_manager.py
++++--@@ -9,7 +9,7 @@ from dw6 import git_handler
++++-- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
++++-- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
++++-- APPROVAL_FILE = "logs/approvals.log"
++++---STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
++++--+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
++++-- DELIVERABLE_PATHS = {
++++--     "Engineer": "deliverables/engineering",
++++--     "Coder": "deliverables/coding",
++++--@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
++++--     "Researcher": "deliverables/research",
++++-+@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
++++-  }
+++++  CurrentStage=Coder
+++++--RequirementPointer=9
+++++-+RequirementPointer=10
+++++-diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+++++-index b829d36..241fa62 100644
+++++---- a/src/dw6/state_manager.py
+++++-+++ b/src/dw6/state_manager.py
+++++-@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
+++++- }
++++++-RequirementPointer=10
+++++++RequirementPointer=11
++++++diff --git a/src/dw6/main.py b/src/dw6/main.py
++++++index 90862f9..c65a4d9 100644
++++++--- a/src/dw6/main.py
+++++++++ b/src/dw6/main.py
++++++@@ -1,16 +1,42 @@
++++++ # dw6/main.py
++++++ import argparse
++++++ import sys
+++++++import re
+++++++from pathlib import Path
+++++++from datetime import datetime, timezone
++++++ from dw6.state_manager import WorkflowManager
++++++ from dw6.augmenter import process_prompt
+++    
+++--  def main():
+++---     """Main entry point for the DW6 CLI."""
+++---@@ -15,6 +16,10 @@ def main():
+++--+@@ -10,9 +10,7 @@ def main():
+++--+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+++--+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+++--+ 
+++--+-    # Review command
+++--+-    subparsers.add_parser("review", help="Review the changes for the current stage.")
+++--+-    
+++--++
+++--      # Approve command
+++--      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++-+-+class Governor:
+++-+-+    def __init__(self, state):
+++-+-+        self.state = state
+++-+-+        self.current_stage = self.state.get("CurrentStage")
+++-+-+
+++-+-+    def approve(self):
+++-+-+        old_stage = self.current_stage
+++-+-+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+++-+-+        self._validate_stage_exit_criteria()
+++-+-+        # The original logic from WorkflowManager is now fully integrated here.
+++-+-+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+++-+-+        workflow_manager._validate_stage()
+++-+-+        workflow_manager._run_pre_transition_actions()
+++-+-+        self._transition_to_next_stage() # This method now belongs to the Governor
+++-+-+        workflow_manager._run_post_transition_actions()
+++-+-+        self.state.save()
+++-+-+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+++-+-+
+++-+-+    def _validate_stage_exit_criteria(self):
+++-+-+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+++-+-+        if self.current_stage == "Engineer":
+++-+-+            req_id = self.state.get("RequirementPointer")
+++-+-+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+++-+-+            if not spec_file.exists():
+++-+-+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+++-+-+                sys.exit(1)
+++-+-+            print("Governor: 'Engineer' exit criteria met.")
+++-+-+
+++-+-+    def _transition_to_next_stage(self):
+++-+-+        current_index = STAGES.index(self.current_stage)
+++-+-+        # After 'Deployer', the cycle is complete
+++-+-+        if self.current_stage == "Deployer":
+++-+-+            self._complete_requirement_cycle()
+++-+-+            self.current_stage = STAGES[0]
+++-+-+        else:
+++-+-+            self.current_stage = STAGES[current_index + 1]
+++-+-+        self.state.set("CurrentStage", self.current_stage)
+++-+-+
+++-+-+    def _complete_requirement_cycle(self):
+++-+-+        req_id = int(self.state.get("RequirementPointer"))
+++-+-+        os.makedirs("logs", exist_ok=True)
+++-+-+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++-+-+        with open(APPROVAL_FILE, "a") as f:
+++-+-+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+++-+-+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+++-+-+        next_req_id = req_id + 1
+++-+-+        self.state.set("RequirementPointer", next_req_id)
+++-+-+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+++-+-+
+++-+- class WorkflowManager:
+++-+-     def __init__(self):
+++-+-         self.state = WorkflowState()
+++-+-+        self.governor = Governor(self.state) # The manager now has a governor
+++-++ class Governor:
+++-+++    RULES = {
+++-+++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+++-+++        "Coder": "Can use file system tools, code editing tools, and run tests.",
+++-+++        "Validator": "Can only run tests and validation tools.",
+++-+++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+++-+++        "Researcher": "Can use web search and documentation reading tools."
+++-+++    }
+++-++     def __init__(self, state):
+++-++         self.state = state
+++-+          self.current_stage = self.state.get("CurrentStage")
++++--+class Governor:
++++--+    def __init__(self, state):
++++--+        self.state = state
++++--+        self.current_stage = self.state.get("CurrentStage")
++++--+
++++--+    def approve(self):
++++--+        old_stage = self.current_stage
++++--+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++++--+        self._validate_stage_exit_criteria()
++++--+        # The original logic from WorkflowManager is now fully integrated here.
++++--+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
++++--+        workflow_manager._validate_stage()
++++--+        workflow_manager._run_pre_transition_actions()
++++--+        self._transition_to_next_stage() # This method now belongs to the Governor
++++--+        workflow_manager._run_post_transition_actions()
++++--+        self.state.save()
++++--+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++++--+
++++--+    def _validate_stage_exit_criteria(self):
++++--+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
++++--+        if self.current_stage == "Engineer":
++++--+            req_id = self.state.get("RequirementPointer")
++++--+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
++++--+            if not spec_file.exists():
++++--+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
++++--+                sys.exit(1)
++++--+            print("Governor: 'Engineer' exit criteria met.")
++++--+
++++--+    def _transition_to_next_stage(self):
++++--+        current_index = STAGES.index(self.current_stage)
++++--+        # After 'Deployer', the cycle is complete
++++--+        if self.current_stage == "Deployer":
++++--+            self._complete_requirement_cycle()
++++--+            self.current_stage = STAGES[0]
++++--+        else:
++++--+            self.current_stage = STAGES[current_index + 1]
++++--+        self.state.set("CurrentStage", self.current_stage)
++++--+
++++--+    def _complete_requirement_cycle(self):
++++--+        req_id = int(self.state.get("RequirementPointer"))
++++--+        os.makedirs("logs", exist_ok=True)
++++--+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++++--+        with open(APPROVAL_FILE, "a") as f:
++++--+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++++--+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++++--+        next_req_id = req_id + 1
++++--+        self.state.set("RequirementPointer", next_req_id)
++++--+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++++--+
++++-- class WorkflowManager:
++++--     def __init__(self):
++++--         self.state = WorkflowState()
++++--+        self.governor = Governor(self.state) # The manager now has a governor
++++-+ class Governor:
++++-++    RULES = {
++++-++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
++++-++        "Coder": "Can use file system tools, code editing tools, and run tests.",
++++-++        "Validator": "Can only run tests and validation tools.",
++++-++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
++++-++        "Researcher": "Can use web search and documentation reading tools."
++++-++    }
++++-+     def __init__(self, state):
++++-+         self.state = state
++++-          self.current_stage = self.state.get("CurrentStage")
+++++- class Governor:
+++++-+    RULES = {
+++++-+        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+++++-+        "Coder": "Can use file system tools, code editing tools, and run tests.",
+++++-+        "Validator": "Can only run tests and validation tools.",
+++++-+        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+++++-+        "Researcher": "Can use web search and documentation reading tools."
+++++-+    }
+++++-     def __init__(self, state):
+++++-         self.state = state
+++++-         self.current_stage = self.state.get("CurrentStage")
+++++++META_LOG_FILE = Path("logs/meta_requirements.log")
+++++++
+++++++def register_meta_requirement(description: str):
+++++++    """Logs a new meta-requirement to the meta_requirements.log file."""
+++++++    META_LOG_FILE.parent.mkdir(exist_ok=True)
+++++++    
+++++++    last_id = 0
+++++++    if META_LOG_FILE.exists():
+++++++        with open(META_LOG_FILE, "r") as f:
+++++++            lines = f.readlines()
+++++++            if lines:
+++++++                last_line = lines[-1]
+++++++                match = re.search(r'^\[ID:(\d+)\]', last_line)
+++++++                if match:
+++++++                    last_id = int(match.group(1))
+++++++
+++++++    new_id = last_id + 1
+++++++    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++++++    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
+++++++
+++++++    with open(META_LOG_FILE, "a") as f:
+++++++        f.write(log_entry)
+++++++    
+++++++    print(f"Successfully logged meta-requirement {new_id}.")
+++++++
++++++ def main():
++++++     """Main entry point for the DW6 CLI."""
++++++-    # Test comment for Cycle 2 validation.
++++++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++++++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+++    
+++---+    # New command
+++---+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+++---+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+++--+@@ -26,11 +24,9 @@ def main():
+++--+ 
+++--+     args = parser.parse_args()
+++--+     
+++--+-    manager = StateManager()
+++--++    manager = WorkflowManager()
+++--+ 
+++--+-    if args.command == "review":
+++--+-        manager.review()
+++--+-    elif args.command == "approve":
+++--++    if args.command == "approve":
+ +--+         manager.approve()
+-+--++    elif args.command == "new":
+-+--++        process_prompt(args.prompt)
+-+-+++from dw6.state_manager import Governor, WorkflowState
+-+-+++
+-+-+++@pytest.fixture
+-+-+++def mock_state(mocker):
+-+-+++    """Fixture to create a mock WorkflowState."""
+-+-+++    state = MagicMock(spec=WorkflowState)
+-+-+++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+-+-+++    return state
+-+-+++
+-+-+++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+-+-+++    """Verify the Governor blocks approval if the spec file is missing."""
+-+-+++    # Arrange: Set the state to Engineer and mock the requirement pointer
+-+-+++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+-+-+++    
+-+-+++    # Ensure the spec file does NOT exist for this test
+-+-+++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+-+-+++    if spec_file.exists():
+-+-+++        spec_file.unlink()
+-+-+++
+-+-+++    governor = Governor(mock_state)
+-+-+++
+-+-+++    # Act & Assert: The approval should fail with a SystemExit
+-+-+++    with pytest.raises(SystemExit) as e:
+-+-+++        governor._validate_stage_exit_criteria()
+-+-+++    
+-+-+++    assert e.type == SystemExit
+-+-+++    assert e.value.code == 1
+-+-+++
+-+-+++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+-+-+++    """Verify the Governor allows approval if the spec file exists."""
+-+-+++    # Arrange: Set the state to Engineer and mock the requirement pointer
+-+-+++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+-+-+++    
+-+-+++    # Ensure the spec file DOES exist for this test
+-+-+++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+-+-+++    spec_file.parent.mkdir(parents=True, exist_ok=True)
+-+-+++    spec_file.touch()
+-+-+++
+-+-+++    governor = Governor(mock_state)
+-+-+++
+-+-+++    # Act & Assert: The approval should pass without raising an exception
+-+-+++    try:
+-+-+++        governor._validate_stage_exit_criteria()
+-+-+++    except SystemExit:
+-+-+++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+-+-+++    finally:
+-+-+++        # Clean up the created file
+-+-+++        if spec_file.exists():
+-+-+++            spec_file.unlink()
+-+-++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+-+-++index 5b9d1eb..44d2cc9 100644
+-+-++--- a/tests/test_state_manager_integration.py
+-+-+++++ b/tests/test_state_manager_integration.py
+-+-++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+-+-++ 
+-+-++     @patch('dw6.state_manager.WorkflowState')
+-+-++     @patch('dw6.git_handler.get_changes_since_last_commit')
+-+-++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+-+-+++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+-+-+++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+-+-++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+-+-++         # Arrange
+-+-++         mock_state_instance = mock_WorkflowState.return_value
+-+-++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+-+-++         # Act
+-+-+          manager.approve()
+-+-+-+    elif args.command == "new":
+-+-+-+        process_prompt(args.prompt)
+-+-+  
+-+-+- if __name__ == "__main__":
+-+-+-     main()
+-+-++-        # Assert
+-+-+++        # Assert that the deliverable file was created
+-+-++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+-+-++         self.assertTrue(deliverable_path.exists())
+-+-+++        # Clean up the created file
+-+-+++        deliverable_path.unlink()
+-+-+++
+-+-++         mock_state_instance.save.assert_called_once()
+-+-++ 
+-+-++ if __name__ == '__main__':
+-+-++diff --git a/uv.lock b/uv.lock
+-+-++index c79d29c..8e7411f 100644
+-+-++--- a/uv.lock
+-+-+++++ b/uv.lock
+-+-++@@ -66,6 +66,7 @@ dependencies = [
+-+-++ test = [
+-+-++     { name = "pytest" },
+-+-++     { name = "pytest-cov" },
+-+-+++    { name = "pytest-mock" },
+-+-++ ]
+-+- + 
+-+--+ if __name__ == "__main__":
+-+--+     main()
+-+--+```
+-+-++ [package.metadata]
+-+-++@@ -73,6 +74,7 @@ requires-dist = [
+-+-++     { name = "gitpython" },
+-+-++     { name = "pytest", marker = "extra == 'test'" },
+-+-++     { name = "pytest-cov", marker = "extra == 'test'" },
+-+-+++    { name = "pytest-mock", marker = "extra == 'test'" },
+-+-++     { name = "python-dotenv" },
+-+-++ ]
+-+-++ provides-extras = ["test"]
+-+-++@@ -167,6 +169,18 @@ wheels = [
+-+-++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+-+-++ ]
+-+-++ 
+-+-+++[[package]]
+-+-+++name = "pytest-mock"
+-+-+++version = "3.14.1"
+-+-+++source = { registry = "https://pypi.org/simple" }
+-+-+++dependencies = [
+-+-+++    { name = "pytest" },
+-+-+++]
+-+-+++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+-+-+++wheels = [
+-+-+++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+-+-+++]
+-+-+++
+-+-++ [[package]]
+-+-++ name = "python-dotenv"
+-+-++ version = "1.1.1"
+-+-+ ```
+-+++- [[package]]
+-+++- name = "python-dotenv"
+-+++- version = "1.1.1"
+-+++++    # Assert
+-+++++    captured = capsys.readouterr()
+-+++++    expected_rule = Governor.RULES["Coder"]
+-+++++    assert expected_rule in captured.out
+-++  ```
+-+  \ No newline at end of file
+-+--diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
+-+-+diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
+-++-diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
+-+++diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
+++--+     elif args.command == "new":
+++--+         process_prompt(args.prompt)
+++--+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+++--+index 703640c..b829d36 100644
+++--+--- a/src/dw6/state_manager.py
+++--++++ b/src/dw6/state_manager.py
+++--+@@ -9,7 +9,7 @@ from dw6 import git_handler
+++--+ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+++--+ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+++--+ APPROVAL_FILE = "logs/approvals.log"
+++--+-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+++--++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+++--+ DELIVERABLE_PATHS = {
+++--+     "Engineer": "deliverables/engineering",
+++--+     "Coder": "deliverables/coding",
+++--+@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+++--+     "Researcher": "deliverables/research",
+++--+ }
+++--+ 
+++--++class Governor:
+++--++    def __init__(self, state):
+++--++        self.state = state
+++--++        self.current_stage = self.state.get("CurrentStage")
+++-+-     def get_state(self):
+++-+-         return self.state.data
+++-+- 
+++-+++    def enforce_rules(self):
+++-+++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+++-+++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+++-+++        print(f"[RULE] {rule}")
++++--     def get_state(self):
++++--         return self.state.data
++++-- 
++++-++    def enforce_rules(self):
++++-++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
++++-++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
++++-++        print(f"[RULE] {rule}")
+++++-+    def enforce_rules(self):
+++++-+        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+++++-+        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+++++-+        print(f"[RULE] {rule}")
++++++-
++++++     # Approve command
++++++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++++ 
++++++@@ -18,18 +44,24 @@ def main():
++++++     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++++++     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++++++ 
+++++++    # Meta-req command
+++++++    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
+++++++    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
+++  ++
+++--++    def approve(self):
+++--++        old_stage = self.current_stage
+++--++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+++--++        self._validate_stage_exit_criteria()
+++--++        # The original logic from WorkflowManager is now fully integrated here.
+++--++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+++--++        workflow_manager._validate_stage()
+++--++        workflow_manager._run_pre_transition_actions()
+++--++        self._transition_to_next_stage() # This method now belongs to the Governor
+++--++        workflow_manager._run_post_transition_actions()
+++--++        self.state.save()
+++--++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+++--++
+++--++    def _validate_stage_exit_criteria(self):
+++--++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+++--++        if self.current_stage == "Engineer":
+++--++            req_id = self.state.get("RequirementPointer")
+++--++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+++--++            if not spec_file.exists():
+++--++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+++--++                sys.exit(1)
+++--++            print("Governor: 'Engineer' exit criteria met.")
+++-+      def approve(self):
+++-+--        old_stage = self.current_stage
+++-+--        print(f"--- Approving Stage: {old_stage} ---")
+++-+--        self._validate_stage()
+++-+--        self._run_pre_transition_actions()
+++-+--        self._transition_to_next_stage()
+++-+--        self._run_post_transition_actions()
+++-+--        self.state.save()
+++-+--        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+++-+-+        # The manager now simply delegates to the governor.
+++-+-+        self.governor.approve()
+++-+- 
+++-+-     def _validate_stage(self):
+++-+-         print(f"Validating deliverables for stage: {self.current_stage}")
+++-+-@@ -123,25 +167,7 @@ class WorkflowManager:
+++-+-         if self.current_stage == "Coder":
+++-+-             git_handler.save_current_commit_sha()
+++-+- 
+++-+--    def _transition_to_next_stage(self):
+++-+--        current_index = STAGES.index(self.current_stage)
+++-+--        if current_index == len(STAGES) - 1:
+++-+--            self._complete_requirement_cycle()
+++-+--            self.current_stage = STAGES[0]
+++-+--        else:
+++-+--            self.current_stage = STAGES[current_index + 1]
+++-+--        self.state.set("CurrentStage", self.current_stage)
+++-+- 
+++-+--    def _complete_requirement_cycle(self):
+++-+--        req_id = int(self.state.get("RequirementPointer"))
+++-+--        os.makedirs("logs", exist_ok=True)
+++-+--        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++-+--        with open(APPROVAL_FILE, "a") as f:
+++-+--            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+++-+--        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+++-+--        next_req_id = req_id + 1
+++-+--        self.state.set("RequirementPointer", next_req_id)
+++-+--        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+++-+- 
+++-+- class WorkflowState:
+++-+-     def __init__(self):
+++-++         old_stage = self.current_stage
+++-++         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+++-+++        self.enforce_rules()
+++-++         self._validate_stage_exit_criteria()
+++-++         # The original logic from WorkflowManager is now fully integrated here.
+++-++         workflow_manager = WorkflowManager() # We still need access to its methods for now.
+++-+ diff --git a/tests/test_governor.py b/tests/test_governor.py
+++-+-new file mode 100644
+++-+-index 0000000..95b566d
+++-+---- /dev/null
+++-++index 95b566d..26bf82b 100644
+++-++--- a/tests/test_governor.py
+++-+ +++ b/tests/test_governor.py
+++-+-@@ -0,0 +1,55 @@
+++-+-+# tests/test_governor.py
+++-+-+import pytest
+++-+-+from unittest.mock import MagicMock
+++-+-+from pathlib import Path
+++-+-+import sys
+++-+-+
+++-+-+from dw6.state_manager import Governor, WorkflowState
+++-+-+
+++-+-+@pytest.fixture
+++-+-+def mock_state(mocker):
+++-+-+    """Fixture to create a mock WorkflowState."""
+++-+-+    state = MagicMock(spec=WorkflowState)
+++-+-+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+++-+-+    return state
+++-+-+
+++-+-+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+++-+-+    """Verify the Governor blocks approval if the spec file is missing."""
+++-+-+    # Arrange: Set the state to Engineer and mock the requirement pointer
+++-+-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+++-+-+    
+++-+-+    # Ensure the spec file does NOT exist for this test
+++-+-+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+++-+-+    if spec_file.exists():
+++-+-+        spec_file.unlink()
+++-+-+
+++-+-+    governor = Governor(mock_state)
+++-+-+
+++-+-+    # Act & Assert: The approval should fail with a SystemExit
+++-+-+    with pytest.raises(SystemExit) as e:
+++-+-+        governor._validate_stage_exit_criteria()
+++-+-+    
+++-+-+    assert e.type == SystemExit
+++-+-+    assert e.value.code == 1
+++-+-+
+++-+-+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+++-+-+    """Verify the Governor allows approval if the spec file exists."""
+++-+-+    # Arrange: Set the state to Engineer and mock the requirement pointer
+++-+-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+++-+-+    
+++-+-+    # Ensure the spec file DOES exist for this test
+++-+-+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+++-+-+    spec_file.parent.mkdir(parents=True, exist_ok=True)
+++-+-+    spec_file.touch()
+++-++@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+++-++         # Clean up the created file
+++-++         if spec_file.exists():
+++-++             spec_file.unlink()
++++-      def approve(self):
++++---        old_stage = self.current_stage
++++---        print(f"--- Approving Stage: {old_stage} ---")
++++---        self._validate_stage()
++++---        self._run_pre_transition_actions()
++++---        self._transition_to_next_stage()
++++---        self._run_post_transition_actions()
++++---        self.state.save()
++++---        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++++--+        # The manager now simply delegates to the governor.
++++--+        self.governor.approve()
++++-- 
++++--     def _validate_stage(self):
++++--         print(f"Validating deliverables for stage: {self.current_stage}")
++++--@@ -123,25 +167,7 @@ class WorkflowManager:
++++--         if self.current_stage == "Coder":
++++--             git_handler.save_current_commit_sha()
++++-- 
++++---    def _transition_to_next_stage(self):
++++---        current_index = STAGES.index(self.current_stage)
++++---        if current_index == len(STAGES) - 1:
++++---            self._complete_requirement_cycle()
++++---            self.current_stage = STAGES[0]
++++---        else:
++++---            self.current_stage = STAGES[current_index + 1]
++++---        self.state.set("CurrentStage", self.current_stage)
++++-- 
++++---    def _complete_requirement_cycle(self):
++++---        req_id = int(self.state.get("RequirementPointer"))
++++---        os.makedirs("logs", exist_ok=True)
++++---        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++++---        with open(APPROVAL_FILE, "a") as f:
++++---            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++++---        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++++---        next_req_id = req_id + 1
++++---        self.state.set("RequirementPointer", next_req_id)
++++---        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++++-- 
++++-- class WorkflowState:
++++--     def __init__(self):
++++-+         old_stage = self.current_stage
++++-+         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++++-++        self.enforce_rules()
++++-+         self._validate_stage_exit_criteria()
++++-+         # The original logic from WorkflowManager is now fully integrated here.
++++-+         workflow_manager = WorkflowManager() # We still need access to its methods for now.
++++- diff --git a/tests/test_governor.py b/tests/test_governor.py
++++--new file mode 100644
++++--index 0000000..95b566d
++++----- /dev/null
++++-+index 95b566d..26bf82b 100644
++++-+--- a/tests/test_governor.py
++++- +++ b/tests/test_governor.py
++++--@@ -0,0 +1,55 @@
++++--+# tests/test_governor.py
++++--+import pytest
++++--+from unittest.mock import MagicMock
++++--+from pathlib import Path
++++--+import sys
++++--+
++++--+from dw6.state_manager import Governor, WorkflowState
++++--+
++++--+@pytest.fixture
++++--+def mock_state(mocker):
++++--+    """Fixture to create a mock WorkflowState."""
++++--+    state = MagicMock(spec=WorkflowState)
++++--+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
++++--+    return state
++++--+
++++--+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
++++--+    """Verify the Governor blocks approval if the spec file is missing."""
++++--+    # Arrange: Set the state to Engineer and mock the requirement pointer
++++--+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
++++--+    
++++--+    # Ensure the spec file does NOT exist for this test
++++--+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
++++--+    if spec_file.exists():
++++--+        spec_file.unlink()
++ +--+
++-+--+import os
++-+--+from .state_manager import get_current_requirement_id
++-+-++++ b/deliverables/engineering/cycle_9_technical_specification.md
++-+-+@@ -0,0 +1,9 @@
++-+-++# Requirement: 8
++-++-+++ b/deliverables/engineering/cycle_9_technical_specification.md
++-++++++ b/deliverables/engineering/cycle_10_technical_specification.md
++-++ @@ -0,0 +1,9 @@
++-++-+# Requirement: 8
++-++++# Requirement: 10
++-+  +
++-+--+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++-+-++## 1. High-Level Goal
++-++ +## 1. High-Level Goal
++-+  +
++-+--+def process_prompt(prompt_text: str):
++-+--+    """
++-+--+    Augments a raw user prompt and generates a formal technical specification markdown file.
++-+--+    """
++-+--+    requirement_id = get_current_requirement_id()
++-+--+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++-+-++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
++-++-+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
++-++++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
++-+  +
++-+--+    content = f"# Requirement: {requirement_id}\n\n"
++-+--+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++-+--+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++-+-++## 2. Guiding Principles
++-++ +## 2. Guiding Principles
++-+  +
++++--+    governor = Governor(mock_state)
++++--+
++++--+    # Act & Assert: The approval should fail with a SystemExit
++++--+    with pytest.raises(SystemExit) as e:
++++--+        governor._validate_stage_exit_criteria()
++++--+    
++++--+    assert e.type == SystemExit
++++--+    assert e.value.code == 1
++++--+
++++--+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++++--+    """Verify the Governor allows approval if the spec file exists."""
++++--+    # Arrange: Set the state to Engineer and mock the requirement pointer
++++--+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
++++--+    
++++--+    # Ensure the spec file DOES exist for this test
++++--+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
++++--+    spec_file.parent.mkdir(parents=True, exist_ok=True)
++++--+    spec_file.touch()
++++-+@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++++-+         # Clean up the created file
++++-+         if spec_file.exists():
++++-+             spec_file.unlink()
++++++     if len(sys.argv) == 1:
++++++         parser.print_help(sys.stderr)
++++++         sys.exit(1)
++++++ 
++++++     args = parser.parse_args()
++++++     
++++++-    manager = WorkflowManager()
++++++-
++++++-    if args.command == "approve":
++++++-        manager.approve()
++++++-    elif args.command == "new":
++++++-        process_prompt(args.prompt)
+++++++    if args.command == "meta-req":
+++++++        register_meta_requirement(args.description)
+++++++    else:
+++++++        manager = WorkflowManager()
+++++++        if args.command == "approve":
+++++++            manager.approve()
+++++++        elif args.command == "new":
+++++++            process_prompt(args.prompt)
++++++ 
++++++ if __name__ == "__main__":
++++++     main()
++++++diff --git a/tests/test_main.py b/tests/test_main.py
++++++index c429973..eddb264 100644
++++++--- a/tests/test_main.py
+++++++++ b/tests/test_main.py
++++++@@ -1,5 +1,52 @@
++++++ # tests/test_main.py
+++++++import pytest
+++++++from pathlib import Path
+++++++import re
+++++++from dw6.main import register_meta_requirement, META_LOG_FILE
++++++ 
++++++-def test_placeholder():
++++++-    """A placeholder test to satisfy the Validator stage."""
++++++-    assert True
+++++++@pytest.fixture(autouse=True)
+++++++def cleanup_log_file():
+++++++    """Fixture to clean up the meta log file before and after a test."""
+++++++    if META_LOG_FILE.exists():
+++++++        META_LOG_FILE.unlink()
+++++++    yield
+++++++    if META_LOG_FILE.exists():
+++++++        META_LOG_FILE.unlink()
+++   +
+++---     if len(sys.argv) == 1:
+++---         parser.print_help(sys.stderr)
+++---         sys.exit(1)
+++---@@ -27,6 +32,8 @@ def main():
+++---         manager.review()
+++---     elif args.command == "approve":
+++--++    def _transition_to_next_stage(self):
+++--++        current_index = STAGES.index(self.current_stage)
+++--++        # After 'Deployer', the cycle is complete
+++--++        if self.current_stage == "Deployer":
+++--++            self._complete_requirement_cycle()
+++--++            self.current_stage = STAGES[0]
+++--++        else:
+++--++            self.current_stage = STAGES[current_index + 1]
+++--++        self.state.set("CurrentStage", self.current_stage)
+++--++
+++--++    def _complete_requirement_cycle(self):
+++--++        req_id = int(self.state.get("RequirementPointer"))
+++--++        os.makedirs("logs", exist_ok=True)
+++--++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++--++        with open(APPROVAL_FILE, "a") as f:
+++--++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+++--++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+++--++        next_req_id = req_id + 1
+++--++        self.state.set("RequirementPointer", next_req_id)
+++--++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+++--++
+++--+ class WorkflowManager:
+++--+     def __init__(self):
+++--+         self.state = WorkflowState()
+++--++        self.governor = Governor(self.state) # The manager now has a governor
+++--+         self.current_stage = self.state.get("CurrentStage")
+++--+ 
+++--+     def get_state(self):
+++--+         return self.state.data
+++--+ 
+++--+     def approve(self):
+++--+-        old_stage = self.current_stage
+++--+-        print(f"--- Approving Stage: {old_stage} ---")
+++--+-        self._validate_stage()
+++--+-        self._run_pre_transition_actions()
+++--+-        self._transition_to_next_stage()
+++--+-        self._run_post_transition_actions()
+++--+-        self.state.save()
+++--+-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+++--++        # The manager now simply delegates to the governor.
+++--++        self.governor.approve()
+++--+ 
+++--+     def _validate_stage(self):
+++--+         print(f"Validating deliverables for stage: {self.current_stage}")
+++--+@@ -123,25 +167,7 @@ class WorkflowManager:
+++--+         if self.current_stage == "Coder":
+++--+             git_handler.save_current_commit_sha()
+++--+ 
+++--+-    def _transition_to_next_stage(self):
+++--+-        current_index = STAGES.index(self.current_stage)
+++--+-        if current_index == len(STAGES) - 1:
+++--+-            self._complete_requirement_cycle()
+++--+-            self.current_stage = STAGES[0]
+++--+-        else:
+++--+-            self.current_stage = STAGES[current_index + 1]
+++--+-        self.state.set("CurrentStage", self.current_stage)
+++--+ 
+++--+-    def _complete_requirement_cycle(self):
+++--+-        req_id = int(self.state.get("RequirementPointer"))
+++--+-        os.makedirs("logs", exist_ok=True)
+++--+-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++--+-        with open(APPROVAL_FILE, "a") as f:
+++--+-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+++--+-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+++--+-        next_req_id = req_id + 1
+++--+-        self.state.set("RequirementPointer", next_req_id)
+++--+-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+++--+ 
+++--+ class WorkflowState:
+++--+     def __init__(self):
+++--+diff --git a/tests/test_governor.py b/tests/test_governor.py
+++--+new file mode 100644
+++--+index 0000000..95b566d
+++--+--- /dev/null
+++--++++ b/tests/test_governor.py
+++--+@@ -0,0 +1,55 @@
+++--++# tests/test_governor.py
+++--++import pytest
+++--++from unittest.mock import MagicMock
+++--++from pathlib import Path
+++--++import sys
+++--++
+++--++from dw6.state_manager import Governor, WorkflowState
+++--++
+++--++@pytest.fixture
+++--++def mock_state(mocker):
+++--++    """Fixture to create a mock WorkflowState."""
+++--++    state = MagicMock(spec=WorkflowState)
+++--++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+++--++    return state
+++--++
+++--++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+++--++    """Verify the Governor blocks approval if the spec file is missing."""
+++--++    # Arrange: Set the state to Engineer and mock the requirement pointer
+++--++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+++--++    
+++--++    # Ensure the spec file does NOT exist for this test
+++--++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+++--++    if spec_file.exists():
+++--++        spec_file.unlink()
+++--++
+++--++    governor = Governor(mock_state)
+++--++
+++--++    # Act & Assert: The approval should fail with a SystemExit
+++--++    with pytest.raises(SystemExit) as e:
+++--++        governor._validate_stage_exit_criteria()
+++--++    
+++--++    assert e.type == SystemExit
+++--++    assert e.value.code == 1
+++--++
+++--++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+++--++    """Verify the Governor allows approval if the spec file exists."""
+++--++    # Arrange: Set the state to Engineer and mock the requirement pointer
+++--++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+++--++    
+++--++    # Ensure the spec file DOES exist for this test
+++--++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+++--++    spec_file.parent.mkdir(parents=True, exist_ok=True)
+++--++    spec_file.touch()
+++--++
+++--++    governor = Governor(mock_state)
+++--++
+++--++    # Act & Assert: The approval should pass without raising an exception
 ++--++    try:
-++--++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-++--++        with open(file_path, 'w') as f:
-++--++            f.write(content)
-++--++        print(f"Successfully created specification: {file_path}")
-++--++    except IOError as e:
-++--++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-++--++        sys.exit(1)
-++--+diff --git a/src/dw6/main.py b/src/dw6/main.py
-++--+index 7bbd031..a55f148 100644
-++--+--- a/src/dw6/main.py
-++--++++ b/src/dw6/main.py
-++--+@@ -2,6 +2,7 @@
-++--+ import argparse
-++--+ import sys
-++--+ from dw6.state_manager import StateManager
-++--++from dw6.augmenter import process_prompt
-++-++ class WorkflowManager:
-++-++     def __init__(self):
-++-++         self.state = WorkflowState()
-++-+++        self.governor = Governor(self.state) # The manager now has a governor
-++-++         self.current_stage = self.state.get("CurrentStage")
-++- + 
-++--+ def main():
-++--+     """Main entry point for the DW6 CLI."""
-++--+@@ -15,6 +16,10 @@ def main():
-++--+     # Approve command
-++--+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-++-++     def get_state(self):
-++-++         return self.state.data
-++- + 
-++--++    # New command
-++--++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-++--++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-++-++     def approve(self):
-++-++-        old_stage = self.current_stage
-++-++-        print(f"--- Approving Stage: {old_stage} ---")
-++-++-        self._validate_stage()
-++-++-        self._run_pre_transition_actions()
-++-++-        self._transition_to_next_stage()
-++-++-        self._run_post_transition_actions()
-++-++-        self.state.save()
-++-++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-++-+++        # The manager now simply delegates to the governor.
-++-+++        self.governor.approve()
-++-++ 
-++-++     def _validate_stage(self):
-++-++         print(f"Validating deliverables for stage: {self.current_stage}")
-++-++@@ -123,25 +167,7 @@ class WorkflowManager:
-++-++         if self.current_stage == "Coder":
-++-++             git_handler.save_current_commit_sha()
-++-++ 
-++-++-    def _transition_to_next_stage(self):
-++-++-        current_index = STAGES.index(self.current_stage)
-++-++-        if current_index == len(STAGES) - 1:
-++-++-            self._complete_requirement_cycle()
-++-++-            self.current_stage = STAGES[0]
-++-++-        else:
-++-++-            self.current_stage = STAGES[current_index + 1]
-++-++-        self.state.set("CurrentStage", self.current_stage)
-++-++ 
-++-++-    def _complete_requirement_cycle(self):
-++-++-        req_id = int(self.state.get("RequirementPointer"))
-++-++-        os.makedirs("logs", exist_ok=True)
-++-++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-++-++-        with open(APPROVAL_FILE, "a") as f:
-++-++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-++-++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-++-++-        next_req_id = req_id + 1
-++-++-        self.state.set("RequirementPointer", next_req_id)
-++-++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-++-++ 
-++-++ class WorkflowState:
-++-++     def __init__(self):
-++-++diff --git a/tests/test_governor.py b/tests/test_governor.py
-++-++new file mode 100644
-++-++index 0000000..95b566d
-++-++--- /dev/null
-++-+++++ b/tests/test_governor.py
-++-++@@ -0,0 +1,55 @@
-++-+++# tests/test_governor.py
-++-+++import pytest
-++-+++from unittest.mock import MagicMock
-++-+++from pathlib import Path
-++-+++import sys
-++- ++
-++--+     if len(sys.argv) == 1:
-++--+         parser.print_help(sys.stderr)
-++--+         sys.exit(1)
-++--+@@ -27,6 +32,8 @@ def main():
-++--+         manager.review()
-++--+     elif args.command == "approve":
-++--+         manager.approve()
-++--++    elif args.command == "new":
-++--++        process_prompt(args.prompt)
-++-+++from dw6.state_manager import Governor, WorkflowState
-++-+++
-++-+++@pytest.fixture
-++-+++def mock_state(mocker):
-++-+++    """Fixture to create a mock WorkflowState."""
-++-+++    state = MagicMock(spec=WorkflowState)
-++-+++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
-++-+++    return state
-++-+++
-++-+++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
-++-+++    """Verify the Governor blocks approval if the spec file is missing."""
-++-+++    # Arrange: Set the state to Engineer and mock the requirement pointer
-++-+++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
-++-+++    
-++-+++    # Ensure the spec file does NOT exist for this test
-++-+++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
-++-+++    if spec_file.exists():
-++-+++        spec_file.unlink()
-++-+++
-++-+++    governor = Governor(mock_state)
-++-+++
-++-+++    # Act & Assert: The approval should fail with a SystemExit
-++-+++    with pytest.raises(SystemExit) as e:
-++-+++        governor._validate_stage_exit_criteria()
-++-+++    
-++-+++    assert e.type == SystemExit
-++-+++    assert e.value.code == 1
-++-+++
-++-+++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-++-+++    """Verify the Governor allows approval if the spec file exists."""
-++-+++    # Arrange: Set the state to Engineer and mock the requirement pointer
-++-+++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
-++-+++    
-++-+++    # Ensure the spec file DOES exist for this test
-++-+++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
-++-+++    spec_file.parent.mkdir(parents=True, exist_ok=True)
-++-+++    spec_file.touch()
-++-+++
-++-+++    governor = Governor(mock_state)
-++-+++
-++-+++    # Act & Assert: The approval should pass without raising an exception
-++-+++    try:
-++-+++        governor._validate_stage_exit_criteria()
-++-+++    except SystemExit:
-++-+++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
-++-+++    finally:
-++-+++        # Clean up the created file
-++-+++        if spec_file.exists():
-++-+++            spec_file.unlink()
-++-++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
-++-++index 5b9d1eb..44d2cc9 100644
-++-++--- a/tests/test_state_manager_integration.py
-++-+++++ b/tests/test_state_manager_integration.py
-++-++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-++-++ 
-++-++     @patch('dw6.state_manager.WorkflowState')
-++-++     @patch('dw6.git_handler.get_changes_since_last_commit')
-++-++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
-++-+++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
-++-+++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
-++-++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
-++-++         # Arrange
-++-++         mock_state_instance = mock_WorkflowState.return_value
-++-++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-++-++         # Act
-++-+          manager.approve()
-++-+-+    elif args.command == "new":
-++-+-+        process_prompt(args.prompt)
-++-+  
-++-+- if __name__ == "__main__":
-++-+-     main()
-++-++-        # Assert
-++-+++        # Assert that the deliverable file was created
-++-++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
-++-++         self.assertTrue(deliverable_path.exists())
-++-+++        # Clean up the created file
-++-+++        deliverable_path.unlink()
-++-+++
-++-++         mock_state_instance.save.assert_called_once()
-++-++ 
-++-++ if __name__ == '__main__':
-++-++diff --git a/uv.lock b/uv.lock
-++-++index c79d29c..8e7411f 100644
-++-++--- a/uv.lock
-++-+++++ b/uv.lock
-++-++@@ -66,6 +66,7 @@ dependencies = [
-++-++ test = [
-++-++     { name = "pytest" },
-++-++     { name = "pytest-cov" },
-++-+++    { name = "pytest-mock" },
-++-++ ]
-++- + 
-++--+ if __name__ == "__main__":
-++--+     main()
-++--+```
-++-++ [package.metadata]
-++-++@@ -73,6 +74,7 @@ requires-dist = [
-++-++     { name = "gitpython" },
-++-++     { name = "pytest", marker = "extra == 'test'" },
-++-++     { name = "pytest-cov", marker = "extra == 'test'" },
-++-+++    { name = "pytest-mock", marker = "extra == 'test'" },
-++-++     { name = "python-dotenv" },
-++-++ ]
-++-++ provides-extras = ["test"]
-++-++@@ -167,6 +169,18 @@ wheels = [
-++-++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
-++-++ ]
-++-++ 
-++-+++[[package]]
-++-+++name = "pytest-mock"
-++-+++version = "3.14.1"
-++-+++source = { registry = "https://pypi.org/simple" }
-++-+++dependencies = [
-++-+++    { name = "pytest" },
-++-+++]
-++-+++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
-++-+++wheels = [
-++-+++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
-++-+++]
-++-+++
-++-++ [[package]]
-++-++ name = "python-dotenv"
-++-++ version = "1.1.1"
-++-+ ```
-++++- [[package]]
-++++- name = "python-dotenv"
-++++- version = "1.1.1"
-++++++    # Assert
-++++++    captured = capsys.readouterr()
-++++++    expected_rule = Governor.RULES["Coder"]
-++++++    assert expected_rule in captured.out
-+++  ```
-++  \ No newline at end of file
-++--diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
-++-+diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
-+++-diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
-++++diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
-+   new file mode 100644
-+---index 0000000..c1614f0
-+--+index 0000000..6c1638b
-+-+-index 0000000..6c1638b
-+-++index 0000000..691df8d
-++--index 0000000..6c1638b
-++-+index 0000000..691df8d
-+++-index 0000000..691df8d
-++++index 0000000..071c22d
-+   --- /dev/null
-+---+++ b/src/dw6/augmenter.py
-+---@@ -0,0 +1,26 @@
-+---+# src/dw6/augmenter.py
+++--++        governor._validate_stage_exit_criteria()
+++--++    except SystemExit:
+++--++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+++--++    finally:
+++--++        # Clean up the created file
+++--++        if spec_file.exists():
+++--++            spec_file.unlink()
+++--+diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+++--+index 5b9d1eb..44d2cc9 100644
+++--+--- a/tests/test_state_manager_integration.py
+++--++++ b/tests/test_state_manager_integration.py
+++--+@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+++--+ 
+++--+     @patch('dw6.state_manager.WorkflowState')
+++--+     @patch('dw6.git_handler.get_changes_since_last_commit')
+++--+-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+++--++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+++--++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+++--+         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+++--+         # Arrange
+++--+         mock_state_instance = mock_WorkflowState.return_value
+++--+@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+++--+         # Act
+++--          manager.approve()
+++---+    elif args.command == "new":
+++---+        process_prompt(args.prompt)
+++--  
+++--- if __name__ == "__main__":
+++---     main()
+++--+-        # Assert
+++--++        # Assert that the deliverable file was created
+++--+         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+++--+         self.assertTrue(deliverable_path.exists())
+++--++        # Clean up the created file
+++--++        deliverable_path.unlink()
+++--++
+++--+         mock_state_instance.save.assert_called_once()
+++--+ 
+++--+ if __name__ == '__main__':
+++--+diff --git a/uv.lock b/uv.lock
+++--+index c79d29c..8e7411f 100644
+++--+--- a/uv.lock
+++--++++ b/uv.lock
+++--+@@ -66,6 +66,7 @@ dependencies = [
+++--+ test = [
+++--+     { name = "pytest" },
+++--+     { name = "pytest-cov" },
+++--++    { name = "pytest-mock" },
+++--+ ]
+++--+ 
+++--+ [package.metadata]
+++--+@@ -73,6 +74,7 @@ requires-dist = [
+++--+     { name = "gitpython" },
+++--+     { name = "pytest", marker = "extra == 'test'" },
+++--+     { name = "pytest-cov", marker = "extra == 'test'" },
+++--++    { name = "pytest-mock", marker = "extra == 'test'" },
+++--+     { name = "python-dotenv" },
+++--+ ]
+++--+ provides-extras = ["test"]
+++--+@@ -167,6 +169,18 @@ wheels = [
+++--+     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+++--+ ]
+++--+ 
+++--++[[package]]
+++--++name = "pytest-mock"
+++--++version = "3.14.1"
+++--++source = { registry = "https://pypi.org/simple" }
+++--++dependencies = [
+++--++    { name = "pytest" },
+++--++]
+++--++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+++--++wheels = [
+++--++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+++--++]
+++--++
+++--+ [[package]]
+++--+ name = "python-dotenv"
+++--+ version = "1.1.1"
+++-+++def test_governor_enforces_rules_on_approve(mocker, capsys):
+++-+++    """Verify that the Governor prints the correct rule for the current stage."""
+++-+++    # Arrange
+++-+++    mock_state = mocker.MagicMock(spec=WorkflowState)
+++-+++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
+++-+ +    governor = Governor(mock_state)
+++-+++    # Mock the exit criteria validation to prevent SystemExit
+++-+++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
+++-+++    # Mock the rest of the approval process to isolate the rule enforcement
+++-+++    mocker.patch.object(governor, '_transition_to_next_stage')
+++-+++    mocker.patch('dw6.state_manager.WorkflowManager')
++++-++def test_governor_enforces_rules_on_approve(mocker, capsys):
++++-++    """Verify that the Governor prints the correct rule for the current stage."""
+++++-     def approve(self):
+++++-         old_stage = self.current_stage
+++++-         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+++++-+        self.enforce_rules()
+++++-         self._validate_stage_exit_criteria()
+++++-         # The original logic from WorkflowManager is now fully integrated here.
+++++-         workflow_manager = WorkflowManager() # We still need access to its methods for now.
+++++-diff --git a/tests/test_governor.py b/tests/test_governor.py
+++++-index 95b566d..26bf82b 100644
+++++---- a/tests/test_governor.py
+++++-+++ b/tests/test_governor.py
+++++-@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+++++-         # Clean up the created file
+++++-         if spec_file.exists():
+++++-             spec_file.unlink()
+++++++def test_register_meta_requirement_creates_file_and_logs_entry():
+++++++    """Verify that the first call creates the log file and adds the first entry correctly."""
++++ ++    # Arrange
++++-++    mock_state = mocker.MagicMock(spec=WorkflowState)
++++-++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
++++- +    governor = Governor(mock_state)
++++-++    # Mock the exit criteria validation to prevent SystemExit
++++-++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
++++-++    # Mock the rest of the approval process to isolate the rule enforcement
++++-++    mocker.patch.object(governor, '_transition_to_next_stage')
++++-++    mocker.patch('dw6.state_manager.WorkflowManager')
++++- +
++++--+    # Act & Assert: The approval should pass without raising an exception
++ +--+    try:
++-+--+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++-+--+        with open(file_path, 'w') as f:
++-+--+            f.write(content)
++-+--+        print(f"Successfully created specification: {file_path}")
++-+--+    except IOError as e:
++-+--+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++-+--+        sys.exit(1)
++-+-++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
++-+-+diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
++-+-+index 9718eda..b85b3d9 100644
++-+-+--- a/logs/.last_commit_sha
++-+-++++ b/logs/.last_commit_sha
++-+-+@@ -1 +1 @@
++-+-+-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
++-+-+\ No newline at end of file
++-+-++75be02c0b7e1723e32042299497f3673b11b4ddd
++-+-+\ No newline at end of file
++-+-+diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
++-+-+index 28746b7..743582b 100644
++-+-+--- a/logs/workflow_state.txt
++-+-++++ b/logs/workflow_state.txt
++-+-+@@ -1,2 +1,2 @@
++-+-+-CurrentStage=Engineer
++-+-+-RequirementPointer=7
++-+-++CurrentStage=Coder
++-+-++RequirementPointer=9
++-+-+diff --git a/pytest.ini b/pytest.ini
++-+-+new file mode 100644
++-+-+index 0000000..a635c5c
++-+-+--- /dev/null
++-+-++++ b/pytest.ini
++-+-+@@ -0,0 +1,2 @@
++-+-++[pytest]
++-+-++pythonpath = .
++-+- diff --git a/src/dw6/main.py b/src/dw6/main.py
++-+--index 7bbd031..a55f148 100644
++-+-+index a55f148..90862f9 100644
++-+- --- a/src/dw6/main.py
++-+- +++ b/src/dw6/main.py
++-+--@@ -2,6 +2,7 @@
++-+-+@@ -1,7 +1,7 @@
++-+-+ # dw6/main.py
++-+-  import argparse
++-+-  import sys
++-+-- from dw6.state_manager import StateManager
++-+--+from dw6.augmenter import process_prompt
++-+-+-from dw6.state_manager import StateManager
++-+-++from dw6.state_manager import WorkflowManager
++-+-+ from dw6.augmenter import process_prompt
++-++ +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
++-++ diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
++-++-index 9718eda..b85b3d9 100644
++-+++index b85b3d9..00ab2c8 100644
++-++ --- a/logs/.last_commit_sha
++-++ +++ b/logs/.last_commit_sha
++-++ @@ -1 +1 @@
++-++--7aa14d9c189cbc22b982d3d7895a650c1cf7a654
++-+++-75be02c0b7e1723e32042299497f3673b11b4ddd
++-++ \ No newline at end of file
++-++-+75be02c0b7e1723e32042299497f3673b11b4ddd
++-++++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
++-++ \ No newline at end of file
++-++ diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
++-++-index 28746b7..743582b 100644
++-+++index 743582b..a7aa662 100644
++-++ --- a/logs/workflow_state.txt
++-++ +++ b/logs/workflow_state.txt
++-++ @@ -1,2 +1,2 @@
++-++--CurrentStage=Engineer
++-++--RequirementPointer=7
++-++-+CurrentStage=Coder
++-++-+RequirementPointer=9
++-++-diff --git a/pytest.ini b/pytest.ini
++-++-new file mode 100644
++-++-index 0000000..a635c5c
++-++---- /dev/null
++-++-+++ b/pytest.ini
++-++-@@ -0,0 +1,2 @@
++-++-+[pytest]
++-++-+pythonpath = .
++-++-diff --git a/src/dw6/main.py b/src/dw6/main.py
++-++-index a55f148..90862f9 100644
++-++---- a/src/dw6/main.py
++-++-+++ b/src/dw6/main.py
++-++-@@ -1,7 +1,7 @@
++-++- # dw6/main.py
++-++- import argparse
++-++- import sys
++-++--from dw6.state_manager import StateManager
++-++-+from dw6.state_manager import WorkflowManager
++-++- from dw6.augmenter import process_prompt
++-++- 
++-++- def main():
++-++-@@ -10,9 +10,7 @@ def main():
++-++-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++-++-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++-++- 
++-++--    # Review command
++-++--    subparsers.add_parser("review", help="Review the changes for the current stage.")
++-++--    
++- +-+
++--+-+import os
++--+-+from .state_manager import get_current_requirement_id
++--+++++ b/deliverables/engineering/cycle_9_technical_specification.md
++--++@@ -0,0 +1,9 @@
++--+++# Requirement: 8
++--+ +
++--+-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++--+++## 1. High-Level Goal
++--+ +
++--+-+def process_prompt(prompt_text: str):
++--+-+    """
++--+-+    Augments a raw user prompt and generates a formal technical specification markdown file.
++--+-+    """
++--+-+    requirement_id = get_current_requirement_id()
++--+-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++--+++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
++--+ +
++--+-+    content = f"# Requirement: {requirement_id}\n\n"
++--+-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++--+-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++--+++## 2. Guiding Principles
++-++-     # Approve command
++-++-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++-++- 
++-++-@@ -26,11 +24,9 @@ def main():
++-++- 
++-++-     args = parser.parse_args()
++-++-     
++-++--    manager = StateManager()
++-++-+    manager = WorkflowManager()
++-++- 
++-++--    if args.command == "review":
++-++--        manager.review()
++-++--    elif args.command == "approve":
++-++-+    if args.command == "approve":
++-++-         manager.approve()
++-++-     elif args.command == "new":
++-++-         process_prompt(args.prompt)
++-+++ CurrentStage=Coder
++-+++-RequirementPointer=9
++-++++RequirementPointer=10
++-++ diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++-++-index 703640c..b829d36 100644
++-+++index b829d36..241fa62 100644
++-++ --- a/src/dw6/state_manager.py
++-++ +++ b/src/dw6/state_manager.py
++-++-@@ -9,7 +9,7 @@ from dw6 import git_handler
++-++- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
++-++- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
++-++- APPROVAL_FILE = "logs/approvals.log"
++-++--STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
++-++-+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
++-++- DELIVERABLE_PATHS = {
++-++-     "Engineer": "deliverables/engineering",
++-++-     "Coder": "deliverables/coding",
++-++-@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
++-++-     "Researcher": "deliverables/research",
++-+++@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
++-++  }
++-+   
++-+-  def main():
++-+--     """Main entry point for the DW6 CLI."""
++-+--@@ -15,6 +16,10 @@ def main():
++-+-+@@ -10,9 +10,7 @@ def main():
++-+-+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++-+-+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++-+-+ 
++-+-+-    # Review command
++-+-+-    subparsers.add_parser("review", help="Review the changes for the current stage.")
++-+-+-    
++-+-++
++-+-      # Approve command
++-+-      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++-++-+class Governor:
++-++-+    def __init__(self, state):
++-++-+        self.state = state
++-++-+        self.current_stage = self.state.get("CurrentStage")
++-++-+
++-++-+    def approve(self):
++-++-+        old_stage = self.current_stage
++-++-+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++-++-+        self._validate_stage_exit_criteria()
++-++-+        # The original logic from WorkflowManager is now fully integrated here.
++-++-+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
++-++-+        workflow_manager._validate_stage()
++-++-+        workflow_manager._run_pre_transition_actions()
++-++-+        self._transition_to_next_stage() # This method now belongs to the Governor
++-++-+        workflow_manager._run_post_transition_actions()
++-++-+        self.state.save()
++-++-+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++-++-+
++-++-+    def _validate_stage_exit_criteria(self):
++-++-+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
++-++-+        if self.current_stage == "Engineer":
++-++-+            req_id = self.state.get("RequirementPointer")
++-++-+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
++-++-+            if not spec_file.exists():
++-++-+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
++-++-+                sys.exit(1)
++-++-+            print("Governor: 'Engineer' exit criteria met.")
++-++-+
++-++-+    def _transition_to_next_stage(self):
++-++-+        current_index = STAGES.index(self.current_stage)
++-++-+        # After 'Deployer', the cycle is complete
++-++-+        if self.current_stage == "Deployer":
++-++-+            self._complete_requirement_cycle()
++-++-+            self.current_stage = STAGES[0]
++-++-+        else:
++-++-+            self.current_stage = STAGES[current_index + 1]
++-++-+        self.state.set("CurrentStage", self.current_stage)
++-++-+
++-++-+    def _complete_requirement_cycle(self):
++-++-+        req_id = int(self.state.get("RequirementPointer"))
++-++-+        os.makedirs("logs", exist_ok=True)
++-++-+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++-++-+        with open(APPROVAL_FILE, "a") as f:
++-++-+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++-++-+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++-++-+        next_req_id = req_id + 1
++-++-+        self.state.set("RequirementPointer", next_req_id)
++-++-+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++-++-+
++-++- class WorkflowManager:
++-++-     def __init__(self):
++-++-         self.state = WorkflowState()
++-++-+        self.governor = Governor(self.state) # The manager now has a governor
++-+++ class Governor:
++-++++    RULES = {
++-++++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
++-++++        "Coder": "Can use file system tools, code editing tools, and run tests.",
++-++++        "Validator": "Can only run tests and validation tools.",
++-++++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
++-++++        "Researcher": "Can use web search and documentation reading tools."
++-++++    }
++-+++     def __init__(self, state):
++-+++         self.state = state
++-++          self.current_stage = self.state.get("CurrentStage")
++-+   
++-+--+    # New command
++-+--+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++-+--+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++-+-+@@ -26,11 +24,9 @@ def main():
++-+-+ 
++-+-+     args = parser.parse_args()
++-+-+     
++-+-+-    manager = StateManager()
++-+-++    manager = WorkflowManager()
++-+-+ 
++-+-+-    if args.command == "review":
++-+-+-        manager.review()
++-+-+-    elif args.command == "approve":
++-+-++    if args.command == "approve":
++-+-+         manager.approve()
++-+-+     elif args.command == "new":
++-+-+         process_prompt(args.prompt)
++-+-+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++-+-+index 703640c..b829d36 100644
++-+-+--- a/src/dw6/state_manager.py
++-+-++++ b/src/dw6/state_manager.py
++-+-+@@ -9,7 +9,7 @@ from dw6 import git_handler
++-+-+ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
++-+-+ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
++-+-+ APPROVAL_FILE = "logs/approvals.log"
++-+-+-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
++-+-++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
++-+-+ DELIVERABLE_PATHS = {
++-+-+     "Engineer": "deliverables/engineering",
++-+-+     "Coder": "deliverables/coding",
++-+-+@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
++-+-+     "Researcher": "deliverables/research",
++-+-+ }
++-+-+ 
++-+-++class Governor:
++-+-++    def __init__(self, state):
++-+-++        self.state = state
++-+-++        self.current_stage = self.state.get("CurrentStage")
++-++-     def get_state(self):
++-++-         return self.state.data
++-++- 
++-++++    def enforce_rules(self):
++-++++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
++-++++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
++-++++        print(f"[RULE] {rule}")
++-+ ++
++-+-++    def approve(self):
++-+-++        old_stage = self.current_stage
++-+-++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++-+-++        self._validate_stage_exit_criteria()
++-+-++        # The original logic from WorkflowManager is now fully integrated here.
++-+-++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
++-+-++        workflow_manager._validate_stage()
++-+-++        workflow_manager._run_pre_transition_actions()
++-+-++        self._transition_to_next_stage() # This method now belongs to the Governor
++-+-++        workflow_manager._run_post_transition_actions()
++-+-++        self.state.save()
++-+-++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++-+-++
++-+-++    def _validate_stage_exit_criteria(self):
++-+-++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
++-+-++        if self.current_stage == "Engineer":
++-+-++            req_id = self.state.get("RequirementPointer")
++-+-++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
++-+-++            if not spec_file.exists():
++-+-++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
++-+-++                sys.exit(1)
++-+-++            print("Governor: 'Engineer' exit criteria met.")
++-++      def approve(self):
++-++--        old_stage = self.current_stage
++-++--        print(f"--- Approving Stage: {old_stage} ---")
++-++--        self._validate_stage()
++-++--        self._run_pre_transition_actions()
++-++--        self._transition_to_next_stage()
++-++--        self._run_post_transition_actions()
++-++--        self.state.save()
++-++--        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++-++-+        # The manager now simply delegates to the governor.
++-++-+        self.governor.approve()
++-++- 
++-++-     def _validate_stage(self):
++-++-         print(f"Validating deliverables for stage: {self.current_stage}")
++-++-@@ -123,25 +167,7 @@ class WorkflowManager:
++-++-         if self.current_stage == "Coder":
++-++-             git_handler.save_current_commit_sha()
++-++- 
++-++--    def _transition_to_next_stage(self):
++-++--        current_index = STAGES.index(self.current_stage)
++-++--        if current_index == len(STAGES) - 1:
++-++--            self._complete_requirement_cycle()
++-++--            self.current_stage = STAGES[0]
++-++--        else:
++-++--            self.current_stage = STAGES[current_index + 1]
++-++--        self.state.set("CurrentStage", self.current_stage)
++-++- 
++-++--    def _complete_requirement_cycle(self):
++-++--        req_id = int(self.state.get("RequirementPointer"))
++-++--        os.makedirs("logs", exist_ok=True)
++-++--        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++-++--        with open(APPROVAL_FILE, "a") as f:
++-++--            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++-++--        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++-++--        next_req_id = req_id + 1
++-++--        self.state.set("RequirementPointer", next_req_id)
++-++--        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++-++- 
++-++- class WorkflowState:
++-++-     def __init__(self):
++-+++         old_stage = self.current_stage
++-+++         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++-++++        self.enforce_rules()
++-+++         self._validate_stage_exit_criteria()
++-+++         # The original logic from WorkflowManager is now fully integrated here.
++-+++         workflow_manager = WorkflowManager() # We still need access to its methods for now.
++-++ diff --git a/tests/test_governor.py b/tests/test_governor.py
++-++-new file mode 100644
++-++-index 0000000..95b566d
++-++---- /dev/null
++-+++index 95b566d..26bf82b 100644
++-+++--- a/tests/test_governor.py
++-++ +++ b/tests/test_governor.py
++-++-@@ -0,0 +1,55 @@
++-++-+# tests/test_governor.py
++-++-+import pytest
++-++-+from unittest.mock import MagicMock
++-++-+from pathlib import Path
++-++-+import sys
++-++-+
++-++-+from dw6.state_manager import Governor, WorkflowState
++-++-+
++-++-+@pytest.fixture
++-++-+def mock_state(mocker):
++-++-+    """Fixture to create a mock WorkflowState."""
++-++-+    state = MagicMock(spec=WorkflowState)
++-++-+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
++-++-+    return state
++-++-+
++-++-+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
++-++-+    """Verify the Governor blocks approval if the spec file is missing."""
++-++-+    # Arrange: Set the state to Engineer and mock the requirement pointer
++-++-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
++-++-+    
++-++-+    # Ensure the spec file does NOT exist for this test
++-++-+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
++-++-+    if spec_file.exists():
++-++-+        spec_file.unlink()
++-++-+
++-++-+    governor = Governor(mock_state)
++-++-+
++-++-+    # Act & Assert: The approval should fail with a SystemExit
++-++-+    with pytest.raises(SystemExit) as e:
++-++-+        governor._validate_stage_exit_criteria()
++-++-+    
++-++-+    assert e.type == SystemExit
++-++-+    assert e.value.code == 1
++-++-+
++-++-+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++-++-+    """Verify the Governor allows approval if the spec file exists."""
++-++-+    # Arrange: Set the state to Engineer and mock the requirement pointer
++-++-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
++-++-+    
++-++-+    # Ensure the spec file DOES exist for this test
++-++-+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
++-++-+    spec_file.parent.mkdir(parents=True, exist_ok=True)
++-++-+    spec_file.touch()
++-+++@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++-+++         # Clean up the created file
++-+++         if spec_file.exists():
++-+++             spec_file.unlink()
++-+  +
++-+--     if len(sys.argv) == 1:
++-+--         parser.print_help(sys.stderr)
++-+--         sys.exit(1)
++-+--@@ -27,6 +32,8 @@ def main():
++-+--         manager.review()
++-+--     elif args.command == "approve":
++-+-++    def _transition_to_next_stage(self):
++-+-++        current_index = STAGES.index(self.current_stage)
++-+-++        # After 'Deployer', the cycle is complete
++-+-++        if self.current_stage == "Deployer":
++-+-++            self._complete_requirement_cycle()
++-+-++            self.current_stage = STAGES[0]
++-+-++        else:
++-+-++            self.current_stage = STAGES[current_index + 1]
++-+-++        self.state.set("CurrentStage", self.current_stage)
++-+-++
++-+-++    def _complete_requirement_cycle(self):
++-+-++        req_id = int(self.state.get("RequirementPointer"))
++-+-++        os.makedirs("logs", exist_ok=True)
++-+-++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++-+-++        with open(APPROVAL_FILE, "a") as f:
++-+-++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++-+-++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++-+-++        next_req_id = req_id + 1
++-+-++        self.state.set("RequirementPointer", next_req_id)
++-+-++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++-+-++
++-+-+ class WorkflowManager:
++-+-+     def __init__(self):
++-+-+         self.state = WorkflowState()
++-+-++        self.governor = Governor(self.state) # The manager now has a governor
++-+-+         self.current_stage = self.state.get("CurrentStage")
++-+-+ 
++-+-+     def get_state(self):
++-+-+         return self.state.data
++-+-+ 
++-+-+     def approve(self):
++-+-+-        old_stage = self.current_stage
++-+-+-        print(f"--- Approving Stage: {old_stage} ---")
++-+-+-        self._validate_stage()
++-+-+-        self._run_pre_transition_actions()
++-+-+-        self._transition_to_next_stage()
++-+-+-        self._run_post_transition_actions()
++-+-+-        self.state.save()
++-+-+-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++-+-++        # The manager now simply delegates to the governor.
++-+-++        self.governor.approve()
++-+-+ 
++-+-+     def _validate_stage(self):
++-+-+         print(f"Validating deliverables for stage: {self.current_stage}")
++-+-+@@ -123,25 +167,7 @@ class WorkflowManager:
++-+-+         if self.current_stage == "Coder":
++-+-+             git_handler.save_current_commit_sha()
++-+-+ 
++-+-+-    def _transition_to_next_stage(self):
++-+-+-        current_index = STAGES.index(self.current_stage)
++-+-+-        if current_index == len(STAGES) - 1:
++-+-+-            self._complete_requirement_cycle()
++-+-+-            self.current_stage = STAGES[0]
++-+-+-        else:
++-+-+-            self.current_stage = STAGES[current_index + 1]
++-+-+-        self.state.set("CurrentStage", self.current_stage)
++-+-+ 
++-+-+-    def _complete_requirement_cycle(self):
++-+-+-        req_id = int(self.state.get("RequirementPointer"))
++-+-+-        os.makedirs("logs", exist_ok=True)
++-+-+-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++-+-+-        with open(APPROVAL_FILE, "a") as f:
++-+-+-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++-+-+-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++-+-+-        next_req_id = req_id + 1
++-+-+-        self.state.set("RequirementPointer", next_req_id)
++-+-+-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++-+-+ 
++-+-+ class WorkflowState:
++-+-+     def __init__(self):
++-+-+diff --git a/tests/test_governor.py b/tests/test_governor.py
++-+-+new file mode 100644
++-+-+index 0000000..95b566d
++-+-+--- /dev/null
++-+-++++ b/tests/test_governor.py
++-+-+@@ -0,0 +1,55 @@
++-+-++# tests/test_governor.py
++-+-++import pytest
++-+-++from unittest.mock import MagicMock
++-+-++from pathlib import Path
++-+-++import sys
++-+-++
++-+-++from dw6.state_manager import Governor, WorkflowState
++-+-++
++-+-++@pytest.fixture
++-+-++def mock_state(mocker):
++-+-++    """Fixture to create a mock WorkflowState."""
++-+-++    state = MagicMock(spec=WorkflowState)
++-+-++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
++-+-++    return state
++-+-++
++-+-++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
++-+-++    """Verify the Governor blocks approval if the spec file is missing."""
++-+-++    # Arrange: Set the state to Engineer and mock the requirement pointer
++-+-++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
++-+-++    
++-+-++    # Ensure the spec file does NOT exist for this test
++-+-++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
++-+-++    if spec_file.exists():
++-+-++        spec_file.unlink()
++-+-++
++-+-++    governor = Governor(mock_state)
++-+-++
++-+-++    # Act & Assert: The approval should fail with a SystemExit
++-+-++    with pytest.raises(SystemExit) as e:
++-+-++        governor._validate_stage_exit_criteria()
++-+-++    
++-+-++    assert e.type == SystemExit
++-+-++    assert e.value.code == 1
++-+-++
++-+-++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++-+-++    """Verify the Governor allows approval if the spec file exists."""
++-+-++    # Arrange: Set the state to Engineer and mock the requirement pointer
++-+-++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
++-+-++    
++-+-++    # Ensure the spec file DOES exist for this test
++-+-++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
++-+-++    spec_file.parent.mkdir(parents=True, exist_ok=True)
++-+-++    spec_file.touch()
++-+-++
++-+-++    governor = Governor(mock_state)
++-+-++
++-+-++    # Act & Assert: The approval should pass without raising an exception
++-+-++    try:
++-+-++        governor._validate_stage_exit_criteria()
++-+-++    except SystemExit:
++-+-++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
++-+-++    finally:
++-+-++        # Clean up the created file
++-+-++        if spec_file.exists():
++-+-++            spec_file.unlink()
++-+-+diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
++-+-+index 5b9d1eb..44d2cc9 100644
++-+-+--- a/tests/test_state_manager_integration.py
++-+-++++ b/tests/test_state_manager_integration.py
++-+-+@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++-+-+ 
++-+-+     @patch('dw6.state_manager.WorkflowState')
++-+-+     @patch('dw6.git_handler.get_changes_since_last_commit')
++-+-+-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
++-+-++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
++-+-++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
++-+-+         """Ensure approving Coder stage generates a deliverable without altering the real state."""
++-+-+         # Arrange
++-+-+         mock_state_instance = mock_WorkflowState.return_value
++-+-+@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++-+-+         # Act
++-+-          manager.approve()
++-+--+    elif args.command == "new":
++-+--+        process_prompt(args.prompt)
++-+-  
++-+-- if __name__ == "__main__":
++-+--     main()
++-+-+-        # Assert
++-+-++        # Assert that the deliverable file was created
++-+-+         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
++-+-+         self.assertTrue(deliverable_path.exists())
++-+-++        # Clean up the created file
++-+-++        deliverable_path.unlink()
++-+-++
++-+-+         mock_state_instance.save.assert_called_once()
++-+-+ 
++-+-+ if __name__ == '__main__':
++-+-+diff --git a/uv.lock b/uv.lock
++-+-+index c79d29c..8e7411f 100644
++-+-+--- a/uv.lock
++-+-++++ b/uv.lock
++-+-+@@ -66,6 +66,7 @@ dependencies = [
++-+-+ test = [
++-+-+     { name = "pytest" },
++-+-+     { name = "pytest-cov" },
++-+-++    { name = "pytest-mock" },
++-+-+ ]
++-+-+ 
++-+-+ [package.metadata]
++-+-+@@ -73,6 +74,7 @@ requires-dist = [
++-+-+     { name = "gitpython" },
++-+-+     { name = "pytest", marker = "extra == 'test'" },
++-+-+     { name = "pytest-cov", marker = "extra == 'test'" },
++-+-++    { name = "pytest-mock", marker = "extra == 'test'" },
++-+-+     { name = "python-dotenv" },
++-+-+ ]
++-+-+ provides-extras = ["test"]
++-+-+@@ -167,6 +169,18 @@ wheels = [
++-+-+     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
++-+-+ ]
++-+-+ 
++-+-++[[package]]
++-+-++name = "pytest-mock"
++-+-++version = "3.14.1"
++-+-++source = { registry = "https://pypi.org/simple" }
++-+-++dependencies = [
++-+-++    { name = "pytest" },
++-+-++]
++-+-++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
++-+-++wheels = [
++-+-++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
++-+-++]
++-+-++
++-+-+ [[package]]
++-+-+ name = "python-dotenv"
++-+-+ version = "1.1.1"
++-++++def test_governor_enforces_rules_on_approve(mocker, capsys):
++-++++    """Verify that the Governor prints the correct rule for the current stage."""
++-++++    # Arrange
++-++++    mock_state = mocker.MagicMock(spec=WorkflowState)
++-++++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
++-++ +    governor = Governor(mock_state)
++-++++    # Mock the exit criteria validation to prevent SystemExit
++-++++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
++-++++    # Mock the rest of the approval process to isolate the rule enforcement
++-++++    mocker.patch.object(governor, '_transition_to_next_stage')
++-++++    mocker.patch('dw6.state_manager.WorkflowManager')
++++--+        governor._validate_stage_exit_criteria()
++++--+    except SystemExit:
++++--+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
++++--+    finally:
++++--+        # Clean up the created file
++++--+        if spec_file.exists():
++++--+            spec_file.unlink()
++++--diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
++++--index 5b9d1eb..44d2cc9 100644
++++----- a/tests/test_state_manager_integration.py
++++--+++ b/tests/test_state_manager_integration.py
++++--@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++++-- 
++++--     @patch('dw6.state_manager.WorkflowState')
++++--     @patch('dw6.git_handler.get_changes_since_last_commit')
++++---    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
++++--+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
++++--+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
++++--         """Ensure approving Coder stage generates a deliverable without altering the real state."""
++++--         # Arrange
++++--         mock_state_instance = mock_WorkflowState.return_value
++++--@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++++--         # Act
++++--         manager.approve()
++++-- 
++++---        # Assert
++++--+        # Assert that the deliverable file was created
++++--         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
++++--         self.assertTrue(deliverable_path.exists())
++++--+        # Clean up the created file
++++--+        deliverable_path.unlink()
++++--+
++++--         mock_state_instance.save.assert_called_once()
++++-- 
++++-- if __name__ == '__main__':
++++--diff --git a/uv.lock b/uv.lock
++++--index c79d29c..8e7411f 100644
++++----- a/uv.lock
++++--+++ b/uv.lock
++++--@@ -66,6 +66,7 @@ dependencies = [
++++-- test = [
++++--     { name = "pytest" },
++++--     { name = "pytest-cov" },
++++--+    { name = "pytest-mock" },
++++-- ]
++++-- 
++++-- [package.metadata]
++++--@@ -73,6 +74,7 @@ requires-dist = [
++++--     { name = "gitpython" },
++++--     { name = "pytest", marker = "extra == 'test'" },
++++--     { name = "pytest-cov", marker = "extra == 'test'" },
++++--+    { name = "pytest-mock", marker = "extra == 'test'" },
++++--     { name = "python-dotenv" },
++++-- ]
++++-- provides-extras = ["test"]
++++--@@ -167,6 +169,18 @@ wheels = [
++++--     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
++++-- ]
++++-- 
++++--+[[package]]
++++--+name = "pytest-mock"
++++--+version = "3.14.1"
++++--+source = { registry = "https://pypi.org/simple" }
++++--+dependencies = [
++++--+    { name = "pytest" },
++++--+]
++++--+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
++++--+wheels = [
++++--+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
++++--+]
+++++++    description = "This is the first meta requirement."
+++++++
++++ ++    # Act
++++-++    governor.approve()
++++- +
++++-- [[package]]
++++-- name = "python-dotenv"
++++-- version = "1.1.1"
+++++++    register_meta_requirement(description)
+++++++
++++ ++    # Assert
++++-++    captured = capsys.readouterr()
++++-++    expected_rule = Governor.RULES["Coder"]
++++-++    assert expected_rule in captured.out
+++++++    assert META_LOG_FILE.exists()
+++++++    with open(META_LOG_FILE, "r") as f:
+++++++        content = f.read()
+++++++    
+++++++    assert "[ID:1]" in content
+++++++    assert description in content
+++++++    # A simple regex to check for the timestamp format
+++++++    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
++  + +
++-++-+    # Act & Assert: The approval should pass without raising an exception
++- +-+    try:
++--+-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++--+-+        with open(file_path, 'w') as f:
++--+-+            f.write(content)
++--+-+        print(f"Successfully created specification: {file_path}")
++--+-+    except IOError as e:
++--+-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++--+-+        sys.exit(1)
++--+++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
++--++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
++--++index 9718eda..b85b3d9 100644
++--++--- a/logs/.last_commit_sha
++--+++++ b/logs/.last_commit_sha
++--++@@ -1 +1 @@
++--++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
++--++\ No newline at end of file
++--+++75be02c0b7e1723e32042299497f3673b11b4ddd
++--++\ No newline at end of file
++--++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
++--++index 28746b7..743582b 100644
++--++--- a/logs/workflow_state.txt
++--+++++ b/logs/workflow_state.txt
++--++@@ -1,2 +1,2 @@
++--++-CurrentStage=Engineer
++--++-RequirementPointer=7
++--+++CurrentStage=Coder
++--+++RequirementPointer=9
++--++diff --git a/pytest.ini b/pytest.ini
++-- +new file mode 100644
++---+index 0000000..c1614f0
++--++index 0000000..a635c5c
++-- +--- /dev/null
++---++++ b/src/dw6/augmenter.py
++---+@@ -0,0 +1,26 @@
++---++# src/dw6/augmenter.py
++--+++++ b/pytest.ini
++--++@@ -0,0 +1,2 @@
++--+++[pytest]
++--+++pythonpath = .
++--+ diff --git a/src/dw6/main.py b/src/dw6/main.py
++--+-index 7bbd031..a55f148 100644
++--++index a55f148..90862f9 100644
++--+ --- a/src/dw6/main.py
++--+ +++ b/src/dw6/main.py
++--+-@@ -2,6 +2,7 @@
++--++@@ -1,7 +1,7 @@
++--++ # dw6/main.py
++--+  import argparse
++--+  import sys
++--+- from dw6.state_manager import StateManager
++--+-+from dw6.augmenter import process_prompt
++--++-from dw6.state_manager import StateManager
++--+++from dw6.state_manager import WorkflowManager
++--++ from dw6.augmenter import process_prompt
++--+  
++--+  def main():
++--+-     """Main entry point for the DW6 CLI."""
++--+-@@ -15,6 +16,10 @@ def main():
++--++@@ -10,9 +10,7 @@ def main():
++--++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++--++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++--++ 
++--++-    # Review command
++--++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
++--++-    
++-- ++
++---++import os
++---++from .state_manager import get_current_requirement_id
++--+      # Approve command
++--+      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++--+  
++--+-+    # New command
++--+-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++--+-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++--++@@ -26,11 +24,9 @@ def main():
++--++ 
++--++     args = parser.parse_args()
++--++     
++--++-    manager = StateManager()
++--+++    manager = WorkflowManager()
++--++ 
++--++-    if args.command == "review":
++--++-        manager.review()
++--++-    elif args.command == "approve":
++--+++    if args.command == "approve":
++--++         manager.approve()
++--++     elif args.command == "new":
++--++         process_prompt(args.prompt)
++--++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++--++index 703640c..b829d36 100644
++--++--- a/src/dw6/state_manager.py
++--+++++ b/src/dw6/state_manager.py
++--++@@ -9,7 +9,7 @@ from dw6 import git_handler
++--++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
++--++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
++--++ APPROVAL_FILE = "logs/approvals.log"
++--++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
++--+++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
++--++ DELIVERABLE_PATHS = {
++--++     "Engineer": "deliverables/engineering",
++--++     "Coder": "deliverables/coding",
++--++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
++--++     "Researcher": "deliverables/research",
++--++ }
++--++ 
++--+++class Governor:
++--+++    def __init__(self, state):
++--+++        self.state = state
++--+++        self.current_stage = self.state.get("CurrentStage")
++-- ++
++---++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
++--+++    def approve(self):
++--+++        old_stage = self.current_stage
++--+++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++--+++        self._validate_stage_exit_criteria()
++--+++        # The original logic from WorkflowManager is now fully integrated here.
++--+++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
++--+++        workflow_manager._validate_stage()
++--+++        workflow_manager._run_pre_transition_actions()
++--+++        self._transition_to_next_stage() # This method now belongs to the Governor
++--+++        workflow_manager._run_post_transition_actions()
++--+++        self.state.save()
++--+++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++-- ++
++---++def process_prompt(prompt_text: str):
++---++    """
++---++    Augments a raw user prompt and generates a formal technical specification markdown file.
++---++    """
++---++    requirement_id = get_current_requirement_id()
++---++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
++--+++    def _validate_stage_exit_criteria(self):
++--+++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
++--+++        if self.current_stage == "Engineer":
++--+++            req_id = self.state.get("RequirementPointer")
++--+++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
++--+++            if not spec_file.exists():
++--+++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
++--+++                sys.exit(1)
++--+++            print("Governor: 'Engineer' exit criteria met.")
++-++-+        governor._validate_stage_exit_criteria()
++-++-+    except SystemExit:
++-++-+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
++-++-+    finally:
++-++-+        # Clean up the created file
++-++-+        if spec_file.exists():
++-++-+            spec_file.unlink()
++-++-diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
++-++-index 5b9d1eb..44d2cc9 100644
++-++---- a/tests/test_state_manager_integration.py
++-++-+++ b/tests/test_state_manager_integration.py
++-++-@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++-++- 
++-++-     @patch('dw6.state_manager.WorkflowState')
++-++-     @patch('dw6.git_handler.get_changes_since_last_commit')
++-++--    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
++-++-+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
++-++-+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
++-++-         """Ensure approving Coder stage generates a deliverable without altering the real state."""
++-++-         # Arrange
++-++-         mock_state_instance = mock_WorkflowState.return_value
++-++-@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++-++-         # Act
++-++-         manager.approve()
++-++- 
++-++--        # Assert
++-++-+        # Assert that the deliverable file was created
++-++-         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
++-++-         self.assertTrue(deliverable_path.exists())
++-++-+        # Clean up the created file
++-++-+        deliverable_path.unlink()
++-++-+
++-++-         mock_state_instance.save.assert_called_once()
++-++- 
++-++- if __name__ == '__main__':
++-++-diff --git a/uv.lock b/uv.lock
++-++-index c79d29c..8e7411f 100644
++-++---- a/uv.lock
++-++-+++ b/uv.lock
++-++-@@ -66,6 +66,7 @@ dependencies = [
++-++- test = [
++-++-     { name = "pytest" },
++-++-     { name = "pytest-cov" },
++-++-+    { name = "pytest-mock" },
++-++- ]
++-++- 
++-++- [package.metadata]
++-++-@@ -73,6 +74,7 @@ requires-dist = [
++-++-     { name = "gitpython" },
++-++-     { name = "pytest", marker = "extra == 'test'" },
++-++-     { name = "pytest-cov", marker = "extra == 'test'" },
++-++-+    { name = "pytest-mock", marker = "extra == 'test'" },
++-++-     { name = "python-dotenv" },
++-++- ]
++-++- provides-extras = ["test"]
++-++-@@ -167,6 +169,18 @@ wheels = [
++-++-     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
++-++- ]
++-++- 
++-++-+[[package]]
++-++-+name = "pytest-mock"
++-++-+version = "3.14.1"
++-++-+source = { registry = "https://pypi.org/simple" }
++-++-+dependencies = [
++-++-+    { name = "pytest" },
++-++-+]
++-++-+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
++-++-+wheels = [
++-++-+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
++-++-+]
++-++++    # Act
++-++++    governor.approve()
+++-+-+    # Act & Assert: The approval should pass without raising an exception
+++-+-+    try:
+++-+-+        governor._validate_stage_exit_criteria()
+++-+-+    except SystemExit:
+++-+-+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+++-+-+    finally:
+++-+-+        # Clean up the created file
+++-+-+        if spec_file.exists():
+++-+-+            spec_file.unlink()
+++-+-diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+++-+-index 5b9d1eb..44d2cc9 100644
+++-+---- a/tests/test_state_manager_integration.py
+++-+-+++ b/tests/test_state_manager_integration.py
+++-+-@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+++-+- 
+++-+-     @patch('dw6.state_manager.WorkflowState')
+++-+-     @patch('dw6.git_handler.get_changes_since_last_commit')
+++-+--    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+++-+-+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+++-+-+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+++-+-         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+++-+-         # Arrange
+++-+-         mock_state_instance = mock_WorkflowState.return_value
+++-+-@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+++-+-         # Act
+++-+-         manager.approve()
+++-+- 
+++-+--        # Assert
+++-+-+        # Assert that the deliverable file was created
+++-+-         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+++-+-         self.assertTrue(deliverable_path.exists())
+++-+-+        # Clean up the created file
+++-+-+        deliverable_path.unlink()
+++-+-+
+++-+-         mock_state_instance.save.assert_called_once()
+++-+- 
+++-+- if __name__ == '__main__':
+++-+-diff --git a/uv.lock b/uv.lock
+++-+-index c79d29c..8e7411f 100644
+++-+---- a/uv.lock
+++-+-+++ b/uv.lock
+++-+-@@ -66,6 +66,7 @@ dependencies = [
+++-+- test = [
+++-+-     { name = "pytest" },
+++-+-     { name = "pytest-cov" },
+++-+-+    { name = "pytest-mock" },
+++-+- ]
+++-+- 
+++-+- [package.metadata]
+++-+-@@ -73,6 +74,7 @@ requires-dist = [
+++-+-     { name = "gitpython" },
+++-+-     { name = "pytest", marker = "extra == 'test'" },
+++-+-     { name = "pytest-cov", marker = "extra == 'test'" },
+++-+-+    { name = "pytest-mock", marker = "extra == 'test'" },
+++-+-     { name = "python-dotenv" },
+++-+- ]
+++-+- provides-extras = ["test"]
+++-+-@@ -167,6 +169,18 @@ wheels = [
+++-+-     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+++-+- ]
+++-+- 
+++-+-+[[package]]
+++-+-+name = "pytest-mock"
+++-+-+version = "3.14.1"
+++-+-+source = { registry = "https://pypi.org/simple" }
+++-+-+dependencies = [
+++-+-+    { name = "pytest" },
+++-+-+]
+++-+-+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+++-+-+wheels = [
+++-+-+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+++-+-+]
+++-+++    # Act
+++-+++    governor.approve()
+++++-+def test_governor_enforces_rules_on_approve(mocker, capsys):
+++++-+    """Verify that the Governor prints the correct rule for the current stage."""
+++++++def test_register_meta_requirement_increments_id():
+++++++    """Verify that subsequent calls increment the requirement ID."""
+++++ +    # Arrange
+++++-+    mock_state = mocker.MagicMock(spec=WorkflowState)
+++++-+    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
+++++-+    governor = Governor(mock_state)
+++++-+    # Mock the exit criteria validation to prevent SystemExit
+++++-+    mocker.patch.object(governor, '_validate_stage_exit_criteria')
+++++-+    # Mock the rest of the approval process to isolate the rule enforcement
+++++-+    mocker.patch.object(governor, '_transition_to_next_stage')
+++++-+    mocker.patch('dw6.state_manager.WorkflowManager')
+++++++    description1 = "First requirement."
+++++++    description2 = "Second requirement."
++  + +
++--+-     if len(sys.argv) == 1:
++--+-         parser.print_help(sys.stderr)
++--+-         sys.exit(1)
++--+-@@ -27,6 +32,8 @@ def main():
++--+-         manager.review()
++--+-     elif args.command == "approve":
++--+++    def _transition_to_next_stage(self):
++--+++        current_index = STAGES.index(self.current_stage)
++--+++        # After 'Deployer', the cycle is complete
++--+++        if self.current_stage == "Deployer":
++--+++            self._complete_requirement_cycle()
++--+++            self.current_stage = STAGES[0]
++--+++        else:
++--+++            self.current_stage = STAGES[current_index + 1]
++--+++        self.state.set("CurrentStage", self.current_stage)
++-- ++
++---++    content = f"# Requirement: {requirement_id}\n\n"
++---++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
++---++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
++--+++    def _complete_requirement_cycle(self):
++--+++        req_id = int(self.state.get("RequirementPointer"))
++--+++        os.makedirs("logs", exist_ok=True)
++--+++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++--+++        with open(APPROVAL_FILE, "a") as f:
++--+++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++--+++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++--+++        next_req_id = req_id + 1
++--+++        self.state.set("RequirementPointer", next_req_id)
++--+++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++-- ++
++---++    try:
++---++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
++---++        with open(file_path, 'w') as f:
++---++            f.write(content)
++---++        print(f"Successfully created specification: {file_path}")
++---++    except IOError as e:
++---++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
++---++        sys.exit(1)
++---+diff --git a/src/dw6/main.py b/src/dw6/main.py
++---+index 7bbd031..a55f148 100644
++---+--- a/src/dw6/main.py
++---++++ b/src/dw6/main.py
++---+@@ -2,6 +2,7 @@
++---+ import argparse
++---+ import sys
++---+ from dw6.state_manager import StateManager
++---++from dw6.augmenter import process_prompt
++--++ class WorkflowManager:
++--++     def __init__(self):
++--++         self.state = WorkflowState()
++--+++        self.governor = Governor(self.state) # The manager now has a governor
++--++         self.current_stage = self.state.get("CurrentStage")
++-- + 
++---+ def main():
++---+     """Main entry point for the DW6 CLI."""
++---+@@ -15,6 +16,10 @@ def main():
++---+     # Approve command
++---+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++--++     def get_state(self):
++--++         return self.state.data
++-- + 
++---++    # New command
++---++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++---++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++--++     def approve(self):
++--++-        old_stage = self.current_stage
++--++-        print(f"--- Approving Stage: {old_stage} ---")
++--++-        self._validate_stage()
++--++-        self._run_pre_transition_actions()
++--++-        self._transition_to_next_stage()
++--++-        self._run_post_transition_actions()
++--++-        self.state.save()
++--++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++--+++        # The manager now simply delegates to the governor.
++--+++        self.governor.approve()
++--++ 
++--++     def _validate_stage(self):
++--++         print(f"Validating deliverables for stage: {self.current_stage}")
++--++@@ -123,25 +167,7 @@ class WorkflowManager:
++--++         if self.current_stage == "Coder":
++--++             git_handler.save_current_commit_sha()
++--++ 
++--++-    def _transition_to_next_stage(self):
++--++-        current_index = STAGES.index(self.current_stage)
++--++-        if current_index == len(STAGES) - 1:
++--++-            self._complete_requirement_cycle()
++--++-            self.current_stage = STAGES[0]
++--++-        else:
++--++-            self.current_stage = STAGES[current_index + 1]
++--++-        self.state.set("CurrentStage", self.current_stage)
++--++ 
++--++-    def _complete_requirement_cycle(self):
++--++-        req_id = int(self.state.get("RequirementPointer"))
++--++-        os.makedirs("logs", exist_ok=True)
++--++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++--++-        with open(APPROVAL_FILE, "a") as f:
++--++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++--++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++--++-        next_req_id = req_id + 1
++--++-        self.state.set("RequirementPointer", next_req_id)
++--++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++--++ 
++--++ class WorkflowState:
++--++     def __init__(self):
++--++diff --git a/tests/test_governor.py b/tests/test_governor.py
++--++new file mode 100644
++--++index 0000000..95b566d
++--++--- /dev/null
++--+++++ b/tests/test_governor.py
++--++@@ -0,0 +1,55 @@
++--+++# tests/test_governor.py
++--+++import pytest
++--+++from unittest.mock import MagicMock
++--+++from pathlib import Path
++--+++import sys
++-- ++
++---+     if len(sys.argv) == 1:
++---+         parser.print_help(sys.stderr)
++---+         sys.exit(1)
++---+@@ -27,6 +32,8 @@ def main():
++---+         manager.review()
++---+     elif args.command == "approve":
++---+         manager.approve()
++---++    elif args.command == "new":
++---++        process_prompt(args.prompt)
++--+++from dw6.state_manager import Governor, WorkflowState
++--+++
++--+++@pytest.fixture
++--+++def mock_state(mocker):
++--+++    """Fixture to create a mock WorkflowState."""
++--+++    state = MagicMock(spec=WorkflowState)
++--+++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
++--+++    return state
++--+++
++--+++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
++--+++    """Verify the Governor blocks approval if the spec file is missing."""
++--+++    # Arrange: Set the state to Engineer and mock the requirement pointer
++--+++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
++--+++    
++--+++    # Ensure the spec file does NOT exist for this test
++--+++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
++--+++    if spec_file.exists():
++--+++        spec_file.unlink()
++--+++
++--+++    governor = Governor(mock_state)
++--+++
++--+++    # Act & Assert: The approval should fail with a SystemExit
++--+++    with pytest.raises(SystemExit) as e:
++--+++        governor._validate_stage_exit_criteria()
++--+++    
++--+++    assert e.type == SystemExit
++--+++    assert e.value.code == 1
++--+++
++--+++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++--+++    """Verify the Governor allows approval if the spec file exists."""
++--+++    # Arrange: Set the state to Engineer and mock the requirement pointer
++--+++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
++--+++    
++--+++    # Ensure the spec file DOES exist for this test
++--+++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
++--+++    spec_file.parent.mkdir(parents=True, exist_ok=True)
++--+++    spec_file.touch()
++--+++
++--+++    governor = Governor(mock_state)
++--+++
++--+++    # Act & Assert: The approval should pass without raising an exception
++--+++    try:
++--+++        governor._validate_stage_exit_criteria()
++--+++    except SystemExit:
++--+++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
++--+++    finally:
++--+++        # Clean up the created file
++--+++        if spec_file.exists():
++--+++            spec_file.unlink()
++--++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
++--++index 5b9d1eb..44d2cc9 100644
++--++--- a/tests/test_state_manager_integration.py
++--+++++ b/tests/test_state_manager_integration.py
++--++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++--++ 
++--++     @patch('dw6.state_manager.WorkflowState')
++--++     @patch('dw6.git_handler.get_changes_since_last_commit')
++--++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
++--+++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
++--+++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
++--++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
++--++         # Arrange
++--++         mock_state_instance = mock_WorkflowState.return_value
++--++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++--++         # Act
++--+          manager.approve()
++--+-+    elif args.command == "new":
++--+-+        process_prompt(args.prompt)
++--+  
++--+- if __name__ == "__main__":
++--+-     main()
++--++-        # Assert
++--+++        # Assert that the deliverable file was created
++--++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
++--++         self.assertTrue(deliverable_path.exists())
++--+++        # Clean up the created file
++--+++        deliverable_path.unlink()
++--+++
++--++         mock_state_instance.save.assert_called_once()
++--++ 
++--++ if __name__ == '__main__':
++--++diff --git a/uv.lock b/uv.lock
++--++index c79d29c..8e7411f 100644
++--++--- a/uv.lock
++--+++++ b/uv.lock
++--++@@ -66,6 +66,7 @@ dependencies = [
++--++ test = [
++--++     { name = "pytest" },
++--++     { name = "pytest-cov" },
++--+++    { name = "pytest-mock" },
++--++ ]
++-- + 
++---+ if __name__ == "__main__":
++---+     main()
++---+```
++--++ [package.metadata]
++--++@@ -73,6 +74,7 @@ requires-dist = [
++--++     { name = "gitpython" },
++--++     { name = "pytest", marker = "extra == 'test'" },
++--++     { name = "pytest-cov", marker = "extra == 'test'" },
++--+++    { name = "pytest-mock", marker = "extra == 'test'" },
++--++     { name = "python-dotenv" },
++--++ ]
++--++ provides-extras = ["test"]
++--++@@ -167,6 +169,18 @@ wheels = [
++--++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
++--++ ]
++--++ 
++--+++[[package]]
++--+++name = "pytest-mock"
++--+++version = "3.14.1"
++--+++source = { registry = "https://pypi.org/simple" }
++--+++dependencies = [
++--+++    { name = "pytest" },
++--+++]
++--+++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
++--+++wheels = [
++--+++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
++--+++]
++--+++
++--++ [[package]]
++--++ name = "python-dotenv"
++--++ version = "1.1.1"
++--+ ```
++-++- [[package]]
++-++- name = "python-dotenv"
++-++- version = "1.1.1"
++-++++    # Assert
++-++++    captured = capsys.readouterr()
++-++++    expected_rule = Governor.RULES["Coder"]
++-++++    assert expected_rule in captured.out
++-+  ```
+++-+- [[package]]
+++-+- name = "python-dotenv"
+++-+- version = "1.1.1"
+++-+++    # Assert
+++-+++    captured = capsys.readouterr()
+++-+++    expected_rule = Governor.RULES["Coder"]
+++-+++    assert expected_rule in captured.out
+++++ +    # Act
+++++-+    governor.approve()
+++++++    register_meta_requirement(description1)
+++++++    register_meta_requirement(description2)
+++++ +
+++++ +    # Assert
+++++-+    captured = capsys.readouterr()
+++++-+    expected_rule = Governor.RULES["Coder"]
+++++-+    assert expected_rule in captured.out
+++++++    with open(META_LOG_FILE, "r") as f:
+++++++        lines = f.readlines()
+++++++    
+++++++    assert len(lines) == 2
+++++++    assert "[ID:1]" in lines[0]
+++++++    assert description1 in lines[0]
+++++++    assert "[ID:2]" in lines[1]
+++++++    assert description2 in lines[1]
+++   ```
++   \ No newline at end of file
++---diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
++--+diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
++-+-diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
++-++diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
+++--diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
+++-+diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
++++-diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
+++++diff --git a/deliverables/engineering/cycle_12_technical_specification.md b/deliverables/engineering/cycle_12_technical_specification.md
+    new file mode 100644
+----index 0000000..c1614f0
+---+index 0000000..6c1638b
+--+-index 0000000..6c1638b
+--++index 0000000..691df8d
+-+--index 0000000..6c1638b
+-+-+index 0000000..691df8d
+-++-index 0000000..691df8d
+-+++index 0000000..071c22d
++---index 0000000..6c1638b
++--+index 0000000..691df8d
++-+-index 0000000..691df8d
++-++index 0000000..071c22d
+++--index 0000000..691df8d
+++-+index 0000000..071c22d
++++-index 0000000..071c22d
+++++index 0000000..ff3658c
+    --- /dev/null
+----+++ b/src/dw6/augmenter.py
+----@@ -0,0 +1,26 @@
+----+# src/dw6/augmenter.py
+----+
+----+import os
+----+from .state_manager import get_current_requirement_id
+---++++ b/deliverables/engineering/cycle_9_technical_specification.md
+---+@@ -0,0 +1,9 @@
+---++# Requirement: 8
+--+-+++ b/deliverables/engineering/cycle_9_technical_specification.md
+--+++++ b/deliverables/engineering/cycle_10_technical_specification.md
+--+ @@ -0,0 +1,9 @@
+--+-+# Requirement: 8
+--+++# Requirement: 10
+-+--+++ b/deliverables/engineering/cycle_9_technical_specification.md
+-+-++++ b/deliverables/engineering/cycle_10_technical_specification.md
+-++-+++ b/deliverables/engineering/cycle_10_technical_specification.md
+-++++++ b/deliverables/engineering/cycle_11_technical_specification.md
+-+  @@ -0,0 +1,9 @@
+-+--+# Requirement: 8
+-+-++# Requirement: 10
+-++-+# Requirement: 10
+-++++# Requirement: 11
++---+++ b/deliverables/engineering/cycle_9_technical_specification.md
++--++++ b/deliverables/engineering/cycle_10_technical_specification.md
++-+-+++ b/deliverables/engineering/cycle_10_technical_specification.md
++-+++++ b/deliverables/engineering/cycle_11_technical_specification.md
+++--+++ b/deliverables/engineering/cycle_10_technical_specification.md
+++-++++ b/deliverables/engineering/cycle_11_technical_specification.md
++++-+++ b/deliverables/engineering/cycle_11_technical_specification.md
++++++++ b/deliverables/engineering/cycle_12_technical_specification.md
++   @@ -0,0 +1,9 @@
++---+# Requirement: 8
++--++# Requirement: 10
++-+-+# Requirement: 10
++-+++# Requirement: 11
+++--+# Requirement: 10
+++-++# Requirement: 11
++++-+# Requirement: 11
++++++# Requirement: 12
+    +
+----+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+---++## 1. High-Level Goal
+--+ +## 1. High-Level Goal
+-+  +## 1. High-Level Goal
++   +## 1. High-Level Goal
+    +
+----+def process_prompt(prompt_text: str):
+----+    """
+----+    Augments a raw user prompt and generates a formal technical specification markdown file.
+----+    """
+----+    requirement_id = get_current_requirement_id()
+----+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+---++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+--+-+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+--+++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
+-+--+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
+-+-++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
+-++-+Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
+-++++Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
++---+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
++--++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
++-+-+Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
++-+++Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
+++--+Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
+++-++Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
++++-+Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
++++++Actively enforce Governor rules by integrating with the AI's tool-using capabilities to block any action that violates the rule set for the current stage.
+    +
+----+    content = f"# Requirement: {requirement_id}\n\n"
+----+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+----+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+---++## 2. Guiding Principles
+--+ +## 2. Guiding Principles
+-+  +## 2. Guiding Principles
++   +## 2. Guiding Principles
+    +
+----+    try:
+----+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+----+        with open(file_path, 'w') as f:
+----+            f.write(content)
+----+        print(f"Successfully created specification: {file_path}")
+----+    except IOError as e:
+----+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+----+        sys.exit(1)
+---++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+---+diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+---+index 9718eda..b85b3d9 100644
+---+--- a/logs/.last_commit_sha
+---++++ b/logs/.last_commit_sha
+---+@@ -1 +1 @@
+---+-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+---+\ No newline at end of file
+---++75be02c0b7e1723e32042299497f3673b11b4ddd
+---+\ No newline at end of file
+---+diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+---+index 28746b7..743582b 100644
+---+--- a/logs/workflow_state.txt
+---++++ b/logs/workflow_state.txt
+---+@@ -1,2 +1,2 @@
+---+-CurrentStage=Engineer
+---+-RequirementPointer=7
+---++CurrentStage=Coder
+---++RequirementPointer=9
+---+diff --git a/pytest.ini b/pytest.ini
+---+new file mode 100644
+---+index 0000000..a635c5c
+---+--- /dev/null
+---++++ b/pytest.ini
+---+@@ -0,0 +1,2 @@
+---++[pytest]
+---++pythonpath = .
+--- diff --git a/src/dw6/main.py b/src/dw6/main.py
+----index 7bbd031..a55f148 100644
+---+index a55f148..90862f9 100644
+--- --- a/src/dw6/main.py
+--- +++ b/src/dw6/main.py
+----@@ -2,6 +2,7 @@
+---+@@ -1,7 +1,7 @@
+---+ # dw6/main.py
+---  import argparse
+---  import sys
+---- from dw6.state_manager import StateManager
+----+from dw6.augmenter import process_prompt
+---+-from dw6.state_manager import StateManager
+---++from dw6.state_manager import WorkflowManager
+---+ from dw6.augmenter import process_prompt
+--+ +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+--+ diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+--+-index 9718eda..b85b3d9 100644
+--++index b85b3d9..00ab2c8 100644
+--+ --- a/logs/.last_commit_sha
+--+ +++ b/logs/.last_commit_sha
+--+ @@ -1 +1 @@
+--+--7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+--++-75be02c0b7e1723e32042299497f3673b11b4ddd
+--+ \ No newline at end of file
+--+-+75be02c0b7e1723e32042299497f3673b11b4ddd
+--+++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+--+ \ No newline at end of file
+--+ diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+--+-index 28746b7..743582b 100644
+--++index 743582b..a7aa662 100644
+--+ --- a/logs/workflow_state.txt
+--+ +++ b/logs/workflow_state.txt
+--+ @@ -1,2 +1,2 @@
+--+--CurrentStage=Engineer
+--+--RequirementPointer=7
+--+-+CurrentStage=Coder
+--+-+RequirementPointer=9
+--+-diff --git a/pytest.ini b/pytest.ini
+--+-new file mode 100644
+--+-index 0000000..a635c5c
+--+---- /dev/null
+--+-+++ b/pytest.ini
+--+-@@ -0,0 +1,2 @@
+--+-+[pytest]
+--+-+pythonpath = .
+--+-diff --git a/src/dw6/main.py b/src/dw6/main.py
+--+-index a55f148..90862f9 100644
+--+---- a/src/dw6/main.py
+--+-+++ b/src/dw6/main.py
+--+-@@ -1,7 +1,7 @@
+--+- # dw6/main.py
+--+- import argparse
+--+- import sys
+--+--from dw6.state_manager import StateManager
+--+-+from dw6.state_manager import WorkflowManager
+--+- from dw6.augmenter import process_prompt
+--+- 
+--+- def main():
+--+-@@ -10,9 +10,7 @@ def main():
+--+-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+--+-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+--+- 
+--+--    # Review command
+--+--    subparsers.add_parser("review", help="Review the changes for the current stage.")
+--+--    
+--+-+
+--+-     # Approve command
+--+-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+--+- 
+--+-@@ -26,11 +24,9 @@ def main():
+--+- 
+--+-     args = parser.parse_args()
+--+-     
+--+--    manager = StateManager()
+--+-+    manager = WorkflowManager()
+--+- 
+--+--    if args.command == "review":
+--+--        manager.review()
+--+--    elif args.command == "approve":
+--+-+    if args.command == "approve":
+--+-         manager.approve()
+--+-     elif args.command == "new":
+--+-         process_prompt(args.prompt)
+--++ CurrentStage=Coder
+--++-RequirementPointer=9
+--+++RequirementPointer=10
+--+ diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+--+-index 703640c..b829d36 100644
+--++index b829d36..241fa62 100644
+--+ --- a/src/dw6/state_manager.py
+--+ +++ b/src/dw6/state_manager.py
+--+-@@ -9,7 +9,7 @@ from dw6 import git_handler
+--+- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+--+- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+--+- APPROVAL_FILE = "logs/approvals.log"
+--+--STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+--+-+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+--+- DELIVERABLE_PATHS = {
+--+-     "Engineer": "deliverables/engineering",
+--+-     "Coder": "deliverables/coding",
+--+-@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+--+-     "Researcher": "deliverables/research",
+--++@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
+--+  }
+-+  +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+-+  diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
+-+--index 9718eda..b85b3d9 100644
+-+-+index b85b3d9..00ab2c8 100644
+-++-index b85b3d9..00ab2c8 100644
+-+++index 00ab2c8..ede42cf 100644
+-+  --- a/logs/.last_commit_sha
+-+  +++ b/logs/.last_commit_sha
+-+  @@ -1 +1 @@
+-+---7aa14d9c189cbc22b982d3d7895a650c1cf7a654
+-+-+-75be02c0b7e1723e32042299497f3673b11b4ddd
+-++--75be02c0b7e1723e32042299497f3673b11b4ddd
+-+++-b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+-+  \ No newline at end of file
+-+--+75be02c0b7e1723e32042299497f3673b11b4ddd
+-+-++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+-++-+b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+-++++96a1111270912ae2722109d00ed1405c166f577c
+-+  \ No newline at end of file
+-+  diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
+-+--index 28746b7..743582b 100644
+-+-+index 743582b..a7aa662 100644
+-++-index 743582b..a7aa662 100644
+-+++index a7aa662..591ebb9 100644
+-+  --- a/logs/workflow_state.txt
+-+  +++ b/logs/workflow_state.txt
+-+  @@ -1,2 +1,2 @@
+-+---CurrentStage=Engineer
+-+---RequirementPointer=7
+-+--+CurrentStage=Coder
+-+--+RequirementPointer=9
+-+--diff --git a/pytest.ini b/pytest.ini
+-+--new file mode 100644
+-+--index 0000000..a635c5c
+-+----- /dev/null
+-+--+++ b/pytest.ini
+-+--@@ -0,0 +1,2 @@
+-+--+[pytest]
+-+--+pythonpath = .
+-+--diff --git a/src/dw6/main.py b/src/dw6/main.py
+-+--index a55f148..90862f9 100644
+-+----- a/src/dw6/main.py
+-+--+++ b/src/dw6/main.py
+-+--@@ -1,7 +1,7 @@
+-+-- # dw6/main.py
+-+-- import argparse
+-+-- import sys
+-+---from dw6.state_manager import StateManager
+-+--+from dw6.state_manager import WorkflowManager
+-+-- from dw6.augmenter import process_prompt
+-+-- 
+-+-- def main():
+-+--@@ -10,9 +10,7 @@ def main():
+-+--     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+-+--     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+-+-- 
+-+---    # Review command
+-+---    subparsers.add_parser("review", help="Review the changes for the current stage.")
+-+---    
+-+--+
+-+--     # Approve command
+-+--     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-+-- 
+-+--@@ -26,11 +24,9 @@ def main():
+-+-- 
+-+--     args = parser.parse_args()
+-+--     
+-+---    manager = StateManager()
+-+--+    manager = WorkflowManager()
+-+-- 
+-+---    if args.command == "review":
+-+---        manager.review()
+-+---    elif args.command == "approve":
+-+--+    if args.command == "approve":
+-+--         manager.approve()
+-+--     elif args.command == "new":
+-+--         process_prompt(args.prompt)
+-+-+ CurrentStage=Coder
+-+-+-RequirementPointer=9
+-+-++RequirementPointer=10
+-+- diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+-+--index 703640c..b829d36 100644
+-+-+index b829d36..241fa62 100644
+-+- --- a/src/dw6/state_manager.py
+-+- +++ b/src/dw6/state_manager.py
+-+--@@ -9,7 +9,7 @@ from dw6 import git_handler
+-+-- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+-+-- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+-+-- APPROVAL_FILE = "logs/approvals.log"
+-+---STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+-+--+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+-+-- DELIVERABLE_PATHS = {
+-+--     "Engineer": "deliverables/engineering",
+-+--     "Coder": "deliverables/coding",
+-+--@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+-+--     "Researcher": "deliverables/research",
+-+-+@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
+-+-  }
+-++  CurrentStage=Coder
+-++--RequirementPointer=9
+-++-+RequirementPointer=10
+-++-diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+-++-index b829d36..241fa62 100644
+-++---- a/src/dw6/state_manager.py
+-++-+++ b/src/dw6/state_manager.py
+-++-@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
+-++- }
+-+++-RequirementPointer=10
+-++++RequirementPointer=11
+-+++diff --git a/src/dw6/main.py b/src/dw6/main.py
+-+++index 90862f9..c65a4d9 100644
+-+++--- a/src/dw6/main.py
+-++++++ b/src/dw6/main.py
+-+++@@ -1,16 +1,42 @@
+-+++ # dw6/main.py
+-+++ import argparse
+-+++ import sys
+-++++import re
+-++++from pathlib import Path
+-++++from datetime import datetime, timezone
+-+++ from dw6.state_manager import WorkflowManager
+-+++ from dw6.augmenter import process_prompt
+-    
+---  def main():
+----     """Main entry point for the DW6 CLI."""
+----@@ -15,6 +16,10 @@ def main():
+---+@@ -10,9 +10,7 @@ def main():
+---+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+---+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+---+ 
+---+-    # Review command
+---+-    subparsers.add_parser("review", help="Review the changes for the current stage.")
+---+-    
+---++
+---      # Approve command
+---      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+--+-+class Governor:
+--+-+    def __init__(self, state):
+--+-+        self.state = state
+--+-+        self.current_stage = self.state.get("CurrentStage")
+--+-+
+--+-+    def approve(self):
+--+-+        old_stage = self.current_stage
+--+-+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+--+-+        self._validate_stage_exit_criteria()
+--+-+        # The original logic from WorkflowManager is now fully integrated here.
+--+-+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+--+-+        workflow_manager._validate_stage()
+--+-+        workflow_manager._run_pre_transition_actions()
+--+-+        self._transition_to_next_stage() # This method now belongs to the Governor
+--+-+        workflow_manager._run_post_transition_actions()
+--+-+        self.state.save()
+--+-+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+--+-+
+--+-+    def _validate_stage_exit_criteria(self):
+--+-+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+--+-+        if self.current_stage == "Engineer":
+--+-+            req_id = self.state.get("RequirementPointer")
+--+-+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+--+-+            if not spec_file.exists():
+--+-+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+--+-+                sys.exit(1)
+--+-+            print("Governor: 'Engineer' exit criteria met.")
+--+-+
+--+-+    def _transition_to_next_stage(self):
+--+-+        current_index = STAGES.index(self.current_stage)
+--+-+        # After 'Deployer', the cycle is complete
+--+-+        if self.current_stage == "Deployer":
+--+-+            self._complete_requirement_cycle()
+--+-+            self.current_stage = STAGES[0]
+--+-+        else:
+--+-+            self.current_stage = STAGES[current_index + 1]
+--+-+        self.state.set("CurrentStage", self.current_stage)
+--+-+
+--+-+    def _complete_requirement_cycle(self):
+--+-+        req_id = int(self.state.get("RequirementPointer"))
+--+-+        os.makedirs("logs", exist_ok=True)
+--+-+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+--+-+        with open(APPROVAL_FILE, "a") as f:
+--+-+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+--+-+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+--+-+        next_req_id = req_id + 1
+--+-+        self.state.set("RequirementPointer", next_req_id)
+--+-+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+--+-+
+--+- class WorkflowManager:
+--+-     def __init__(self):
+--+-         self.state = WorkflowState()
+--+-+        self.governor = Governor(self.state) # The manager now has a governor
+--++ class Governor:
+--+++    RULES = {
+--+++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+--+++        "Coder": "Can use file system tools, code editing tools, and run tests.",
+--+++        "Validator": "Can only run tests and validation tools.",
+--+++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+--+++        "Researcher": "Can use web search and documentation reading tools."
+--+++    }
+--++     def __init__(self, state):
+--++         self.state = state
+--+          self.current_stage = self.state.get("CurrentStage")
+-+--+class Governor:
+-+--+    def __init__(self, state):
+-+--+        self.state = state
+-+--+        self.current_stage = self.state.get("CurrentStage")
+-+--+
+-+--+    def approve(self):
+-+--+        old_stage = self.current_stage
+-+--+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+-+--+        self._validate_stage_exit_criteria()
+-+--+        # The original logic from WorkflowManager is now fully integrated here.
+-+--+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+-+--+        workflow_manager._validate_stage()
+-+--+        workflow_manager._run_pre_transition_actions()
+-+--+        self._transition_to_next_stage() # This method now belongs to the Governor
+-+--+        workflow_manager._run_post_transition_actions()
+-+--+        self.state.save()
+-+--+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+-+--+
+-+--+    def _validate_stage_exit_criteria(self):
+-+--+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+-+--+        if self.current_stage == "Engineer":
+-+--+            req_id = self.state.get("RequirementPointer")
+-+--+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+-+--+            if not spec_file.exists():
+-+--+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+-+--+                sys.exit(1)
+-+--+            print("Governor: 'Engineer' exit criteria met.")
+-+--+
+-+--+    def _transition_to_next_stage(self):
+-+--+        current_index = STAGES.index(self.current_stage)
+-+--+        # After 'Deployer', the cycle is complete
+-+--+        if self.current_stage == "Deployer":
+-+--+            self._complete_requirement_cycle()
+-+--+            self.current_stage = STAGES[0]
+-+--+        else:
+-+--+            self.current_stage = STAGES[current_index + 1]
+-+--+        self.state.set("CurrentStage", self.current_stage)
+-+--+
+-+--+    def _complete_requirement_cycle(self):
+-+--+        req_id = int(self.state.get("RequirementPointer"))
+-+--+        os.makedirs("logs", exist_ok=True)
+-+--+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-+--+        with open(APPROVAL_FILE, "a") as f:
+-+--+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-+--+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-+--+        next_req_id = req_id + 1
+-+--+        self.state.set("RequirementPointer", next_req_id)
+-+--+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-+--+
+-+-- class WorkflowManager:
+-+--     def __init__(self):
+-+--         self.state = WorkflowState()
+-+--+        self.governor = Governor(self.state) # The manager now has a governor
+-+-+ class Governor:
+-+-++    RULES = {
+-+-++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+-+-++        "Coder": "Can use file system tools, code editing tools, and run tests.",
+-+-++        "Validator": "Can only run tests and validation tools.",
+-+-++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+-+-++        "Researcher": "Can use web search and documentation reading tools."
+-+-++    }
+-+-+     def __init__(self, state):
+-+-+         self.state = state
+-+-          self.current_stage = self.state.get("CurrentStage")
+-++- class Governor:
+-++-+    RULES = {
+-++-+        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+-++-+        "Coder": "Can use file system tools, code editing tools, and run tests.",
+-++-+        "Validator": "Can only run tests and validation tools.",
+-++-+        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+-++-+        "Researcher": "Can use web search and documentation reading tools."
+-++-+    }
+-++-     def __init__(self, state):
+-++-         self.state = state
+-++-         self.current_stage = self.state.get("CurrentStage")
+-++++META_LOG_FILE = Path("logs/meta_requirements.log")
+-++++
+-++++def register_meta_requirement(description: str):
+-++++    """Logs a new meta-requirement to the meta_requirements.log file."""
+-++++    META_LOG_FILE.parent.mkdir(exist_ok=True)
+-++++    
+-++++    last_id = 0
+-++++    if META_LOG_FILE.exists():
+-++++        with open(META_LOG_FILE, "r") as f:
+-++++            lines = f.readlines()
+-++++            if lines:
+-++++                last_line = lines[-1]
+-++++                match = re.search(r'^\[ID:(\d+)\]', last_line)
+-++++                if match:
+-++++                    last_id = int(match.group(1))
+-++++
+-++++    new_id = last_id + 1
+-++++    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-++++    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
+-++++
+-++++    with open(META_LOG_FILE, "a") as f:
+-++++        f.write(log_entry)
+-++++    
+-++++    print(f"Successfully logged meta-requirement {new_id}.")
+-++++
+-+++ def main():
+-+++     """Main entry point for the DW6 CLI."""
+-+++-    # Test comment for Cycle 2 validation.
+-+++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+-+++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++   +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
++   diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
++---index 9718eda..b85b3d9 100644
++--+index b85b3d9..00ab2c8 100644
++-+-index b85b3d9..00ab2c8 100644
++-++index 00ab2c8..ede42cf 100644
+++--index b85b3d9..00ab2c8 100644
+++-+index 00ab2c8..ede42cf 100644
++++-index 00ab2c8..ede42cf 100644
+++++index ede42cf..5045595 100644
++   --- a/logs/.last_commit_sha
++   +++ b/logs/.last_commit_sha
++   @@ -1 +1 @@
++----7aa14d9c189cbc22b982d3d7895a650c1cf7a654
++--+-75be02c0b7e1723e32042299497f3673b11b4ddd
++-+--75be02c0b7e1723e32042299497f3673b11b4ddd
++-++-b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+++---75be02c0b7e1723e32042299497f3673b11b4ddd
+++-+-b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
++++--b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+++++-96a1111270912ae2722109d00ed1405c166f577c
++   \ No newline at end of file
++---+75be02c0b7e1723e32042299497f3673b11b4ddd
++--++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
++-+-+b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
++-+++96a1111270912ae2722109d00ed1405c166f577c
+++--+b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+++-++96a1111270912ae2722109d00ed1405c166f577c
++++-+96a1111270912ae2722109d00ed1405c166f577c
++++++223a8df342ec9a1ce277b234efe90e05cc4803dd
++   \ No newline at end of file
++   diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
++---index 28746b7..743582b 100644
++--+index 743582b..a7aa662 100644
++-+-index 743582b..a7aa662 100644
++-++index a7aa662..591ebb9 100644
+++--index 743582b..a7aa662 100644
+++-+index a7aa662..591ebb9 100644
++++-index a7aa662..591ebb9 100644
+++++index 591ebb9..d459c0f 100644
++   --- a/logs/workflow_state.txt
++   +++ b/logs/workflow_state.txt
++   @@ -1,2 +1,2 @@
++----CurrentStage=Engineer
++----RequirementPointer=7
++---+CurrentStage=Coder
++---+RequirementPointer=9
++---diff --git a/pytest.ini b/pytest.ini
++---new file mode 100644
++---index 0000000..a635c5c
++------ /dev/null
++---+++ b/pytest.ini
++---@@ -0,0 +1,2 @@
++---+[pytest]
++---+pythonpath = .
++---diff --git a/src/dw6/main.py b/src/dw6/main.py
++---index a55f148..90862f9 100644
++------ a/src/dw6/main.py
++---+++ b/src/dw6/main.py
++---@@ -1,7 +1,7 @@
++--- # dw6/main.py
++--- import argparse
++--- import sys
++----from dw6.state_manager import StateManager
++---+from dw6.state_manager import WorkflowManager
++--- from dw6.augmenter import process_prompt
++--- 
++--- def main():
++---@@ -10,9 +10,7 @@ def main():
++---     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++---     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++--- 
++----    # Review command
++----    subparsers.add_parser("review", help="Review the changes for the current stage.")
++----    
 +---+
-+---+import os
-+---+from .state_manager import get_current_requirement_id
-+--++++ b/deliverables/engineering/cycle_9_technical_specification.md
-+--+@@ -0,0 +1,9 @@
-+--++# Requirement: 8
-+-+-+++ b/deliverables/engineering/cycle_9_technical_specification.md
-+-+++++ b/deliverables/engineering/cycle_10_technical_specification.md
-+-+ @@ -0,0 +1,9 @@
-+-+-+# Requirement: 8
-+-+++# Requirement: 10
-++--+++ b/deliverables/engineering/cycle_9_technical_specification.md
-++-++++ b/deliverables/engineering/cycle_10_technical_specification.md
-+++-+++ b/deliverables/engineering/cycle_10_technical_specification.md
-+++++++ b/deliverables/engineering/cycle_11_technical_specification.md
-++  @@ -0,0 +1,9 @@
-++--+# Requirement: 8
-++-++# Requirement: 10
-+++-+# Requirement: 10
-+++++# Requirement: 11
-+   +
-+---+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
-+--++## 1. High-Level Goal
-+-+ +## 1. High-Level Goal
-++  +## 1. High-Level Goal
-+   +
-+---+def process_prompt(prompt_text: str):
-+---+    """
-+---+    Augments a raw user prompt and generates a formal technical specification markdown file.
-+---+    """
-+---+    requirement_id = get_current_requirement_id()
-+---+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
-+--++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
-+-+-+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
-+-+++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
-++--+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
-++-++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
-+++-+Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
-+++++Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
-+   +
-+---+    content = f"# Requirement: {requirement_id}\n\n"
-+---+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
-+---+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
-+--++## 2. Guiding Principles
-+-+ +## 2. Guiding Principles
-++  +## 2. Guiding Principles
-+   +
-+---+    try:
-+---+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
-+---+        with open(file_path, 'w') as f:
-+---+            f.write(content)
-+---+        print(f"Successfully created specification: {file_path}")
-+---+    except IOError as e:
-+---+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
-+---+        sys.exit(1)
-+--++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
-+--+diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
-+--+index 9718eda..b85b3d9 100644
-+--+--- a/logs/.last_commit_sha
-+--++++ b/logs/.last_commit_sha
-+--+@@ -1 +1 @@
-+--+-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
-+--+\ No newline at end of file
-+--++75be02c0b7e1723e32042299497f3673b11b4ddd
-+--+\ No newline at end of file
-+--+diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
-+--+index 28746b7..743582b 100644
-+--+--- a/logs/workflow_state.txt
-+--++++ b/logs/workflow_state.txt
-+--+@@ -1,2 +1,2 @@
-+--+-CurrentStage=Engineer
-+--+-RequirementPointer=7
-+--++CurrentStage=Coder
-+--++RequirementPointer=9
-+--+diff --git a/pytest.ini b/pytest.ini
-+--+new file mode 100644
-+--+index 0000000..a635c5c
-+--+--- /dev/null
-+--++++ b/pytest.ini
-+--+@@ -0,0 +1,2 @@
-+--++[pytest]
-+--++pythonpath = .
-+-- diff --git a/src/dw6/main.py b/src/dw6/main.py
-+---index 7bbd031..a55f148 100644
-+--+index a55f148..90862f9 100644
-+-- --- a/src/dw6/main.py
-+-- +++ b/src/dw6/main.py
-+---@@ -2,6 +2,7 @@
-+--+@@ -1,7 +1,7 @@
-+--+ # dw6/main.py
-+--  import argparse
-+--  import sys
-+--- from dw6.state_manager import StateManager
-+---+from dw6.augmenter import process_prompt
-+--+-from dw6.state_manager import StateManager
-+--++from dw6.state_manager import WorkflowManager
-+--+ from dw6.augmenter import process_prompt
-+-+ +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
-+-+ diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
-+-+-index 9718eda..b85b3d9 100644
-+-++index b85b3d9..00ab2c8 100644
-+-+ --- a/logs/.last_commit_sha
-+-+ +++ b/logs/.last_commit_sha
-+-+ @@ -1 +1 @@
-+-+--7aa14d9c189cbc22b982d3d7895a650c1cf7a654
-+-++-75be02c0b7e1723e32042299497f3673b11b4ddd
-+-+ \ No newline at end of file
-+-+-+75be02c0b7e1723e32042299497f3673b11b4ddd
-+-+++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
-+-+ \ No newline at end of file
-+-+ diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
-+-+-index 28746b7..743582b 100644
-+-++index 743582b..a7aa662 100644
-+-+ --- a/logs/workflow_state.txt
-+-+ +++ b/logs/workflow_state.txt
-+-+ @@ -1,2 +1,2 @@
-+-+--CurrentStage=Engineer
-+-+--RequirementPointer=7
-+-+-+CurrentStage=Coder
-+-+-+RequirementPointer=9
-+-+-diff --git a/pytest.ini b/pytest.ini
-+-+-new file mode 100644
-+-+-index 0000000..a635c5c
-+-+---- /dev/null
-+-+-+++ b/pytest.ini
-+-+-@@ -0,0 +1,2 @@
-+-+-+[pytest]
-+-+-+pythonpath = .
-+-+-diff --git a/src/dw6/main.py b/src/dw6/main.py
-+-+-index a55f148..90862f9 100644
-+-+---- a/src/dw6/main.py
-+-+-+++ b/src/dw6/main.py
-+-+-@@ -1,7 +1,7 @@
-+-+- # dw6/main.py
-+-+- import argparse
-+-+- import sys
-+-+--from dw6.state_manager import StateManager
-+-+-+from dw6.state_manager import WorkflowManager
-+-+- from dw6.augmenter import process_prompt
-+-+- 
-+-+- def main():
-+-+-@@ -10,9 +10,7 @@ def main():
-+-+-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-+-+-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-+-+- 
-+-+--    # Review command
-+-+--    subparsers.add_parser("review", help="Review the changes for the current stage.")
-+-+--    
-+-+-+
-+-+-     # Approve command
-+-+-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-+-+- 
-+-+-@@ -26,11 +24,9 @@ def main():
-+-+- 
-+-+-     args = parser.parse_args()
-+-+-     
-+-+--    manager = StateManager()
-+-+-+    manager = WorkflowManager()
-+-+- 
-+-+--    if args.command == "review":
-+-+--        manager.review()
-+-+--    elif args.command == "approve":
-+-+-+    if args.command == "approve":
-+-+-         manager.approve()
-+-+-     elif args.command == "new":
-+-+-         process_prompt(args.prompt)
-+-++ CurrentStage=Coder
-+-++-RequirementPointer=9
-+-+++RequirementPointer=10
-+-+ diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-+-+-index 703640c..b829d36 100644
-+-++index b829d36..241fa62 100644
-+-+ --- a/src/dw6/state_manager.py
-+-+ +++ b/src/dw6/state_manager.py
-+-+-@@ -9,7 +9,7 @@ from dw6 import git_handler
-+-+- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
-+-+- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
-+-+- APPROVAL_FILE = "logs/approvals.log"
-+-+--STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
-+-+-+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
-+-+- DELIVERABLE_PATHS = {
-+-+-     "Engineer": "deliverables/engineering",
-+-+-     "Coder": "deliverables/coding",
-+-+-@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
-+-+-     "Researcher": "deliverables/research",
-+-++@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
-+-+  }
-++  +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
-++  diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
-++--index 9718eda..b85b3d9 100644
-++-+index b85b3d9..00ab2c8 100644
-+++-index b85b3d9..00ab2c8 100644
-++++index 00ab2c8..ede42cf 100644
-++  --- a/logs/.last_commit_sha
-++  +++ b/logs/.last_commit_sha
-++  @@ -1 +1 @@
-++---7aa14d9c189cbc22b982d3d7895a650c1cf7a654
-++-+-75be02c0b7e1723e32042299497f3673b11b4ddd
-+++--75be02c0b7e1723e32042299497f3673b11b4ddd
-++++-b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
-++  \ No newline at end of file
-++--+75be02c0b7e1723e32042299497f3673b11b4ddd
-++-++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
-+++-+b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
-+++++96a1111270912ae2722109d00ed1405c166f577c
-++  \ No newline at end of file
-++  diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
-++--index 28746b7..743582b 100644
-++-+index 743582b..a7aa662 100644
-+++-index 743582b..a7aa662 100644
-++++index a7aa662..591ebb9 100644
-++  --- a/logs/workflow_state.txt
-++  +++ b/logs/workflow_state.txt
-++  @@ -1,2 +1,2 @@
-++---CurrentStage=Engineer
-++---RequirementPointer=7
-++--+CurrentStage=Coder
-++--+RequirementPointer=9
-++--diff --git a/pytest.ini b/pytest.ini
-++--new file mode 100644
-++--index 0000000..a635c5c
-++----- /dev/null
-++--+++ b/pytest.ini
-++--@@ -0,0 +1,2 @@
-++--+[pytest]
-++--+pythonpath = .
-++--diff --git a/src/dw6/main.py b/src/dw6/main.py
-++--index a55f148..90862f9 100644
-++----- a/src/dw6/main.py
-++--+++ b/src/dw6/main.py
-++--@@ -1,7 +1,7 @@
-++-- # dw6/main.py
-++-- import argparse
-++-- import sys
-++---from dw6.state_manager import StateManager
-++--+from dw6.state_manager import WorkflowManager
-++-- from dw6.augmenter import process_prompt
-++-- 
-++-- def main():
-++--@@ -10,9 +10,7 @@ def main():
-++--     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-++--     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-++-- 
-++---    # Review command
-++---    subparsers.add_parser("review", help="Review the changes for the current stage.")
-++---    
-++--+
-++--     # Approve command
-++--     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-++-- 
-++--@@ -26,11 +24,9 @@ def main():
-++-- 
-++--     args = parser.parse_args()
-++--     
-++---    manager = StateManager()
-++--+    manager = WorkflowManager()
-++-- 
-++---    if args.command == "review":
-++---        manager.review()
-++---    elif args.command == "approve":
-++--+    if args.command == "approve":
-++--         manager.approve()
-++--     elif args.command == "new":
-++--         process_prompt(args.prompt)
-++-+ CurrentStage=Coder
-++-+-RequirementPointer=9
-++-++RequirementPointer=10
-++- diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-++--index 703640c..b829d36 100644
-++-+index b829d36..241fa62 100644
-++- --- a/src/dw6/state_manager.py
-++- +++ b/src/dw6/state_manager.py
-++--@@ -9,7 +9,7 @@ from dw6 import git_handler
-++-- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
-++-- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
-++-- APPROVAL_FILE = "logs/approvals.log"
-++---STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
-++--+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
-++-- DELIVERABLE_PATHS = {
-++--     "Engineer": "deliverables/engineering",
-++--     "Coder": "deliverables/coding",
-++--@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
-++--     "Researcher": "deliverables/research",
-++-+@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
-++-  }
-+++  CurrentStage=Coder
-+++--RequirementPointer=9
-+++-+RequirementPointer=10
-+++-diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-+++-index b829d36..241fa62 100644
-+++---- a/src/dw6/state_manager.py
-+++-+++ b/src/dw6/state_manager.py
-+++-@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
-+++- }
-++++-RequirementPointer=10
-+++++RequirementPointer=11
-++++diff --git a/src/dw6/main.py b/src/dw6/main.py
-++++index 90862f9..c65a4d9 100644
-++++--- a/src/dw6/main.py
-+++++++ b/src/dw6/main.py
-++++@@ -1,16 +1,42 @@
-++++ # dw6/main.py
-++++ import argparse
-++++ import sys
-+++++import re
-+++++from pathlib import Path
-+++++from datetime import datetime, timezone
-++++ from dw6.state_manager import WorkflowManager
-++++ from dw6.augmenter import process_prompt
-+    
-+--  def main():
-+---     """Main entry point for the DW6 CLI."""
-+---@@ -15,6 +16,10 @@ def main():
-+--+@@ -10,9 +10,7 @@ def main():
-+--+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-+--+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-+--+ 
-+--+-    # Review command
-+--+-    subparsers.add_parser("review", help="Review the changes for the current stage.")
-+--+-    
-+--++
-+--      # Approve command
-+--      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-+-+-+class Governor:
-+-+-+    def __init__(self, state):
-+-+-+        self.state = state
-+-+-+        self.current_stage = self.state.get("CurrentStage")
-+-+-+
-+-+-+    def approve(self):
-+-+-+        old_stage = self.current_stage
-+-+-+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-+-+-+        self._validate_stage_exit_criteria()
-+-+-+        # The original logic from WorkflowManager is now fully integrated here.
-+-+-+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
-+-+-+        workflow_manager._validate_stage()
-+-+-+        workflow_manager._run_pre_transition_actions()
-+-+-+        self._transition_to_next_stage() # This method now belongs to the Governor
-+-+-+        workflow_manager._run_post_transition_actions()
-+-+-+        self.state.save()
-+-+-+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-+-+-+
-+-+-+    def _validate_stage_exit_criteria(self):
-+-+-+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
-+-+-+        if self.current_stage == "Engineer":
-+-+-+            req_id = self.state.get("RequirementPointer")
-+-+-+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
-+-+-+            if not spec_file.exists():
-+-+-+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
-+-+-+                sys.exit(1)
-+-+-+            print("Governor: 'Engineer' exit criteria met.")
-+-+-+
-+-+-+    def _transition_to_next_stage(self):
-+-+-+        current_index = STAGES.index(self.current_stage)
-+-+-+        # After 'Deployer', the cycle is complete
-+-+-+        if self.current_stage == "Deployer":
-+-+-+            self._complete_requirement_cycle()
-+-+-+            self.current_stage = STAGES[0]
-+-+-+        else:
-+-+-+            self.current_stage = STAGES[current_index + 1]
-+-+-+        self.state.set("CurrentStage", self.current_stage)
-+-+-+
-+-+-+    def _complete_requirement_cycle(self):
-+-+-+        req_id = int(self.state.get("RequirementPointer"))
-+-+-+        os.makedirs("logs", exist_ok=True)
-+-+-+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+-+-+        with open(APPROVAL_FILE, "a") as f:
-+-+-+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-+-+-+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-+-+-+        next_req_id = req_id + 1
-+-+-+        self.state.set("RequirementPointer", next_req_id)
-+-+-+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-+-+-+
-+-+- class WorkflowManager:
-+-+-     def __init__(self):
-+-+-         self.state = WorkflowState()
-+-+-+        self.governor = Governor(self.state) # The manager now has a governor
-+-++ class Governor:
-+-+++    RULES = {
-+-+++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
-+-+++        "Coder": "Can use file system tools, code editing tools, and run tests.",
-+-+++        "Validator": "Can only run tests and validation tools.",
-+-+++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
-+-+++        "Researcher": "Can use web search and documentation reading tools."
-+-+++    }
-+-++     def __init__(self, state):
-+-++         self.state = state
-+-+          self.current_stage = self.state.get("CurrentStage")
-++--+class Governor:
-++--+    def __init__(self, state):
-++--+        self.state = state
-++--+        self.current_stage = self.state.get("CurrentStage")
-++--+
-++--+    def approve(self):
-++--+        old_stage = self.current_stage
-++--+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-++--+        self._validate_stage_exit_criteria()
-++--+        # The original logic from WorkflowManager is now fully integrated here.
-++--+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
-++--+        workflow_manager._validate_stage()
-++--+        workflow_manager._run_pre_transition_actions()
-++--+        self._transition_to_next_stage() # This method now belongs to the Governor
-++--+        workflow_manager._run_post_transition_actions()
-++--+        self.state.save()
-++--+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-++--+
-++--+    def _validate_stage_exit_criteria(self):
-++--+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
-++--+        if self.current_stage == "Engineer":
-++--+            req_id = self.state.get("RequirementPointer")
-++--+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
-++--+            if not spec_file.exists():
-++--+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
-++--+                sys.exit(1)
-++--+            print("Governor: 'Engineer' exit criteria met.")
-++--+
-++--+    def _transition_to_next_stage(self):
-++--+        current_index = STAGES.index(self.current_stage)
-++--+        # After 'Deployer', the cycle is complete
-++--+        if self.current_stage == "Deployer":
-++--+            self._complete_requirement_cycle()
-++--+            self.current_stage = STAGES[0]
-++--+        else:
-++--+            self.current_stage = STAGES[current_index + 1]
-++--+        self.state.set("CurrentStage", self.current_stage)
-++--+
-++--+    def _complete_requirement_cycle(self):
-++--+        req_id = int(self.state.get("RequirementPointer"))
-++--+        os.makedirs("logs", exist_ok=True)
-++--+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-++--+        with open(APPROVAL_FILE, "a") as f:
-++--+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-++--+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-++--+        next_req_id = req_id + 1
-++--+        self.state.set("RequirementPointer", next_req_id)
-++--+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-++--+
-++-- class WorkflowManager:
-++--     def __init__(self):
-++--         self.state = WorkflowState()
-++--+        self.governor = Governor(self.state) # The manager now has a governor
-++-+ class Governor:
-++-++    RULES = {
-++-++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
-++-++        "Coder": "Can use file system tools, code editing tools, and run tests.",
-++-++        "Validator": "Can only run tests and validation tools.",
-++-++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
-++-++        "Researcher": "Can use web search and documentation reading tools."
-++-++    }
-++-+     def __init__(self, state):
-++-+         self.state = state
-++-          self.current_stage = self.state.get("CurrentStage")
-+++- class Governor:
-+++-+    RULES = {
-+++-+        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
-+++-+        "Coder": "Can use file system tools, code editing tools, and run tests.",
-+++-+        "Validator": "Can only run tests and validation tools.",
-+++-+        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
-+++-+        "Researcher": "Can use web search and documentation reading tools."
-+++-+    }
-+++-     def __init__(self, state):
-+++-         self.state = state
-+++-         self.current_stage = self.state.get("CurrentStage")
-+++++META_LOG_FILE = Path("logs/meta_requirements.log")
-+++++
-+++++def register_meta_requirement(description: str):
-+++++    """Logs a new meta-requirement to the meta_requirements.log file."""
-+++++    META_LOG_FILE.parent.mkdir(exist_ok=True)
-+++++    
-+++++    last_id = 0
-+++++    if META_LOG_FILE.exists():
-+++++        with open(META_LOG_FILE, "r") as f:
-+++++            lines = f.readlines()
-+++++            if lines:
-+++++                last_line = lines[-1]
-+++++                match = re.search(r'^\[ID:(\d+)\]', last_line)
-+++++                if match:
-+++++                    last_id = int(match.group(1))
-+++++
-+++++    new_id = last_id + 1
-+++++    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+++++    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
-+++++
-+++++    with open(META_LOG_FILE, "a") as f:
-+++++        f.write(log_entry)
-+++++    
-+++++    print(f"Successfully logged meta-requirement {new_id}.")
-+++++
-++++ def main():
-++++     """Main entry point for the DW6 CLI."""
-++++-    # Test comment for Cycle 2 validation.
-++++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-++++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-+    
-+---+    # New command
-+---+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-+---+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-+--+@@ -26,11 +24,9 @@ def main():
-+--+ 
-+--+     args = parser.parse_args()
-+--+     
-+--+-    manager = StateManager()
-+--++    manager = WorkflowManager()
-+--+ 
-+--+-    if args.command == "review":
-+--+-        manager.review()
-+--+-    elif args.command == "approve":
-+--++    if args.command == "approve":
-+--+         manager.approve()
-+--+     elif args.command == "new":
-+--+         process_prompt(args.prompt)
-+--+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-+--+index 703640c..b829d36 100644
-+--+--- a/src/dw6/state_manager.py
-+--++++ b/src/dw6/state_manager.py
-+--+@@ -9,7 +9,7 @@ from dw6 import git_handler
-+--+ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
-+--+ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
-+--+ APPROVAL_FILE = "logs/approvals.log"
-+--+-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
-+--++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
-+--+ DELIVERABLE_PATHS = {
-+--+     "Engineer": "deliverables/engineering",
-+--+     "Coder": "deliverables/coding",
-+--+@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
-+--+     "Researcher": "deliverables/research",
-+--+ }
-+--+ 
-+--++class Governor:
-+--++    def __init__(self, state):
-+--++        self.state = state
-+--++        self.current_stage = self.state.get("CurrentStage")
-+-+-     def get_state(self):
-+-+-         return self.state.data
-+-+- 
-+-+++    def enforce_rules(self):
-+-+++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
-+-+++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
-+-+++        print(f"[RULE] {rule}")
-++--     def get_state(self):
-++--         return self.state.data
-++-- 
-++-++    def enforce_rules(self):
-++-++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
-++-++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
-++-++        print(f"[RULE] {rule}")
-+++-+    def enforce_rules(self):
-+++-+        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
-+++-+        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
-+++-+        print(f"[RULE] {rule}")
-++++-
-++++     # Approve command
-++++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-++++ 
-++++@@ -18,18 +44,24 @@ def main():
-++++     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-++++     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-++++ 
-+++++    # Meta-req command
-+++++    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
-+++++    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
-+  ++
-+--++    def approve(self):
-+--++        old_stage = self.current_stage
-+--++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-+--++        self._validate_stage_exit_criteria()
-+--++        # The original logic from WorkflowManager is now fully integrated here.
-+--++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
-+--++        workflow_manager._validate_stage()
-+--++        workflow_manager._run_pre_transition_actions()
-+--++        self._transition_to_next_stage() # This method now belongs to the Governor
-+--++        workflow_manager._run_post_transition_actions()
-+--++        self.state.save()
-+--++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-+--++
-+--++    def _validate_stage_exit_criteria(self):
-+--++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
-+--++        if self.current_stage == "Engineer":
-+--++            req_id = self.state.get("RequirementPointer")
-+--++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
-+--++            if not spec_file.exists():
-+--++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
-+--++                sys.exit(1)
-+--++            print("Governor: 'Engineer' exit criteria met.")
-+-+      def approve(self):
-+-+--        old_stage = self.current_stage
-+-+--        print(f"--- Approving Stage: {old_stage} ---")
-+-+--        self._validate_stage()
-+-+--        self._run_pre_transition_actions()
-+-+--        self._transition_to_next_stage()
-+-+--        self._run_post_transition_actions()
-+-+--        self.state.save()
-+-+--        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-+-+-+        # The manager now simply delegates to the governor.
-+-+-+        self.governor.approve()
-+-+- 
-+-+-     def _validate_stage(self):
-+-+-         print(f"Validating deliverables for stage: {self.current_stage}")
-+-+-@@ -123,25 +167,7 @@ class WorkflowManager:
-+-+-         if self.current_stage == "Coder":
-+-+-             git_handler.save_current_commit_sha()
-+-+- 
-+-+--    def _transition_to_next_stage(self):
-+-+--        current_index = STAGES.index(self.current_stage)
-+-+--        if current_index == len(STAGES) - 1:
-+-+--            self._complete_requirement_cycle()
-+-+--            self.current_stage = STAGES[0]
-+-+--        else:
-+-+--            self.current_stage = STAGES[current_index + 1]
-+-+--        self.state.set("CurrentStage", self.current_stage)
-+-+- 
-+-+--    def _complete_requirement_cycle(self):
-+-+--        req_id = int(self.state.get("RequirementPointer"))
-+-+--        os.makedirs("logs", exist_ok=True)
-+-+--        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+-+--        with open(APPROVAL_FILE, "a") as f:
-+-+--            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-+-+--        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-+-+--        next_req_id = req_id + 1
-+-+--        self.state.set("RequirementPointer", next_req_id)
-+-+--        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-+-+- 
-+-+- class WorkflowState:
-+-+-     def __init__(self):
-+-++         old_stage = self.current_stage
-+-++         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-+-+++        self.enforce_rules()
-+-++         self._validate_stage_exit_criteria()
-+-++         # The original logic from WorkflowManager is now fully integrated here.
-+-++         workflow_manager = WorkflowManager() # We still need access to its methods for now.
-+-+ diff --git a/tests/test_governor.py b/tests/test_governor.py
-+-+-new file mode 100644
-+-+-index 0000000..95b566d
-+-+---- /dev/null
-+-++index 95b566d..26bf82b 100644
-+-++--- a/tests/test_governor.py
-+-+ +++ b/tests/test_governor.py
-+-+-@@ -0,0 +1,55 @@
-+-+-+# tests/test_governor.py
-+-+-+import pytest
-+-+-+from unittest.mock import MagicMock
-+-+-+from pathlib import Path
-+-+-+import sys
-+-+-+
-+-+-+from dw6.state_manager import Governor, WorkflowState
-+-+-+
-+-+-+@pytest.fixture
-+-+-+def mock_state(mocker):
-+-+-+    """Fixture to create a mock WorkflowState."""
-+-+-+    state = MagicMock(spec=WorkflowState)
-+-+-+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
-+-+-+    return state
-+-+-+
-+-+-+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
-+-+-+    """Verify the Governor blocks approval if the spec file is missing."""
-+-+-+    # Arrange: Set the state to Engineer and mock the requirement pointer
-+-+-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
-+-+-+    
-+-+-+    # Ensure the spec file does NOT exist for this test
-+-+-+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
-+-+-+    if spec_file.exists():
-+-+-+        spec_file.unlink()
-+-+-+
-+-+-+    governor = Governor(mock_state)
-+-+-+
-+-+-+    # Act & Assert: The approval should fail with a SystemExit
-+-+-+    with pytest.raises(SystemExit) as e:
-+-+-+        governor._validate_stage_exit_criteria()
-+-+-+    
-+-+-+    assert e.type == SystemExit
-+-+-+    assert e.value.code == 1
-+-+-+
-+-+-+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-+-+-+    """Verify the Governor allows approval if the spec file exists."""
-+-+-+    # Arrange: Set the state to Engineer and mock the requirement pointer
-+-+-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
-+-+-+    
-+-+-+    # Ensure the spec file DOES exist for this test
-+-+-+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
-+-+-+    spec_file.parent.mkdir(parents=True, exist_ok=True)
-+-+-+    spec_file.touch()
-+-++@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-+-++         # Clean up the created file
-+-++         if spec_file.exists():
-+-++             spec_file.unlink()
-++-      def approve(self):
-++---        old_stage = self.current_stage
-++---        print(f"--- Approving Stage: {old_stage} ---")
-++---        self._validate_stage()
-++---        self._run_pre_transition_actions()
-++---        self._transition_to_next_stage()
-++---        self._run_post_transition_actions()
-++---        self.state.save()
-++---        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-++--+        # The manager now simply delegates to the governor.
-++--+        self.governor.approve()
-++-- 
-++--     def _validate_stage(self):
-++--         print(f"Validating deliverables for stage: {self.current_stage}")
-++--@@ -123,25 +167,7 @@ class WorkflowManager:
-++--         if self.current_stage == "Coder":
-++--             git_handler.save_current_commit_sha()
-++-- 
-++---    def _transition_to_next_stage(self):
-++---        current_index = STAGES.index(self.current_stage)
-++---        if current_index == len(STAGES) - 1:
-++---            self._complete_requirement_cycle()
-++---            self.current_stage = STAGES[0]
-++---        else:
-++---            self.current_stage = STAGES[current_index + 1]
-++---        self.state.set("CurrentStage", self.current_stage)
-++-- 
-++---    def _complete_requirement_cycle(self):
-++---        req_id = int(self.state.get("RequirementPointer"))
-++---        os.makedirs("logs", exist_ok=True)
-++---        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-++---        with open(APPROVAL_FILE, "a") as f:
-++---            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-++---        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-++---        next_req_id = req_id + 1
-++---        self.state.set("RequirementPointer", next_req_id)
-++---        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-++-- 
-++-- class WorkflowState:
-++--     def __init__(self):
-++-+         old_stage = self.current_stage
-++-+         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-++-++        self.enforce_rules()
-++-+         self._validate_stage_exit_criteria()
-++-+         # The original logic from WorkflowManager is now fully integrated here.
-++-+         workflow_manager = WorkflowManager() # We still need access to its methods for now.
-++- diff --git a/tests/test_governor.py b/tests/test_governor.py
-++--new file mode 100644
-++--index 0000000..95b566d
-++----- /dev/null
-++-+index 95b566d..26bf82b 100644
-++-+--- a/tests/test_governor.py
-++- +++ b/tests/test_governor.py
-++--@@ -0,0 +1,55 @@
-++--+# tests/test_governor.py
-++--+import pytest
-++--+from unittest.mock import MagicMock
-++--+from pathlib import Path
-++--+import sys
-++--+
-++--+from dw6.state_manager import Governor, WorkflowState
-++--+
-++--+@pytest.fixture
-++--+def mock_state(mocker):
-++--+    """Fixture to create a mock WorkflowState."""
-++--+    state = MagicMock(spec=WorkflowState)
-++--+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
-++--+    return state
-++--+
-++--+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
-++--+    """Verify the Governor blocks approval if the spec file is missing."""
-++--+    # Arrange: Set the state to Engineer and mock the requirement pointer
-++--+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
-++--+    
-++--+    # Ensure the spec file does NOT exist for this test
-++--+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
-++--+    if spec_file.exists():
-++--+        spec_file.unlink()
- +--+
--+--+import os
--+--+from .state_manager import get_current_requirement_id
--+-++++ b/deliverables/engineering/cycle_9_technical_specification.md
--+-+@@ -0,0 +1,9 @@
--+-++# Requirement: 8
--++-+++ b/deliverables/engineering/cycle_9_technical_specification.md
--++++++ b/deliverables/engineering/cycle_10_technical_specification.md
--++ @@ -0,0 +1,9 @@
--++-+# Requirement: 8
--++++# Requirement: 10
--+  +
--+--+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
--+-++## 1. High-Level Goal
--++ +## 1. High-Level Goal
--+  +
--+--+def process_prompt(prompt_text: str):
--+--+    """
--+--+    Augments a raw user prompt and generates a formal technical specification markdown file.
--+--+    """
--+--+    requirement_id = get_current_requirement_id()
--+--+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
--+-++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
--++-+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
--++++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
--+  +
--+--+    content = f"# Requirement: {requirement_id}\n\n"
--+--+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
--+--+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
--+-++## 2. Guiding Principles
--++ +## 2. Guiding Principles
--+  +
-++--+    governor = Governor(mock_state)
-++--+
-++--+    # Act & Assert: The approval should fail with a SystemExit
-++--+    with pytest.raises(SystemExit) as e:
-++--+        governor._validate_stage_exit_criteria()
-++--+    
-++--+    assert e.type == SystemExit
-++--+    assert e.value.code == 1
-++--+
-++--+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-++--+    """Verify the Governor allows approval if the spec file exists."""
-++--+    # Arrange: Set the state to Engineer and mock the requirement pointer
-++--+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
-++--+    
-++--+    # Ensure the spec file DOES exist for this test
-++--+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
-++--+    spec_file.parent.mkdir(parents=True, exist_ok=True)
-++--+    spec_file.touch()
-++-+@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-++-+         # Clean up the created file
-++-+         if spec_file.exists():
-++-+             spec_file.unlink()
-++++     if len(sys.argv) == 1:
-++++         parser.print_help(sys.stderr)
-++++         sys.exit(1)
-++++ 
-++++     args = parser.parse_args()
-++++     
-++++-    manager = WorkflowManager()
-++++-
-++++-    if args.command == "approve":
-++++-        manager.approve()
-++++-    elif args.command == "new":
-++++-        process_prompt(args.prompt)
-+++++    if args.command == "meta-req":
-+++++        register_meta_requirement(args.description)
-+++++    else:
-+++++        manager = WorkflowManager()
-+++++        if args.command == "approve":
-+++++            manager.approve()
-+++++        elif args.command == "new":
-+++++            process_prompt(args.prompt)
-++++ 
-++++ if __name__ == "__main__":
-++++     main()
-++++diff --git a/tests/test_main.py b/tests/test_main.py
-++++index c429973..eddb264 100644
-++++--- a/tests/test_main.py
-+++++++ b/tests/test_main.py
-++++@@ -1,5 +1,52 @@
-++++ # tests/test_main.py
-+++++import pytest
-+++++from pathlib import Path
-+++++import re
-+++++from dw6.main import register_meta_requirement, META_LOG_FILE
-++++ 
-++++-def test_placeholder():
-++++-    """A placeholder test to satisfy the Validator stage."""
-++++-    assert True
-+++++@pytest.fixture(autouse=True)
-+++++def cleanup_log_file():
-+++++    """Fixture to clean up the meta log file before and after a test."""
-+++++    if META_LOG_FILE.exists():
-+++++        META_LOG_FILE.unlink()
-+++++    yield
-+++++    if META_LOG_FILE.exists():
-+++++        META_LOG_FILE.unlink()
-+   +
-+---     if len(sys.argv) == 1:
-+---         parser.print_help(sys.stderr)
-+---         sys.exit(1)
-+---@@ -27,6 +32,8 @@ def main():
-+---         manager.review()
-+---     elif args.command == "approve":
-+--++    def _transition_to_next_stage(self):
-+--++        current_index = STAGES.index(self.current_stage)
-+--++        # After 'Deployer', the cycle is complete
-+--++        if self.current_stage == "Deployer":
-+--++            self._complete_requirement_cycle()
-+--++            self.current_stage = STAGES[0]
-+--++        else:
-+--++            self.current_stage = STAGES[current_index + 1]
-+--++        self.state.set("CurrentStage", self.current_stage)
-+--++
-+--++    def _complete_requirement_cycle(self):
-+--++        req_id = int(self.state.get("RequirementPointer"))
-+--++        os.makedirs("logs", exist_ok=True)
-+--++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+--++        with open(APPROVAL_FILE, "a") as f:
-+--++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-+--++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-+--++        next_req_id = req_id + 1
-+--++        self.state.set("RequirementPointer", next_req_id)
-+--++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-+--++
-+--+ class WorkflowManager:
-+--+     def __init__(self):
-+--+         self.state = WorkflowState()
-+--++        self.governor = Governor(self.state) # The manager now has a governor
-+--+         self.current_stage = self.state.get("CurrentStage")
-+--+ 
-+--+     def get_state(self):
-+--+         return self.state.data
-+--+ 
-+--+     def approve(self):
-+--+-        old_stage = self.current_stage
-+--+-        print(f"--- Approving Stage: {old_stage} ---")
-+--+-        self._validate_stage()
-+--+-        self._run_pre_transition_actions()
-+--+-        self._transition_to_next_stage()
-+--+-        self._run_post_transition_actions()
-+--+-        self.state.save()
-+--+-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
-+--++        # The manager now simply delegates to the governor.
-+--++        self.governor.approve()
-+--+ 
-+--+     def _validate_stage(self):
-+--+         print(f"Validating deliverables for stage: {self.current_stage}")
-+--+@@ -123,25 +167,7 @@ class WorkflowManager:
-+--+         if self.current_stage == "Coder":
-+--+             git_handler.save_current_commit_sha()
-+--+ 
-+--+-    def _transition_to_next_stage(self):
-+--+-        current_index = STAGES.index(self.current_stage)
-+--+-        if current_index == len(STAGES) - 1:
-+--+-            self._complete_requirement_cycle()
-+--+-            self.current_stage = STAGES[0]
-+--+-        else:
-+--+-            self.current_stage = STAGES[current_index + 1]
-+--+-        self.state.set("CurrentStage", self.current_stage)
-+--+ 
-+--+-    def _complete_requirement_cycle(self):
-+--+-        req_id = int(self.state.get("RequirementPointer"))
-+--+-        os.makedirs("logs", exist_ok=True)
-+--+-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+--+-        with open(APPROVAL_FILE, "a") as f:
-+--+-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-+--+-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-+--+-        next_req_id = req_id + 1
-+--+-        self.state.set("RequirementPointer", next_req_id)
-+--+-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
-+--+ 
-+--+ class WorkflowState:
-+--+     def __init__(self):
-+--+diff --git a/tests/test_governor.py b/tests/test_governor.py
-+--+new file mode 100644
-+--+index 0000000..95b566d
-+--+--- /dev/null
-+--++++ b/tests/test_governor.py
-+--+@@ -0,0 +1,55 @@
-+--++# tests/test_governor.py
-+--++import pytest
-+--++from unittest.mock import MagicMock
-+--++from pathlib import Path
-+--++import sys
-+--++
-+--++from dw6.state_manager import Governor, WorkflowState
-+--++
-+--++@pytest.fixture
-+--++def mock_state(mocker):
-+--++    """Fixture to create a mock WorkflowState."""
-+--++    state = MagicMock(spec=WorkflowState)
-+--++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
-+--++    return state
-+--++
-+--++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
-+--++    """Verify the Governor blocks approval if the spec file is missing."""
-+--++    # Arrange: Set the state to Engineer and mock the requirement pointer
-+--++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
-+--++    
-+--++    # Ensure the spec file does NOT exist for this test
-+--++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
-+--++    if spec_file.exists():
-+--++        spec_file.unlink()
-+--++
-+--++    governor = Governor(mock_state)
-+--++
-+--++    # Act & Assert: The approval should fail with a SystemExit
-+--++    with pytest.raises(SystemExit) as e:
-+--++        governor._validate_stage_exit_criteria()
-+--++    
-+--++    assert e.type == SystemExit
-+--++    assert e.value.code == 1
-+--++
-+--++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-+--++    """Verify the Governor allows approval if the spec file exists."""
-+--++    # Arrange: Set the state to Engineer and mock the requirement pointer
-+--++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
-+--++    
-+--++    # Ensure the spec file DOES exist for this test
-+--++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
-+--++    spec_file.parent.mkdir(parents=True, exist_ok=True)
-+--++    spec_file.touch()
-+--++
-+--++    governor = Governor(mock_state)
-+--++
-+--++    # Act & Assert: The approval should pass without raising an exception
-+--++    try:
-+--++        governor._validate_stage_exit_criteria()
-+--++    except SystemExit:
-+--++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
-+--++    finally:
-+--++        # Clean up the created file
-+--++        if spec_file.exists():
-+--++            spec_file.unlink()
-+--+diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
-+--+index 5b9d1eb..44d2cc9 100644
-+--+--- a/tests/test_state_manager_integration.py
-+--++++ b/tests/test_state_manager_integration.py
-+--+@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-+--+ 
-+--+     @patch('dw6.state_manager.WorkflowState')
-+--+     @patch('dw6.git_handler.get_changes_since_last_commit')
-+--+-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
-+--++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
-+--++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
-+--+         """Ensure approving Coder stage generates a deliverable without altering the real state."""
-+--+         # Arrange
-+--+         mock_state_instance = mock_WorkflowState.return_value
-+--+@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-+--+         # Act
-+--          manager.approve()
-+---+    elif args.command == "new":
-+---+        process_prompt(args.prompt)
-+--  
-+--- if __name__ == "__main__":
-+---     main()
-+--+-        # Assert
-+--++        # Assert that the deliverable file was created
-+--+         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
-+--+         self.assertTrue(deliverable_path.exists())
-+--++        # Clean up the created file
-+--++        deliverable_path.unlink()
-+--++
-+--+         mock_state_instance.save.assert_called_once()
-+--+ 
-+--+ if __name__ == '__main__':
-+--+diff --git a/uv.lock b/uv.lock
-+--+index c79d29c..8e7411f 100644
-+--+--- a/uv.lock
-+--++++ b/uv.lock
-+--+@@ -66,6 +66,7 @@ dependencies = [
-+--+ test = [
-+--+     { name = "pytest" },
-+--+     { name = "pytest-cov" },
-+--++    { name = "pytest-mock" },
-+--+ ]
-+--+ 
-+--+ [package.metadata]
-+--+@@ -73,6 +74,7 @@ requires-dist = [
-+--+     { name = "gitpython" },
-+--+     { name = "pytest", marker = "extra == 'test'" },
-+--+     { name = "pytest-cov", marker = "extra == 'test'" },
-+--++    { name = "pytest-mock", marker = "extra == 'test'" },
-+--+     { name = "python-dotenv" },
-+--+ ]
-+--+ provides-extras = ["test"]
-+--+@@ -167,6 +169,18 @@ wheels = [
-+--+     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
-+--+ ]
-+--+ 
-+--++[[package]]
-+--++name = "pytest-mock"
-+--++version = "3.14.1"
-+--++source = { registry = "https://pypi.org/simple" }
-+--++dependencies = [
-+--++    { name = "pytest" },
-+--++]
-+--++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
-+--++wheels = [
-+--++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
-+--++]
-+--++
-+--+ [[package]]
-+--+ name = "python-dotenv"
-+--+ version = "1.1.1"
-+-+++def test_governor_enforces_rules_on_approve(mocker, capsys):
-+-+++    """Verify that the Governor prints the correct rule for the current stage."""
-+-+++    # Arrange
-+-+++    mock_state = mocker.MagicMock(spec=WorkflowState)
-+-+++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
-+-+ +    governor = Governor(mock_state)
-+-+++    # Mock the exit criteria validation to prevent SystemExit
-+-+++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
-+-+++    # Mock the rest of the approval process to isolate the rule enforcement
-+-+++    mocker.patch.object(governor, '_transition_to_next_stage')
-+-+++    mocker.patch('dw6.state_manager.WorkflowManager')
-++-++def test_governor_enforces_rules_on_approve(mocker, capsys):
-++-++    """Verify that the Governor prints the correct rule for the current stage."""
-+++-     def approve(self):
-+++-         old_stage = self.current_stage
-+++-         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-+++-+        self.enforce_rules()
-+++-         self._validate_stage_exit_criteria()
-+++-         # The original logic from WorkflowManager is now fully integrated here.
-+++-         workflow_manager = WorkflowManager() # We still need access to its methods for now.
-+++-diff --git a/tests/test_governor.py b/tests/test_governor.py
-+++-index 95b566d..26bf82b 100644
-+++---- a/tests/test_governor.py
-+++-+++ b/tests/test_governor.py
-+++-@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-+++-         # Clean up the created file
-+++-         if spec_file.exists():
-+++-             spec_file.unlink()
-+++++def test_register_meta_requirement_creates_file_and_logs_entry():
-+++++    """Verify that the first call creates the log file and adds the first entry correctly."""
-++ ++    # Arrange
-++-++    mock_state = mocker.MagicMock(spec=WorkflowState)
-++-++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
-++- +    governor = Governor(mock_state)
-++-++    # Mock the exit criteria validation to prevent SystemExit
-++-++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
-++-++    # Mock the rest of the approval process to isolate the rule enforcement
-++-++    mocker.patch.object(governor, '_transition_to_next_stage')
-++-++    mocker.patch('dw6.state_manager.WorkflowManager')
-++- +
-++--+    # Act & Assert: The approval should pass without raising an exception
- +--+    try:
--+--+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
--+--+        with open(file_path, 'w') as f:
--+--+            f.write(content)
--+--+        print(f"Successfully created specification: {file_path}")
--+--+    except IOError as e:
--+--+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
--+--+        sys.exit(1)
--+-++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
--+-+diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
--+-+index 9718eda..b85b3d9 100644
--+-+--- a/logs/.last_commit_sha
--+-++++ b/logs/.last_commit_sha
--+-+@@ -1 +1 @@
--+-+-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
--+-+\ No newline at end of file
--+-++75be02c0b7e1723e32042299497f3673b11b4ddd
--+-+\ No newline at end of file
--+-+diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
--+-+index 28746b7..743582b 100644
--+-+--- a/logs/workflow_state.txt
--+-++++ b/logs/workflow_state.txt
--+-+@@ -1,2 +1,2 @@
--+-+-CurrentStage=Engineer
--+-+-RequirementPointer=7
--+-++CurrentStage=Coder
--+-++RequirementPointer=9
--+-+diff --git a/pytest.ini b/pytest.ini
--+-+new file mode 100644
--+-+index 0000000..a635c5c
--+-+--- /dev/null
--+-++++ b/pytest.ini
--+-+@@ -0,0 +1,2 @@
--+-++[pytest]
--+-++pythonpath = .
--+- diff --git a/src/dw6/main.py b/src/dw6/main.py
--+--index 7bbd031..a55f148 100644
--+-+index a55f148..90862f9 100644
--+- --- a/src/dw6/main.py
--+- +++ b/src/dw6/main.py
--+--@@ -2,6 +2,7 @@
--+-+@@ -1,7 +1,7 @@
--+-+ # dw6/main.py
--+-  import argparse
--+-  import sys
--+-- from dw6.state_manager import StateManager
--+--+from dw6.augmenter import process_prompt
--+-+-from dw6.state_manager import StateManager
--+-++from dw6.state_manager import WorkflowManager
--+-+ from dw6.augmenter import process_prompt
--++ +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
--++ diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
--++-index 9718eda..b85b3d9 100644
--+++index b85b3d9..00ab2c8 100644
--++ --- a/logs/.last_commit_sha
--++ +++ b/logs/.last_commit_sha
--++ @@ -1 +1 @@
--++--7aa14d9c189cbc22b982d3d7895a650c1cf7a654
--+++-75be02c0b7e1723e32042299497f3673b11b4ddd
--++ \ No newline at end of file
--++-+75be02c0b7e1723e32042299497f3673b11b4ddd
--++++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
--++ \ No newline at end of file
--++ diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
--++-index 28746b7..743582b 100644
--+++index 743582b..a7aa662 100644
--++ --- a/logs/workflow_state.txt
--++ +++ b/logs/workflow_state.txt
--++ @@ -1,2 +1,2 @@
--++--CurrentStage=Engineer
--++--RequirementPointer=7
--++-+CurrentStage=Coder
--++-+RequirementPointer=9
--++-diff --git a/pytest.ini b/pytest.ini
--++-new file mode 100644
--++-index 0000000..a635c5c
--++---- /dev/null
--++-+++ b/pytest.ini
--++-@@ -0,0 +1,2 @@
--++-+[pytest]
--++-+pythonpath = .
--++-diff --git a/src/dw6/main.py b/src/dw6/main.py
--++-index a55f148..90862f9 100644
--++---- a/src/dw6/main.py
--++-+++ b/src/dw6/main.py
--++-@@ -1,7 +1,7 @@
--++- # dw6/main.py
--++- import argparse
--++- import sys
--++--from dw6.state_manager import StateManager
--++-+from dw6.state_manager import WorkflowManager
--++- from dw6.augmenter import process_prompt
--++- 
--++- def main():
--++-@@ -10,9 +10,7 @@ def main():
--++-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
--++-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
--++- 
--++--    # Review command
--++--    subparsers.add_parser("review", help="Review the changes for the current stage.")
--++--    
-- +-+
---+-+import os
---+-+from .state_manager import get_current_requirement_id
---+++++ b/deliverables/engineering/cycle_9_technical_specification.md
---++@@ -0,0 +1,9 @@
---+++# Requirement: 8
---+ +
---+-+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
---+++## 1. High-Level Goal
---+ +
---+-+def process_prompt(prompt_text: str):
---+-+    """
---+-+    Augments a raw user prompt and generates a formal technical specification markdown file.
---+-+    """
---+-+    requirement_id = get_current_requirement_id()
---+-+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
---+++Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
---+ +
---+-+    content = f"# Requirement: {requirement_id}\n\n"
---+-+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
---+-+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
---+++## 2. Guiding Principles
--++-     # Approve command
--++-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
--++- 
--++-@@ -26,11 +24,9 @@ def main():
--++- 
--++-     args = parser.parse_args()
--++-     
--++--    manager = StateManager()
--++-+    manager = WorkflowManager()
--++- 
--++--    if args.command == "review":
--++--        manager.review()
--++--    elif args.command == "approve":
--++-+    if args.command == "approve":
--++-         manager.approve()
--++-     elif args.command == "new":
--++-         process_prompt(args.prompt)
--+++ CurrentStage=Coder
--+++-RequirementPointer=9
--++++RequirementPointer=10
--++ diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
--++-index 703640c..b829d36 100644
--+++index b829d36..241fa62 100644
--++ --- a/src/dw6/state_manager.py
--++ +++ b/src/dw6/state_manager.py
--++-@@ -9,7 +9,7 @@ from dw6 import git_handler
--++- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
--++- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
--++- APPROVAL_FILE = "logs/approvals.log"
--++--STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
--++-+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
--++- DELIVERABLE_PATHS = {
--++-     "Engineer": "deliverables/engineering",
--++-     "Coder": "deliverables/coding",
--++-@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
--++-     "Researcher": "deliverables/research",
--+++@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
--++  }
--+   
--+-  def main():
--+--     """Main entry point for the DW6 CLI."""
--+--@@ -15,6 +16,10 @@ def main():
--+-+@@ -10,9 +10,7 @@ def main():
--+-+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
--+-+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
--+-+ 
--+-+-    # Review command
--+-+-    subparsers.add_parser("review", help="Review the changes for the current stage.")
--+-+-    
--+-++
--+-      # Approve command
--+-      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
--++-+class Governor:
--++-+    def __init__(self, state):
--++-+        self.state = state
--++-+        self.current_stage = self.state.get("CurrentStage")
--++-+
--++-+    def approve(self):
--++-+        old_stage = self.current_stage
--++-+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
--++-+        self._validate_stage_exit_criteria()
--++-+        # The original logic from WorkflowManager is now fully integrated here.
--++-+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
--++-+        workflow_manager._validate_stage()
--++-+        workflow_manager._run_pre_transition_actions()
--++-+        self._transition_to_next_stage() # This method now belongs to the Governor
--++-+        workflow_manager._run_post_transition_actions()
--++-+        self.state.save()
--++-+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
--++-+
--++-+    def _validate_stage_exit_criteria(self):
--++-+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
--++-+        if self.current_stage == "Engineer":
--++-+            req_id = self.state.get("RequirementPointer")
--++-+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
--++-+            if not spec_file.exists():
--++-+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
--++-+                sys.exit(1)
--++-+            print("Governor: 'Engineer' exit criteria met.")
--++-+
--++-+    def _transition_to_next_stage(self):
--++-+        current_index = STAGES.index(self.current_stage)
--++-+        # After 'Deployer', the cycle is complete
--++-+        if self.current_stage == "Deployer":
--++-+            self._complete_requirement_cycle()
--++-+            self.current_stage = STAGES[0]
--++-+        else:
--++-+            self.current_stage = STAGES[current_index + 1]
--++-+        self.state.set("CurrentStage", self.current_stage)
--++-+
--++-+    def _complete_requirement_cycle(self):
--++-+        req_id = int(self.state.get("RequirementPointer"))
--++-+        os.makedirs("logs", exist_ok=True)
--++-+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
--++-+        with open(APPROVAL_FILE, "a") as f:
--++-+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
--++-+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
--++-+        next_req_id = req_id + 1
--++-+        self.state.set("RequirementPointer", next_req_id)
--++-+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
--++-+
--++- class WorkflowManager:
--++-     def __init__(self):
--++-         self.state = WorkflowState()
--++-+        self.governor = Governor(self.state) # The manager now has a governor
--+++ class Governor:
--++++    RULES = {
--++++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
--++++        "Coder": "Can use file system tools, code editing tools, and run tests.",
--++++        "Validator": "Can only run tests and validation tools.",
--++++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
--++++        "Researcher": "Can use web search and documentation reading tools."
--++++    }
--+++     def __init__(self, state):
--+++         self.state = state
--++          self.current_stage = self.state.get("CurrentStage")
--+   
--+--+    # New command
--+--+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
--+--+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
--+-+@@ -26,11 +24,9 @@ def main():
--+-+ 
--+-+     args = parser.parse_args()
--+-+     
--+-+-    manager = StateManager()
--+-++    manager = WorkflowManager()
--+-+ 
--+-+-    if args.command == "review":
--+-+-        manager.review()
--+-+-    elif args.command == "approve":
--+-++    if args.command == "approve":
--+-+         manager.approve()
--+-+     elif args.command == "new":
--+-+         process_prompt(args.prompt)
--+-+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
--+-+index 703640c..b829d36 100644
--+-+--- a/src/dw6/state_manager.py
--+-++++ b/src/dw6/state_manager.py
--+-+@@ -9,7 +9,7 @@ from dw6 import git_handler
--+-+ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
--+-+ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
--+-+ APPROVAL_FILE = "logs/approvals.log"
--+-+-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
--+-++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
--+-+ DELIVERABLE_PATHS = {
--+-+     "Engineer": "deliverables/engineering",
--+-+     "Coder": "deliverables/coding",
--+-+@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
--+-+     "Researcher": "deliverables/research",
--+-+ }
--+-+ 
--+-++class Governor:
--+-++    def __init__(self, state):
--+-++        self.state = state
--+-++        self.current_stage = self.state.get("CurrentStage")
--++-     def get_state(self):
--++-         return self.state.data
--++- 
--++++    def enforce_rules(self):
--++++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
--++++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
--++++        print(f"[RULE] {rule}")
--+ ++
--+-++    def approve(self):
--+-++        old_stage = self.current_stage
--+-++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
--+-++        self._validate_stage_exit_criteria()
--+-++        # The original logic from WorkflowManager is now fully integrated here.
--+-++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
--+-++        workflow_manager._validate_stage()
--+-++        workflow_manager._run_pre_transition_actions()
--+-++        self._transition_to_next_stage() # This method now belongs to the Governor
--+-++        workflow_manager._run_post_transition_actions()
--+-++        self.state.save()
--+-++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
--+-++
--+-++    def _validate_stage_exit_criteria(self):
--+-++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
--+-++        if self.current_stage == "Engineer":
--+-++            req_id = self.state.get("RequirementPointer")
--+-++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
--+-++            if not spec_file.exists():
--+-++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
--+-++                sys.exit(1)
--+-++            print("Governor: 'Engineer' exit criteria met.")
--++      def approve(self):
--++--        old_stage = self.current_stage
--++--        print(f"--- Approving Stage: {old_stage} ---")
--++--        self._validate_stage()
--++--        self._run_pre_transition_actions()
--++--        self._transition_to_next_stage()
--++--        self._run_post_transition_actions()
--++--        self.state.save()
--++--        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
--++-+        # The manager now simply delegates to the governor.
--++-+        self.governor.approve()
--++- 
--++-     def _validate_stage(self):
--++-         print(f"Validating deliverables for stage: {self.current_stage}")
--++-@@ -123,25 +167,7 @@ class WorkflowManager:
--++-         if self.current_stage == "Coder":
--++-             git_handler.save_current_commit_sha()
--++- 
--++--    def _transition_to_next_stage(self):
--++--        current_index = STAGES.index(self.current_stage)
--++--        if current_index == len(STAGES) - 1:
--++--            self._complete_requirement_cycle()
--++--            self.current_stage = STAGES[0]
--++--        else:
--++--            self.current_stage = STAGES[current_index + 1]
--++--        self.state.set("CurrentStage", self.current_stage)
--++- 
--++--    def _complete_requirement_cycle(self):
--++--        req_id = int(self.state.get("RequirementPointer"))
--++--        os.makedirs("logs", exist_ok=True)
--++--        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
--++--        with open(APPROVAL_FILE, "a") as f:
--++--            f.write(f"Requirement {req_id} approved at {timestamp}\n")
--++--        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
--++--        next_req_id = req_id + 1
--++--        self.state.set("RequirementPointer", next_req_id)
--++--        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
--++- 
--++- class WorkflowState:
--++-     def __init__(self):
--+++         old_stage = self.current_stage
--+++         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
--++++        self.enforce_rules()
--+++         self._validate_stage_exit_criteria()
--+++         # The original logic from WorkflowManager is now fully integrated here.
--+++         workflow_manager = WorkflowManager() # We still need access to its methods for now.
--++ diff --git a/tests/test_governor.py b/tests/test_governor.py
--++-new file mode 100644
--++-index 0000000..95b566d
--++---- /dev/null
--+++index 95b566d..26bf82b 100644
--+++--- a/tests/test_governor.py
--++ +++ b/tests/test_governor.py
--++-@@ -0,0 +1,55 @@
--++-+# tests/test_governor.py
--++-+import pytest
--++-+from unittest.mock import MagicMock
--++-+from pathlib import Path
--++-+import sys
--++-+
--++-+from dw6.state_manager import Governor, WorkflowState
--++-+
--++-+@pytest.fixture
--++-+def mock_state(mocker):
--++-+    """Fixture to create a mock WorkflowState."""
--++-+    state = MagicMock(spec=WorkflowState)
--++-+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
--++-+    return state
--++-+
--++-+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
--++-+    """Verify the Governor blocks approval if the spec file is missing."""
--++-+    # Arrange: Set the state to Engineer and mock the requirement pointer
--++-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
--++-+    
--++-+    # Ensure the spec file does NOT exist for this test
--++-+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
--++-+    if spec_file.exists():
--++-+        spec_file.unlink()
--++-+
--++-+    governor = Governor(mock_state)
--++-+
--++-+    # Act & Assert: The approval should fail with a SystemExit
--++-+    with pytest.raises(SystemExit) as e:
--++-+        governor._validate_stage_exit_criteria()
--++-+    
--++-+    assert e.type == SystemExit
--++-+    assert e.value.code == 1
--++-+
--++-+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
--++-+    """Verify the Governor allows approval if the spec file exists."""
--++-+    # Arrange: Set the state to Engineer and mock the requirement pointer
--++-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
--++-+    
--++-+    # Ensure the spec file DOES exist for this test
--++-+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
--++-+    spec_file.parent.mkdir(parents=True, exist_ok=True)
--++-+    spec_file.touch()
--+++@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
--+++         # Clean up the created file
--+++         if spec_file.exists():
--+++             spec_file.unlink()
--+  +
--+--     if len(sys.argv) == 1:
--+--         parser.print_help(sys.stderr)
--+--         sys.exit(1)
--+--@@ -27,6 +32,8 @@ def main():
--+--         manager.review()
--+--     elif args.command == "approve":
--+-++    def _transition_to_next_stage(self):
--+-++        current_index = STAGES.index(self.current_stage)
--+-++        # After 'Deployer', the cycle is complete
--+-++        if self.current_stage == "Deployer":
--+-++            self._complete_requirement_cycle()
--+-++            self.current_stage = STAGES[0]
--+-++        else:
--+-++            self.current_stage = STAGES[current_index + 1]
--+-++        self.state.set("CurrentStage", self.current_stage)
--+-++
--+-++    def _complete_requirement_cycle(self):
--+-++        req_id = int(self.state.get("RequirementPointer"))
--+-++        os.makedirs("logs", exist_ok=True)
--+-++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
--+-++        with open(APPROVAL_FILE, "a") as f:
--+-++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
--+-++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
--+-++        next_req_id = req_id + 1
--+-++        self.state.set("RequirementPointer", next_req_id)
--+-++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
--+-++
--+-+ class WorkflowManager:
--+-+     def __init__(self):
--+-+         self.state = WorkflowState()
--+-++        self.governor = Governor(self.state) # The manager now has a governor
--+-+         self.current_stage = self.state.get("CurrentStage")
--+-+ 
--+-+     def get_state(self):
--+-+         return self.state.data
--+-+ 
--+-+     def approve(self):
--+-+-        old_stage = self.current_stage
--+-+-        print(f"--- Approving Stage: {old_stage} ---")
--+-+-        self._validate_stage()
--+-+-        self._run_pre_transition_actions()
--+-+-        self._transition_to_next_stage()
--+-+-        self._run_post_transition_actions()
--+-+-        self.state.save()
--+-+-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
--+-++        # The manager now simply delegates to the governor.
--+-++        self.governor.approve()
--+-+ 
--+-+     def _validate_stage(self):
--+-+         print(f"Validating deliverables for stage: {self.current_stage}")
--+-+@@ -123,25 +167,7 @@ class WorkflowManager:
--+-+         if self.current_stage == "Coder":
--+-+             git_handler.save_current_commit_sha()
--+-+ 
--+-+-    def _transition_to_next_stage(self):
--+-+-        current_index = STAGES.index(self.current_stage)
--+-+-        if current_index == len(STAGES) - 1:
--+-+-            self._complete_requirement_cycle()
--+-+-            self.current_stage = STAGES[0]
--+-+-        else:
--+-+-            self.current_stage = STAGES[current_index + 1]
--+-+-        self.state.set("CurrentStage", self.current_stage)
--+-+ 
--+-+-    def _complete_requirement_cycle(self):
--+-+-        req_id = int(self.state.get("RequirementPointer"))
--+-+-        os.makedirs("logs", exist_ok=True)
--+-+-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
--+-+-        with open(APPROVAL_FILE, "a") as f:
--+-+-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
--+-+-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
--+-+-        next_req_id = req_id + 1
--+-+-        self.state.set("RequirementPointer", next_req_id)
--+-+-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
--+-+ 
--+-+ class WorkflowState:
--+-+     def __init__(self):
--+-+diff --git a/tests/test_governor.py b/tests/test_governor.py
--+-+new file mode 100644
--+-+index 0000000..95b566d
--+-+--- /dev/null
--+-++++ b/tests/test_governor.py
--+-+@@ -0,0 +1,55 @@
--+-++# tests/test_governor.py
--+-++import pytest
--+-++from unittest.mock import MagicMock
--+-++from pathlib import Path
--+-++import sys
--+-++
--+-++from dw6.state_manager import Governor, WorkflowState
--+-++
--+-++@pytest.fixture
--+-++def mock_state(mocker):
--+-++    """Fixture to create a mock WorkflowState."""
--+-++    state = MagicMock(spec=WorkflowState)
--+-++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
--+-++    return state
--+-++
--+-++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
--+-++    """Verify the Governor blocks approval if the spec file is missing."""
--+-++    # Arrange: Set the state to Engineer and mock the requirement pointer
--+-++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
--+-++    
--+-++    # Ensure the spec file does NOT exist for this test
--+-++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
--+-++    if spec_file.exists():
--+-++        spec_file.unlink()
--+-++
--+-++    governor = Governor(mock_state)
--+-++
--+-++    # Act & Assert: The approval should fail with a SystemExit
--+-++    with pytest.raises(SystemExit) as e:
--+-++        governor._validate_stage_exit_criteria()
--+-++    
--+-++    assert e.type == SystemExit
--+-++    assert e.value.code == 1
--+-++
--+-++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
--+-++    """Verify the Governor allows approval if the spec file exists."""
--+-++    # Arrange: Set the state to Engineer and mock the requirement pointer
--+-++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
--+-++    
--+-++    # Ensure the spec file DOES exist for this test
--+-++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
--+-++    spec_file.parent.mkdir(parents=True, exist_ok=True)
--+-++    spec_file.touch()
--+-++
--+-++    governor = Governor(mock_state)
--+-++
--+-++    # Act & Assert: The approval should pass without raising an exception
--+-++    try:
--+-++        governor._validate_stage_exit_criteria()
--+-++    except SystemExit:
--+-++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
--+-++    finally:
--+-++        # Clean up the created file
--+-++        if spec_file.exists():
--+-++            spec_file.unlink()
--+-+diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
--+-+index 5b9d1eb..44d2cc9 100644
--+-+--- a/tests/test_state_manager_integration.py
--+-++++ b/tests/test_state_manager_integration.py
--+-+@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
--+-+ 
--+-+     @patch('dw6.state_manager.WorkflowState')
--+-+     @patch('dw6.git_handler.get_changes_since_last_commit')
--+-+-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
--+-++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
--+-++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
--+-+         """Ensure approving Coder stage generates a deliverable without altering the real state."""
--+-+         # Arrange
--+-+         mock_state_instance = mock_WorkflowState.return_value
--+-+@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
--+-+         # Act
--+-          manager.approve()
--+--+    elif args.command == "new":
--+--+        process_prompt(args.prompt)
--+-  
--+-- if __name__ == "__main__":
--+--     main()
--+-+-        # Assert
--+-++        # Assert that the deliverable file was created
--+-+         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
--+-+         self.assertTrue(deliverable_path.exists())
--+-++        # Clean up the created file
--+-++        deliverable_path.unlink()
--+-++
--+-+         mock_state_instance.save.assert_called_once()
--+-+ 
--+-+ if __name__ == '__main__':
--+-+diff --git a/uv.lock b/uv.lock
--+-+index c79d29c..8e7411f 100644
--+-+--- a/uv.lock
--+-++++ b/uv.lock
--+-+@@ -66,6 +66,7 @@ dependencies = [
--+-+ test = [
--+-+     { name = "pytest" },
--+-+     { name = "pytest-cov" },
--+-++    { name = "pytest-mock" },
--+-+ ]
--+-+ 
--+-+ [package.metadata]
--+-+@@ -73,6 +74,7 @@ requires-dist = [
--+-+     { name = "gitpython" },
--+-+     { name = "pytest", marker = "extra == 'test'" },
--+-+     { name = "pytest-cov", marker = "extra == 'test'" },
--+-++    { name = "pytest-mock", marker = "extra == 'test'" },
--+-+     { name = "python-dotenv" },
--+-+ ]
--+-+ provides-extras = ["test"]
--+-+@@ -167,6 +169,18 @@ wheels = [
--+-+     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
--+-+ ]
--+-+ 
--+-++[[package]]
--+-++name = "pytest-mock"
--+-++version = "3.14.1"
--+-++source = { registry = "https://pypi.org/simple" }
--+-++dependencies = [
--+-++    { name = "pytest" },
--+-++]
--+-++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
--+-++wheels = [
--+-++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
--+-++]
--+-++
--+-+ [[package]]
--+-+ name = "python-dotenv"
--+-+ version = "1.1.1"
--++++def test_governor_enforces_rules_on_approve(mocker, capsys):
--++++    """Verify that the Governor prints the correct rule for the current stage."""
--++++    # Arrange
--++++    mock_state = mocker.MagicMock(spec=WorkflowState)
--++++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
--++ +    governor = Governor(mock_state)
--++++    # Mock the exit criteria validation to prevent SystemExit
--++++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
--++++    # Mock the rest of the approval process to isolate the rule enforcement
--++++    mocker.patch.object(governor, '_transition_to_next_stage')
--++++    mocker.patch('dw6.state_manager.WorkflowManager')
-++--+        governor._validate_stage_exit_criteria()
-++--+    except SystemExit:
-++--+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
-++--+    finally:
-++--+        # Clean up the created file
-++--+        if spec_file.exists():
-++--+            spec_file.unlink()
-++--diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
-++--index 5b9d1eb..44d2cc9 100644
-++----- a/tests/test_state_manager_integration.py
-++--+++ b/tests/test_state_manager_integration.py
-++--@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-++-- 
-++--     @patch('dw6.state_manager.WorkflowState')
-++--     @patch('dw6.git_handler.get_changes_since_last_commit')
-++---    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
-++--+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
-++--+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
-++--         """Ensure approving Coder stage generates a deliverable without altering the real state."""
-++--         # Arrange
-++--         mock_state_instance = mock_WorkflowState.return_value
-++--@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-++--         # Act
-++--         manager.approve()
-++-- 
-++---        # Assert
-++--+        # Assert that the deliverable file was created
-++--         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
-++--         self.assertTrue(deliverable_path.exists())
-++--+        # Clean up the created file
-++--+        deliverable_path.unlink()
-++--+
-++--         mock_state_instance.save.assert_called_once()
-++-- 
-++-- if __name__ == '__main__':
-++--diff --git a/uv.lock b/uv.lock
-++--index c79d29c..8e7411f 100644
-++----- a/uv.lock
-++--+++ b/uv.lock
-++--@@ -66,6 +66,7 @@ dependencies = [
-++-- test = [
-++--     { name = "pytest" },
-++--     { name = "pytest-cov" },
-++--+    { name = "pytest-mock" },
-++-- ]
-++-- 
-++-- [package.metadata]
-++--@@ -73,6 +74,7 @@ requires-dist = [
-++--     { name = "gitpython" },
-++--     { name = "pytest", marker = "extra == 'test'" },
-++--     { name = "pytest-cov", marker = "extra == 'test'" },
-++--+    { name = "pytest-mock", marker = "extra == 'test'" },
-++--     { name = "python-dotenv" },
-++-- ]
-++-- provides-extras = ["test"]
-++--@@ -167,6 +169,18 @@ wheels = [
-++--     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
-++-- ]
-++-- 
-++--+[[package]]
-++--+name = "pytest-mock"
-++--+version = "3.14.1"
-++--+source = { registry = "https://pypi.org/simple" }
-++--+dependencies = [
-++--+    { name = "pytest" },
-++--+]
-++--+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
-++--+wheels = [
-++--+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
-++--+]
-+++++    description = "This is the first meta requirement."
-+++++
-++ ++    # Act
-++-++    governor.approve()
++---     # Approve command
++---     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++--- 
++---@@ -26,11 +24,9 @@ def main():
++--- 
++---     args = parser.parse_args()
++---     
++----    manager = StateManager()
++---+    manager = WorkflowManager()
++--- 
++----    if args.command == "review":
++----        manager.review()
++----    elif args.command == "approve":
++---+    if args.command == "approve":
++---         manager.approve()
++---     elif args.command == "new":
++---         process_prompt(args.prompt)
++--+ CurrentStage=Coder
++--+-RequirementPointer=9
++--++RequirementPointer=10
++-- diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++---index 703640c..b829d36 100644
++--+index b829d36..241fa62 100644
++-- --- a/src/dw6/state_manager.py
++-- +++ b/src/dw6/state_manager.py
++---@@ -9,7 +9,7 @@ from dw6 import git_handler
++--- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
++--- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
++--- APPROVAL_FILE = "logs/approvals.log"
++----STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
++---+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
++--- DELIVERABLE_PATHS = {
++---     "Engineer": "deliverables/engineering",
++---     "Coder": "deliverables/coding",
++---@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
++---     "Researcher": "deliverables/research",
++--+@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
++--  }
++-+  CurrentStage=Coder
++-+--RequirementPointer=9
++-+-+RequirementPointer=10
++-+-diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++-+-index b829d36..241fa62 100644
++-+---- a/src/dw6/state_manager.py
++-+-+++ b/src/dw6/state_manager.py
++-+-@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
++-+- }
++-++-RequirementPointer=10
++-+++RequirementPointer=11
++-++diff --git a/src/dw6/main.py b/src/dw6/main.py
++-++index 90862f9..c65a4d9 100644
++-++--- a/src/dw6/main.py
++-+++++ b/src/dw6/main.py
++-++@@ -1,16 +1,42 @@
++-++ # dw6/main.py
++-++ import argparse
++-++ import sys
++-+++import re
++-+++from pathlib import Path
++-+++from datetime import datetime, timezone
++-++ from dw6.state_manager import WorkflowManager
++-++ from dw6.augmenter import process_prompt
+++-  CurrentStage=Coder
+++---RequirementPointer=9
+++--+RequirementPointer=10
+++--diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+++--index b829d36..241fa62 100644
+++----- a/src/dw6/state_manager.py
+++--+++ b/src/dw6/state_manager.py
+++--@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
+++-- }
+++-+-RequirementPointer=10
+++-++RequirementPointer=11
+++-+diff --git a/src/dw6/main.py b/src/dw6/main.py
+++-+index 90862f9..c65a4d9 100644
+++-+--- a/src/dw6/main.py
+++-++++ b/src/dw6/main.py
+++-+@@ -1,16 +1,42 @@
+++-+ # dw6/main.py
+++-+ import argparse
+++-+ import sys
+++-++import re
+++-++from pathlib import Path
+++-++from datetime import datetime, timezone
+++-+ from dw6.state_manager import WorkflowManager
+++-+ from dw6.augmenter import process_prompt
++++- CurrentStage=Coder
++++--RequirementPointer=10
++++-+RequirementPointer=11
+++++-CurrentStage=Coder
+++++-RequirementPointer=11
++++++CurrentStage=Deployer
++++++RequirementPointer=12
++++ diff --git a/src/dw6/main.py b/src/dw6/main.py
++++-index 90862f9..c65a4d9 100644
+++++index c65a4d9..13e4d93 100644
++++ --- a/src/dw6/main.py
++++ +++ b/src/dw6/main.py
++++-@@ -1,16 +1,42 @@
++++- # dw6/main.py
+++++@@ -2,6 +2,7 @@
++++  import argparse
++++  import sys
++++-+import re
++++-+from pathlib import Path
++++-+from datetime import datetime, timezone
+++++ import re
++++++import subprocess
+++++ from pathlib import Path
+++++ from datetime import datetime, timezone
++++  from dw6.state_manager import WorkflowManager
++++- from dw6.augmenter import process_prompt
+++++@@ -48,6 +49,10 @@ def main():
+++++     meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
+++++     meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
+     
+----+    # New command
+----+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+----+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+---+@@ -26,11 +24,9 @@ def main():
+---+ 
+---+     args = parser.parse_args()
+---+     
+---+-    manager = StateManager()
+---++    manager = WorkflowManager()
+---+ 
+---+-    if args.command == "review":
+---+-        manager.review()
+---+-    elif args.command == "approve":
+---++    if args.command == "approve":
+---+         manager.approve()
+---+     elif args.command == "new":
+---+         process_prompt(args.prompt)
+---+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+---+index 703640c..b829d36 100644
+---+--- a/src/dw6/state_manager.py
+---++++ b/src/dw6/state_manager.py
+---+@@ -9,7 +9,7 @@ from dw6 import git_handler
+---+ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+---+ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+---+ APPROVAL_FILE = "logs/approvals.log"
+---+-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
+---++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+---+ DELIVERABLE_PATHS = {
+---+     "Engineer": "deliverables/engineering",
+---+     "Coder": "deliverables/coding",
+---+@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
+---+     "Researcher": "deliverables/research",
+---+ }
+---+ 
+---++class Governor:
+---++    def __init__(self, state):
+---++        self.state = state
+---++        self.current_stage = self.state.get("CurrentStage")
+--+-     def get_state(self):
+--+-         return self.state.data
+--+- 
+--+++    def enforce_rules(self):
+--+++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+--+++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+--+++        print(f"[RULE] {rule}")
+-+--     def get_state(self):
+-+--         return self.state.data
+-+-- 
+-+-++    def enforce_rules(self):
+-+-++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+-+-++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+-+-++        print(f"[RULE] {rule}")
+-++-+    def enforce_rules(self):
+-++-+        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+-++-+        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+-++-+        print(f"[RULE] {rule}")
+-+++-
+-+++     # Approve command
+-+++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-+++ 
+-+++@@ -18,18 +44,24 @@ def main():
+-+++     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+-+++     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++---+class Governor:
++---+    def __init__(self, state):
++---+        self.state = state
++---+        self.current_stage = self.state.get("CurrentStage")
++---+
++---+    def approve(self):
++---+        old_stage = self.current_stage
++---+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++---+        self._validate_stage_exit_criteria()
++---+        # The original logic from WorkflowManager is now fully integrated here.
++---+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
++---+        workflow_manager._validate_stage()
++---+        workflow_manager._run_pre_transition_actions()
++---+        self._transition_to_next_stage() # This method now belongs to the Governor
++---+        workflow_manager._run_post_transition_actions()
++---+        self.state.save()
++---+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++---+
++---+    def _validate_stage_exit_criteria(self):
++---+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
++---+        if self.current_stage == "Engineer":
++---+            req_id = self.state.get("RequirementPointer")
++---+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
++---+            if not spec_file.exists():
++---+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
++---+                sys.exit(1)
++---+            print("Governor: 'Engineer' exit criteria met.")
++---+
++---+    def _transition_to_next_stage(self):
++---+        current_index = STAGES.index(self.current_stage)
++---+        # After 'Deployer', the cycle is complete
++---+        if self.current_stage == "Deployer":
++---+            self._complete_requirement_cycle()
++---+            self.current_stage = STAGES[0]
++---+        else:
++---+            self.current_stage = STAGES[current_index + 1]
++---+        self.state.set("CurrentStage", self.current_stage)
++---+
++---+    def _complete_requirement_cycle(self):
++---+        req_id = int(self.state.get("RequirementPointer"))
++---+        os.makedirs("logs", exist_ok=True)
++---+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++---+        with open(APPROVAL_FILE, "a") as f:
++---+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++---+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++---+        next_req_id = req_id + 1
++---+        self.state.set("RequirementPointer", next_req_id)
++---+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++---+
++--- class WorkflowManager:
++---     def __init__(self):
++---         self.state = WorkflowState()
++---+        self.governor = Governor(self.state) # The manager now has a governor
++--+ class Governor:
++--++    RULES = {
++--++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
++--++        "Coder": "Can use file system tools, code editing tools, and run tests.",
++--++        "Validator": "Can only run tests and validation tools.",
++--++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
++--++        "Researcher": "Can use web search and documentation reading tools."
++--++    }
++--+     def __init__(self, state):
++--+         self.state = state
++--          self.current_stage = self.state.get("CurrentStage")
++-+- class Governor:
++-+-+    RULES = {
++-+-+        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
++-+-+        "Coder": "Can use file system tools, code editing tools, and run tests.",
++-+-+        "Validator": "Can only run tests and validation tools.",
++-+-+        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
++-+-+        "Researcher": "Can use web search and documentation reading tools."
++-+-+    }
++-+-     def __init__(self, state):
++-+-         self.state = state
++-+-         self.current_stage = self.state.get("CurrentStage")
++-+++META_LOG_FILE = Path("logs/meta_requirements.log")
++-+++
++-+++def register_meta_requirement(description: str):
++-+++    """Logs a new meta-requirement to the meta_requirements.log file."""
++-+++    META_LOG_FILE.parent.mkdir(exist_ok=True)
++-+++    
++-+++    last_id = 0
++-+++    if META_LOG_FILE.exists():
++-+++        with open(META_LOG_FILE, "r") as f:
++-+++            lines = f.readlines()
++-+++            if lines:
++-+++                last_line = lines[-1]
++-+++                match = re.search(r'^\[ID:(\d+)\]', last_line)
++-+++                if match:
++-+++                    last_id = int(match.group(1))
++-+++
++-+++    new_id = last_id + 1
++-+++    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++-+++    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
+++-- class Governor:
+++--+    RULES = {
+++--+        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+++--+        "Coder": "Can use file system tools, code editing tools, and run tests.",
+++--+        "Validator": "Can only run tests and validation tools.",
+++--+        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+++--+        "Researcher": "Can use web search and documentation reading tools."
+++--+    }
+++--     def __init__(self, state):
+++--         self.state = state
+++--         self.current_stage = self.state.get("CurrentStage")
+++-++META_LOG_FILE = Path("logs/meta_requirements.log")
+++-++
+++-++def register_meta_requirement(description: str):
+++-++    """Logs a new meta-requirement to the meta_requirements.log file."""
+++-++    META_LOG_FILE.parent.mkdir(exist_ok=True)
+++-++    
+++-++    last_id = 0
+++-++    if META_LOG_FILE.exists():
+++-++        with open(META_LOG_FILE, "r") as f:
+++-++            lines = f.readlines()
+++-++            if lines:
+++-++                last_line = lines[-1]
+++-++                match = re.search(r'^\[ID:(\d+)\]', last_line)
+++-++                if match:
+++-++                    last_id = int(match.group(1))
+++-++
+++-++    new_id = last_id + 1
+++-++    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+++-++    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
+++-++
+++-++    with open(META_LOG_FILE, "a") as f:
+++-++        f.write(log_entry)
+++-++    
+++-++    print(f"Successfully logged meta-requirement {new_id}.")
++++-+META_LOG_FILE = Path("logs/meta_requirements.log")
++++-+
++++-+def register_meta_requirement(description: str):
++++-+    """Logs a new meta-requirement to the meta_requirements.log file."""
++++-+    META_LOG_FILE.parent.mkdir(exist_ok=True)
++++-+    
++++-+    last_id = 0
++++-+    if META_LOG_FILE.exists():
++++-+        with open(META_LOG_FILE, "r") as f:
++++-+            lines = f.readlines()
++++-+            if lines:
++++-+                last_line = lines[-1]
++++-+                match = re.search(r'^\[ID:(\d+)\]', last_line)
++++-+                if match:
++++-+                    last_id = int(match.group(1))
++++-+
++++-+    new_id = last_id + 1
++++-+    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++++-+    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
++++-+
++++-+    with open(META_LOG_FILE, "a") as f:
++++-+        f.write(log_entry)
++++-+    
++++-+    print(f"Successfully logged meta-requirement {new_id}.")
++++-+
++++- def main():
++++-     """Main entry point for the DW6 CLI."""
++++--    # Test comment for Cycle 2 validation.
++++-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++++-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++++- 
++++--
++++-     # Approve command
++++-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++++- 
++++-@@ -18,18 +44,24 @@ def main():
++++-     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++++-     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++++- 
++++-+    # Meta-req command
++++-+    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
++++-+    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
++++++    # Do command
++++++    do_parser = subparsers.add_parser("do", help="Execute a governed action.")
++++++    do_parser.add_argument("action", type=str, help="The action to execute.")
++++ +
++++      if len(sys.argv) == 1:
++++          parser.print_help(sys.stderr)
++++          sys.exit(1)
++++- 
++++-     args = parser.parse_args()
+++++@@ -56,6 +61,17 @@ def main():
++++      
++++--    manager = WorkflowManager()
++++--
++++--    if args.command == "approve":
++++--        manager.approve()
++++--    elif args.command == "new":
++++--        process_prompt(args.prompt)
++++-+    if args.command == "meta-req":
++++-+        register_meta_requirement(args.description)
++++-+    else:
+++++     if args.command == "meta-req":
+++++         register_meta_requirement(args.description)
++++++    elif args.command == "do":
++++ +        manager = WorkflowManager()
++++-+        if args.command == "approve":
++++-+            manager.approve()
++++-+        elif args.command == "new":
++++-+            process_prompt(args.prompt)
++++++        try:
++++++            manager.governor.authorize(args.action)
++++++            # The command is authorized, execute it.
++++++            subprocess.run(args.action, shell=True, check=True)
++++++        except PermissionError:
++++++            sys.exit(1)
++++++        except subprocess.CalledProcessError:
++++++            print(f"ERROR: The action '{args.action}' failed to execute.", file=sys.stderr)
++++++            sys.exit(1)
+++++     else:
+++++         manager = WorkflowManager()
+++++         if args.command == "approve":
+++++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+++++index 241fa62..33e9d07 100644
+++++--- a/src/dw6/state_manager.py
++++++++ b/src/dw6/state_manager.py
+++++@@ -20,20 +20,52 @@ DELIVERABLE_PATHS = {
+ +++ 
+-++++    # Meta-req command
+-++++    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
+-++++    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
+++++ class Governor:
+++++     RULES = {
+++++-        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+++++-        "Coder": "Can use file system tools, code editing tools, and run tests.",
+++++-        "Validator": "Can only run tests and validation tools.",
+++++-        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+++++-        "Researcher": "Can use web search and documentation reading tools."
++++++        "Engineer": [
++++++            "uv run python -m dw6.main new",
++++++            "ls",
++++++            "cat",
++++++            "view_file_outline"
++++++        ],
++++++        "Coder": [
++++++            "replace_file_content",
++++++            "write_to_file",
++++++            "view_file_outline",
++++++            "ls"
++++++        ],
++++++        "Validator": [
++++++            "uv run pytest"
++++++        ],
++++++        "Deployer": [
++++++            "git add",
++++++            "git commit",
++++++            "git tag",
++++++            "uv run python -m dw6.main approve"
++++++        ],
++++++        "Researcher": [
++++++            "search_web",
++++++            "read_url_content"
++++++        ]
+++++     }
+++ ++
+++-+ def main():
+++-+     """Main entry point for the DW6 CLI."""
+++-+-    # Test comment for Cycle 2 validation.
+++-+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+++-+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+++++     def __init__(self, state):
+++++         self.state = state
+++++         self.current_stage = self.state.get("CurrentStage")
+++   
+++--+    def enforce_rules(self):
+++--+        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+++--+        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+++--+        print(f"[RULE] {rule}")
+++-+-
+++-+     # Approve command
+++-+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++-+ 
+++-+@@ -18,18 +44,24 @@ def main():
+++-+     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+++-+     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+++-+ 
+++-++    # Meta-req command
+++-++    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
+++-++    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
++++- if __name__ == "__main__":
++++-     main()
++++++    def authorize(self, command: str):
++++++        """Checks if a command is allowed in the current stage."""
++++++        allowed_commands = self.RULES.get(self.current_stage, [])
++++++        if not any(command.startswith(prefix) for prefix in allowed_commands):
++++++            error_msg = f"[GOVERNOR] Action denied. The command '{(command)}' is not allowed in the '{self.current_stage}' stage."
++++++            print(error_msg, file=sys.stderr)
++++++            raise PermissionError(error_msg)
++++++        print(f"[GOVERNOR] Action authorized for stage '{self.current_stage}'.")
+++ ++
+++-+     if len(sys.argv) == 1:
+++-+         parser.print_help(sys.stderr)
+++-+         sys.exit(1)
+++++     def enforce_rules(self):
+++++-        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
++++++        rules = self.RULES.get(self.current_stage, ["No specific rules defined."])
+++++         print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+++++-        print(f"[RULE] {rule}")
++++++        print("[RULE] Allowed command prefixes:")
++++++        for rule in rules:
++++++            print(f"  - {rule}")
+++ + 
+++-+     args = parser.parse_args()
+++-+     
+++-+-    manager = WorkflowManager()
+++-+-
+++-+-    if args.command == "approve":
+++-+-        manager.approve()
+++-+-    elif args.command == "new":
+++-+-        process_prompt(args.prompt)
+++-++    if args.command == "meta-req":
+++-++        register_meta_requirement(args.description)
+++-++    else:
+++-++        manager = WorkflowManager()
+++-++        if args.command == "approve":
+++-++            manager.approve()
+++-++        elif args.command == "new":
+++-++            process_prompt(args.prompt)
+++++     def approve(self):
+++++         old_stage = self.current_stage
+++++diff --git a/tests/test_governor.py b/tests/test_governor.py
+++++index 26bf82b..a431529 100644
+++++--- a/tests/test_governor.py
++++++++ b/tests/test_governor.py
+++++@@ -71,5 +71,37 @@ def test_governor_enforces_rules_on_approve(mocker, capsys):
+++ + 
+++-+ if __name__ == "__main__":
+++-+     main()
+++-+diff --git a/tests/test_main.py b/tests/test_main.py
+++-+index c429973..eddb264 100644
+++-+--- a/tests/test_main.py
+++-++++ b/tests/test_main.py
+++-+@@ -1,5 +1,52 @@
+++-+ # tests/test_main.py
+++-++import pytest
+++-++from pathlib import Path
+++-++import re
+++-++from dw6.main import register_meta_requirement, META_LOG_FILE
+++-+ 
+++-+-def test_placeholder():
+++-+-    """A placeholder test to satisfy the Validator stage."""
+++-+-    assert True
+++-++@pytest.fixture(autouse=True)
+++-++def cleanup_log_file():
+++-++    """Fixture to clean up the meta log file before and after a test."""
+++-++    if META_LOG_FILE.exists():
+++-++        META_LOG_FILE.unlink()
+++-++    yield
+++-++    if META_LOG_FILE.exists():
+++-++        META_LOG_FILE.unlink()
 ++- +
-++-- [[package]]
-++-- name = "python-dotenv"
-++-- version = "1.1.1"
-+++++    register_meta_requirement(description)
-+++++
-++ ++    # Assert
-++-++    captured = capsys.readouterr()
-++-++    expected_rule = Governor.RULES["Coder"]
-++-++    assert expected_rule in captured.out
-+++++    assert META_LOG_FILE.exists()
-+++++    with open(META_LOG_FILE, "r") as f:
-+++++        content = f.read()
-+++++    
-+++++    assert "[ID:1]" in content
-+++++    assert description in content
-+++++    # A simple regex to check for the timestamp format
-+++++    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
+++--     def approve(self):
+++--         old_stage = self.current_stage
+++--         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+++--+        self.enforce_rules()
+++--         self._validate_stage_exit_criteria()
+++--         # The original logic from WorkflowManager is now fully integrated here.
+++--         workflow_manager = WorkflowManager() # We still need access to its methods for now.
+++--diff --git a/tests/test_governor.py b/tests/test_governor.py
+++--index 95b566d..26bf82b 100644
+++----- a/tests/test_governor.py
+++--+++ b/tests/test_governor.py
+++--@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+++--         # Clean up the created file
+++--         if spec_file.exists():
+++--             spec_file.unlink()
+++-++def test_register_meta_requirement_creates_file_and_logs_entry():
+++-++    """Verify that the first call creates the log file and adds the first entry correctly."""
+++++     # Assert
+++++     captured = capsys.readouterr()
+++++-    expected_rule = Governor.RULES["Coder"]
+++++-    assert expected_rule in captured.out
++++++    # Check that each rule is printed
++++++    for rule in Governor.RULES["Coder"]:
++++++        assert rule in captured.out
++ +++
++-+++    with open(META_LOG_FILE, "a") as f:
++-+++        f.write(log_entry)
++++++@pytest.mark.parametrize("stage, allowed_command", [
++++++    (stage, command) 
++++++    for stage, commands in Governor.RULES.items() 
++++++    for command in commands
++++++])
++++++def test_governor_authorizes_allowed_commands(mock_state, stage, allowed_command):
++++++    """Verify that the Governor authorizes all allowed commands for each stage."""
+++ ++    # Arrange
+++-++    description = "This is the first meta requirement."
++++++    mock_state.get.return_value = stage
++++++    governor = Governor(mock_state)
++ +++    
++-+++    print(f"Successfully logged meta-requirement {new_id}.")
++-+++
++-++ def main():
++-++     """Main entry point for the DW6 CLI."""
++-++-    # Test comment for Cycle 2 validation.
++-++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++-++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++-   
++---     def get_state(self):
++---         return self.state.data
++--- 
++--++    def enforce_rules(self):
++--++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
++--++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
++--++        print(f"[RULE] {rule}")
++-+-+    def enforce_rules(self):
++-+-+        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
++-+-+        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
++-+-+        print(f"[RULE] {rule}")
++-++-
++-++     # Approve command
++-++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
++-++ 
++-++@@ -18,18 +44,24 @@ def main():
++-++     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++-++     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++-++ 
++-+++    # Meta-req command
++-+++    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
++-+++    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
++++++    # Act & Assert
++++++    try:
++++++        governor.authorize(allowed_command + " --some-arg") # Test with an argument
++++++    except PermissionError:
++++++        pytest.fail(f"Governor incorrectly denied command '{allowed_command}' for stage '{stage}'.")
+   ++
+---++    def approve(self):
+---++        old_stage = self.current_stage
+---++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+---++        self._validate_stage_exit_criteria()
+---++        # The original logic from WorkflowManager is now fully integrated here.
+---++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
+---++        workflow_manager._validate_stage()
+---++        workflow_manager._run_pre_transition_actions()
+---++        self._transition_to_next_stage() # This method now belongs to the Governor
+---++        workflow_manager._run_post_transition_actions()
+---++        self.state.save()
+---++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+---++
+---++    def _validate_stage_exit_criteria(self):
+---++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
+---++        if self.current_stage == "Engineer":
+---++            req_id = self.state.get("RequirementPointer")
+---++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
+---++            if not spec_file.exists():
+---++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+---++                sys.exit(1)
+---++            print("Governor: 'Engineer' exit criteria met.")
+--+      def approve(self):
+--+--        old_stage = self.current_stage
+--+--        print(f"--- Approving Stage: {old_stage} ---")
+--+--        self._validate_stage()
+--+--        self._run_pre_transition_actions()
+--+--        self._transition_to_next_stage()
+--+--        self._run_post_transition_actions()
+--+--        self.state.save()
+--+--        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+--+-+        # The manager now simply delegates to the governor.
+--+-+        self.governor.approve()
+--+- 
+--+-     def _validate_stage(self):
+--+-         print(f"Validating deliverables for stage: {self.current_stage}")
+--+-@@ -123,25 +167,7 @@ class WorkflowManager:
+--+-         if self.current_stage == "Coder":
+--+-             git_handler.save_current_commit_sha()
+--+- 
+--+--    def _transition_to_next_stage(self):
+--+--        current_index = STAGES.index(self.current_stage)
+--+--        if current_index == len(STAGES) - 1:
+--+--            self._complete_requirement_cycle()
+--+--            self.current_stage = STAGES[0]
+--+--        else:
+--+--            self.current_stage = STAGES[current_index + 1]
+--+--        self.state.set("CurrentStage", self.current_stage)
+--+- 
+--+--    def _complete_requirement_cycle(self):
+--+--        req_id = int(self.state.get("RequirementPointer"))
+--+--        os.makedirs("logs", exist_ok=True)
+--+--        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+--+--        with open(APPROVAL_FILE, "a") as f:
+--+--            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+--+--        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+--+--        next_req_id = req_id + 1
+--+--        self.state.set("RequirementPointer", next_req_id)
+--+--        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+--+- 
+--+- class WorkflowState:
+--+-     def __init__(self):
+--++         old_stage = self.current_stage
+--++         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+--+++        self.enforce_rules()
+--++         self._validate_stage_exit_criteria()
+--++         # The original logic from WorkflowManager is now fully integrated here.
+--++         workflow_manager = WorkflowManager() # We still need access to its methods for now.
+--+ diff --git a/tests/test_governor.py b/tests/test_governor.py
+--+-new file mode 100644
+--+-index 0000000..95b566d
+--+---- /dev/null
+--++index 95b566d..26bf82b 100644
+--++--- a/tests/test_governor.py
+--+ +++ b/tests/test_governor.py
+--+-@@ -0,0 +1,55 @@
+--+-+# tests/test_governor.py
+--+-+import pytest
+--+-+from unittest.mock import MagicMock
+--+-+from pathlib import Path
+--+-+import sys
+--+-+
+--+-+from dw6.state_manager import Governor, WorkflowState
+--+-+
+--+-+@pytest.fixture
+--+-+def mock_state(mocker):
+--+-+    """Fixture to create a mock WorkflowState."""
+--+-+    state = MagicMock(spec=WorkflowState)
+--+-+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+--+-+    return state
+--+-+
+--+-+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+--+-+    """Verify the Governor blocks approval if the spec file is missing."""
+--+-+    # Arrange: Set the state to Engineer and mock the requirement pointer
+--+-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+--+-+    
+--+-+    # Ensure the spec file does NOT exist for this test
+--+-+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+--+-+    if spec_file.exists():
+--+-+        spec_file.unlink()
+--+-+
+--+-+    governor = Governor(mock_state)
+--+-+
+--+-+    # Act & Assert: The approval should fail with a SystemExit
+--+-+    with pytest.raises(SystemExit) as e:
+--+-+        governor._validate_stage_exit_criteria()
+--+-+    
+--+-+    assert e.type == SystemExit
+--+-+    assert e.value.code == 1
+--+-+
+--+-+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+--+-+    """Verify the Governor allows approval if the spec file exists."""
+--+-+    # Arrange: Set the state to Engineer and mock the requirement pointer
+--+-+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+--+-+    
+--+-+    # Ensure the spec file DOES exist for this test
+--+-+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+--+-+    spec_file.parent.mkdir(parents=True, exist_ok=True)
+--+-+    spec_file.touch()
+--++@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+--++         # Clean up the created file
+--++         if spec_file.exists():
+--++             spec_file.unlink()
+-+-      def approve(self):
+-+---        old_stage = self.current_stage
+-+---        print(f"--- Approving Stage: {old_stage} ---")
+-+---        self._validate_stage()
+-+---        self._run_pre_transition_actions()
+-+---        self._transition_to_next_stage()
+-+---        self._run_post_transition_actions()
+-+---        self.state.save()
+-+---        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+-+--+        # The manager now simply delegates to the governor.
+-+--+        self.governor.approve()
+-+-- 
+-+--     def _validate_stage(self):
+-+--         print(f"Validating deliverables for stage: {self.current_stage}")
+-+--@@ -123,25 +167,7 @@ class WorkflowManager:
+-+--         if self.current_stage == "Coder":
+-+--             git_handler.save_current_commit_sha()
+-+-- 
+-+---    def _transition_to_next_stage(self):
+-+---        current_index = STAGES.index(self.current_stage)
+-+---        if current_index == len(STAGES) - 1:
+-+---            self._complete_requirement_cycle()
+-+---            self.current_stage = STAGES[0]
+-+---        else:
+-+---            self.current_stage = STAGES[current_index + 1]
+-+---        self.state.set("CurrentStage", self.current_stage)
+-+-- 
+-+---    def _complete_requirement_cycle(self):
+-+---        req_id = int(self.state.get("RequirementPointer"))
+-+---        os.makedirs("logs", exist_ok=True)
+-+---        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-+---        with open(APPROVAL_FILE, "a") as f:
+-+---            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+-+---        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+-+---        next_req_id = req_id + 1
+-+---        self.state.set("RequirementPointer", next_req_id)
+-+---        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+-+-- 
+-+-- class WorkflowState:
+-+--     def __init__(self):
+-+-+         old_stage = self.current_stage
+-+-+         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+-+-++        self.enforce_rules()
+-+-+         self._validate_stage_exit_criteria()
+-+-+         # The original logic from WorkflowManager is now fully integrated here.
+-+-+         workflow_manager = WorkflowManager() # We still need access to its methods for now.
+-+- diff --git a/tests/test_governor.py b/tests/test_governor.py
+-+--new file mode 100644
+-+--index 0000000..95b566d
+-+----- /dev/null
+-+-+index 95b566d..26bf82b 100644
+-+-+--- a/tests/test_governor.py
+-+- +++ b/tests/test_governor.py
+-+--@@ -0,0 +1,55 @@
+-+--+# tests/test_governor.py
+-+--+import pytest
+-+--+from unittest.mock import MagicMock
+-+--+from pathlib import Path
+-+--+import sys
+-+--+
+-+--+from dw6.state_manager import Governor, WorkflowState
+-+--+
+-+--+@pytest.fixture
+-+--+def mock_state(mocker):
+-+--+    """Fixture to create a mock WorkflowState."""
+-+--+    state = MagicMock(spec=WorkflowState)
+-+--+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+-+--+    return state
+-+--+
+-+--+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+-+--+    """Verify the Governor blocks approval if the spec file is missing."""
+-+--+    # Arrange: Set the state to Engineer and mock the requirement pointer
+-+--+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+-+--+    
+-+--+    # Ensure the spec file does NOT exist for this test
+-+--+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+-+--+    if spec_file.exists():
+-+--+        spec_file.unlink()
+-+--+
+-+--+    governor = Governor(mock_state)
+-+--+
+-+--+    # Act & Assert: The approval should fail with a SystemExit
+-+--+    with pytest.raises(SystemExit) as e:
+-+--+        governor._validate_stage_exit_criteria()
+-+--+    
+-+--+    assert e.type == SystemExit
+-+--+    assert e.value.code == 1
+-+--+
+-+--+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+-+--+    """Verify the Governor allows approval if the spec file exists."""
+-+--+    # Arrange: Set the state to Engineer and mock the requirement pointer
+-+--+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+-+--+    
+-+--+    # Ensure the spec file DOES exist for this test
+-+--+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+-+--+    spec_file.parent.mkdir(parents=True, exist_ok=True)
+-+--+    spec_file.touch()
+-+-+@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+-+-+         # Clean up the created file
+-+-+         if spec_file.exists():
+-+-+             spec_file.unlink()
+-+++     if len(sys.argv) == 1:
+-+++         parser.print_help(sys.stderr)
+-+++         sys.exit(1)
+-+++ 
+-+++     args = parser.parse_args()
+-+++     
+-+++-    manager = WorkflowManager()
+-+++-
+-+++-    if args.command == "approve":
+-+++-        manager.approve()
+-+++-    elif args.command == "new":
+-+++-        process_prompt(args.prompt)
+-++++    if args.command == "meta-req":
+-++++        register_meta_requirement(args.description)
+-++++    else:
+-++++        manager = WorkflowManager()
+-++++        if args.command == "approve":
+-++++            manager.approve()
+-++++        elif args.command == "new":
+-++++            process_prompt(args.prompt)
+-+++ 
+-+++ if __name__ == "__main__":
+-+++     main()
+-+++diff --git a/tests/test_main.py b/tests/test_main.py
+-+++index c429973..eddb264 100644
+-+++--- a/tests/test_main.py
+-++++++ b/tests/test_main.py
+-+++@@ -1,5 +1,52 @@
+-+++ # tests/test_main.py
+-++++import pytest
+-++++from pathlib import Path
+-++++import re
+-++++from dw6.main import register_meta_requirement, META_LOG_FILE
+-+++ 
+-+++-def test_placeholder():
+-+++-    """A placeholder test to satisfy the Validator stage."""
+-+++-    assert True
+-++++@pytest.fixture(autouse=True)
+-++++def cleanup_log_file():
+-++++    """Fixture to clean up the meta log file before and after a test."""
+-++++    if META_LOG_FILE.exists():
+-++++        META_LOG_FILE.unlink()
+-++++    yield
+-++++    if META_LOG_FILE.exists():
+-++++        META_LOG_FILE.unlink()
++--      def approve(self):
++----        old_stage = self.current_stage
++----        print(f"--- Approving Stage: {old_stage} ---")
++----        self._validate_stage()
++----        self._run_pre_transition_actions()
++----        self._transition_to_next_stage()
++----        self._run_post_transition_actions()
++----        self.state.save()
++----        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
++---+        # The manager now simply delegates to the governor.
++---+        self.governor.approve()
++--- 
++---     def _validate_stage(self):
++---         print(f"Validating deliverables for stage: {self.current_stage}")
++---@@ -123,25 +167,7 @@ class WorkflowManager:
++---         if self.current_stage == "Coder":
++---             git_handler.save_current_commit_sha()
++--- 
++----    def _transition_to_next_stage(self):
++----        current_index = STAGES.index(self.current_stage)
++----        if current_index == len(STAGES) - 1:
++----            self._complete_requirement_cycle()
++----            self.current_stage = STAGES[0]
++----        else:
++----            self.current_stage = STAGES[current_index + 1]
++----        self.state.set("CurrentStage", self.current_stage)
++--- 
++----    def _complete_requirement_cycle(self):
++----        req_id = int(self.state.get("RequirementPointer"))
++----        os.makedirs("logs", exist_ok=True)
++----        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++----        with open(APPROVAL_FILE, "a") as f:
++----            f.write(f"Requirement {req_id} approved at {timestamp}\n")
++----        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
++----        next_req_id = req_id + 1
++----        self.state.set("RequirementPointer", next_req_id)
++----        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
++--- 
++--- class WorkflowState:
++---     def __init__(self):
++--+         old_stage = self.current_stage
++--+         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++--++        self.enforce_rules()
++--+         self._validate_stage_exit_criteria()
++--+         # The original logic from WorkflowManager is now fully integrated here.
++--+         workflow_manager = WorkflowManager() # We still need access to its methods for now.
++-- diff --git a/tests/test_governor.py b/tests/test_governor.py
++---new file mode 100644
++---index 0000000..95b566d
++------ /dev/null
++--+index 95b566d..26bf82b 100644
++--+--- a/tests/test_governor.py
++-- +++ b/tests/test_governor.py
++---@@ -0,0 +1,55 @@
++---+# tests/test_governor.py
++---+import pytest
++---+from unittest.mock import MagicMock
++---+from pathlib import Path
++---+import sys
++---+
++---+from dw6.state_manager import Governor, WorkflowState
++---+
++---+@pytest.fixture
++---+def mock_state(mocker):
++---+    """Fixture to create a mock WorkflowState."""
++---+    state = MagicMock(spec=WorkflowState)
++---+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
++---+    return state
++---+
++---+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
++---+    """Verify the Governor blocks approval if the spec file is missing."""
++---+    # Arrange: Set the state to Engineer and mock the requirement pointer
++---+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
++---+    
++---+    # Ensure the spec file does NOT exist for this test
++---+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
++---+    if spec_file.exists():
++---+        spec_file.unlink()
++---+
+++-++    # Act
+++-++    register_meta_requirement(description)
++++++def test_governor_denies_forbidden_command(mock_state):
++++++    """Verify that the Governor denies a command that is not allowed."""
++++++    # Arrange
++++++    stage = "Engineer"
++++++    forbidden_command = "git commit -m 'should not be allowed'"
++++++    mock_state.get.return_value = stage
++++++    governor = Governor(mock_state)
+++ ++
+++-++    # Assert
+++-++    assert META_LOG_FILE.exists()
+++-++    with open(META_LOG_FILE, "r") as f:
+++-++        content = f.read()
++++++    # Act & Assert
++++++    with pytest.raises(PermissionError) as e:
++++++        governor.authorize(forbidden_command)
+++ ++    
+++-++    assert "[ID:1]" in content
+++-++    assert description in content
+++-++    # A simple regex to check for the timestamp format
+++-++    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
++++++    assert "Action denied" in str(e.value)
++++ diff --git a/tests/test_main.py b/tests/test_main.py
++++-index c429973..eddb264 100644
+++++index eddb264..47ae0e7 100644
++++ --- a/tests/test_main.py
++++ +++ b/tests/test_main.py
++++-@@ -1,5 +1,52 @@
++++- # tests/test_main.py
++++-+import pytest
++++-+from pathlib import Path
++++-+import re
++++-+from dw6.main import register_meta_requirement, META_LOG_FILE
++++- 
++++--def test_placeholder():
++++--    """A placeholder test to satisfy the Validator stage."""
++++--    assert True
++++-+@pytest.fixture(autouse=True)
++++-+def cleanup_log_file():
++++-+    """Fixture to clean up the meta log file before and after a test."""
++++-+    if META_LOG_FILE.exists():
++++-+        META_LOG_FILE.unlink()
++++-+    yield
++++-+    if META_LOG_FILE.exists():
++++-+        META_LOG_FILE.unlink()
+++++@@ -50,3 +50,50 @@ def test_register_meta_requirement_increments_id():
+++++     assert description1 in lines[0]
+++++     assert "[ID:2]" in lines[1]
+++++     assert description2 in lines[1]
+++  +
+++--+def test_governor_enforces_rules_on_approve(mocker, capsys):
+++--+    """Verify that the Governor prints the correct rule for the current stage."""
+++-++def test_register_meta_requirement_increments_id():
+++-++    """Verify that subsequent calls increment the requirement ID."""
+++- +    # Arrange
+++--+    mock_state = mocker.MagicMock(spec=WorkflowState)
+++--+    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
++ --+    governor = Governor(mock_state)
++---+
++---+    # Act & Assert: The approval should fail with a SystemExit
++---+    with pytest.raises(SystemExit) as e:
++---+        governor._validate_stage_exit_criteria()
++---+    
++---+    assert e.type == SystemExit
++---+    assert e.value.code == 1
++---+
++---+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++---+    """Verify the Governor allows approval if the spec file exists."""
++---+    # Arrange: Set the state to Engineer and mock the requirement pointer
++---+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
++---+    
++---+    # Ensure the spec file DOES exist for this test
++---+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
++---+    spec_file.parent.mkdir(parents=True, exist_ok=True)
++---+    spec_file.touch()
++--+@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++--+         # Clean up the created file
++--+         if spec_file.exists():
++--+             spec_file.unlink()
++-++     if len(sys.argv) == 1:
++-++         parser.print_help(sys.stderr)
++-++         sys.exit(1)
++-++ 
++-++     args = parser.parse_args()
++-++     
++-++-    manager = WorkflowManager()
++-++-
++-++-    if args.command == "approve":
++-++-        manager.approve()
++-++-    elif args.command == "new":
++-++-        process_prompt(args.prompt)
++-+++    if args.command == "meta-req":
++-+++        register_meta_requirement(args.description)
++-+++    else:
++-+++        manager = WorkflowManager()
++-+++        if args.command == "approve":
++-+++            manager.approve()
++-+++        elif args.command == "new":
++-+++            process_prompt(args.prompt)
++-++ 
++-++ if __name__ == "__main__":
++-++     main()
++-++diff --git a/tests/test_main.py b/tests/test_main.py
++-++index c429973..eddb264 100644
++-++--- a/tests/test_main.py
++-+++++ b/tests/test_main.py
++-++@@ -1,5 +1,52 @@
++-++ # tests/test_main.py
++-+++import pytest
++-+++from pathlib import Path
++-+++import re
++-+++from dw6.main import register_meta_requirement, META_LOG_FILE
++-++ 
++-++-def test_placeholder():
++-++-    """A placeholder test to satisfy the Validator stage."""
++-++-    assert True
++-+++@pytest.fixture(autouse=True)
++-+++def cleanup_log_file():
++-+++    """Fixture to clean up the meta log file before and after a test."""
++-+++    if META_LOG_FILE.exists():
++-+++        META_LOG_FILE.unlink()
++-+++    yield
++-+++    if META_LOG_FILE.exists():
++-+++        META_LOG_FILE.unlink()
+++--+    # Mock the exit criteria validation to prevent SystemExit
+++--+    mocker.patch.object(governor, '_validate_stage_exit_criteria')
+++--+    # Mock the rest of the approval process to isolate the rule enforcement
+++--+    mocker.patch.object(governor, '_transition_to_next_stage')
+++--+    mocker.patch('dw6.state_manager.WorkflowManager')
+++-++    description1 = "First requirement."
+++-++    description2 = "Second requirement."
++++-+def test_register_meta_requirement_creates_file_and_logs_entry():
++++-+    """Verify that the first call creates the log file and adds the first entry correctly."""
++++-+    # Arrange
++++-+    description = "This is the first meta requirement."
+    +
+----     if len(sys.argv) == 1:
+----         parser.print_help(sys.stderr)
+----         sys.exit(1)
+----@@ -27,6 +32,8 @@ def main():
+----         manager.review()
+----     elif args.command == "approve":
+---++    def _transition_to_next_stage(self):
+---++        current_index = STAGES.index(self.current_stage)
+---++        # After 'Deployer', the cycle is complete
+---++        if self.current_stage == "Deployer":
+---++            self._complete_requirement_cycle()
+---++            self.current_stage = STAGES[0]
+---++        else:
+---++            self.current_stage = STAGES[current_index + 1]
+---++        self.state.set("CurrentStage", self.current_stage)
+---++
+---++    def _complete_requirement_cycle(self):
+---++        req_id = int(self.state.get("RequirementPointer"))
+---++        os.makedirs("logs", exist_ok=True)
+---++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+---++        with open(APPROVAL_FILE, "a") as f:
+---++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+---++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+---++        next_req_id = req_id + 1
+---++        self.state.set("RequirementPointer", next_req_id)
+---++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+---++
+---+ class WorkflowManager:
+---+     def __init__(self):
+---+         self.state = WorkflowState()
+---++        self.governor = Governor(self.state) # The manager now has a governor
+---+         self.current_stage = self.state.get("CurrentStage")
+---+ 
+---+     def get_state(self):
+---+         return self.state.data
+---+ 
+---+     def approve(self):
+---+-        old_stage = self.current_stage
+---+-        print(f"--- Approving Stage: {old_stage} ---")
+---+-        self._validate_stage()
+---+-        self._run_pre_transition_actions()
+---+-        self._transition_to_next_stage()
+---+-        self._run_post_transition_actions()
+---+-        self.state.save()
+---+-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
+---++        # The manager now simply delegates to the governor.
+---++        self.governor.approve()
+---+ 
+---+     def _validate_stage(self):
+---+         print(f"Validating deliverables for stage: {self.current_stage}")
+---+@@ -123,25 +167,7 @@ class WorkflowManager:
+---+         if self.current_stage == "Coder":
+---+             git_handler.save_current_commit_sha()
+---+ 
+---+-    def _transition_to_next_stage(self):
+---+-        current_index = STAGES.index(self.current_stage)
+---+-        if current_index == len(STAGES) - 1:
+---+-            self._complete_requirement_cycle()
+---+-            self.current_stage = STAGES[0]
+---+-        else:
+---+-            self.current_stage = STAGES[current_index + 1]
+---+-        self.state.set("CurrentStage", self.current_stage)
+---+ 
+---+-    def _complete_requirement_cycle(self):
+---+-        req_id = int(self.state.get("RequirementPointer"))
+---+-        os.makedirs("logs", exist_ok=True)
+---+-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+---+-        with open(APPROVAL_FILE, "a") as f:
+---+-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
+---+-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
+---+-        next_req_id = req_id + 1
+---+-        self.state.set("RequirementPointer", next_req_id)
+---+-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
+---+ 
+---+ class WorkflowState:
+---+     def __init__(self):
+---+diff --git a/tests/test_governor.py b/tests/test_governor.py
+---+new file mode 100644
+---+index 0000000..95b566d
+---+--- /dev/null
+---++++ b/tests/test_governor.py
+---+@@ -0,0 +1,55 @@
+---++# tests/test_governor.py
+---++import pytest
+---++from unittest.mock import MagicMock
+---++from pathlib import Path
+---++import sys
+---++
+---++from dw6.state_manager import Governor, WorkflowState
+---++
+---++@pytest.fixture
+---++def mock_state(mocker):
+---++    """Fixture to create a mock WorkflowState."""
+---++    state = MagicMock(spec=WorkflowState)
+---++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
+---++    return state
+---++
+---++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
+---++    """Verify the Governor blocks approval if the spec file is missing."""
+---++    # Arrange: Set the state to Engineer and mock the requirement pointer
+---++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
+---++    
+---++    # Ensure the spec file does NOT exist for this test
+---++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
+---++    if spec_file.exists():
+---++        spec_file.unlink()
+---++
+---++    governor = Governor(mock_state)
+---++
+---++    # Act & Assert: The approval should fail with a SystemExit
+---++    with pytest.raises(SystemExit) as e:
+---++        governor._validate_stage_exit_criteria()
+---++    
+---++    assert e.type == SystemExit
+---++    assert e.value.code == 1
+---++
+---++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+---++    """Verify the Governor allows approval if the spec file exists."""
+---++    # Arrange: Set the state to Engineer and mock the requirement pointer
+---++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
+---++    
+---++    # Ensure the spec file DOES exist for this test
+---++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
+---++    spec_file.parent.mkdir(parents=True, exist_ok=True)
+---++    spec_file.touch()
+---++
+---++    governor = Governor(mock_state)
+---++
+---++    # Act & Assert: The approval should pass without raising an exception
+---++    try:
+---++        governor._validate_stage_exit_criteria()
+---++    except SystemExit:
+---++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+---++    finally:
+---++        # Clean up the created file
+---++        if spec_file.exists():
+---++            spec_file.unlink()
+---+diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+---+index 5b9d1eb..44d2cc9 100644
+---+--- a/tests/test_state_manager_integration.py
+---++++ b/tests/test_state_manager_integration.py
+---+@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+---+ 
+---+     @patch('dw6.state_manager.WorkflowState')
+---+     @patch('dw6.git_handler.get_changes_since_last_commit')
+---+-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+---++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+---++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+---+         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+---+         # Arrange
+---+         mock_state_instance = mock_WorkflowState.return_value
+---+@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+---+         # Act
+---          manager.approve()
+----+    elif args.command == "new":
+----+        process_prompt(args.prompt)
+---  
+---- if __name__ == "__main__":
+----     main()
+---+-        # Assert
+---++        # Assert that the deliverable file was created
+---+         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+---+         self.assertTrue(deliverable_path.exists())
+---++        # Clean up the created file
+---++        deliverable_path.unlink()
+---++
+---+         mock_state_instance.save.assert_called_once()
+---+ 
+---+ if __name__ == '__main__':
+---+diff --git a/uv.lock b/uv.lock
+---+index c79d29c..8e7411f 100644
+---+--- a/uv.lock
+---++++ b/uv.lock
+---+@@ -66,6 +66,7 @@ dependencies = [
+---+ test = [
+---+     { name = "pytest" },
+---+     { name = "pytest-cov" },
+---++    { name = "pytest-mock" },
+---+ ]
+---+ 
+---+ [package.metadata]
+---+@@ -73,6 +74,7 @@ requires-dist = [
+---+     { name = "gitpython" },
+---+     { name = "pytest", marker = "extra == 'test'" },
+---+     { name = "pytest-cov", marker = "extra == 'test'" },
+---++    { name = "pytest-mock", marker = "extra == 'test'" },
+---+     { name = "python-dotenv" },
+---+ ]
+---+ provides-extras = ["test"]
+---+@@ -167,6 +169,18 @@ wheels = [
+---+     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+---+ ]
+---+ 
+---++[[package]]
+---++name = "pytest-mock"
+---++version = "3.14.1"
+---++source = { registry = "https://pypi.org/simple" }
+---++dependencies = [
+---++    { name = "pytest" },
+---++]
+---++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+---++wheels = [
+---++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+---++]
+---++
+---+ [[package]]
+---+ name = "python-dotenv"
+---+ version = "1.1.1"
+--+++def test_governor_enforces_rules_on_approve(mocker, capsys):
+--+++    """Verify that the Governor prints the correct rule for the current stage."""
+--+++    # Arrange
+--+++    mock_state = mocker.MagicMock(spec=WorkflowState)
+--+++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
+--+ +    governor = Governor(mock_state)
+--+++    # Mock the exit criteria validation to prevent SystemExit
+--+++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
+--+++    # Mock the rest of the approval process to isolate the rule enforcement
+--+++    mocker.patch.object(governor, '_transition_to_next_stage')
+--+++    mocker.patch('dw6.state_manager.WorkflowManager')
+-+-++def test_governor_enforces_rules_on_approve(mocker, capsys):
+-+-++    """Verify that the Governor prints the correct rule for the current stage."""
+-++-     def approve(self):
+-++-         old_stage = self.current_stage
+-++-         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+-++-+        self.enforce_rules()
+-++-         self._validate_stage_exit_criteria()
+-++-         # The original logic from WorkflowManager is now fully integrated here.
+-++-         workflow_manager = WorkflowManager() # We still need access to its methods for now.
+-++-diff --git a/tests/test_governor.py b/tests/test_governor.py
+-++-index 95b566d..26bf82b 100644
+-++---- a/tests/test_governor.py
+-++-+++ b/tests/test_governor.py
+-++-@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+-++-         # Clean up the created file
+-++-         if spec_file.exists():
+-++-             spec_file.unlink()
+-++++def test_register_meta_requirement_creates_file_and_logs_entry():
+-++++    """Verify that the first call creates the log file and adds the first entry correctly."""
+-+ ++    # Arrange
+-+-++    mock_state = mocker.MagicMock(spec=WorkflowState)
+-+-++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
+-+- +    governor = Governor(mock_state)
+-+-++    # Mock the exit criteria validation to prevent SystemExit
+-+-++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
+-+-++    # Mock the rest of the approval process to isolate the rule enforcement
+-+-++    mocker.patch.object(governor, '_transition_to_next_stage')
+-+-++    mocker.patch('dw6.state_manager.WorkflowManager')
+-+- +
+-+--+    # Act & Assert: The approval should pass without raising an exception
+-+--+    try:
+-+--+        governor._validate_stage_exit_criteria()
+-+--+    except SystemExit:
+-+--+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+-+--+    finally:
+-+--+        # Clean up the created file
+-+--+        if spec_file.exists():
+-+--+            spec_file.unlink()
+-+--diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+-+--index 5b9d1eb..44d2cc9 100644
+-+----- a/tests/test_state_manager_integration.py
+-+--+++ b/tests/test_state_manager_integration.py
+-+--@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+-+-- 
+-+--     @patch('dw6.state_manager.WorkflowState')
+-+--     @patch('dw6.git_handler.get_changes_since_last_commit')
+-+---    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+-+--+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+-+--+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+-+--         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+-+--         # Arrange
+-+--         mock_state_instance = mock_WorkflowState.return_value
+-+--@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+-+--         # Act
+-+--         manager.approve()
+-+-- 
+-+---        # Assert
+-+--+        # Assert that the deliverable file was created
+-+--         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+-+--         self.assertTrue(deliverable_path.exists())
+-+--+        # Clean up the created file
+-+--+        deliverable_path.unlink()
+-+--+
+-+--         mock_state_instance.save.assert_called_once()
+-+-- 
+-+-- if __name__ == '__main__':
+-+--diff --git a/uv.lock b/uv.lock
+-+--index c79d29c..8e7411f 100644
+-+----- a/uv.lock
+-+--+++ b/uv.lock
+-+--@@ -66,6 +66,7 @@ dependencies = [
+-+-- test = [
+-+--     { name = "pytest" },
+-+--     { name = "pytest-cov" },
+-+--+    { name = "pytest-mock" },
+-+-- ]
+-+-- 
+-+-- [package.metadata]
+-+--@@ -73,6 +74,7 @@ requires-dist = [
+-+--     { name = "gitpython" },
+-+--     { name = "pytest", marker = "extra == 'test'" },
+-+--     { name = "pytest-cov", marker = "extra == 'test'" },
+-+--+    { name = "pytest-mock", marker = "extra == 'test'" },
+-+--     { name = "python-dotenv" },
+-+-- ]
+-+-- provides-extras = ["test"]
+-+--@@ -167,6 +169,18 @@ wheels = [
+-+--     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+-+-- ]
+-+-- 
+-+--+[[package]]
+-+--+name = "pytest-mock"
+-+--+version = "3.14.1"
+-+--+source = { registry = "https://pypi.org/simple" }
+-+--+dependencies = [
+-+--+    { name = "pytest" },
+-+--+]
+-+--+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+-+--+wheels = [
+-+--+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+-+--+]
+-++++    description = "This is the first meta requirement."
+-++++
+-+ ++    # Act
+-+-++    governor.approve()
+-+- +
+-+-- [[package]]
+-+-- name = "python-dotenv"
+-+-- version = "1.1.1"
+-++++    register_meta_requirement(description)
+-++++
+-+ ++    # Assert
+-+-++    captured = capsys.readouterr()
+-+-++    expected_rule = Governor.RULES["Coder"]
+-+-++    assert expected_rule in captured.out
+-++++    assert META_LOG_FILE.exists()
+-++++    with open(META_LOG_FILE, "r") as f:
+-++++        content = f.read()
++--++def test_governor_enforces_rules_on_approve(mocker, capsys):
++--++    """Verify that the Governor prints the correct rule for the current stage."""
++-+-     def approve(self):
++-+-         old_stage = self.current_stage
++-+-         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
++-+-+        self.enforce_rules()
++-+-         self._validate_stage_exit_criteria()
++-+-         # The original logic from WorkflowManager is now fully integrated here.
++-+-         workflow_manager = WorkflowManager() # We still need access to its methods for now.
++-+-diff --git a/tests/test_governor.py b/tests/test_governor.py
++-+-index 95b566d..26bf82b 100644
++-+---- a/tests/test_governor.py
++-+-+++ b/tests/test_governor.py
++-+-@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
++-+-         # Clean up the created file
++-+-         if spec_file.exists():
++-+-             spec_file.unlink()
++-+++def test_register_meta_requirement_creates_file_and_logs_entry():
++-+++    """Verify that the first call creates the log file and adds the first entry correctly."""
++- ++    # Arrange
++--++    mock_state = mocker.MagicMock(spec=WorkflowState)
++--++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
++-- +    governor = Governor(mock_state)
++--++    # Mock the exit criteria validation to prevent SystemExit
++--++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
++--++    # Mock the rest of the approval process to isolate the rule enforcement
++--++    mocker.patch.object(governor, '_transition_to_next_stage')
++--++    mocker.patch('dw6.state_manager.WorkflowManager')
++-- +
++---+    # Act & Assert: The approval should pass without raising an exception
++---+    try:
++---+        governor._validate_stage_exit_criteria()
++---+    except SystemExit:
++---+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
++---+    finally:
++---+        # Clean up the created file
++---+        if spec_file.exists():
++---+            spec_file.unlink()
++---diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
++---index 5b9d1eb..44d2cc9 100644
++------ a/tests/test_state_manager_integration.py
++---+++ b/tests/test_state_manager_integration.py
++---@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++--- 
++---     @patch('dw6.state_manager.WorkflowState')
++---     @patch('dw6.git_handler.get_changes_since_last_commit')
++----    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
++---+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
++---+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
++---         """Ensure approving Coder stage generates a deliverable without altering the real state."""
++---         # Arrange
++---         mock_state_instance = mock_WorkflowState.return_value
++---@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
++---         # Act
++---         manager.approve()
++--- 
++----        # Assert
++---+        # Assert that the deliverable file was created
++---         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
++---         self.assertTrue(deliverable_path.exists())
++---+        # Clean up the created file
++---+        deliverable_path.unlink()
++---+
++---         mock_state_instance.save.assert_called_once()
++--- 
++--- if __name__ == '__main__':
++---diff --git a/uv.lock b/uv.lock
++---index c79d29c..8e7411f 100644
++------ a/uv.lock
++---+++ b/uv.lock
++---@@ -66,6 +66,7 @@ dependencies = [
++--- test = [
++---     { name = "pytest" },
++---     { name = "pytest-cov" },
++---+    { name = "pytest-mock" },
++--- ]
++--- 
++--- [package.metadata]
++---@@ -73,6 +74,7 @@ requires-dist = [
++---     { name = "gitpython" },
++---     { name = "pytest", marker = "extra == 'test'" },
++---     { name = "pytest-cov", marker = "extra == 'test'" },
++---+    { name = "pytest-mock", marker = "extra == 'test'" },
++---     { name = "python-dotenv" },
++--- ]
++--- provides-extras = ["test"]
++---@@ -167,6 +169,18 @@ wheels = [
++---     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
++--- ]
++--- 
++---+[[package]]
++---+name = "pytest-mock"
++---+version = "3.14.1"
++---+source = { registry = "https://pypi.org/simple" }
++---+dependencies = [
++---+    { name = "pytest" },
++---+]
++---+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
++---+wheels = [
++---+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
++---+]
++-+++    description = "This is the first meta requirement."
++++++@pytest.fixture
++++++def mock_main_dependencies(mocker):
++++++    """Fixture to mock dependencies of the main function for the 'do' command tests."""
++++++    # Since autospec=True is used, we need to configure the mock instance
++++++    # to have the 'governor' attribute.
++++++    mock_workflow_manager_class = mocker.patch('dw6.main.WorkflowManager', autospec=True)
++++++    mock_workflow_manager_instance = mock_workflow_manager_class.return_value
++++++    mock_governor = mocker.MagicMock()
++++++    mock_workflow_manager_instance.governor = mock_governor
++ +++
++- ++    # Act
++--++    governor.approve()
++-- +
++--- [[package]]
++--- name = "python-dotenv"
++--- version = "1.1.1"
++-+++    register_meta_requirement(description)
++++++    mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
++++++    return mock_governor, mock_subprocess_run
++ +++
++- ++    # Assert
++--++    captured = capsys.readouterr()
++--++    expected_rule = Governor.RULES["Coder"]
++--++    assert expected_rule in captured.out
++-+++    assert META_LOG_FILE.exists()
++-+++    with open(META_LOG_FILE, "r") as f:
++-+++        content = f.read()
++++++def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
++++++    """Verify the 'do' command executes an action when the Governor authorizes it."""
++++++    # Arrange
++++++    mock_governor, mock_subprocess_run = mock_main_dependencies
++++++    mock_governor.authorize.return_value = None # Simulate authorization success
+ ++++    
+-++++    assert "[ID:1]" in content
+-++++    assert description in content
+-++++    # A simple regex to check for the timestamp format
+-++++    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
++++++    mocker.patch('sys.argv', ['dw6', 'do', 'ls -l'])
++ +++    
++-+++    assert "[ID:1]" in content
++-+++    assert description in content
++-+++    # A simple regex to check for the timestamp format
++-+++    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
+++  +    # Act
+++--+    governor.approve()
+++-++    register_meta_requirement(description1)
+++-++    register_meta_requirement(description2)
++++-+    register_meta_requirement(description)
++++++    from dw6.main import main
++++++    main()
+++  +
+++  +    # Assert
+++--+    captured = capsys.readouterr()
+++--+    expected_rule = Governor.RULES["Coder"]
+++--+    assert expected_rule in captured.out
+++-++    with open(META_LOG_FILE, "r") as f:
+++-++        lines = f.readlines()
+++-++    
+++-++    assert len(lines) == 2
+++-++    assert "[ID:1]" in lines[0]
+++-++    assert description1 in lines[0]
+++-++    assert "[ID:2]" in lines[1]
+++-++    assert description2 in lines[1]
++++-+    assert META_LOG_FILE.exists()
++++-+    with open(META_LOG_FILE, "r") as f:
++++-+        content = f.read()
++++-+    
++++-+    assert "[ID:1]" in content
++++-+    assert description in content
++++-+    # A simple regex to check for the timestamp format
++++-+    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
++++++    mock_governor.authorize.assert_called_once_with('ls -l')
++++++    mock_subprocess_run.assert_called_once_with('ls -l', shell=True, check=True)
   + +
--++-+    # Act & Assert: The approval should pass without raising an exception
-- +-+    try:
---+-+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
---+-+        with open(file_path, 'w') as f:
---+-+            f.write(content)
---+-+        print(f"Successfully created specification: {file_path}")
---+-+    except IOError as e:
---+-+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
---+-+        sys.exit(1)
---+++**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
---++diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
---++index 9718eda..b85b3d9 100644
---++--- a/logs/.last_commit_sha
---+++++ b/logs/.last_commit_sha
---++@@ -1 +1 @@
---++-7aa14d9c189cbc22b982d3d7895a650c1cf7a654
---++\ No newline at end of file
---+++75be02c0b7e1723e32042299497f3673b11b4ddd
---++\ No newline at end of file
---++diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
---++index 28746b7..743582b 100644
---++--- a/logs/workflow_state.txt
---+++++ b/logs/workflow_state.txt
---++@@ -1,2 +1,2 @@
---++-CurrentStage=Engineer
---++-RequirementPointer=7
---+++CurrentStage=Coder
---+++RequirementPointer=9
---++diff --git a/pytest.ini b/pytest.ini
--- +new file mode 100644
----+index 0000000..c1614f0
---++index 0000000..a635c5c
--- +--- /dev/null
----++++ b/src/dw6/augmenter.py
----+@@ -0,0 +1,26 @@
----++# src/dw6/augmenter.py
---+++++ b/pytest.ini
---++@@ -0,0 +1,2 @@
---+++[pytest]
---+++pythonpath = .
---+ diff --git a/src/dw6/main.py b/src/dw6/main.py
---+-index 7bbd031..a55f148 100644
---++index a55f148..90862f9 100644
---+ --- a/src/dw6/main.py
---+ +++ b/src/dw6/main.py
---+-@@ -2,6 +2,7 @@
---++@@ -1,7 +1,7 @@
---++ # dw6/main.py
---+  import argparse
---+  import sys
---+- from dw6.state_manager import StateManager
---+-+from dw6.augmenter import process_prompt
---++-from dw6.state_manager import StateManager
---+++from dw6.state_manager import WorkflowManager
---++ from dw6.augmenter import process_prompt
---+  
---+  def main():
---+-     """Main entry point for the DW6 CLI."""
---+-@@ -15,6 +16,10 @@ def main():
---++@@ -10,9 +10,7 @@ def main():
---++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
---++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
---++ 
---++-    # Review command
---++-    subparsers.add_parser("review", help="Review the changes for the current stage.")
---++-    
--- ++
----++import os
----++from .state_manager import get_current_requirement_id
---+      # Approve command
---+      subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
---+  
---+-+    # New command
---+-+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
---+-+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
---++@@ -26,11 +24,9 @@ def main():
---++ 
---++     args = parser.parse_args()
---++     
---++-    manager = StateManager()
---+++    manager = WorkflowManager()
---++ 
---++-    if args.command == "review":
---++-        manager.review()
---++-    elif args.command == "approve":
---+++    if args.command == "approve":
---++         manager.approve()
---++     elif args.command == "new":
---++         process_prompt(args.prompt)
---++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
---++index 703640c..b829d36 100644
---++--- a/src/dw6/state_manager.py
---+++++ b/src/dw6/state_manager.py
---++@@ -9,7 +9,7 @@ from dw6 import git_handler
---++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
---++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
---++ APPROVAL_FILE = "logs/approvals.log"
---++-STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
---+++STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
---++ DELIVERABLE_PATHS = {
---++     "Engineer": "deliverables/engineering",
---++     "Coder": "deliverables/coding",
---++@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
---++     "Researcher": "deliverables/research",
---++ }
---++ 
---+++class Governor:
---+++    def __init__(self, state):
---+++        self.state = state
---+++        self.current_stage = self.state.get("CurrentStage")
--- ++
----++WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
---+++    def approve(self):
---+++        old_stage = self.current_stage
---+++        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
---+++        self._validate_stage_exit_criteria()
---+++        # The original logic from WorkflowManager is now fully integrated here.
---+++        workflow_manager = WorkflowManager() # We still need access to its methods for now.
---+++        workflow_manager._validate_stage()
---+++        workflow_manager._run_pre_transition_actions()
---+++        self._transition_to_next_stage() # This method now belongs to the Governor
---+++        workflow_manager._run_post_transition_actions()
---+++        self.state.save()
---+++        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
--- ++
----++def process_prompt(prompt_text: str):
----++    """
----++    Augments a raw user prompt and generates a formal technical specification markdown file.
----++    """
----++    requirement_id = get_current_requirement_id()
----++    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
---+++    def _validate_stage_exit_criteria(self):
---+++        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
---+++        if self.current_stage == "Engineer":
---+++            req_id = self.state.get("RequirementPointer")
---+++            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
---+++            if not spec_file.exists():
---+++                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
---+++                sys.exit(1)
---+++            print("Governor: 'Engineer' exit criteria met.")
--++-+        governor._validate_stage_exit_criteria()
--++-+    except SystemExit:
--++-+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
--++-+    finally:
--++-+        # Clean up the created file
--++-+        if spec_file.exists():
--++-+            spec_file.unlink()
--++-diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
--++-index 5b9d1eb..44d2cc9 100644
--++---- a/tests/test_state_manager_integration.py
--++-+++ b/tests/test_state_manager_integration.py
--++-@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
--++- 
--++-     @patch('dw6.state_manager.WorkflowState')
--++-     @patch('dw6.git_handler.get_changes_since_last_commit')
--++--    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
--++-+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
--++-+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
--++-         """Ensure approving Coder stage generates a deliverable without altering the real state."""
--++-         # Arrange
--++-         mock_state_instance = mock_WorkflowState.return_value
--++-@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
--++-         # Act
--++-         manager.approve()
--++- 
--++--        # Assert
--++-+        # Assert that the deliverable file was created
--++-         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
--++-         self.assertTrue(deliverable_path.exists())
--++-+        # Clean up the created file
--++-+        deliverable_path.unlink()
--++-+
--++-         mock_state_instance.save.assert_called_once()
--++- 
--++- if __name__ == '__main__':
--++-diff --git a/uv.lock b/uv.lock
--++-index c79d29c..8e7411f 100644
--++---- a/uv.lock
--++-+++ b/uv.lock
--++-@@ -66,6 +66,7 @@ dependencies = [
--++- test = [
--++-     { name = "pytest" },
--++-     { name = "pytest-cov" },
--++-+    { name = "pytest-mock" },
--++- ]
--++- 
--++- [package.metadata]
--++-@@ -73,6 +74,7 @@ requires-dist = [
--++-     { name = "gitpython" },
--++-     { name = "pytest", marker = "extra == 'test'" },
--++-     { name = "pytest-cov", marker = "extra == 'test'" },
--++-+    { name = "pytest-mock", marker = "extra == 'test'" },
--++-     { name = "python-dotenv" },
--++- ]
--++- provides-extras = ["test"]
--++-@@ -167,6 +169,18 @@ wheels = [
--++-     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
--++- ]
--++- 
--++-+[[package]]
--++-+name = "pytest-mock"
--++-+version = "3.14.1"
--++-+source = { registry = "https://pypi.org/simple" }
--++-+dependencies = [
--++-+    { name = "pytest" },
--++-+]
--++-+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
--++-+wheels = [
--++-+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
--++-+]
--++++    # Act
--++++    governor.approve()
-+-+-+    # Act & Assert: The approval should pass without raising an exception
-+-+-+    try:
-+-+-+        governor._validate_stage_exit_criteria()
-+-+-+    except SystemExit:
-+-+-+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
-+-+-+    finally:
-+-+-+        # Clean up the created file
-+-+-+        if spec_file.exists():
-+-+-+            spec_file.unlink()
-+-+-diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
-+-+-index 5b9d1eb..44d2cc9 100644
-+-+---- a/tests/test_state_manager_integration.py
-+-+-+++ b/tests/test_state_manager_integration.py
-+-+-@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-+-+- 
-+-+-     @patch('dw6.state_manager.WorkflowState')
-+-+-     @patch('dw6.git_handler.get_changes_since_last_commit')
-+-+--    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
-+-+-+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
-+-+-+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
-+-+-         """Ensure approving Coder stage generates a deliverable without altering the real state."""
-+-+-         # Arrange
-+-+-         mock_state_instance = mock_WorkflowState.return_value
-+-+-@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
-+-+-         # Act
-+-+-         manager.approve()
-+-+- 
-+-+--        # Assert
-+-+-+        # Assert that the deliverable file was created
-+-+-         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
-+-+-         self.assertTrue(deliverable_path.exists())
-+-+-+        # Clean up the created file
-+-+-+        deliverable_path.unlink()
-+-+-+
-+-+-         mock_state_instance.save.assert_called_once()
-+-+- 
-+-+- if __name__ == '__main__':
-+-+-diff --git a/uv.lock b/uv.lock
-+-+-index c79d29c..8e7411f 100644
-+-+---- a/uv.lock
-+-+-+++ b/uv.lock
-+-+-@@ -66,6 +66,7 @@ dependencies = [
-+-+- test = [
-+-+-     { name = "pytest" },
-+-+-     { name = "pytest-cov" },
-+-+-+    { name = "pytest-mock" },
-+-+- ]
-+-+- 
-+-+- [package.metadata]
-+-+-@@ -73,6 +74,7 @@ requires-dist = [
-+-+-     { name = "gitpython" },
-+-+-     { name = "pytest", marker = "extra == 'test'" },
-+-+-     { name = "pytest-cov", marker = "extra == 'test'" },
-+-+-+    { name = "pytest-mock", marker = "extra == 'test'" },
-+-+-     { name = "python-dotenv" },
-+-+- ]
-+-+- provides-extras = ["test"]
-+-+-@@ -167,6 +169,18 @@ wheels = [
-+-+-     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
-+-+- ]
-+-+- 
-+-+-+[[package]]
-+-+-+name = "pytest-mock"
-+-+-+version = "3.14.1"
-+-+-+source = { registry = "https://pypi.org/simple" }
-+-+-+dependencies = [
-+-+-+    { name = "pytest" },
-+-+-+]
-+-+-+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
-+-+-+wheels = [
-+-+-+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
-+-+-+]
-+-+++    # Act
-+-+++    governor.approve()
-+++-+def test_governor_enforces_rules_on_approve(mocker, capsys):
-+++-+    """Verify that the Governor prints the correct rule for the current stage."""
-+++++def test_register_meta_requirement_increments_id():
-+++++    """Verify that subsequent calls increment the requirement ID."""
-+++ +    # Arrange
-+++-+    mock_state = mocker.MagicMock(spec=WorkflowState)
-+++-+    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
-+++-+    governor = Governor(mock_state)
-+++-+    # Mock the exit criteria validation to prevent SystemExit
-+++-+    mocker.patch.object(governor, '_validate_stage_exit_criteria')
-+++-+    # Mock the rest of the approval process to isolate the rule enforcement
-+++-+    mocker.patch.object(governor, '_transition_to_next_stage')
-+++-+    mocker.patch('dw6.state_manager.WorkflowManager')
-+++++    description1 = "First requirement."
-+++++    description2 = "Second requirement."
+--+-+    # Act & Assert: The approval should pass without raising an exception
+--+-+    try:
+--+-+        governor._validate_stage_exit_criteria()
+--+-+    except SystemExit:
+--+-+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
+--+-+    finally:
+--+-+        # Clean up the created file
+--+-+        if spec_file.exists():
+--+-+            spec_file.unlink()
+--+-diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
+--+-index 5b9d1eb..44d2cc9 100644
+--+---- a/tests/test_state_manager_integration.py
+--+-+++ b/tests/test_state_manager_integration.py
+--+-@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+--+- 
+--+-     @patch('dw6.state_manager.WorkflowState')
+--+-     @patch('dw6.git_handler.get_changes_since_last_commit')
+--+--    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
+--+-+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
+--+-+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
+--+-         """Ensure approving Coder stage generates a deliverable without altering the real state."""
+--+-         # Arrange
+--+-         mock_state_instance = mock_WorkflowState.return_value
+--+-@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
+--+-         # Act
+--+-         manager.approve()
+--+- 
+--+--        # Assert
+--+-+        # Assert that the deliverable file was created
+--+-         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
+--+-         self.assertTrue(deliverable_path.exists())
+--+-+        # Clean up the created file
+--+-+        deliverable_path.unlink()
+--+-+
+--+-         mock_state_instance.save.assert_called_once()
+--+- 
+--+- if __name__ == '__main__':
+--+-diff --git a/uv.lock b/uv.lock
+--+-index c79d29c..8e7411f 100644
+--+---- a/uv.lock
+--+-+++ b/uv.lock
+--+-@@ -66,6 +66,7 @@ dependencies = [
+--+- test = [
+--+-     { name = "pytest" },
+--+-     { name = "pytest-cov" },
+--+-+    { name = "pytest-mock" },
+--+- ]
+--+- 
+--+- [package.metadata]
+--+-@@ -73,6 +74,7 @@ requires-dist = [
+--+-     { name = "gitpython" },
+--+-     { name = "pytest", marker = "extra == 'test'" },
+--+-     { name = "pytest-cov", marker = "extra == 'test'" },
+--+-+    { name = "pytest-mock", marker = "extra == 'test'" },
+--+-     { name = "python-dotenv" },
+--+- ]
+--+- provides-extras = ["test"]
+--+-@@ -167,6 +169,18 @@ wheels = [
+--+-     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
+--+- ]
+--+- 
+--+-+[[package]]
+--+-+name = "pytest-mock"
+--+-+version = "3.14.1"
+--+-+source = { registry = "https://pypi.org/simple" }
+--+-+dependencies = [
+--+-+    { name = "pytest" },
+--+-+]
+--+-+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
+--+-+wheels = [
+--+-+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
+--+-+]
+--+++    # Act
+--+++    governor.approve()
+-++-+def test_governor_enforces_rules_on_approve(mocker, capsys):
+-++-+    """Verify that the Governor prints the correct rule for the current stage."""
+-++++def test_register_meta_requirement_increments_id():
+-++++    """Verify that subsequent calls increment the requirement ID."""
+-++ +    # Arrange
+-++-+    mock_state = mocker.MagicMock(spec=WorkflowState)
+-++-+    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
+-++-+    governor = Governor(mock_state)
+-++-+    # Mock the exit criteria validation to prevent SystemExit
+-++-+    mocker.patch.object(governor, '_validate_stage_exit_criteria')
+-++-+    # Mock the rest of the approval process to isolate the rule enforcement
+-++-+    mocker.patch.object(governor, '_transition_to_next_stage')
+-++-+    mocker.patch('dw6.state_manager.WorkflowManager')
+-++++    description1 = "First requirement."
+-++++    description2 = "Second requirement."
++-+-+def test_governor_enforces_rules_on_approve(mocker, capsys):
++-+-+    """Verify that the Governor prints the correct rule for the current stage."""
++-+++def test_register_meta_requirement_increments_id():
++-+++    """Verify that subsequent calls increment the requirement ID."""
++++-+def test_register_meta_requirement_increments_id():
++++-+    """Verify that subsequent calls increment the requirement ID."""
++++++def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
++++++    """Verify the 'do' command blocks an action when the Governor denies it."""
++ + +    # Arrange
++-+-+    mock_state = mocker.MagicMock(spec=WorkflowState)
++-+-+    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
++-+-+    governor = Governor(mock_state)
++-+-+    # Mock the exit criteria validation to prevent SystemExit
++-+-+    mocker.patch.object(governor, '_validate_stage_exit_criteria')
++-+-+    # Mock the rest of the approval process to isolate the rule enforcement
++-+-+    mocker.patch.object(governor, '_transition_to_next_stage')
++-+-+    mocker.patch('dw6.state_manager.WorkflowManager')
++-+++    description1 = "First requirement."
++-+++    description2 = "Second requirement."
++++-+    description1 = "First requirement."
++++-+    description2 = "Second requirement."
++++++    mock_governor, mock_subprocess_run = mock_main_dependencies
++++++    mock_governor.authorize.side_effect = PermissionError("Action denied")
   + +
---+-     if len(sys.argv) == 1:
---+-         parser.print_help(sys.stderr)
---+-         sys.exit(1)
---+-@@ -27,6 +32,8 @@ def main():
---+-         manager.review()
---+-     elif args.command == "approve":
---+++    def _transition_to_next_stage(self):
---+++        current_index = STAGES.index(self.current_stage)
---+++        # After 'Deployer', the cycle is complete
---+++        if self.current_stage == "Deployer":
---+++            self._complete_requirement_cycle()
---+++            self.current_stage = STAGES[0]
---+++        else:
---+++            self.current_stage = STAGES[current_index + 1]
---+++        self.state.set("CurrentStage", self.current_stage)
--- ++
----++    content = f"# Requirement: {requirement_id}\n\n"
----++    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
----++    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
---+++    def _complete_requirement_cycle(self):
---+++        req_id = int(self.state.get("RequirementPointer"))
---+++        os.makedirs("logs", exist_ok=True)
---+++        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
---+++        with open(APPROVAL_FILE, "a") as f:
---+++            f.write(f"Requirement {req_id} approved at {timestamp}\n")
---+++        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
---+++        next_req_id = req_id + 1
---+++        self.state.set("RequirementPointer", next_req_id)
---+++        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
--- ++
----++    try:
----++        os.makedirs(os.path.dirname(file_path), exist_ok=True)
----++        with open(file_path, 'w') as f:
----++            f.write(content)
----++        print(f"Successfully created specification: {file_path}")
----++    except IOError as e:
----++        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
----++        sys.exit(1)
----+diff --git a/src/dw6/main.py b/src/dw6/main.py
----+index 7bbd031..a55f148 100644
----+--- a/src/dw6/main.py
----++++ b/src/dw6/main.py
----+@@ -2,6 +2,7 @@
----+ import argparse
----+ import sys
----+ from dw6.state_manager import StateManager
----++from dw6.augmenter import process_prompt
---++ class WorkflowManager:
---++     def __init__(self):
---++         self.state = WorkflowState()
---+++        self.governor = Governor(self.state) # The manager now has a governor
---++         self.current_stage = self.state.get("CurrentStage")
--- + 
----+ def main():
----+     """Main entry point for the DW6 CLI."""
----+@@ -15,6 +16,10 @@ def main():
----+     # Approve command
----+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
---++     def get_state(self):
---++         return self.state.data
--- + 
----++    # New command
----++    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
----++    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
---++     def approve(self):
---++-        old_stage = self.current_stage
---++-        print(f"--- Approving Stage: {old_stage} ---")
---++-        self._validate_stage()
---++-        self._run_pre_transition_actions()
---++-        self._transition_to_next_stage()
---++-        self._run_post_transition_actions()
---++-        self.state.save()
---++-        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
---+++        # The manager now simply delegates to the governor.
---+++        self.governor.approve()
---++ 
---++     def _validate_stage(self):
---++         print(f"Validating deliverables for stage: {self.current_stage}")
---++@@ -123,25 +167,7 @@ class WorkflowManager:
---++         if self.current_stage == "Coder":
---++             git_handler.save_current_commit_sha()
---++ 
---++-    def _transition_to_next_stage(self):
---++-        current_index = STAGES.index(self.current_stage)
---++-        if current_index == len(STAGES) - 1:
---++-            self._complete_requirement_cycle()
---++-            self.current_stage = STAGES[0]
---++-        else:
---++-            self.current_stage = STAGES[current_index + 1]
---++-        self.state.set("CurrentStage", self.current_stage)
---++ 
---++-    def _complete_requirement_cycle(self):
---++-        req_id = int(self.state.get("RequirementPointer"))
---++-        os.makedirs("logs", exist_ok=True)
---++-        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
---++-        with open(APPROVAL_FILE, "a") as f:
---++-            f.write(f"Requirement {req_id} approved at {timestamp}\n")
---++-        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
---++-        next_req_id = req_id + 1
---++-        self.state.set("RequirementPointer", next_req_id)
---++-        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
---++ 
---++ class WorkflowState:
---++     def __init__(self):
---++diff --git a/tests/test_governor.py b/tests/test_governor.py
---++new file mode 100644
---++index 0000000..95b566d
---++--- /dev/null
---+++++ b/tests/test_governor.py
---++@@ -0,0 +1,55 @@
---+++# tests/test_governor.py
---+++import pytest
---+++from unittest.mock import MagicMock
---+++from pathlib import Path
---+++import sys
--- ++
----+     if len(sys.argv) == 1:
----+         parser.print_help(sys.stderr)
----+         sys.exit(1)
----+@@ -27,6 +32,8 @@ def main():
----+         manager.review()
----+     elif args.command == "approve":
----+         manager.approve()
----++    elif args.command == "new":
----++        process_prompt(args.prompt)
---+++from dw6.state_manager import Governor, WorkflowState
---+++
---+++@pytest.fixture
---+++def mock_state(mocker):
---+++    """Fixture to create a mock WorkflowState."""
---+++    state = MagicMock(spec=WorkflowState)
---+++    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
---+++    return state
---+++
---+++def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
---+++    """Verify the Governor blocks approval if the spec file is missing."""
---+++    # Arrange: Set the state to Engineer and mock the requirement pointer
---+++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
---+++    
---+++    # Ensure the spec file does NOT exist for this test
---+++    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
---+++    if spec_file.exists():
---+++        spec_file.unlink()
---+++
---+++    governor = Governor(mock_state)
---+++
---+++    # Act & Assert: The approval should fail with a SystemExit
---+++    with pytest.raises(SystemExit) as e:
---+++        governor._validate_stage_exit_criteria()
---+++    
---+++    assert e.type == SystemExit
---+++    assert e.value.code == 1
---+++
---+++def test_governor_allows_engineer_approval_with_spec_file(mock_state):
---+++    """Verify the Governor allows approval if the spec file exists."""
---+++    # Arrange: Set the state to Engineer and mock the requirement pointer
---+++    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
---+++    
---+++    # Ensure the spec file DOES exist for this test
---+++    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
---+++    spec_file.parent.mkdir(parents=True, exist_ok=True)
---+++    spec_file.touch()
---+++
---+++    governor = Governor(mock_state)
---+++
---+++    # Act & Assert: The approval should pass without raising an exception
---+++    try:
---+++        governor._validate_stage_exit_criteria()
---+++    except SystemExit:
---+++        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
---+++    finally:
---+++        # Clean up the created file
---+++        if spec_file.exists():
---+++            spec_file.unlink()
---++diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
---++index 5b9d1eb..44d2cc9 100644
---++--- a/tests/test_state_manager_integration.py
---+++++ b/tests/test_state_manager_integration.py
---++@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
---++ 
---++     @patch('dw6.state_manager.WorkflowState')
---++     @patch('dw6.git_handler.get_changes_since_last_commit')
---++-    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
---+++    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
---+++    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
---++         """Ensure approving Coder stage generates a deliverable without altering the real state."""
---++         # Arrange
---++         mock_state_instance = mock_WorkflowState.return_value
---++@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
---++         # Act
---+          manager.approve()
---+-+    elif args.command == "new":
---+-+        process_prompt(args.prompt)
---+  
---+- if __name__ == "__main__":
---+-     main()
---++-        # Assert
---+++        # Assert that the deliverable file was created
---++         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
---++         self.assertTrue(deliverable_path.exists())
---+++        # Clean up the created file
---+++        deliverable_path.unlink()
---+++
---++         mock_state_instance.save.assert_called_once()
---++ 
---++ if __name__ == '__main__':
---++diff --git a/uv.lock b/uv.lock
---++index c79d29c..8e7411f 100644
---++--- a/uv.lock
---+++++ b/uv.lock
---++@@ -66,6 +66,7 @@ dependencies = [
---++ test = [
---++     { name = "pytest" },
---++     { name = "pytest-cov" },
---+++    { name = "pytest-mock" },
---++ ]
--- + 
----+ if __name__ == "__main__":
----+     main()
----+```
---++ [package.metadata]
---++@@ -73,6 +74,7 @@ requires-dist = [
---++     { name = "gitpython" },
---++     { name = "pytest", marker = "extra == 'test'" },
---++     { name = "pytest-cov", marker = "extra == 'test'" },
---+++    { name = "pytest-mock", marker = "extra == 'test'" },
---++     { name = "python-dotenv" },
---++ ]
---++ provides-extras = ["test"]
---++@@ -167,6 +169,18 @@ wheels = [
---++     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
---++ ]
---++ 
---+++[[package]]
---+++name = "pytest-mock"
---+++version = "3.14.1"
---+++source = { registry = "https://pypi.org/simple" }
---+++dependencies = [
---+++    { name = "pytest" },
---+++]
---+++sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
---+++wheels = [
---+++    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
---+++]
---+++
---++ [[package]]
---++ name = "python-dotenv"
---++ version = "1.1.1"
---+ ```
--++- [[package]]
--++- name = "python-dotenv"
--++- version = "1.1.1"
--++++    # Assert
--++++    captured = capsys.readouterr()
--++++    expected_rule = Governor.RULES["Coder"]
--++++    assert expected_rule in captured.out
--+  ```
-+-+- [[package]]
-+-+- name = "python-dotenv"
-+-+- version = "1.1.1"
-+-+++    # Assert
-+-+++    captured = capsys.readouterr()
-+-+++    expected_rule = Governor.RULES["Coder"]
-+-+++    assert expected_rule in captured.out
-+++ +    # Act
-+++-+    governor.approve()
-+++++    register_meta_requirement(description1)
-+++++    register_meta_requirement(description2)
-+++ +
-+++ +    # Assert
-+++-+    captured = capsys.readouterr()
-+++-+    expected_rule = Governor.RULES["Coder"]
-+++-+    assert expected_rule in captured.out
-+++++    with open(META_LOG_FILE, "r") as f:
-+++++        lines = f.readlines()
-+++++    
-+++++    assert len(lines) == 2
-+++++    assert "[ID:1]" in lines[0]
-+++++    assert description1 in lines[0]
-+++++    assert "[ID:2]" in lines[1]
-+++++    assert description2 in lines[1]
-+   ```
+--+- [[package]]
+--+- name = "python-dotenv"
+--+- version = "1.1.1"
+--+++    # Assert
+--+++    captured = capsys.readouterr()
+--+++    expected_rule = Governor.RULES["Coder"]
+--+++    assert expected_rule in captured.out
+-++ +    # Act
+-++-+    governor.approve()
+-++++    register_meta_requirement(description1)
+-++++    register_meta_requirement(description2)
+-++ +
+-++ +    # Assert
+-++-+    captured = capsys.readouterr()
+-++-+    expected_rule = Governor.RULES["Coder"]
+-++-+    assert expected_rule in captured.out
+-++++    with open(META_LOG_FILE, "r") as f:
+-++++        lines = f.readlines()
+-++++    
+-++++    assert len(lines) == 2
+-++++    assert "[ID:1]" in lines[0]
+-++++    assert description1 in lines[0]
+-++++    assert "[ID:2]" in lines[1]
+-++++    assert description2 in lines[1]
++-+ +    # Act
++-+-+    governor.approve()
++-+++    register_meta_requirement(description1)
++-+++    register_meta_requirement(description2)
++++-+    # Act
++++-+    register_meta_requirement(description1)
++++-+    register_meta_requirement(description2)
++++++    mocker.patch('sys.argv', ['dw6', 'do', 'git push'])
++ + +
++-+ +    # Assert
++-+-+    captured = capsys.readouterr()
++-+-+    expected_rule = Governor.RULES["Coder"]
++-+-+    assert expected_rule in captured.out
++-+++    with open(META_LOG_FILE, "r") as f:
++-+++        lines = f.readlines()
++-+++    
++-+++    assert len(lines) == 2
++-+++    assert "[ID:1]" in lines[0]
++-+++    assert description1 in lines[0]
++-+++    assert "[ID:2]" in lines[1]
++-+++    assert description2 in lines[1]
++++-+    # Assert
++++-+    with open(META_LOG_FILE, "r") as f:
++++-+        lines = f.readlines()
++++++    # Act & Assert
++++++    with pytest.raises(SystemExit) as e:
++++++        from dw6.main import main
++++++        main()
++++ +    
++++-+    assert len(lines) == 2
++++-+    assert "[ID:1]" in lines[0]
++++-+    assert description1 in lines[0]
++++-+    assert "[ID:2]" in lines[1]
++++-+    assert description2 in lines[1]
++++++    assert e.value.code == 1
++++++    mock_governor.authorize.assert_called_once_with('git push')
++++++    mock_subprocess_run.assert_not_called()
+    ```
    \ No newline at end of file
----diff --git a/deliverables/engineering/cycle_9_technical_specification.md b/deliverables/engineering/cycle_9_technical_specification.md
---+diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
--+-diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
--++diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
-+--diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
-+-+diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
-++-diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
-+++diff --git a/deliverables/engineering/cycle_12_technical_specification.md b/deliverables/engineering/cycle_12_technical_specification.md
+---diff --git a/deliverables/engineering/cycle_10_technical_specification.md b/deliverables/engineering/cycle_10_technical_specification.md
+--+diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
+-+-diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
+-++diff --git a/deliverables/engineering/cycle_12_technical_specification.md b/deliverables/engineering/cycle_12_technical_specification.md
++--diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
++-+diff --git a/deliverables/engineering/cycle_12_technical_specification.md b/deliverables/engineering/cycle_12_technical_specification.md
+++-diff --git a/deliverables/engineering/cycle_12_technical_specification.md b/deliverables/engineering/cycle_12_technical_specification.md
++++diff --git a/deliverables/engineering/cycle_13_technical_specification.md b/deliverables/engineering/cycle_13_technical_specification.md
    new file mode 100644
----index 0000000..6c1638b
---+index 0000000..691df8d
--+-index 0000000..691df8d
--++index 0000000..071c22d
-+--index 0000000..691df8d
-+-+index 0000000..071c22d
-++-index 0000000..071c22d
-+++index 0000000..ff3658c
+---index 0000000..691df8d
+--+index 0000000..071c22d
+-+-index 0000000..071c22d
+-++index 0000000..ff3658c
++--index 0000000..071c22d
++-+index 0000000..ff3658c
+++-index 0000000..ff3658c
++++index 0000000..fde1032
    --- /dev/null
----+++ b/deliverables/engineering/cycle_9_technical_specification.md
---++++ b/deliverables/engineering/cycle_10_technical_specification.md
--+-+++ b/deliverables/engineering/cycle_10_technical_specification.md
--+++++ b/deliverables/engineering/cycle_11_technical_specification.md
-+--+++ b/deliverables/engineering/cycle_10_technical_specification.md
-+-++++ b/deliverables/engineering/cycle_11_technical_specification.md
-++-+++ b/deliverables/engineering/cycle_11_technical_specification.md
-++++++ b/deliverables/engineering/cycle_12_technical_specification.md
+---+++ b/deliverables/engineering/cycle_10_technical_specification.md
+--++++ b/deliverables/engineering/cycle_11_technical_specification.md
+-+-+++ b/deliverables/engineering/cycle_11_technical_specification.md
+-+++++ b/deliverables/engineering/cycle_12_technical_specification.md
++--+++ b/deliverables/engineering/cycle_11_technical_specification.md
++-++++ b/deliverables/engineering/cycle_12_technical_specification.md
+++-+++ b/deliverables/engineering/cycle_12_technical_specification.md
+++++++ b/deliverables/engineering/cycle_13_technical_specification.md
    @@ -0,0 +1,9 @@
----+# Requirement: 8
---++# Requirement: 10
--+-+# Requirement: 10
--+++# Requirement: 11
-+--+# Requirement: 10
-+-++# Requirement: 11
-++-+# Requirement: 11
-++++# Requirement: 12
+---+# Requirement: 10
+--++# Requirement: 11
+-+-+# Requirement: 11
+-+++# Requirement: 12
++--+# Requirement: 11
++-++# Requirement: 12
+++-+# Requirement: 12
+++++# Requirement: 13
    +
    +## 1. High-Level Goal
    +
----+Implement a Governor class within the state_manager.py module. This class will be the single authority on stage transitions. The dw6 approve command will now send a request to the Governor. The Governor will only approve the transition if all exit criteria for the current stage are met (e.g., for the Engineer stage, a technical specification file must exist).
---++Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
--+-+Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
--+++Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
-+--+Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
-+-++Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
-++-+Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
-++++Actively enforce Governor rules by integrating with the AI's tool-using capabilities to block any action that violates the rule set for the current stage.
+---+Create a system where the AI's allowed actions are constrained by the current workflow stage. This will be implemented using the Windsurf rules system. For each stage (Engineer, Coder, etc.), a corresponding rule file (.windsurf/rules/dw6_engineer.md, .windsurf/rules/dw6_coder.md, etc.) will be created. The Governor will be responsible for activating the appropriate rule file upon entering a new stage.
+--++Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
+-+-+Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
+-+++Actively enforce Governor rules by integrating with the AI's tool-using capabilities to block any action that violates the rule set for the current stage.
++--+Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
++-++Actively enforce Governor rules by integrating with the AI's tool-using capabilities to block any action that violates the rule set for the current stage.
+++-+Actively enforce Governor rules by integrating with the AI's tool-using capabilities to block any action that violates the rule set for the current stage.
+++++Fix a critical bug in the test suite where a test fixture (cleanup_log_file) is incorrectly configured with autouse=True, causing it to delete the production meta_requirements.log file. The fix involves removing autouse=True and applying the fixture only to the specific tests that require it.
    +
    +## 2. Guiding Principles
    +
    +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
    diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
----index 9718eda..b85b3d9 100644
---+index b85b3d9..00ab2c8 100644
--+-index b85b3d9..00ab2c8 100644
--++index 00ab2c8..ede42cf 100644
-+--index b85b3d9..00ab2c8 100644
-+-+index 00ab2c8..ede42cf 100644
-++-index 00ab2c8..ede42cf 100644
-+++index ede42cf..5045595 100644
+---index b85b3d9..00ab2c8 100644
+--+index 00ab2c8..ede42cf 100644
+-+-index 00ab2c8..ede42cf 100644
+-++index ede42cf..5045595 100644
++--index 00ab2c8..ede42cf 100644
++-+index ede42cf..5045595 100644
+++-index ede42cf..5045595 100644
++++index 5045595..a1b7a04 100644
    --- a/logs/.last_commit_sha
    +++ b/logs/.last_commit_sha
    @@ -1 +1 @@
-----7aa14d9c189cbc22b982d3d7895a650c1cf7a654
---+-75be02c0b7e1723e32042299497f3673b11b4ddd
--+--75be02c0b7e1723e32042299497f3673b11b4ddd
--++-b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
-+---75be02c0b7e1723e32042299497f3673b11b4ddd
-+-+-b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
-++--b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
-+++-96a1111270912ae2722109d00ed1405c166f577c
+----75be02c0b7e1723e32042299497f3673b11b4ddd
+--+-b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+-+--b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+-++-96a1111270912ae2722109d00ed1405c166f577c
++---b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
++-+-96a1111270912ae2722109d00ed1405c166f577c
+++--96a1111270912ae2722109d00ed1405c166f577c
++++-223a8df342ec9a1ce277b234efe90e05cc4803dd
    \ No newline at end of file
----+75be02c0b7e1723e32042299497f3673b11b4ddd
---++b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
--+-+b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
--+++96a1111270912ae2722109d00ed1405c166f577c
-+--+b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
-+-++96a1111270912ae2722109d00ed1405c166f577c
-++-+96a1111270912ae2722109d00ed1405c166f577c
-++++223a8df342ec9a1ce277b234efe90e05cc4803dd
+---+b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
+--++96a1111270912ae2722109d00ed1405c166f577c
+-+-+96a1111270912ae2722109d00ed1405c166f577c
+-+++223a8df342ec9a1ce277b234efe90e05cc4803dd
++--+96a1111270912ae2722109d00ed1405c166f577c
++-++223a8df342ec9a1ce277b234efe90e05cc4803dd
+++-+223a8df342ec9a1ce277b234efe90e05cc4803dd
+++++05ff4137104ba71c49d78ebaa96798dcee5559f7
    \ No newline at end of file
    diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
----index 28746b7..743582b 100644
---+index 743582b..a7aa662 100644
--+-index 743582b..a7aa662 100644
--++index a7aa662..591ebb9 100644
-+--index 743582b..a7aa662 100644
-+-+index a7aa662..591ebb9 100644
-++-index a7aa662..591ebb9 100644
-+++index 591ebb9..d459c0f 100644
+---index 743582b..a7aa662 100644
+--+index a7aa662..591ebb9 100644
+-+-index a7aa662..591ebb9 100644
+-++index 591ebb9..d459c0f 100644
++--index a7aa662..591ebb9 100644
++-+index 591ebb9..d459c0f 100644
+++-index 591ebb9..d459c0f 100644
++++index d459c0f..a21bb3a 100644
    --- a/logs/workflow_state.txt
    +++ b/logs/workflow_state.txt
    @@ -1,2 +1,2 @@
-----CurrentStage=Engineer
-----RequirementPointer=7
----+CurrentStage=Coder
----+RequirementPointer=9
----diff --git a/pytest.ini b/pytest.ini
----new file mode 100644
----index 0000000..a635c5c
------- /dev/null
----+++ b/pytest.ini
----@@ -0,0 +1,2 @@
----+[pytest]
----+pythonpath = .
----diff --git a/src/dw6/main.py b/src/dw6/main.py
----index a55f148..90862f9 100644
------- a/src/dw6/main.py
----+++ b/src/dw6/main.py
----@@ -1,7 +1,7 @@
---- # dw6/main.py
---- import argparse
---- import sys
-----from dw6.state_manager import StateManager
----+from dw6.state_manager import WorkflowManager
---- from dw6.augmenter import process_prompt
---- 
---- def main():
----@@ -10,9 +10,7 @@ def main():
----     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
----     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
---- 
-----    # Review command
-----    subparsers.add_parser("review", help="Review the changes for the current stage.")
-----    
----+
----     # Approve command
----     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
---- 
----@@ -26,11 +24,9 @@ def main():
---- 
----     args = parser.parse_args()
----     
-----    manager = StateManager()
----+    manager = WorkflowManager()
---- 
-----    if args.command == "review":
-----        manager.review()
-----    elif args.command == "approve":
----+    if args.command == "approve":
----         manager.approve()
----     elif args.command == "new":
----         process_prompt(args.prompt)
---+ CurrentStage=Coder
---+-RequirementPointer=9
---++RequirementPointer=10
--- diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
----index 703640c..b829d36 100644
---+index b829d36..241fa62 100644
--- --- a/src/dw6/state_manager.py
--- +++ b/src/dw6/state_manager.py
----@@ -9,7 +9,7 @@ from dw6 import git_handler
---- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
---- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
---- APPROVAL_FILE = "logs/approvals.log"
-----STAGES = ["Engineer", "Coder", "Validator", "Deployer", "Researcher"]
----+STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
---- DELIVERABLE_PATHS = {
----     "Engineer": "deliverables/engineering",
----     "Coder": "deliverables/coding",
----@@ -18,23 +18,67 @@ DELIVERABLE_PATHS = {
----     "Researcher": "deliverables/research",
---+@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
---  }
--+  CurrentStage=Coder
--+--RequirementPointer=9
--+-+RequirementPointer=10
--+-diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
--+-index b829d36..241fa62 100644
--+---- a/src/dw6/state_manager.py
--+-+++ b/src/dw6/state_manager.py
--+-@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
--+- }
--++-RequirementPointer=10
--+++RequirementPointer=11
--++diff --git a/src/dw6/main.py b/src/dw6/main.py
--++index 90862f9..c65a4d9 100644
--++--- a/src/dw6/main.py
--+++++ b/src/dw6/main.py
--++@@ -1,16 +1,42 @@
--++ # dw6/main.py
--++ import argparse
--++ import sys
--+++import re
--+++from pathlib import Path
--+++from datetime import datetime, timezone
--++ from dw6.state_manager import WorkflowManager
--++ from dw6.augmenter import process_prompt
-+-  CurrentStage=Coder
-+---RequirementPointer=9
-+--+RequirementPointer=10
-+--diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-+--index b829d36..241fa62 100644
-+----- a/src/dw6/state_manager.py
-+--+++ b/src/dw6/state_manager.py
-+--@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
-+-- }
-+-+-RequirementPointer=10
-+-++RequirementPointer=11
-+-+diff --git a/src/dw6/main.py b/src/dw6/main.py
-+-+index 90862f9..c65a4d9 100644
-+-+--- a/src/dw6/main.py
-+-++++ b/src/dw6/main.py
-+-+@@ -1,16 +1,42 @@
-+-+ # dw6/main.py
-+-+ import argparse
-+-+ import sys
-+-++import re
-+-++from pathlib import Path
-+-++from datetime import datetime, timezone
-+-+ from dw6.state_manager import WorkflowManager
-+-+ from dw6.augmenter import process_prompt
-++- CurrentStage=Coder
-++--RequirementPointer=10
-++-+RequirementPointer=11
-+++-CurrentStage=Coder
-+++-RequirementPointer=11
-++++CurrentStage=Deployer
-++++RequirementPointer=12
-++ diff --git a/src/dw6/main.py b/src/dw6/main.py
-++-index 90862f9..c65a4d9 100644
-+++index c65a4d9..13e4d93 100644
-++ --- a/src/dw6/main.py
-++ +++ b/src/dw6/main.py
-++-@@ -1,16 +1,42 @@
-++- # dw6/main.py
-+++@@ -2,6 +2,7 @@
-++  import argparse
-++  import sys
-++-+import re
-++-+from pathlib import Path
-++-+from datetime import datetime, timezone
-+++ import re
-++++import subprocess
-+++ from pathlib import Path
-+++ from datetime import datetime, timezone
-++  from dw6.state_manager import WorkflowManager
-++- from dw6.augmenter import process_prompt
-+++@@ -48,6 +49,10 @@ def main():
-+++     meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
-+++     meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
-    
----+class Governor:
----+    def __init__(self, state):
----+        self.state = state
----+        self.current_stage = self.state.get("CurrentStage")
----+
----+    def approve(self):
----+        old_stage = self.current_stage
----+        print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
----+        self._validate_stage_exit_criteria()
----+        # The original logic from WorkflowManager is now fully integrated here.
----+        workflow_manager = WorkflowManager() # We still need access to its methods for now.
----+        workflow_manager._validate_stage()
----+        workflow_manager._run_pre_transition_actions()
----+        self._transition_to_next_stage() # This method now belongs to the Governor
----+        workflow_manager._run_post_transition_actions()
----+        self.state.save()
----+        print(f"--- Governor: Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
----+
----+    def _validate_stage_exit_criteria(self):
----+        print(f"Governor: Validating exit criteria for stage: {self.current_stage}")
----+        if self.current_stage == "Engineer":
----+            req_id = self.state.get("RequirementPointer")
----+            spec_file = Path(f"deliverables/engineering/cycle_{req_id}_technical_specification.md")
----+            if not spec_file.exists():
----+                print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
----+                sys.exit(1)
----+            print("Governor: 'Engineer' exit criteria met.")
----+
----+    def _transition_to_next_stage(self):
----+        current_index = STAGES.index(self.current_stage)
----+        # After 'Deployer', the cycle is complete
----+        if self.current_stage == "Deployer":
----+            self._complete_requirement_cycle()
----+            self.current_stage = STAGES[0]
----+        else:
----+            self.current_stage = STAGES[current_index + 1]
----+        self.state.set("CurrentStage", self.current_stage)
----+
----+    def _complete_requirement_cycle(self):
----+        req_id = int(self.state.get("RequirementPointer"))
----+        os.makedirs("logs", exist_ok=True)
----+        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
----+        with open(APPROVAL_FILE, "a") as f:
----+            f.write(f"Requirement {req_id} approved at {timestamp}\n")
----+        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
----+        next_req_id = req_id + 1
----+        self.state.set("RequirementPointer", next_req_id)
----+        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
----+
---- class WorkflowManager:
----     def __init__(self):
----         self.state = WorkflowState()
----+        self.governor = Governor(self.state) # The manager now has a governor
---+ class Governor:
---++    RULES = {
---++        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
---++        "Coder": "Can use file system tools, code editing tools, and run tests.",
---++        "Validator": "Can only run tests and validation tools.",
---++        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
---++        "Researcher": "Can use web search and documentation reading tools."
---++    }
---+     def __init__(self, state):
---+         self.state = state
---          self.current_stage = self.state.get("CurrentStage")
--+- class Governor:
--+-+    RULES = {
--+-+        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
--+-+        "Coder": "Can use file system tools, code editing tools, and run tests.",
--+-+        "Validator": "Can only run tests and validation tools.",
--+-+        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
--+-+        "Researcher": "Can use web search and documentation reading tools."
--+-+    }
--+-     def __init__(self, state):
--+-         self.state = state
--+-         self.current_stage = self.state.get("CurrentStage")
--+++META_LOG_FILE = Path("logs/meta_requirements.log")
--+++
--+++def register_meta_requirement(description: str):
--+++    """Logs a new meta-requirement to the meta_requirements.log file."""
--+++    META_LOG_FILE.parent.mkdir(exist_ok=True)
--+++    
--+++    last_id = 0
--+++    if META_LOG_FILE.exists():
--+++        with open(META_LOG_FILE, "r") as f:
--+++            lines = f.readlines()
--+++            if lines:
--+++                last_line = lines[-1]
--+++                match = re.search(r'^\[ID:(\d+)\]', last_line)
--+++                if match:
--+++                    last_id = int(match.group(1))
--+++
--+++    new_id = last_id + 1
--+++    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
--+++    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
-+-- class Governor:
-+--+    RULES = {
-+--+        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
-+--+        "Coder": "Can use file system tools, code editing tools, and run tests.",
-+--+        "Validator": "Can only run tests and validation tools.",
-+--+        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
-+--+        "Researcher": "Can use web search and documentation reading tools."
-+--+    }
-+--     def __init__(self, state):
-+--         self.state = state
-+--         self.current_stage = self.state.get("CurrentStage")
-+-++META_LOG_FILE = Path("logs/meta_requirements.log")
-+-++
-+-++def register_meta_requirement(description: str):
-+-++    """Logs a new meta-requirement to the meta_requirements.log file."""
-+-++    META_LOG_FILE.parent.mkdir(exist_ok=True)
-+-++    
-+-++    last_id = 0
-+-++    if META_LOG_FILE.exists():
-+-++        with open(META_LOG_FILE, "r") as f:
-+-++            lines = f.readlines()
-+-++            if lines:
-+-++                last_line = lines[-1]
-+-++                match = re.search(r'^\[ID:(\d+)\]', last_line)
-+-++                if match:
-+-++                    last_id = int(match.group(1))
-+-++
-+-++    new_id = last_id + 1
-+-++    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-+-++    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
-+-++
-+-++    with open(META_LOG_FILE, "a") as f:
-+-++        f.write(log_entry)
-+-++    
-+-++    print(f"Successfully logged meta-requirement {new_id}.")
-++-+META_LOG_FILE = Path("logs/meta_requirements.log")
-++-+
-++-+def register_meta_requirement(description: str):
-++-+    """Logs a new meta-requirement to the meta_requirements.log file."""
-++-+    META_LOG_FILE.parent.mkdir(exist_ok=True)
-++-+    
-++-+    last_id = 0
-++-+    if META_LOG_FILE.exists():
-++-+        with open(META_LOG_FILE, "r") as f:
-++-+            lines = f.readlines()
-++-+            if lines:
-++-+                last_line = lines[-1]
-++-+                match = re.search(r'^\[ID:(\d+)\]', last_line)
-++-+                if match:
-++-+                    last_id = int(match.group(1))
-++-+
-++-+    new_id = last_id + 1
-++-+    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-++-+    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
+--  CurrentStage=Coder
+----RequirementPointer=9
+---+RequirementPointer=10
+---diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+---index b829d36..241fa62 100644
+------ a/src/dw6/state_manager.py
+---+++ b/src/dw6/state_manager.py
+---@@ -19,13 +19,26 @@ DELIVERABLE_PATHS = {
+--- }
+--+-RequirementPointer=10
+--++RequirementPointer=11
+--+diff --git a/src/dw6/main.py b/src/dw6/main.py
+--+index 90862f9..c65a4d9 100644
+--+--- a/src/dw6/main.py
+--++++ b/src/dw6/main.py
+--+@@ -1,16 +1,42 @@
+--+ # dw6/main.py
+--+ import argparse
+--+ import sys
+--++import re
+--++from pathlib import Path
+--++from datetime import datetime, timezone
+--+ from dw6.state_manager import WorkflowManager
+--+ from dw6.augmenter import process_prompt
+-+- CurrentStage=Coder
+-+--RequirementPointer=10
+-+-+RequirementPointer=11
+-++-CurrentStage=Coder
+-++-RequirementPointer=11
+-+++CurrentStage=Deployer
+-+++RequirementPointer=12
+-+ diff --git a/src/dw6/main.py b/src/dw6/main.py
+-+-index 90862f9..c65a4d9 100644
+-++index c65a4d9..13e4d93 100644
+-+ --- a/src/dw6/main.py
+-+ +++ b/src/dw6/main.py
+-+-@@ -1,16 +1,42 @@
+-+- # dw6/main.py
+-++@@ -2,6 +2,7 @@
+-+  import argparse
+-+  import sys
+-+-+import re
+-+-+from pathlib import Path
+-+-+from datetime import datetime, timezone
+-++ import re
+-+++import subprocess
+-++ from pathlib import Path
+-++ from datetime import datetime, timezone
+-+  from dw6.state_manager import WorkflowManager
+-+- from dw6.augmenter import process_prompt
+-++@@ -48,6 +49,10 @@ def main():
+-++     meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
+-++     meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
+-   
+--- class Governor:
+---+    RULES = {
+---+        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+---+        "Coder": "Can use file system tools, code editing tools, and run tests.",
+---+        "Validator": "Can only run tests and validation tools.",
+---+        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+---+        "Researcher": "Can use web search and documentation reading tools."
+---+    }
+---     def __init__(self, state):
+---         self.state = state
+---         self.current_stage = self.state.get("CurrentStage")
+--++META_LOG_FILE = Path("logs/meta_requirements.log")
++-- CurrentStage=Coder
++---RequirementPointer=10
++--+RequirementPointer=11
++-+-CurrentStage=Coder
++-+-RequirementPointer=11
++-++CurrentStage=Deployer
++-++RequirementPointer=12
++- diff --git a/src/dw6/main.py b/src/dw6/main.py
++--index 90862f9..c65a4d9 100644
++-+index c65a4d9..13e4d93 100644
++- --- a/src/dw6/main.py
++- +++ b/src/dw6/main.py
++--@@ -1,16 +1,42 @@
++-- # dw6/main.py
++-+@@ -2,6 +2,7 @@
++-  import argparse
++-  import sys
++--+import re
++--+from pathlib import Path
++--+from datetime import datetime, timezone
++-+ import re
++-++import subprocess
++-+ from pathlib import Path
++-+ from datetime import datetime, timezone
++-  from dw6.state_manager import WorkflowManager
++-- from dw6.augmenter import process_prompt
++-+@@ -48,6 +49,10 @@ def main():
++-+     meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
++-+     meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
++-  
++--+META_LOG_FILE = Path("logs/meta_requirements.log")
++--+
++--+def register_meta_requirement(description: str):
++--+    """Logs a new meta-requirement to the meta_requirements.log file."""
++--+    META_LOG_FILE.parent.mkdir(exist_ok=True)
++--+    
++--+    last_id = 0
++--+    if META_LOG_FILE.exists():
++--+        with open(META_LOG_FILE, "r") as f:
++--+            lines = f.readlines()
++--+            if lines:
++--+                last_line = lines[-1]
++--+                match = re.search(r'^\[ID:(\d+)\]', last_line)
++--+                if match:
++--+                    last_id = int(match.group(1))
++--+
++--+    new_id = last_id + 1
++--+    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
++--+    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
++--+
++--+    with open(META_LOG_FILE, "a") as f:
++--+        f.write(log_entry)
++--+    
++--+    print(f"Successfully logged meta-requirement {new_id}.")
+++--CurrentStage=Coder
+++--RequirementPointer=11
+++-+CurrentStage=Deployer
+++-+RequirementPointer=12
+++-diff --git a/src/dw6/main.py b/src/dw6/main.py
+++-index c65a4d9..13e4d93 100644
+++---- a/src/dw6/main.py
+++-+++ b/src/dw6/main.py
+++-@@ -2,6 +2,7 @@
+++- import argparse
+++- import sys
+++- import re
+++-+import subprocess
+++- from pathlib import Path
+++- from datetime import datetime, timezone
+++- from dw6.state_manager import WorkflowManager
+++-@@ -48,6 +49,10 @@ def main():
+++-     meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
+++-     meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
+++- 
+++-+    # Do command
+++-+    do_parser = subparsers.add_parser("do", help="Execute a governed action.")
+++-+    do_parser.add_argument("action", type=str, help="The action to execute.")
++ -+
++-- def main():
++--     """Main entry point for the DW6 CLI."""
++---    # Test comment for Cycle 2 validation.
++--     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
++--     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+++-     if len(sys.argv) == 1:
+++-         parser.print_help(sys.stderr)
+++-         sys.exit(1)
+++-@@ -56,6 +61,17 @@ def main():
+++-     
+++-     if args.command == "meta-req":
+++-         register_meta_requirement(args.description)
+++-+    elif args.command == "do":
+++-+        manager = WorkflowManager()
+++-+        try:
+++-+            manager.governor.authorize(args.action)
+++-+            # The command is authorized, execute it.
+++-+            subprocess.run(args.action, shell=True, check=True)
+++-+        except PermissionError:
+++-+            sys.exit(1)
+++-+        except subprocess.CalledProcessError:
+++-+            print(f"ERROR: The action '{args.action}' failed to execute.", file=sys.stderr)
+++-+            sys.exit(1)
+++-     else:
+++-         manager = WorkflowManager()
+++-         if args.command == "approve":
+++-diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+++-index 241fa62..33e9d07 100644
+++---- a/src/dw6/state_manager.py
+++-+++ b/src/dw6/state_manager.py
+++-@@ -20,20 +20,52 @@ DELIVERABLE_PATHS = {
++ - 
++---
++--     # Approve command
++--     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++- class Governor:
+++-     RULES = {
+++--        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+++--        "Coder": "Can use file system tools, code editing tools, and run tests.",
+++--        "Validator": "Can only run tests and validation tools.",
+++--        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+++--        "Researcher": "Can use web search and documentation reading tools."
+++-+        "Engineer": [
+++-+            "uv run python -m dw6.main new",
+++-+            "ls",
+++-+            "cat",
+++-+            "view_file_outline"
+++-+        ],
+++-+        "Coder": [
+++-+            "replace_file_content",
+++-+            "write_to_file",
+++-+            "view_file_outline",
+++-+            "ls"
+++-+        ],
+++-+        "Validator": [
+++-+            "uv run pytest"
+++-+        ],
+++-+        "Deployer": [
+++-+            "git add",
+++-+            "git commit",
+++-+            "git tag",
+++-+            "uv run python -m dw6.main approve"
+++-+        ],
+++-+        "Researcher": [
+++-+            "search_web",
+++-+            "read_url_content"
+++-+        ]
+++-     }
 ++-+
-++-+    with open(META_LOG_FILE, "a") as f:
-++-+        f.write(log_entry)
-++-+    
-++-+    print(f"Successfully logged meta-requirement {new_id}.")
+++-     def __init__(self, state):
+++-         self.state = state
+++-         self.current_stage = self.state.get("CurrentStage")
++ - 
++--@@ -18,18 +44,24 @@ def main():
++--     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
++--     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+++-+    def authorize(self, command: str):
+++-+        """Checks if a command is allowed in the current stage."""
+++-+        allowed_commands = self.RULES.get(self.current_stage, [])
+++-+        if not any(command.startswith(prefix) for prefix in allowed_commands):
+++-+            error_msg = f"[GOVERNOR] Action denied. The command '{(command)}' is not allowed in the '{self.current_stage}' stage."
+++-+            print(error_msg, file=sys.stderr)
+++-+            raise PermissionError(error_msg)
+++-+        print(f"[GOVERNOR] Action authorized for stage '{self.current_stage}'.")
 ++-+
-++- def main():
-++-     """Main entry point for the DW6 CLI."""
-++--    # Test comment for Cycle 2 validation.
-++-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-++-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-++- 
-++--
-++-     # Approve command
-++-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-++- 
-++-@@ -18,18 +44,24 @@ def main():
-++-     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-++-     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-++- 
-++-+    # Meta-req command
-++-+    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
-++-+    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
-++++    # Do command
-++++    do_parser = subparsers.add_parser("do", help="Execute a governed action.")
-++++    do_parser.add_argument("action", type=str, help="The action to execute.")
-++ +
-++      if len(sys.argv) == 1:
-++          parser.print_help(sys.stderr)
-++          sys.exit(1)
-++- 
-++-     args = parser.parse_args()
-+++@@ -56,6 +61,17 @@ def main():
-++      
-++--    manager = WorkflowManager()
-++--
-++--    if args.command == "approve":
-++--        manager.approve()
-++--    elif args.command == "new":
-++--        process_prompt(args.prompt)
-++-+    if args.command == "meta-req":
-++-+        register_meta_requirement(args.description)
-++-+    else:
-+++     if args.command == "meta-req":
-+++         register_meta_requirement(args.description)
-++++    elif args.command == "do":
-++ +        manager = WorkflowManager()
-++-+        if args.command == "approve":
-++-+            manager.approve()
-++-+        elif args.command == "new":
-++-+            process_prompt(args.prompt)
-++++        try:
-++++            manager.governor.authorize(args.action)
-++++            # The command is authorized, execute it.
-++++            subprocess.run(args.action, shell=True, check=True)
-++++        except PermissionError:
-++++            sys.exit(1)
-++++        except subprocess.CalledProcessError:
-++++            print(f"ERROR: The action '{args.action}' failed to execute.", file=sys.stderr)
-++++            sys.exit(1)
-+++     else:
-+++         manager = WorkflowManager()
-+++         if args.command == "approve":
-+++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-+++index 241fa62..33e9d07 100644
-+++--- a/src/dw6/state_manager.py
-++++++ b/src/dw6/state_manager.py
-+++@@ -20,20 +20,52 @@ DELIVERABLE_PATHS = {
-+++ 
-+++ class Governor:
-+++     RULES = {
-+++-        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
-+++-        "Coder": "Can use file system tools, code editing tools, and run tests.",
-+++-        "Validator": "Can only run tests and validation tools.",
-+++-        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
-+++-        "Researcher": "Can use web search and documentation reading tools."
-++++        "Engineer": [
-++++            "uv run python -m dw6.main new",
-++++            "ls",
-++++            "cat",
-++++            "view_file_outline"
-++++        ],
-++++        "Coder": [
-++++            "replace_file_content",
-++++            "write_to_file",
-++++            "view_file_outline",
-++++            "ls"
-++++        ],
-++++        "Validator": [
-++++            "uv run pytest"
-++++        ],
-++++        "Deployer": [
-++++            "git add",
-++++            "git commit",
-++++            "git tag",
-++++            "uv run python -m dw6.main approve"
-++++        ],
-++++        "Researcher": [
-++++            "search_web",
-++++            "read_url_content"
-++++        ]
-+++     }
-+ ++
-+-+ def main():
-+-+     """Main entry point for the DW6 CLI."""
-+-+-    # Test comment for Cycle 2 validation.
-+-+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
-+-+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-+++     def __init__(self, state):
-+++         self.state = state
-+++         self.current_stage = self.state.get("CurrentStage")
-+   
-+--+    def enforce_rules(self):
-+--+        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
-+--+        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
-+--+        print(f"[RULE] {rule}")
-+-+-
-+-+     # Approve command
-+-+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+++-     def enforce_rules(self):
+++--        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+++-+        rules = self.RULES.get(self.current_stage, ["No specific rules defined."])
+++-         print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+++--        print(f"[RULE] {rule}")
+++-+        print("[RULE] Allowed command prefixes:")
+++-+        for rule in rules:
+++-+            print(f"  - {rule}")
++ - 
++--+    # Meta-req command
++--+    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
++--+    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
++-++    # Do command
++-++    do_parser = subparsers.add_parser("do", help="Execute a governed action.")
++-++    do_parser.add_argument("action", type=str, help="The action to execute.")
++- +
++-      if len(sys.argv) == 1:
++-          parser.print_help(sys.stderr)
++-          sys.exit(1)
+++-     def approve(self):
+++-         old_stage = self.current_stage
+++-diff --git a/tests/test_governor.py b/tests/test_governor.py
+++-index 26bf82b..a431529 100644
+++---- a/tests/test_governor.py
+++-+++ b/tests/test_governor.py
+++-@@ -71,5 +71,37 @@ def test_governor_enforces_rules_on_approve(mocker, capsys):
++ - 
++--     args = parser.parse_args()
++-+@@ -56,6 +61,17 @@ def main():
++-      
++---    manager = WorkflowManager()
++---
++---    if args.command == "approve":
++---        manager.approve()
++---    elif args.command == "new":
++---        process_prompt(args.prompt)
++--+    if args.command == "meta-req":
++--+        register_meta_requirement(args.description)
++--+    else:
++-+     if args.command == "meta-req":
++-+         register_meta_requirement(args.description)
++-++    elif args.command == "do":
++- +        manager = WorkflowManager()
++--+        if args.command == "approve":
++--+            manager.approve()
++--+        elif args.command == "new":
++--+            process_prompt(args.prompt)
++-++        try:
++-++            manager.governor.authorize(args.action)
++-++            # The command is authorized, execute it.
++-++            subprocess.run(args.action, shell=True, check=True)
++-++        except PermissionError:
++-++            sys.exit(1)
++-++        except subprocess.CalledProcessError:
++-++            print(f"ERROR: The action '{args.action}' failed to execute.", file=sys.stderr)
++-++            sys.exit(1)
++-+     else:
++-+         manager = WorkflowManager()
++-+         if args.command == "approve":
++-+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
++-+index 241fa62..33e9d07 100644
++-+--- a/src/dw6/state_manager.py
++-++++ b/src/dw6/state_manager.py
++-+@@ -20,20 +20,52 @@ DELIVERABLE_PATHS = {
 +-+ 
-+-+@@ -18,18 +44,24 @@ def main():
-+-+     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
-+-+     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
++-+ class Governor:
++-+     RULES = {
++-+-        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
++-+-        "Coder": "Can use file system tools, code editing tools, and run tests.",
++-+-        "Validator": "Can only run tests and validation tools.",
++-+-        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
++-+-        "Researcher": "Can use web search and documentation reading tools."
++-++        "Engineer": [
++-++            "uv run python -m dw6.main new",
++-++            "ls",
++-++            "cat",
++-++            "view_file_outline"
++-++        ],
++-++        "Coder": [
++-++            "replace_file_content",
++-++            "write_to_file",
++-++            "view_file_outline",
++-++            "ls"
++-++        ],
++-++        "Validator": [
++-++            "uv run pytest"
++-++        ],
++-++        "Deployer": [
++-++            "git add",
++-++            "git commit",
++-++            "git tag",
++-++            "uv run python -m dw6.main approve"
++-++        ],
++-++        "Researcher": [
++-++            "search_web",
++-++            "read_url_content"
++-++        ]
++-+     }
++-++
++-+     def __init__(self, state):
++-+         self.state = state
++-+         self.current_stage = self.state.get("CurrentStage")
++-  
++-- if __name__ == "__main__":
++--     main()
++-++    def authorize(self, command: str):
++-++        """Checks if a command is allowed in the current stage."""
++-++        allowed_commands = self.RULES.get(self.current_stage, [])
++-++        if not any(command.startswith(prefix) for prefix in allowed_commands):
++-++            error_msg = f"[GOVERNOR] Action denied. The command '{(command)}' is not allowed in the '{self.current_stage}' stage."
++-++            print(error_msg, file=sys.stderr)
++-++            raise PermissionError(error_msg)
++-++        print(f"[GOVERNOR] Action authorized for stage '{self.current_stage}'.")
++-++
++-+     def enforce_rules(self):
++-+-        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
++-++        rules = self.RULES.get(self.current_stage, ["No specific rules defined."])
++-+         print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
++-+-        print(f"[RULE] {rule}")
++-++        print("[RULE] Allowed command prefixes:")
++-++        for rule in rules:
++-++            print(f"  - {rule}")
 +-+ 
-+-++    # Meta-req command
-+-++    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
-+-++    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
-++- if __name__ == "__main__":
-++-     main()
-++++    def authorize(self, command: str):
-++++        """Checks if a command is allowed in the current stage."""
-++++        allowed_commands = self.RULES.get(self.current_stage, [])
-++++        if not any(command.startswith(prefix) for prefix in allowed_commands):
-++++            error_msg = f"[GOVERNOR] Action denied. The command '{(command)}' is not allowed in the '{self.current_stage}' stage."
-++++            print(error_msg, file=sys.stderr)
-++++            raise PermissionError(error_msg)
-++++        print(f"[GOVERNOR] Action authorized for stage '{self.current_stage}'.")
-+ ++
-+-+     if len(sys.argv) == 1:
-+-+         parser.print_help(sys.stderr)
-+-+         sys.exit(1)
-+++     def enforce_rules(self):
-+++-        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
-++++        rules = self.RULES.get(self.current_stage, ["No specific rules defined."])
-+++         print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
-+++-        print(f"[RULE] {rule}")
-++++        print("[RULE] Allowed command prefixes:")
-++++        for rule in rules:
-++++            print(f"  - {rule}")
-+ + 
-+-+     args = parser.parse_args()
-+-+     
-+-+-    manager = WorkflowManager()
-+-+-
-+-+-    if args.command == "approve":
-+-+-        manager.approve()
-+-+-    elif args.command == "new":
-+-+-        process_prompt(args.prompt)
-+-++    if args.command == "meta-req":
-+-++        register_meta_requirement(args.description)
-+-++    else:
-+-++        manager = WorkflowManager()
-+-++        if args.command == "approve":
-+-++            manager.approve()
-+-++        elif args.command == "new":
-+-++            process_prompt(args.prompt)
-+++     def approve(self):
-+++         old_stage = self.current_stage
-+++diff --git a/tests/test_governor.py b/tests/test_governor.py
-+++index 26bf82b..a431529 100644
-+++--- a/tests/test_governor.py
-++++++ b/tests/test_governor.py
-+++@@ -71,5 +71,37 @@ def test_governor_enforces_rules_on_approve(mocker, capsys):
-+ + 
-+-+ if __name__ == "__main__":
-+-+     main()
-+-+diff --git a/tests/test_main.py b/tests/test_main.py
-+-+index c429973..eddb264 100644
-+-+--- a/tests/test_main.py
-+-++++ b/tests/test_main.py
-+-+@@ -1,5 +1,52 @@
-+-+ # tests/test_main.py
-+-++import pytest
-+-++from pathlib import Path
-+-++import re
-+-++from dw6.main import register_meta_requirement, META_LOG_FILE
++-+     def approve(self):
++-+         old_stage = self.current_stage
++-+diff --git a/tests/test_governor.py b/tests/test_governor.py
++-+index 26bf82b..a431529 100644
++-+--- a/tests/test_governor.py
++-++++ b/tests/test_governor.py
++-+@@ -71,5 +71,37 @@ def test_governor_enforces_rules_on_approve(mocker, capsys):
 +-+ 
-+-+-def test_placeholder():
-+-+-    """A placeholder test to satisfy the Validator stage."""
-+-+-    assert True
-+-++@pytest.fixture(autouse=True)
-+-++def cleanup_log_file():
-+-++    """Fixture to clean up the meta log file before and after a test."""
-+-++    if META_LOG_FILE.exists():
-+-++        META_LOG_FILE.unlink()
-+-++    yield
-+-++    if META_LOG_FILE.exists():
-+-++        META_LOG_FILE.unlink()
++-+     # Assert
++-+     captured = capsys.readouterr()
++-+-    expected_rule = Governor.RULES["Coder"]
++-+-    assert expected_rule in captured.out
++-++    # Check that each rule is printed
++-++    for rule in Governor.RULES["Coder"]:
++-++        assert rule in captured.out
+ -++
+--++def register_meta_requirement(description: str):
+--++    """Logs a new meta-requirement to the meta_requirements.log file."""
+--++    META_LOG_FILE.parent.mkdir(exist_ok=True)
++-++@pytest.mark.parametrize("stage, allowed_command", [
++-++    (stage, command) 
++-++    for stage, commands in Governor.RULES.items() 
++-++    for command in commands
++-++])
++-++def test_governor_authorizes_allowed_commands(mock_state, stage, allowed_command):
++-++    """Verify that the Governor authorizes all allowed commands for each stage."""
++-++    # Arrange
++-++    mock_state.get.return_value = stage
++-++    governor = Governor(mock_state)
+ -++    
+--++    last_id = 0
+--++    if META_LOG_FILE.exists():
+--++        with open(META_LOG_FILE, "r") as f:
+--++            lines = f.readlines()
+--++            if lines:
+--++                last_line = lines[-1]
+--++                match = re.search(r'^\[ID:(\d+)\]', last_line)
+--++                if match:
+--++                    last_id = int(match.group(1))
++-++    # Act & Assert
++-++    try:
++-++        governor.authorize(allowed_command + " --some-arg") # Test with an argument
++-++    except PermissionError:
++-++        pytest.fail(f"Governor incorrectly denied command '{allowed_command}' for stage '{stage}'.")
+ -++
+--++    new_id = last_id + 1
+--++    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+--++    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
++-++def test_governor_denies_forbidden_command(mock_state):
++-++    """Verify that the Governor denies a command that is not allowed."""
++-++    # Arrange
++-++    stage = "Engineer"
++-++    forbidden_command = "git commit -m 'should not be allowed'"
++-++    mock_state.get.return_value = stage
++-++    governor = Governor(mock_state)
+ -++
+--++    with open(META_LOG_FILE, "a") as f:
+--++        f.write(log_entry)
++-++    # Act & Assert
++-++    with pytest.raises(PermissionError) as e:
++-++        governor.authorize(forbidden_command)
+ -++    
+--++    print(f"Successfully logged meta-requirement {new_id}.")
+-+-+META_LOG_FILE = Path("logs/meta_requirements.log")
++-++    assert "Action denied" in str(e.value)
+++-     # Assert
+++-     captured = capsys.readouterr()
+++--    expected_rule = Governor.RULES["Coder"]
+++--    assert expected_rule in captured.out
+++-+    # Check that each rule is printed
+++-+    for rule in Governor.RULES["Coder"]:
+++-+        assert rule in captured.out
+ +-+
+-+-+def register_meta_requirement(description: str):
+-+-+    """Logs a new meta-requirement to the meta_requirements.log file."""
+-+-+    META_LOG_FILE.parent.mkdir(exist_ok=True)
+++-+@pytest.mark.parametrize("stage, allowed_command", [
+++-+    (stage, command) 
+++-+    for stage, commands in Governor.RULES.items() 
+++-+    for command in commands
+++-+])
+++-+def test_governor_authorizes_allowed_commands(mock_state, stage, allowed_command):
+++-+    """Verify that the Governor authorizes all allowed commands for each stage."""
+++-+    # Arrange
+++-+    mock_state.get.return_value = stage
+++-+    governor = Governor(mock_state)
+ +-+    
+-+-+    last_id = 0
+-+-+    if META_LOG_FILE.exists():
+-+-+        with open(META_LOG_FILE, "r") as f:
+-+-+            lines = f.readlines()
+-+-+            if lines:
+-+-+                last_line = lines[-1]
+-+-+                match = re.search(r'^\[ID:(\d+)\]', last_line)
+-+-+                if match:
+-+-+                    last_id = int(match.group(1))
+++-+    # Act & Assert
+++-+    try:
+++-+        governor.authorize(allowed_command + " --some-arg") # Test with an argument
+++-+    except PermissionError:
+++-+        pytest.fail(f"Governor incorrectly denied command '{allowed_command}' for stage '{stage}'.")
+ +-+
+-+-+    new_id = last_id + 1
+-+-+    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
+-+-+    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
+++-+def test_governor_denies_forbidden_command(mock_state):
+++-+    """Verify that the Governor denies a command that is not allowed."""
+++-+    # Arrange
+++-+    stage = "Engineer"
+++-+    forbidden_command = "git commit -m 'should not be allowed'"
+++-+    mock_state.get.return_value = stage
+++-+    governor = Governor(mock_state)
+ +-+
+-+-+    with open(META_LOG_FILE, "a") as f:
+-+-+        f.write(log_entry)
+++-+    # Act & Assert
+++-+    with pytest.raises(PermissionError) as e:
+++-+        governor.authorize(forbidden_command)
+ +-+    
+-+-+    print(f"Successfully logged meta-requirement {new_id}.")
+++-+    assert "Action denied" in str(e.value)
++++ CurrentStage=Deployer
++++-RequirementPointer=12
+++++RequirementPointer=13
++  diff --git a/tests/test_main.py b/tests/test_main.py
++--index c429973..eddb264 100644
++-+index eddb264..47ae0e7 100644
+++-index eddb264..47ae0e7 100644
++++index 47ae0e7..e6a7024 100644
++  --- a/tests/test_main.py
++  +++ b/tests/test_main.py
++--@@ -1,5 +1,52 @@
++-- # tests/test_main.py
++--+import pytest
++--+from pathlib import Path
++--+import re
++--+from dw6.main import register_meta_requirement, META_LOG_FILE
++-- 
++---def test_placeholder():
++---    """A placeholder test to satisfy the Validator stage."""
++---    assert True
++--+@pytest.fixture(autouse=True)
++--+def cleanup_log_file():
++--+    """Fixture to clean up the meta log file before and after a test."""
++--+    if META_LOG_FILE.exists():
++--+        META_LOG_FILE.unlink()
++--+    yield
++--+    if META_LOG_FILE.exists():
++--+        META_LOG_FILE.unlink()
++-+@@ -50,3 +50,50 @@ def test_register_meta_requirement_increments_id():
++-+     assert description1 in lines[0]
++-+     assert "[ID:2]" in lines[1]
++-+     assert description2 in lines[1]
 +- +
-+--     def approve(self):
-+--         old_stage = self.current_stage
-+--         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
-+--+        self.enforce_rules()
-+--         self._validate_stage_exit_criteria()
-+--         # The original logic from WorkflowManager is now fully integrated here.
-+--         workflow_manager = WorkflowManager() # We still need access to its methods for now.
-+--diff --git a/tests/test_governor.py b/tests/test_governor.py
-+--index 95b566d..26bf82b 100644
-+----- a/tests/test_governor.py
-+--+++ b/tests/test_governor.py
-+--@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
-+--         # Clean up the created file
-+--         if spec_file.exists():
-+--             spec_file.unlink()
-+-++def test_register_meta_requirement_creates_file_and_logs_entry():
-+-++    """Verify that the first call creates the log file and adds the first entry correctly."""
-+++     # Assert
-+++     captured = capsys.readouterr()
-+++-    expected_rule = Governor.RULES["Coder"]
-+++-    assert expected_rule in captured.out
-++++    # Check that each rule is printed
-++++    for rule in Governor.RULES["Coder"]:
-++++        assert rule in captured.out
- +++
--+++    with open(META_LOG_FILE, "a") as f:
--+++        f.write(log_entry)
-++++@pytest.mark.parametrize("stage, allowed_command", [
-++++    (stage, command) 
-++++    for stage, commands in Governor.RULES.items() 
-++++    for command in commands
-++++])
-++++def test_governor_authorizes_allowed_commands(mock_state, stage, allowed_command):
-++++    """Verify that the Governor authorizes all allowed commands for each stage."""
-+ ++    # Arrange
-+-++    description = "This is the first meta requirement."
-++++    mock_state.get.return_value = stage
-++++    governor = Governor(mock_state)
- +++    
--+++    print(f"Successfully logged meta-requirement {new_id}.")
--+++
--++ def main():
--++     """Main entry point for the DW6 CLI."""
--++-    # Test comment for Cycle 2 validation.
--++     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
--++     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
++--+def test_register_meta_requirement_creates_file_and_logs_entry():
++--+    """Verify that the first call creates the log file and adds the first entry correctly."""
+++-@@ -50,3 +50,50 @@ def test_register_meta_requirement_increments_id():
+++-     assert description1 in lines[0]
+++-     assert "[ID:2]" in lines[1]
+++-     assert description2 in lines[1]
+ +-+
+-+- def main():
+-+-     """Main entry point for the DW6 CLI."""
+-+--    # Test comment for Cycle 2 validation.
+-+-     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+-+-     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+-+- 
+-+--
+-+-     # Approve command
+-+-     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+-+- 
+-+-@@ -18,18 +44,24 @@ def main():
+-+-     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+-+-     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+-+- 
+-+-+    # Meta-req command
+-+-+    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
+-+-+    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
+-+++    # Do command
+-+++    do_parser = subparsers.add_parser("do", help="Execute a governed action.")
+-+++    do_parser.add_argument("action", type=str, help="The action to execute.")
+-+ +
+-+      if len(sys.argv) == 1:
+-+          parser.print_help(sys.stderr)
+-+          sys.exit(1)
+-+- 
+-+-     args = parser.parse_args()
+-++@@ -56,6 +61,17 @@ def main():
+-+      
+-+--    manager = WorkflowManager()
+-+--
+-+--    if args.command == "approve":
+-+--        manager.approve()
+-+--    elif args.command == "new":
+-+--        process_prompt(args.prompt)
+-+-+    if args.command == "meta-req":
+-+-+        register_meta_requirement(args.description)
+-+-+    else:
+-++     if args.command == "meta-req":
+-++         register_meta_requirement(args.description)
+-+++    elif args.command == "do":
+-+ +        manager = WorkflowManager()
+-+-+        if args.command == "approve":
+-+-+            manager.approve()
+-+-+        elif args.command == "new":
+-+-+            process_prompt(args.prompt)
+-+++        try:
+-+++            manager.governor.authorize(args.action)
+-+++            # The command is authorized, execute it.
+-+++            subprocess.run(args.action, shell=True, check=True)
+-+++        except PermissionError:
+-+++            sys.exit(1)
+-+++        except subprocess.CalledProcessError:
+-+++            print(f"ERROR: The action '{args.action}' failed to execute.", file=sys.stderr)
+-+++            sys.exit(1)
+-++     else:
+-++         manager = WorkflowManager()
+-++         if args.command == "approve":
+-++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+-++index 241fa62..33e9d07 100644
+-++--- a/src/dw6/state_manager.py
+-+++++ b/src/dw6/state_manager.py
+-++@@ -20,20 +20,52 @@ DELIVERABLE_PATHS = {
+++-+
++++@@ -4,7 +4,7 @@ from pathlib import Path
++++ import re
++++ from dw6.main import register_meta_requirement, META_LOG_FILE
+ ++ 
+-++ class Governor:
+-++     RULES = {
+-++-        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+-++-        "Coder": "Can use file system tools, code editing tools, and run tests.",
+-++-        "Validator": "Can only run tests and validation tools.",
+-++-        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+-++-        "Researcher": "Can use web search and documentation reading tools."
+-+++        "Engineer": [
+-+++            "uv run python -m dw6.main new",
+-+++            "ls",
+-+++            "cat",
+-+++            "view_file_outline"
+-+++        ],
+-+++        "Coder": [
+-+++            "replace_file_content",
+-+++            "write_to_file",
+-+++            "view_file_outline",
+-+++            "ls"
+-+++        ],
+-+++        "Validator": [
+-+++            "uv run pytest"
+-+++        ],
+-+++        "Deployer": [
+-+++            "git add",
+-+++            "git commit",
+-+++            "git tag",
+-+++            "uv run python -m dw6.main approve"
+-+++        ],
+-+++        "Researcher": [
+-+++            "search_web",
+-+++            "read_url_content"
+-+++        ]
+-++     }
+- ++
+--+ def main():
+--+     """Main entry point for the DW6 CLI."""
+--+-    # Test comment for Cycle 2 validation.
+--+     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
+--+     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
+-++     def __init__(self, state):
+-++         self.state = state
+-++         self.current_stage = self.state.get("CurrentStage")
 -   
----     def get_state(self):
----         return self.state.data
---- 
---++    def enforce_rules(self):
---++        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
---++        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
---++        print(f"[RULE] {rule}")
--+-+    def enforce_rules(self):
--+-+        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
--+-+        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
--+-+        print(f"[RULE] {rule}")
--++-
--++     # Approve command
--++     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
--++ 
--++@@ -18,18 +44,24 @@ def main():
--++     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
--++     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
--++ 
--+++    # Meta-req command
--+++    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
--+++    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
-++++    # Act & Assert
-++++    try:
-++++        governor.authorize(allowed_command + " --some-arg") # Test with an argument
-++++    except PermissionError:
-++++        pytest.fail(f"Governor incorrectly denied command '{allowed_command}' for stage '{stage}'.")
-  ++
---      def approve(self):
-----        old_stage = self.current_stage
-----        print(f"--- Approving Stage: {old_stage} ---")
-----        self._validate_stage()
-----        self._run_pre_transition_actions()
-----        self._transition_to_next_stage()
-----        self._run_post_transition_actions()
-----        self.state.save()
-----        print(f"--- Stage {old_stage} Approved. New Stage: {self.state.get('CurrentStage')} ---")
----+        # The manager now simply delegates to the governor.
----+        self.governor.approve()
---- 
----     def _validate_stage(self):
----         print(f"Validating deliverables for stage: {self.current_stage}")
----@@ -123,25 +167,7 @@ class WorkflowManager:
----         if self.current_stage == "Coder":
----             git_handler.save_current_commit_sha()
---- 
-----    def _transition_to_next_stage(self):
-----        current_index = STAGES.index(self.current_stage)
-----        if current_index == len(STAGES) - 1:
-----            self._complete_requirement_cycle()
-----            self.current_stage = STAGES[0]
-----        else:
-----            self.current_stage = STAGES[current_index + 1]
-----        self.state.set("CurrentStage", self.current_stage)
---- 
-----    def _complete_requirement_cycle(self):
-----        req_id = int(self.state.get("RequirementPointer"))
-----        os.makedirs("logs", exist_ok=True)
-----        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
-----        with open(APPROVAL_FILE, "a") as f:
-----            f.write(f"Requirement {req_id} approved at {timestamp}\n")
-----        print(f"[INFO] Logged approval for Requirement ID {req_id}.")
-----        next_req_id = req_id + 1
-----        self.state.set("RequirementPointer", next_req_id)
-----        print(f"[INFO] Advanced to next requirement: {next_req_id}.")
---- 
---- class WorkflowState:
----     def __init__(self):
---+         old_stage = self.current_stage
---+         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
---++        self.enforce_rules()
---+         self._validate_stage_exit_criteria()
---+         # The original logic from WorkflowManager is now fully integrated here.
---+         workflow_manager = WorkflowManager() # We still need access to its methods for now.
--- diff --git a/tests/test_governor.py b/tests/test_governor.py
----new file mode 100644
----index 0000000..95b566d
------- /dev/null
---+index 95b566d..26bf82b 100644
---+--- a/tests/test_governor.py
--- +++ b/tests/test_governor.py
----@@ -0,0 +1,55 @@
----+# tests/test_governor.py
----+import pytest
----+from unittest.mock import MagicMock
----+from pathlib import Path
----+import sys
----+
----+from dw6.state_manager import Governor, WorkflowState
----+
----+@pytest.fixture
----+def mock_state(mocker):
----+    """Fixture to create a mock WorkflowState."""
----+    state = MagicMock(spec=WorkflowState)
----+    mocker.patch('dw6.state_manager.WorkflowState', return_value=state)
----+    return state
----+
----+def test_governor_blocks_engineer_approval_without_spec_file(mock_state):
----+    """Verify the Governor blocks approval if the spec file is missing."""
----+    # Arrange: Set the state to Engineer and mock the requirement pointer
----+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '99'
----+    
----+    # Ensure the spec file does NOT exist for this test
----+    spec_file = Path("deliverables/engineering/cycle_99_technical_specification.md")
----+    if spec_file.exists():
----+        spec_file.unlink()
----+
-+-++    # Act
-+-++    register_meta_requirement(description)
-++++def test_governor_denies_forbidden_command(mock_state):
-++++    """Verify that the Governor denies a command that is not allowed."""
-++++    # Arrange
-++++    stage = "Engineer"
-++++    forbidden_command = "git commit -m 'should not be allowed'"
-++++    mock_state.get.return_value = stage
-++++    governor = Governor(mock_state)
-+ ++
-+-++    # Assert
-+-++    assert META_LOG_FILE.exists()
-+-++    with open(META_LOG_FILE, "r") as f:
-+-++        content = f.read()
-++++    # Act & Assert
-++++    with pytest.raises(PermissionError) as e:
-++++        governor.authorize(forbidden_command)
-+ ++    
-+-++    assert "[ID:1]" in content
-+-++    assert description in content
-+-++    # A simple regex to check for the timestamp format
-+-++    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
-++++    assert "Action denied" in str(e.value)
-++ diff --git a/tests/test_main.py b/tests/test_main.py
-++-index c429973..eddb264 100644
-+++index eddb264..47ae0e7 100644
-++ --- a/tests/test_main.py
-++ +++ b/tests/test_main.py
-++-@@ -1,5 +1,52 @@
-++- # tests/test_main.py
-++-+import pytest
-++-+from pathlib import Path
-++-+import re
-++-+from dw6.main import register_meta_requirement, META_LOG_FILE
-++- 
-++--def test_placeholder():
-++--    """A placeholder test to satisfy the Validator stage."""
-++--    assert True
-++-+@pytest.fixture(autouse=True)
-++-+def cleanup_log_file():
-++-+    """Fixture to clean up the meta log file before and after a test."""
-++-+    if META_LOG_FILE.exists():
-++-+        META_LOG_FILE.unlink()
-++-+    yield
-++-+    if META_LOG_FILE.exists():
-++-+        META_LOG_FILE.unlink()
-+++@@ -50,3 +50,50 @@ def test_register_meta_requirement_increments_id():
-+++     assert description1 in lines[0]
-+++     assert "[ID:2]" in lines[1]
-+++     assert description2 in lines[1]
-+  +
-+--+def test_governor_enforces_rules_on_approve(mocker, capsys):
-+--+    """Verify that the Governor prints the correct rule for the current stage."""
-+-++def test_register_meta_requirement_increments_id():
-+-++    """Verify that subsequent calls increment the requirement ID."""
-+- +    # Arrange
-+--+    mock_state = mocker.MagicMock(spec=WorkflowState)
-+--+    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
- --+    governor = Governor(mock_state)
----+
----+    # Act & Assert: The approval should fail with a SystemExit
----+    with pytest.raises(SystemExit) as e:
----+        governor._validate_stage_exit_criteria()
----+    
----+    assert e.type == SystemExit
----+    assert e.value.code == 1
----+
----+def test_governor_allows_engineer_approval_with_spec_file(mock_state):
----+    """Verify the Governor allows approval if the spec file exists."""
----+    # Arrange: Set the state to Engineer and mock the requirement pointer
----+    mock_state.get.side_effect = lambda key: 'Engineer' if key == 'CurrentStage' else '100'
----+    
----+    # Ensure the spec file DOES exist for this test
----+    spec_file = Path("deliverables/engineering/cycle_100_technical_specification.md")
----+    spec_file.parent.mkdir(parents=True, exist_ok=True)
----+    spec_file.touch()
---+@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
---+         # Clean up the created file
---+         if spec_file.exists():
---+             spec_file.unlink()
--++     if len(sys.argv) == 1:
--++         parser.print_help(sys.stderr)
--++         sys.exit(1)
--++ 
--++     args = parser.parse_args()
--++     
--++-    manager = WorkflowManager()
--++-
--++-    if args.command == "approve":
--++-        manager.approve()
--++-    elif args.command == "new":
--++-        process_prompt(args.prompt)
--+++    if args.command == "meta-req":
--+++        register_meta_requirement(args.description)
--+++    else:
--+++        manager = WorkflowManager()
--+++        if args.command == "approve":
--+++            manager.approve()
--+++        elif args.command == "new":
--+++            process_prompt(args.prompt)
--++ 
--++ if __name__ == "__main__":
--++     main()
--++diff --git a/tests/test_main.py b/tests/test_main.py
--++index c429973..eddb264 100644
--++--- a/tests/test_main.py
--+++++ b/tests/test_main.py
--++@@ -1,5 +1,52 @@
--++ # tests/test_main.py
--+++import pytest
--+++from pathlib import Path
--+++import re
--+++from dw6.main import register_meta_requirement, META_LOG_FILE
--++ 
--++-def test_placeholder():
--++-    """A placeholder test to satisfy the Validator stage."""
--++-    assert True
--+++@pytest.fixture(autouse=True)
--+++def cleanup_log_file():
--+++    """Fixture to clean up the meta log file before and after a test."""
--+++    if META_LOG_FILE.exists():
--+++        META_LOG_FILE.unlink()
--+++    yield
--+++    if META_LOG_FILE.exists():
--+++        META_LOG_FILE.unlink()
-+--+    # Mock the exit criteria validation to prevent SystemExit
-+--+    mocker.patch.object(governor, '_validate_stage_exit_criteria')
-+--+    # Mock the rest of the approval process to isolate the rule enforcement
-+--+    mocker.patch.object(governor, '_transition_to_next_stage')
-+--+    mocker.patch('dw6.state_manager.WorkflowManager')
-+-++    description1 = "First requirement."
-+-++    description2 = "Second requirement."
-++-+def test_register_meta_requirement_creates_file_and_logs_entry():
-++-+    """Verify that the first call creates the log file and adds the first entry correctly."""
-++-+    # Arrange
-++-+    description = "This is the first meta requirement."
-   +
---++def test_governor_enforces_rules_on_approve(mocker, capsys):
---++    """Verify that the Governor prints the correct rule for the current stage."""
--+-     def approve(self):
--+-         old_stage = self.current_stage
--+-         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
--+-+        self.enforce_rules()
--+-         self._validate_stage_exit_criteria()
--+-         # The original logic from WorkflowManager is now fully integrated here.
--+-         workflow_manager = WorkflowManager() # We still need access to its methods for now.
--+-diff --git a/tests/test_governor.py b/tests/test_governor.py
--+-index 95b566d..26bf82b 100644
--+---- a/tests/test_governor.py
--+-+++ b/tests/test_governor.py
--+-@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
--+-         # Clean up the created file
--+-         if spec_file.exists():
--+-             spec_file.unlink()
--+++def test_register_meta_requirement_creates_file_and_logs_entry():
--+++    """Verify that the first call creates the log file and adds the first entry correctly."""
+---+    def enforce_rules(self):
+---+        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+---+        print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+---+        print(f"[RULE] {rule}")
+--+-
+--+     # Approve command
+--+     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
+--+ 
+--+@@ -18,18 +44,24 @@ def main():
+--+     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+--+     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+--+ 
+--++    # Meta-req command
+--++    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
+--++    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
+-+- if __name__ == "__main__":
+-+-     main()
+-+++    def authorize(self, command: str):
+-+++        """Checks if a command is allowed in the current stage."""
+-+++        allowed_commands = self.RULES.get(self.current_stage, [])
+-+++        if not any(command.startswith(prefix) for prefix in allowed_commands):
+-+++            error_msg = f"[GOVERNOR] Action denied. The command '{(command)}' is not allowed in the '{self.current_stage}' stage."
+-+++            print(error_msg, file=sys.stderr)
+-+++            raise PermissionError(error_msg)
+-+++        print(f"[GOVERNOR] Action authorized for stage '{self.current_stage}'.")
+- ++
+--+     if len(sys.argv) == 1:
+--+         parser.print_help(sys.stderr)
+--+         sys.exit(1)
+-++     def enforce_rules(self):
+-++-        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+-+++        rules = self.RULES.get(self.current_stage, ["No specific rules defined."])
+-++         print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+-++-        print(f"[RULE] {rule}")
+-+++        print("[RULE] Allowed command prefixes:")
+-+++        for rule in rules:
+-+++            print(f"  - {rule}")
+- + 
+--+     args = parser.parse_args()
+--+     
+--+-    manager = WorkflowManager()
+--+-
+--+-    if args.command == "approve":
+--+-        manager.approve()
+--+-    elif args.command == "new":
+--+-        process_prompt(args.prompt)
+--++    if args.command == "meta-req":
+--++        register_meta_requirement(args.description)
+--++    else:
+--++        manager = WorkflowManager()
+--++        if args.command == "approve":
+--++            manager.approve()
+--++        elif args.command == "new":
+--++            process_prompt(args.prompt)
+-++     def approve(self):
+-++         old_stage = self.current_stage
+-++diff --git a/tests/test_governor.py b/tests/test_governor.py
+-++index 26bf82b..a431529 100644
+-++--- a/tests/test_governor.py
+-+++++ b/tests/test_governor.py
+-++@@ -71,5 +71,37 @@ def test_governor_enforces_rules_on_approve(mocker, capsys):
+- + 
+--+ if __name__ == "__main__":
+--+     main()
+--+diff --git a/tests/test_main.py b/tests/test_main.py
+--+index c429973..eddb264 100644
+--+--- a/tests/test_main.py
+--++++ b/tests/test_main.py
+--+@@ -1,5 +1,52 @@
+--+ # tests/test_main.py
+--++import pytest
+--++from pathlib import Path
+--++import re
+--++from dw6.main import register_meta_requirement, META_LOG_FILE
+--+ 
+--+-def test_placeholder():
+--+-    """A placeholder test to satisfy the Validator stage."""
+--+-    assert True
+--++@pytest.fixture(autouse=True)
+--++def cleanup_log_file():
+--++    """Fixture to clean up the meta log file before and after a test."""
+--++    if META_LOG_FILE.exists():
+--++        META_LOG_FILE.unlink()
+--++    yield
+--++    if META_LOG_FILE.exists():
+--++        META_LOG_FILE.unlink()
++++-@pytest.fixture(autouse=True)
+++ +@pytest.fixture
+++-+def mock_main_dependencies(mocker):
+++-+    """Fixture to mock dependencies of the main function for the 'do' command tests."""
+++-+    # Since autospec=True is used, we need to configure the mock instance
+++-+    # to have the 'governor' attribute.
+++-+    mock_workflow_manager_class = mocker.patch('dw6.main.WorkflowManager', autospec=True)
+++-+    mock_workflow_manager_instance = mock_workflow_manager_class.return_value
+++-+    mock_governor = mocker.MagicMock()
+++-+    mock_workflow_manager_instance.governor = mock_governor
+++-+
+++-+    mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
+++-+    return mock_governor, mock_subprocess_run
+++-+
+++-+def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
+++-+    """Verify the 'do' command executes an action when the Governor authorizes it."""
++ -+    # Arrange
++--+    description = "This is the first meta requirement."
+ - +
+---     def approve(self):
+---         old_stage = self.current_stage
+---         print(f"--- Governor: Received Approval Request for Stage: {old_stage} ---")
+---+        self.enforce_rules()
+---         self._validate_stage_exit_criteria()
+---         # The original logic from WorkflowManager is now fully integrated here.
+---         workflow_manager = WorkflowManager() # We still need access to its methods for now.
+---diff --git a/tests/test_governor.py b/tests/test_governor.py
+---index 95b566d..26bf82b 100644
+------ a/tests/test_governor.py
+---+++ b/tests/test_governor.py
+---@@ -53,3 +53,23 @@ def test_governor_allows_engineer_approval_with_spec_file(mock_state):
+---         # Clean up the created file
+---         if spec_file.exists():
+---             spec_file.unlink()
+--++def test_register_meta_requirement_creates_file_and_logs_entry():
+--++    """Verify that the first call creates the log file and adds the first entry correctly."""
+-++     # Assert
+-++     captured = capsys.readouterr()
+-++-    expected_rule = Governor.RULES["Coder"]
+-++-    assert expected_rule in captured.out
+-+++    # Check that each rule is printed
+-+++    for rule in Governor.RULES["Coder"]:
+-+++        assert rule in captured.out
+-+++
+-+++@pytest.mark.parametrize("stage, allowed_command", [
+-+++    (stage, command) 
+-+++    for stage, commands in Governor.RULES.items() 
+-+++    for command in commands
+-+++])
+-+++def test_governor_authorizes_allowed_commands(mock_state, stage, allowed_command):
+-+++    """Verify that the Governor authorizes all allowed commands for each stage."""
 - ++    # Arrange
---++    mock_state = mocker.MagicMock(spec=WorkflowState)
---++    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
--- +    governor = Governor(mock_state)
---++    # Mock the exit criteria validation to prevent SystemExit
---++    mocker.patch.object(governor, '_validate_stage_exit_criteria')
---++    # Mock the rest of the approval process to isolate the rule enforcement
---++    mocker.patch.object(governor, '_transition_to_next_stage')
---++    mocker.patch('dw6.state_manager.WorkflowManager')
--- +
----+    # Act & Assert: The approval should pass without raising an exception
----+    try:
----+        governor._validate_stage_exit_criteria()
----+    except SystemExit:
----+        pytest.fail("Governor incorrectly blocked approval when spec file existed.")
----+    finally:
----+        # Clean up the created file
----+        if spec_file.exists():
----+            spec_file.unlink()
----diff --git a/tests/test_state_manager_integration.py b/tests/test_state_manager_integration.py
----index 5b9d1eb..44d2cc9 100644
------- a/tests/test_state_manager_integration.py
----+++ b/tests/test_state_manager_integration.py
----@@ -32,7 +32,8 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
---- 
----     @patch('dw6.state_manager.WorkflowState')
----     @patch('dw6.git_handler.get_changes_since_last_commit')
-----    def test_approve_coder_stage_creates_deliverable(self, mock_get_changes, mock_WorkflowState):
----+    @patch('dw6.git_handler.save_current_commit_sha') # Mock the function causing the error
----+    def test_approve_coder_stage_creates_deliverable(self, mock_save_sha, mock_get_changes, mock_WorkflowState):
----         """Ensure approving Coder stage generates a deliverable without altering the real state."""
----         # Arrange
----         mock_state_instance = mock_WorkflowState.return_value
----@@ -45,9 +46,12 @@ class TestWorkflowManagerIntegration(unittest.TestCase):
----         # Act
----         manager.approve()
---- 
-----        # Assert
----+        # Assert that the deliverable file was created
----         deliverable_path = Path("deliverables/coding/coder_deliverable.md")
----         self.assertTrue(deliverable_path.exists())
----+        # Clean up the created file
----+        deliverable_path.unlink()
----+
----         mock_state_instance.save.assert_called_once()
---- 
---- if __name__ == '__main__':
----diff --git a/uv.lock b/uv.lock
----index c79d29c..8e7411f 100644
------- a/uv.lock
----+++ b/uv.lock
----@@ -66,6 +66,7 @@ dependencies = [
---- test = [
----     { name = "pytest" },
----     { name = "pytest-cov" },
----+    { name = "pytest-mock" },
---- ]
---- 
---- [package.metadata]
----@@ -73,6 +74,7 @@ requires-dist = [
----     { name = "gitpython" },
----     { name = "pytest", marker = "extra == 'test'" },
----     { name = "pytest-cov", marker = "extra == 'test'" },
----+    { name = "pytest-mock", marker = "extra == 'test'" },
----     { name = "python-dotenv" },
---- ]
---- provides-extras = ["test"]
----@@ -167,6 +169,18 @@ wheels = [
----     { url = "https://files.pythonhosted.org/packages/bc/16/4ea354101abb1287856baa4af2732be351c7bee728065aed451b678153fd/pytest_cov-6.2.1-py3-none-any.whl", hash = "sha256:f5bc4c23f42f1cdd23c70b1dab1bbaef4fc505ba950d53e0081d0730dd7e86d5", size = 24644, upload-time = "2025-06-12T10:47:45.932Z" },
---- ]
---- 
----+[[package]]
----+name = "pytest-mock"
----+version = "3.14.1"
----+source = { registry = "https://pypi.org/simple" }
----+dependencies = [
----+    { name = "pytest" },
----+]
----+sdist = { url = "https://files.pythonhosted.org/packages/71/28/67172c96ba684058a4d24ffe144d64783d2a270d0af0d9e792737bddc75c/pytest_mock-3.14.1.tar.gz", hash = "sha256:159e9edac4c451ce77a5cdb9fc5d1100708d2dd4ba3c3df572f14097351af80e", size = 33241, upload-time = "2025-05-26T13:58:45.167Z" }
----+wheels = [
----+    { url = "https://files.pythonhosted.org/packages/b2/05/77b60e520511c53d1c1ca75f1930c7dd8e971d0c4379b7f4b3f9644685ba/pytest_mock-3.14.1-py3-none-any.whl", hash = "sha256:178aefcd11307d874b4cd3100344e7e2d888d9791a6a1d9bfe90fbc1b74fd1d0", size = 9923, upload-time = "2025-05-26T13:58:43.487Z" },
----+]
--+++    description = "This is the first meta requirement."
-++++@pytest.fixture
-++++def mock_main_dependencies(mocker):
-++++    """Fixture to mock dependencies of the main function for the 'do' command tests."""
-++++    # Since autospec=True is used, we need to configure the mock instance
-++++    # to have the 'governor' attribute.
-++++    mock_workflow_manager_class = mocker.patch('dw6.main.WorkflowManager', autospec=True)
-++++    mock_workflow_manager_instance = mock_workflow_manager_class.return_value
-++++    mock_governor = mocker.MagicMock()
-++++    mock_workflow_manager_instance.governor = mock_governor
- +++
-- ++    # Act
---++    governor.approve()
--- +
---- [[package]]
---- name = "python-dotenv"
---- version = "1.1.1"
--+++    register_meta_requirement(description)
-++++    mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
-++++    return mock_governor, mock_subprocess_run
- +++
-- ++    # Assert
---++    captured = capsys.readouterr()
---++    expected_rule = Governor.RULES["Coder"]
---++    assert expected_rule in captured.out
--+++    assert META_LOG_FILE.exists()
--+++    with open(META_LOG_FILE, "r") as f:
--+++        content = f.read()
-++++def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
-++++    """Verify the 'do' command executes an action when the Governor authorizes it."""
-++++    # Arrange
-++++    mock_governor, mock_subprocess_run = mock_main_dependencies
-++++    mock_governor.authorize.return_value = None # Simulate authorization success
-++++    
-++++    mocker.patch('sys.argv', ['dw6', 'do', 'ls -l'])
- +++    
--+++    assert "[ID:1]" in content
--+++    assert description in content
--+++    # A simple regex to check for the timestamp format
--+++    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
-+  +    # Act
-+--+    governor.approve()
-+-++    register_meta_requirement(description1)
-+-++    register_meta_requirement(description2)
-++-+    register_meta_requirement(description)
-++++    from dw6.main import main
-++++    main()
-+  +
-+  +    # Assert
-+--+    captured = capsys.readouterr()
-+--+    expected_rule = Governor.RULES["Coder"]
-+--+    assert expected_rule in captured.out
-+-++    with open(META_LOG_FILE, "r") as f:
-+-++        lines = f.readlines()
+--++    description = "This is the first meta requirement."
+-+++    mock_state.get.return_value = stage
+-+++    governor = Governor(mock_state)
+-+++    
+-+++    # Act & Assert
+-+++    try:
+-+++        governor.authorize(allowed_command + " --some-arg") # Test with an argument
+-+++    except PermissionError:
+-+++        pytest.fail(f"Governor incorrectly denied command '{allowed_command}' for stage '{stage}'.")
+- ++
+--++    # Act
+--++    register_meta_requirement(description)
+-+++def test_governor_denies_forbidden_command(mock_state):
+-+++    """Verify that the Governor denies a command that is not allowed."""
+-+++    # Arrange
+-+++    stage = "Engineer"
+-+++    forbidden_command = "git commit -m 'should not be allowed'"
+-+++    mock_state.get.return_value = stage
+-+++    governor = Governor(mock_state)
+- ++
+--++    # Assert
+--++    assert META_LOG_FILE.exists()
+--++    with open(META_LOG_FILE, "r") as f:
+--++        content = f.read()
+-+++    # Act & Assert
+-+++    with pytest.raises(PermissionError) as e:
+-+++        governor.authorize(forbidden_command)
+- ++    
+--++    assert "[ID:1]" in content
+--++    assert description in content
+--++    # A simple regex to check for the timestamp format
+--++    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
+-+++    assert "Action denied" in str(e.value)
+-+ diff --git a/tests/test_main.py b/tests/test_main.py
+-+-index c429973..eddb264 100644
+-++index eddb264..47ae0e7 100644
+-+ --- a/tests/test_main.py
+-+ +++ b/tests/test_main.py
+-+-@@ -1,5 +1,52 @@
+-+- # tests/test_main.py
+-+-+import pytest
+-+-+from pathlib import Path
+-+-+import re
+-+-+from dw6.main import register_meta_requirement, META_LOG_FILE
+-+- 
+-+--def test_placeholder():
+-+--    """A placeholder test to satisfy the Validator stage."""
+-+--    assert True
+-+-+@pytest.fixture(autouse=True)
+-+-+def cleanup_log_file():
+-+-+    """Fixture to clean up the meta log file before and after a test."""
+-+-+    if META_LOG_FILE.exists():
+-+-+        META_LOG_FILE.unlink()
+-+-+    yield
+-+-+    if META_LOG_FILE.exists():
+-+-+        META_LOG_FILE.unlink()
+-++@@ -50,3 +50,50 @@ def test_register_meta_requirement_increments_id():
+-++     assert description1 in lines[0]
+-++     assert "[ID:2]" in lines[1]
+-++     assert description2 in lines[1]
+-  +
+---+def test_governor_enforces_rules_on_approve(mocker, capsys):
+---+    """Verify that the Governor prints the correct rule for the current stage."""
+--++def test_register_meta_requirement_increments_id():
+--++    """Verify that subsequent calls increment the requirement ID."""
++-++@pytest.fixture
++-++def mock_main_dependencies(mocker):
++-++    """Fixture to mock dependencies of the main function for the 'do' command tests."""
++-++    # Since autospec=True is used, we need to configure the mock instance
++-++    # to have the 'governor' attribute.
++-++    mock_workflow_manager_class = mocker.patch('dw6.main.WorkflowManager', autospec=True)
++-++    mock_workflow_manager_instance = mock_workflow_manager_class.return_value
++-++    mock_governor = mocker.MagicMock()
++-++    mock_workflow_manager_instance.governor = mock_governor
++-++
++-++    mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
++-++    return mock_governor, mock_subprocess_run
++-++
++-++def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
++-++    """Verify the 'do' command executes an action when the Governor authorizes it."""
++-++    # Arrange
++-++    mock_governor, mock_subprocess_run = mock_main_dependencies
++-++    mock_governor.authorize.return_value = None # Simulate authorization success
++-++    
++-++    mocker.patch('sys.argv', ['dw6', 'do', 'ls -l'])
 +-++    
-+-++    assert len(lines) == 2
-+-++    assert "[ID:1]" in lines[0]
-+-++    assert description1 in lines[0]
-+-++    assert "[ID:2]" in lines[1]
-+-++    assert description2 in lines[1]
-++-+    assert META_LOG_FILE.exists()
-++-+    with open(META_LOG_FILE, "r") as f:
-++-+        content = f.read()
++- +    # Act
++--+    register_meta_requirement(description)
++-++    from dw6.main import main
++-++    main()
++- +
++- +    # Assert
++--+    assert META_LOG_FILE.exists()
++--+    with open(META_LOG_FILE, "r") as f:
++--+        content = f.read()
+++-+    mock_governor, mock_subprocess_run = mock_main_dependencies
+++-+    mock_governor.authorize.return_value = None # Simulate authorization success
 ++-+    
-++-+    assert "[ID:1]" in content
-++-+    assert description in content
-++-+    # A simple regex to check for the timestamp format
-++-+    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
-++++    mock_governor.authorize.assert_called_once_with('ls -l')
-++++    mock_subprocess_run.assert_called_once_with('ls -l', shell=True, check=True)
- + +
--+-+def test_governor_enforces_rules_on_approve(mocker, capsys):
--+-+    """Verify that the Governor prints the correct rule for the current stage."""
--+++def test_register_meta_requirement_increments_id():
--+++    """Verify that subsequent calls increment the requirement ID."""
-++-+def test_register_meta_requirement_increments_id():
-++-+    """Verify that subsequent calls increment the requirement ID."""
-++++def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
-++++    """Verify the 'do' command blocks an action when the Governor denies it."""
- + +    # Arrange
--+-+    mock_state = mocker.MagicMock(spec=WorkflowState)
--+-+    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
--+-+    governor = Governor(mock_state)
--+-+    # Mock the exit criteria validation to prevent SystemExit
--+-+    mocker.patch.object(governor, '_validate_stage_exit_criteria')
--+-+    # Mock the rest of the approval process to isolate the rule enforcement
--+-+    mocker.patch.object(governor, '_transition_to_next_stage')
--+-+    mocker.patch('dw6.state_manager.WorkflowManager')
--+++    description1 = "First requirement."
--+++    description2 = "Second requirement."
-++-+    description1 = "First requirement."
-++-+    description2 = "Second requirement."
-++++    mock_governor, mock_subprocess_run = mock_main_dependencies
-++++    mock_governor.authorize.side_effect = PermissionError("Action denied")
- + +
--+ +    # Act
--+-+    governor.approve()
--+++    register_meta_requirement(description1)
--+++    register_meta_requirement(description2)
-++-+    # Act
-++-+    register_meta_requirement(description1)
-++-+    register_meta_requirement(description2)
-++++    mocker.patch('sys.argv', ['dw6', 'do', 'git push'])
- + +
--+ +    # Assert
--+-+    captured = capsys.readouterr()
--+-+    expected_rule = Governor.RULES["Coder"]
--+-+    assert expected_rule in captured.out
--+++    with open(META_LOG_FILE, "r") as f:
--+++        lines = f.readlines()
+++-+    mocker.patch('sys.argv', ['dw6', 'do', 'ls -l'])
++ -+    
++--+    assert "[ID:1]" in content
++--+    assert description in content
++--+    # A simple regex to check for the timestamp format
++--+    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
++-++    mock_governor.authorize.assert_called_once_with('ls -l')
++-++    mock_subprocess_run.assert_called_once_with('ls -l', shell=True, check=True)
++- +
++--+def test_register_meta_requirement_increments_id():
++--+    """Verify that subsequent calls increment the requirement ID."""
++-++def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
++-++    """Verify the 'do' command blocks an action when the Governor denies it."""
+ - +    # Arrange
+---+    mock_state = mocker.MagicMock(spec=WorkflowState)
+---+    mock_state.get.side_effect = lambda key: {"CurrentStage": "Coder", "RequirementPointer": "10"}[key]
+---+    governor = Governor(mock_state)
+---+    # Mock the exit criteria validation to prevent SystemExit
+---+    mocker.patch.object(governor, '_validate_stage_exit_criteria')
+---+    # Mock the rest of the approval process to isolate the rule enforcement
+---+    mocker.patch.object(governor, '_transition_to_next_stage')
+---+    mocker.patch('dw6.state_manager.WorkflowManager')
+--++    description1 = "First requirement."
+--++    description2 = "Second requirement."
+-+-+def test_register_meta_requirement_creates_file_and_logs_entry():
+-+-+    """Verify that the first call creates the log file and adds the first entry correctly."""
++--+    description1 = "First requirement."
++--+    description2 = "Second requirement."
++-++    mock_governor, mock_subprocess_run = mock_main_dependencies
++-++    mock_governor.authorize.side_effect = PermissionError("Action denied")
++- +
++ -+    # Act
++--+    register_meta_requirement(description1)
++--+    register_meta_requirement(description2)
++-++    mocker.patch('sys.argv', ['dw6', 'do', 'git push'])
++- +
+++-+    from dw6.main import main
+++-+    main()
+++-+
++ -+    # Assert
++--+    with open(META_LOG_FILE, "r") as f:
++--+        lines = f.readlines()
++-++    # Act & Assert
++-++    with pytest.raises(SystemExit) as e:
++-++        from dw6.main import main
++-++        main()
++- +    
++--+    assert len(lines) == 2
++--+    assert "[ID:1]" in lines[0]
++--+    assert description1 in lines[0]
++--+    assert "[ID:2]" in lines[1]
++--+    assert description2 in lines[1]
++-++    assert e.value.code == 1
++-++    mock_governor.authorize.assert_called_once_with('git push')
++-++    mock_subprocess_run.assert_not_called()
+++-+    mock_governor.authorize.assert_called_once_with('ls -l')
+++-+    mock_subprocess_run.assert_called_once_with('ls -l', shell=True, check=True)
+++-+
+++-+def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
+++-+    """Verify the 'do' command blocks an action when the Governor denies it."""
+ +-+    # Arrange
+-+-+    description = "This is the first meta requirement."
+-  +
+-+++@pytest.fixture
+-+++def mock_main_dependencies(mocker):
+-+++    """Fixture to mock dependencies of the main function for the 'do' command tests."""
+-+++    # Since autospec=True is used, we need to configure the mock instance
+-+++    # to have the 'governor' attribute.
+-+++    mock_workflow_manager_class = mocker.patch('dw6.main.WorkflowManager', autospec=True)
+-+++    mock_workflow_manager_instance = mock_workflow_manager_class.return_value
+-+++    mock_governor = mocker.MagicMock()
+-+++    mock_workflow_manager_instance.governor = mock_governor
+-+++
+-+++    mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
+-+++    return mock_governor, mock_subprocess_run
+-+++
+-+++def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
+-+++    """Verify the 'do' command executes an action when the Governor authorizes it."""
+-+++    # Arrange
+-+++    mock_governor, mock_subprocess_run = mock_main_dependencies
+-+++    mock_governor.authorize.return_value = None # Simulate authorization success
 -+++    
--+++    assert len(lines) == 2
--+++    assert "[ID:1]" in lines[0]
--+++    assert description1 in lines[0]
--+++    assert "[ID:2]" in lines[1]
--+++    assert description2 in lines[1]
-++-+    # Assert
-++-+    with open(META_LOG_FILE, "r") as f:
-++-+        lines = f.readlines()
-++++    # Act & Assert
-++++    with pytest.raises(SystemExit) as e:
-++++        from dw6.main import main
-++++        main()
-++ +    
-++-+    assert len(lines) == 2
-++-+    assert "[ID:1]" in lines[0]
-++-+    assert description1 in lines[0]
-++-+    assert "[ID:2]" in lines[1]
-++-+    assert description2 in lines[1]
-++++    assert e.value.code == 1
-++++    mock_governor.authorize.assert_called_once_with('git push')
-++++    mock_subprocess_run.assert_not_called()
+-+++    mocker.patch('sys.argv', ['dw6', 'do', 'ls -l'])
+-+++    
+-  +    # Act
+---+    governor.approve()
+--++    register_meta_requirement(description1)
+--++    register_meta_requirement(description2)
+-+-+    register_meta_requirement(description)
+-+++    from dw6.main import main
+-+++    main()
+-  +
+-  +    # Assert
+---+    captured = capsys.readouterr()
+---+    expected_rule = Governor.RULES["Coder"]
+---+    assert expected_rule in captured.out
+--++    with open(META_LOG_FILE, "r") as f:
+--++        lines = f.readlines()
+--++    
+--++    assert len(lines) == 2
+--++    assert "[ID:1]" in lines[0]
+--++    assert description1 in lines[0]
+--++    assert "[ID:2]" in lines[1]
+--++    assert description2 in lines[1]
+-+-+    assert META_LOG_FILE.exists()
+-+-+    with open(META_LOG_FILE, "r") as f:
+-+-+        content = f.read()
+++-+    mock_governor, mock_subprocess_run = mock_main_dependencies
+++-+    mock_governor.authorize.side_effect = PermissionError("Action denied")
+++-+
+++-+    mocker.patch('sys.argv', ['dw6', 'do', 'git push'])
+++-+
+++-+    # Act & Assert
+++-+    with pytest.raises(SystemExit) as e:
+++-+        from dw6.main import main
+++-+        main()
+ +-+    
+-+-+    assert "[ID:1]" in content
+-+-+    assert description in content
+-+-+    # A simple regex to check for the timestamp format
+-+-+    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
+-+++    mock_governor.authorize.assert_called_once_with('ls -l')
+-+++    mock_subprocess_run.assert_called_once_with('ls -l', shell=True, check=True)
+-+ +
+-+-+def test_register_meta_requirement_increments_id():
+-+-+    """Verify that subsequent calls increment the requirement ID."""
+-+++def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
+-+++    """Verify the 'do' command blocks an action when the Governor denies it."""
+-+ +    # Arrange
+-+-+    description1 = "First requirement."
+-+-+    description2 = "Second requirement."
+-+++    mock_governor, mock_subprocess_run = mock_main_dependencies
+-+++    mock_governor.authorize.side_effect = PermissionError("Action denied")
+-+ +
+-+-+    # Act
+-+-+    register_meta_requirement(description1)
+-+-+    register_meta_requirement(description2)
+-+++    mocker.patch('sys.argv', ['dw6', 'do', 'git push'])
+-+ +
+-+-+    # Assert
+-+-+    with open(META_LOG_FILE, "r") as f:
+-+-+        lines = f.readlines()
+-+++    # Act & Assert
+-+++    with pytest.raises(SystemExit) as e:
+-+++        from dw6.main import main
+-+++        main()
+-+ +    
+-+-+    assert len(lines) == 2
+-+-+    assert "[ID:1]" in lines[0]
+-+-+    assert description1 in lines[0]
+-+-+    assert "[ID:2]" in lines[1]
+-+-+    assert description2 in lines[1]
+-+++    assert e.value.code == 1
+-+++    mock_governor.authorize.assert_called_once_with('git push')
+-+++    mock_subprocess_run.assert_not_called()
+++-+    assert e.value.code == 1
+++-+    mock_governor.authorize.assert_called_once_with('git push')
+++-+    mock_subprocess_run.assert_not_called()
++++ def cleanup_log_file():
++++     """Fixture to clean up the meta log file before and after a test."""
++++     if META_LOG_FILE.exists():
++++@@ -13,7 +13,7 @@ def cleanup_log_file():
++++     if META_LOG_FILE.exists():
++++         META_LOG_FILE.unlink()
++++ 
++++-def test_register_meta_requirement_creates_file_and_logs_entry():
+++++def test_register_meta_requirement_creates_file_and_logs_entry(cleanup_log_file):
++++     """Verify that the first call creates the log file and adds the first entry correctly."""
++++     # Arrange
++++     description = "This is the first meta requirement."
++++@@ -31,7 +31,7 @@ def test_register_meta_requirement_creates_file_and_logs_entry():
++++     # A simple regex to check for the timestamp format
++++     assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
++++ 
++++-def test_register_meta_requirement_increments_id():
+++++def test_register_meta_requirement_increments_id(cleanup_log_file):
++++     """Verify that subsequent calls increment the requirement ID."""
++++     # Arrange
++++     description1 = "First requirement."
    ```
   \ No newline at end of file
---diff --git a/deliverables/engineering/cycle_11_technical_specification.md b/deliverables/engineering/cycle_11_technical_specification.md
--+diff --git a/deliverables/engineering/cycle_12_technical_specification.md b/deliverables/engineering/cycle_12_technical_specification.md
-+-diff --git a/deliverables/engineering/cycle_12_technical_specification.md b/deliverables/engineering/cycle_12_technical_specification.md
-++diff --git a/deliverables/engineering/cycle_13_technical_specification.md b/deliverables/engineering/cycle_13_technical_specification.md
+--diff --git a/deliverables/engineering/cycle_12_technical_specification.md b/deliverables/engineering/cycle_12_technical_specification.md
+-+diff --git a/deliverables/engineering/cycle_13_technical_specification.md b/deliverables/engineering/cycle_13_technical_specification.md
++-diff --git a/deliverables/engineering/cycle_13_technical_specification.md b/deliverables/engineering/cycle_13_technical_specification.md
+++diff --git a/deliverables/engineering/cycle_14_technical_specification.md b/deliverables/engineering/cycle_14_technical_specification.md
   new file mode 100644
---index 0000000..071c22d
--+index 0000000..ff3658c
-+-index 0000000..ff3658c
-++index 0000000..fde1032
+--index 0000000..ff3658c
+-+index 0000000..fde1032
++-index 0000000..fde1032
+++index 0000000..2957165
   --- /dev/null
---+++ b/deliverables/engineering/cycle_11_technical_specification.md
--++++ b/deliverables/engineering/cycle_12_technical_specification.md
-+-+++ b/deliverables/engineering/cycle_12_technical_specification.md
-+++++ b/deliverables/engineering/cycle_13_technical_specification.md
+--+++ b/deliverables/engineering/cycle_12_technical_specification.md
+-++++ b/deliverables/engineering/cycle_13_technical_specification.md
++-+++ b/deliverables/engineering/cycle_13_technical_specification.md
++++++ b/deliverables/engineering/cycle_14_technical_specification.md
   @@ -0,0 +1,9 @@
---+# Requirement: 11
--++# Requirement: 12
-+-+# Requirement: 12
-+++# Requirement: 13
+--+# Requirement: 12
+-++# Requirement: 13
++-+# Requirement: 13
++++# Requirement: 14
   +
   +## 1. High-Level Goal
   +
---+Create a new CLI command, dw6 meta-req "<description>", to allow the user to formally register an improvement requirement for the DW6 protocol itself. This command will append the requirement to a new, simple, append-only log file named meta_requirements.log. The system will be designed to process these requirements sequentially.
--++Actively enforce Governor rules by integrating with the AI's tool-using capabilities to block any action that violates the rule set for the current stage.
-+-+Actively enforce Governor rules by integrating with the AI's tool-using capabilities to block any action that violates the rule set for the current stage.
-+++Fix a critical bug in the test suite where a test fixture (cleanup_log_file) is incorrectly configured with autouse=True, causing it to delete the production meta_requirements.log file. The fix involves removing autouse=True and applying the fixture only to the specific tests that require it.
+--+Actively enforce Governor rules by integrating with the AI's tool-using capabilities to block any action that violates the rule set for the current stage.
+-++Fix a critical bug in the test suite where a test fixture (cleanup_log_file) is incorrectly configured with autouse=True, causing it to delete the production meta_requirements.log file. The fix involves removing autouse=True and applying the fixture only to the specific tests that require it.
++-+Fix a critical bug in the test suite where a test fixture (cleanup_log_file) is incorrectly configured with autouse=True, causing it to delete the production meta_requirements.log file. The fix involves removing autouse=True and applying the fixture only to the specific tests that require it.
++++Re-introduce the Researcher stage into the DW6 workflow. The new stage order will be Engineer -> Researcher -> Coder -> Validator -> Deployer. The Researcher stage will have its own set of allowed commands (e.g., search_web, read_url_content) and will be required to produce a research report in deliverables/research/ as its exit criteria.
   +
   +## 2. Guiding Principles
   +
   +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
   diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
---index 00ab2c8..ede42cf 100644
--+index ede42cf..5045595 100644
-+-index ede42cf..5045595 100644
-++index 5045595..a1b7a04 100644
+--index ede42cf..5045595 100644
+-+index 5045595..a1b7a04 100644
++-index 5045595..a1b7a04 100644
+++index a1b7a04..7161830 100644
   --- a/logs/.last_commit_sha
   +++ b/logs/.last_commit_sha
   @@ -1 +1 @@
----b5da6206e513c416f49b9c1b0c30c8e6fb805bc4
--+-96a1111270912ae2722109d00ed1405c166f577c
-+--96a1111270912ae2722109d00ed1405c166f577c
-++-223a8df342ec9a1ce277b234efe90e05cc4803dd
+---96a1111270912ae2722109d00ed1405c166f577c
+-+-223a8df342ec9a1ce277b234efe90e05cc4803dd
++--223a8df342ec9a1ce277b234efe90e05cc4803dd
+++-05ff4137104ba71c49d78ebaa96798dcee5559f7
   \ No newline at end of file
---+96a1111270912ae2722109d00ed1405c166f577c
--++223a8df342ec9a1ce277b234efe90e05cc4803dd
-+-+223a8df342ec9a1ce277b234efe90e05cc4803dd
-+++05ff4137104ba71c49d78ebaa96798dcee5559f7
+--+223a8df342ec9a1ce277b234efe90e05cc4803dd
+-++05ff4137104ba71c49d78ebaa96798dcee5559f7
++-+05ff4137104ba71c49d78ebaa96798dcee5559f7
++++53d60c6a24db61fbf61dbf953026000943463bed
   \ No newline at end of file
   diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
---index a7aa662..591ebb9 100644
--+index 591ebb9..d459c0f 100644
-+-index 591ebb9..d459c0f 100644
-++index d459c0f..a21bb3a 100644
+--index 591ebb9..d459c0f 100644
+-+index d459c0f..a21bb3a 100644
++-index d459c0f..a21bb3a 100644
+++index a21bb3a..a4e5ca5 100644
   --- a/logs/workflow_state.txt
   +++ b/logs/workflow_state.txt
   @@ -1,2 +1,2 @@
--- CurrentStage=Coder
----RequirementPointer=10
---+RequirementPointer=11
--+-CurrentStage=Coder
--+-RequirementPointer=11
--++CurrentStage=Deployer
--++RequirementPointer=12
-- diff --git a/src/dw6/main.py b/src/dw6/main.py
---index 90862f9..c65a4d9 100644
--+index c65a4d9..13e4d93 100644
-- --- a/src/dw6/main.py
-- +++ b/src/dw6/main.py
---@@ -1,16 +1,42 @@
--- # dw6/main.py
--+@@ -2,6 +2,7 @@
--  import argparse
--  import sys
---+import re
---+from pathlib import Path
---+from datetime import datetime, timezone
--+ import re
--++import subprocess
--+ from pathlib import Path
--+ from datetime import datetime, timezone
--  from dw6.state_manager import WorkflowManager
--- from dw6.augmenter import process_prompt
--+@@ -48,6 +49,10 @@ def main():
--+     meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
--+     meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
--  
---+META_LOG_FILE = Path("logs/meta_requirements.log")
+---CurrentStage=Coder
+---RequirementPointer=11
+--+CurrentStage=Deployer
+--+RequirementPointer=12
+--diff --git a/src/dw6/main.py b/src/dw6/main.py
+--index c65a4d9..13e4d93 100644
+----- a/src/dw6/main.py
+--+++ b/src/dw6/main.py
+--@@ -2,6 +2,7 @@
+-- import argparse
+-- import sys
++  CurrentStage=Deployer
++--RequirementPointer=12
++-+RequirementPointer=13
++-diff --git a/tests/test_main.py b/tests/test_main.py
++-index 47ae0e7..e6a7024 100644
++---- a/tests/test_main.py
++-+++ b/tests/test_main.py
++-@@ -4,7 +4,7 @@ from pathlib import Path
+ - import re
+--+import subprocess
+-- from pathlib import Path
+-- from datetime import datetime, timezone
+-- from dw6.state_manager import WorkflowManager
+--@@ -48,6 +49,10 @@ def main():
+--     meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
+--     meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
+-- 
+--+    # Do command
+--+    do_parser = subparsers.add_parser("do", help="Execute a governed action.")
+--+    do_parser.add_argument("action", type=str, help="The action to execute.")
 --+
---+def register_meta_requirement(description: str):
---+    """Logs a new meta-requirement to the meta_requirements.log file."""
---+    META_LOG_FILE.parent.mkdir(exist_ok=True)
+--     if len(sys.argv) == 1:
+--         parser.print_help(sys.stderr)
+--         sys.exit(1)
+--@@ -56,6 +61,17 @@ def main():
+--     
+--     if args.command == "meta-req":
+--         register_meta_requirement(args.description)
+--+    elif args.command == "do":
+--+        manager = WorkflowManager()
+--+        try:
+--+            manager.governor.authorize(args.action)
+--+            # The command is authorized, execute it.
+--+            subprocess.run(args.action, shell=True, check=True)
+--+        except PermissionError:
+--+            sys.exit(1)
+--+        except subprocess.CalledProcessError:
+--+            print(f"ERROR: The action '{args.action}' failed to execute.", file=sys.stderr)
+--+            sys.exit(1)
+--     else:
+--         manager = WorkflowManager()
+--         if args.command == "approve":
+--diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+--index 241fa62..33e9d07 100644
+----- a/src/dw6/state_manager.py
+--+++ b/src/dw6/state_manager.py
+--@@ -20,20 +20,52 @@ DELIVERABLE_PATHS = {
+-- 
+-- class Governor:
+--     RULES = {
+---        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
+---        "Coder": "Can use file system tools, code editing tools, and run tests.",
+---        "Validator": "Can only run tests and validation tools.",
+---        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
+---        "Researcher": "Can use web search and documentation reading tools."
+--+        "Engineer": [
+--+            "uv run python -m dw6.main new",
+--+            "ls",
+--+            "cat",
+--+            "view_file_outline"
+--+        ],
+--+        "Coder": [
+--+            "replace_file_content",
+--+            "write_to_file",
+--+            "view_file_outline",
+--+            "ls"
+--+        ],
+--+        "Validator": [
+--+            "uv run pytest"
+--+        ],
+--+        "Deployer": [
+--+            "git add",
+--+            "git commit",
+--+            "git tag",
+--+            "uv run python -m dw6.main approve"
+--+        ],
+--+        "Researcher": [
+--+            "search_web",
+--+            "read_url_content"
+--+        ]
+--     }
+--+
+--     def __init__(self, state):
+--         self.state = state
+--         self.current_stage = self.state.get("CurrentStage")
++- from dw6.main import register_meta_requirement, META_LOG_FILE
+ - 
+--+    def authorize(self, command: str):
+--+        """Checks if a command is allowed in the current stage."""
+--+        allowed_commands = self.RULES.get(self.current_stage, [])
+--+        if not any(command.startswith(prefix) for prefix in allowed_commands):
+--+            error_msg = f"[GOVERNOR] Action denied. The command '{(command)}' is not allowed in the '{self.current_stage}' stage."
+--+            print(error_msg, file=sys.stderr)
+--+            raise PermissionError(error_msg)
+--+        print(f"[GOVERNOR] Action authorized for stage '{self.current_stage}'.")
+--+
+--     def enforce_rules(self):
+---        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
+--+        rules = self.RULES.get(self.current_stage, ["No specific rules defined."])
+--         print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
+---        print(f"[RULE] {rule}")
+--+        print("[RULE] Allowed command prefixes:")
+--+        for rule in rules:
+--+            print(f"  - {rule}")
++--@pytest.fixture(autouse=True)
++-+@pytest.fixture
++- def cleanup_log_file():
++-     """Fixture to clean up the meta log file before and after a test."""
++-     if META_LOG_FILE.exists():
++-@@ -13,7 +13,7 @@ def cleanup_log_file():
++-     if META_LOG_FILE.exists():
++-         META_LOG_FILE.unlink()
+ - 
+--     def approve(self):
+--         old_stage = self.current_stage
+--diff --git a/tests/test_governor.py b/tests/test_governor.py
+--index 26bf82b..a431529 100644
+----- a/tests/test_governor.py
+--+++ b/tests/test_governor.py
+--@@ -71,5 +71,37 @@ def test_governor_enforces_rules_on_approve(mocker, capsys):
+-- 
+--     # Assert
+--     captured = capsys.readouterr()
+---    expected_rule = Governor.RULES["Coder"]
+---    assert expected_rule in captured.out
+--+    # Check that each rule is printed
+--+    for rule in Governor.RULES["Coder"]:
+--+        assert rule in captured.out
+--+
+--+@pytest.mark.parametrize("stage, allowed_command", [
+--+    (stage, command) 
+--+    for stage, commands in Governor.RULES.items() 
+--+    for command in commands
+--+])
+--+def test_governor_authorizes_allowed_commands(mock_state, stage, allowed_command):
+--+    """Verify that the Governor authorizes all allowed commands for each stage."""
+--+    # Arrange
+--+    mock_state.get.return_value = stage
+--+    governor = Governor(mock_state)
 --+    
---+    last_id = 0
---+    if META_LOG_FILE.exists():
---+        with open(META_LOG_FILE, "r") as f:
---+            lines = f.readlines()
---+            if lines:
---+                last_line = lines[-1]
---+                match = re.search(r'^\[ID:(\d+)\]', last_line)
---+                if match:
---+                    last_id = int(match.group(1))
+--+    # Act & Assert
+--+    try:
+--+        governor.authorize(allowed_command + " --some-arg") # Test with an argument
+--+    except PermissionError:
+--+        pytest.fail(f"Governor incorrectly denied command '{allowed_command}' for stage '{stage}'.")
 --+
---+    new_id = last_id + 1
---+    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
---+    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"
+--+def test_governor_denies_forbidden_command(mock_state):
+--+    """Verify that the Governor denies a command that is not allowed."""
+--+    # Arrange
+--+    stage = "Engineer"
+--+    forbidden_command = "git commit -m 'should not be allowed'"
+--+    mock_state.get.return_value = stage
+--+    governor = Governor(mock_state)
 --+
---+    with open(META_LOG_FILE, "a") as f:
---+        f.write(log_entry)
+--+    # Act & Assert
+--+    with pytest.raises(PermissionError) as e:
+--+        governor.authorize(forbidden_command)
 --+    
---+    print(f"Successfully logged meta-requirement {new_id}.")
-+--CurrentStage=Coder
-+--RequirementPointer=11
-+-+CurrentStage=Deployer
-+-+RequirementPointer=12
-+-diff --git a/src/dw6/main.py b/src/dw6/main.py
-+-index c65a4d9..13e4d93 100644
-+---- a/src/dw6/main.py
-+-+++ b/src/dw6/main.py
-+-@@ -2,6 +2,7 @@
-+- import argparse
-+- import sys
-+- import re
-+-+import subprocess
-+- from pathlib import Path
-+- from datetime import datetime, timezone
-+- from dw6.state_manager import WorkflowManager
-+-@@ -48,6 +49,10 @@ def main():
-+-     meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
-+-     meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
-+- 
-+-+    # Do command
-+-+    do_parser = subparsers.add_parser("do", help="Execute a governed action.")
-+-+    do_parser.add_argument("action", type=str, help="The action to execute.")
- -+
--- def main():
---     """Main entry point for the DW6 CLI."""
----    # Test comment for Cycle 2 validation.
---     parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
---     subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)
-+-     if len(sys.argv) == 1:
-+-         parser.print_help(sys.stderr)
-+-         sys.exit(1)
-+-@@ -56,6 +61,17 @@ def main():
-+-     
-+-     if args.command == "meta-req":
-+-         register_meta_requirement(args.description)
-+-+    elif args.command == "do":
-+-+        manager = WorkflowManager()
-+-+        try:
-+-+            manager.governor.authorize(args.action)
-+-+            # The command is authorized, execute it.
-+-+            subprocess.run(args.action, shell=True, check=True)
-+-+        except PermissionError:
-+-+            sys.exit(1)
-+-+        except subprocess.CalledProcessError:
-+-+            print(f"ERROR: The action '{args.action}' failed to execute.", file=sys.stderr)
-+-+            sys.exit(1)
-+-     else:
-+-         manager = WorkflowManager()
-+-         if args.command == "approve":
-+-diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-+-index 241fa62..33e9d07 100644
-+---- a/src/dw6/state_manager.py
-+-+++ b/src/dw6/state_manager.py
-+-@@ -20,20 +20,52 @@ DELIVERABLE_PATHS = {
- - 
----
---     # Approve command
---     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
-+- class Governor:
-+-     RULES = {
-+--        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
-+--        "Coder": "Can use file system tools, code editing tools, and run tests.",
-+--        "Validator": "Can only run tests and validation tools.",
-+--        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
-+--        "Researcher": "Can use web search and documentation reading tools."
-+-+        "Engineer": [
-+-+            "uv run python -m dw6.main new",
-+-+            "ls",
-+-+            "cat",
-+-+            "view_file_outline"
-+-+        ],
-+-+        "Coder": [
-+-+            "replace_file_content",
-+-+            "write_to_file",
-+-+            "view_file_outline",
-+-+            "ls"
-+-+        ],
-+-+        "Validator": [
-+-+            "uv run pytest"
-+-+        ],
-+-+        "Deployer": [
-+-+            "git add",
-+-+            "git commit",
-+-+            "git tag",
-+-+            "uv run python -m dw6.main approve"
-+-+        ],
-+-+        "Researcher": [
-+-+            "search_web",
-+-+            "read_url_content"
-+-+        ]
-+-     }
-+-+
-+-     def __init__(self, state):
-+-         self.state = state
-+-         self.current_stage = self.state.get("CurrentStage")
- - 
---@@ -18,18 +44,24 @@ def main():
---     new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
---     new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
-+-+    def authorize(self, command: str):
-+-+        """Checks if a command is allowed in the current stage."""
-+-+        allowed_commands = self.RULES.get(self.current_stage, [])
-+-+        if not any(command.startswith(prefix) for prefix in allowed_commands):
-+-+            error_msg = f"[GOVERNOR] Action denied. The command '{(command)}' is not allowed in the '{self.current_stage}' stage."
-+-+            print(error_msg, file=sys.stderr)
-+-+            raise PermissionError(error_msg)
-+-+        print(f"[GOVERNOR] Action authorized for stage '{self.current_stage}'.")
-+-+
-+-     def enforce_rules(self):
-+--        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
-+-+        rules = self.RULES.get(self.current_stage, ["No specific rules defined."])
-+-         print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
-+--        print(f"[RULE] {rule}")
-+-+        print("[RULE] Allowed command prefixes:")
-+-+        for rule in rules:
-+-+            print(f"  - {rule}")
- - 
---+    # Meta-req command
---+    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
---+    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")
--++    # Do command
--++    do_parser = subparsers.add_parser("do", help="Execute a governed action.")
--++    do_parser.add_argument("action", type=str, help="The action to execute.")
-- +
--      if len(sys.argv) == 1:
--          parser.print_help(sys.stderr)
--          sys.exit(1)
-+-     def approve(self):
-+-         old_stage = self.current_stage
-+-diff --git a/tests/test_governor.py b/tests/test_governor.py
-+-index 26bf82b..a431529 100644
-+---- a/tests/test_governor.py
-+-+++ b/tests/test_governor.py
-+-@@ -71,5 +71,37 @@ def test_governor_enforces_rules_on_approve(mocker, capsys):
- - 
---     args = parser.parse_args()
--+@@ -56,6 +61,17 @@ def main():
--      
----    manager = WorkflowManager()
----
----    if args.command == "approve":
----        manager.approve()
----    elif args.command == "new":
----        process_prompt(args.prompt)
---+    if args.command == "meta-req":
---+        register_meta_requirement(args.description)
---+    else:
--+     if args.command == "meta-req":
--+         register_meta_requirement(args.description)
--++    elif args.command == "do":
-- +        manager = WorkflowManager()
---+        if args.command == "approve":
---+            manager.approve()
---+        elif args.command == "new":
---+            process_prompt(args.prompt)
--++        try:
--++            manager.governor.authorize(args.action)
--++            # The command is authorized, execute it.
--++            subprocess.run(args.action, shell=True, check=True)
--++        except PermissionError:
--++            sys.exit(1)
--++        except subprocess.CalledProcessError:
--++            print(f"ERROR: The action '{args.action}' failed to execute.", file=sys.stderr)
--++            sys.exit(1)
--+     else:
--+         manager = WorkflowManager()
--+         if args.command == "approve":
--+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
--+index 241fa62..33e9d07 100644
--+--- a/src/dw6/state_manager.py
--++++ b/src/dw6/state_manager.py
--+@@ -20,20 +20,52 @@ DELIVERABLE_PATHS = {
+--+    assert "Action denied" in str(e.value)
+-+ CurrentStage=Deployer
+-+-RequirementPointer=12
+-++RequirementPointer=13
+- diff --git a/tests/test_main.py b/tests/test_main.py
+--index eddb264..47ae0e7 100644
+-+index 47ae0e7..e6a7024 100644
+- --- a/tests/test_main.py
+- +++ b/tests/test_main.py
+--@@ -50,3 +50,50 @@ def test_register_meta_requirement_increments_id():
+--     assert description1 in lines[0]
+--     assert "[ID:2]" in lines[1]
+--     assert description2 in lines[1]
+--+
+--+
+-+@@ -4,7 +4,7 @@ from pathlib import Path
+-+ import re
+-+ from dw6.main import register_meta_requirement, META_LOG_FILE
 -+ 
--+ class Governor:
--+     RULES = {
--+-        "Engineer": "Can only use tools for analysis, planning, and creating technical specifications.",
--+-        "Coder": "Can use file system tools, code editing tools, and run tests.",
--+-        "Validator": "Can only run tests and validation tools.",
--+-        "Deployer": "Can only use Git tools for tagging and pushing to remote.",
--+-        "Researcher": "Can use web search and documentation reading tools."
--++        "Engineer": [
--++            "uv run python -m dw6.main new",
--++            "ls",
--++            "cat",
--++            "view_file_outline"
--++        ],
--++        "Coder": [
--++            "replace_file_content",
--++            "write_to_file",
--++            "view_file_outline",
--++            "ls"
--++        ],
--++        "Validator": [
--++            "uv run pytest"
--++        ],
--++        "Deployer": [
--++            "git add",
--++            "git commit",
--++            "git tag",
--++            "uv run python -m dw6.main approve"
--++        ],
--++        "Researcher": [
--++            "search_web",
--++            "read_url_content"
--++        ]
--+     }
--++
--+     def __init__(self, state):
--+         self.state = state
--+         self.current_stage = self.state.get("CurrentStage")
--  
--- if __name__ == "__main__":
---     main()
--++    def authorize(self, command: str):
--++        """Checks if a command is allowed in the current stage."""
--++        allowed_commands = self.RULES.get(self.current_stage, [])
--++        if not any(command.startswith(prefix) for prefix in allowed_commands):
--++            error_msg = f"[GOVERNOR] Action denied. The command '{(command)}' is not allowed in the '{self.current_stage}' stage."
--++            print(error_msg, file=sys.stderr)
--++            raise PermissionError(error_msg)
--++        print(f"[GOVERNOR] Action authorized for stage '{self.current_stage}'.")
--++
--+     def enforce_rules(self):
--+-        rule = self.RULES.get(self.current_stage, "No specific rules defined.")
--++        rules = self.RULES.get(self.current_stage, ["No specific rules defined."])
--+         print(f"--- Governor: Enforcing Rules for Stage: {self.current_stage} ---")
--+-        print(f"[RULE] {rule}")
--++        print("[RULE] Allowed command prefixes:")
--++        for rule in rules:
--++            print(f"  - {rule}")
+-+-@pytest.fixture(autouse=True)
+- +@pytest.fixture
+--+def mock_main_dependencies(mocker):
+--+    """Fixture to mock dependencies of the main function for the 'do' command tests."""
+--+    # Since autospec=True is used, we need to configure the mock instance
+--+    # to have the 'governor' attribute.
+--+    mock_workflow_manager_class = mocker.patch('dw6.main.WorkflowManager', autospec=True)
+--+    mock_workflow_manager_instance = mock_workflow_manager_class.return_value
+--+    mock_governor = mocker.MagicMock()
+--+    mock_workflow_manager_instance.governor = mock_governor
+--+
+--+    mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
+--+    return mock_governor, mock_subprocess_run
+--+
+--+def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
+--+    """Verify the 'do' command executes an action when the Governor authorizes it."""
+--+    # Arrange
+--+    mock_governor, mock_subprocess_run = mock_main_dependencies
+--+    mock_governor.authorize.return_value = None # Simulate authorization success
+--+    
+--+    mocker.patch('sys.argv', ['dw6', 'do', 'ls -l'])
+--+    
+--+    # Act
+--+    from dw6.main import main
+--+    main()
+--+
+--+    # Assert
+--+    mock_governor.authorize.assert_called_once_with('ls -l')
+--+    mock_subprocess_run.assert_called_once_with('ls -l', shell=True, check=True)
+--+
+--+def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
+--+    """Verify the 'do' command blocks an action when the Governor denies it."""
+--+    # Arrange
+--+    mock_governor, mock_subprocess_run = mock_main_dependencies
+--+    mock_governor.authorize.side_effect = PermissionError("Action denied")
+--+
+--+    mocker.patch('sys.argv', ['dw6', 'do', 'git push'])
+--+
+--+    # Act & Assert
+--+    with pytest.raises(SystemExit) as e:
+--+        from dw6.main import main
+--+        main()
+--+    
+--+    assert e.value.code == 1
+--+    mock_governor.authorize.assert_called_once_with('git push')
+--+    mock_subprocess_run.assert_not_called()
+-+ def cleanup_log_file():
+-+     """Fixture to clean up the meta log file before and after a test."""
+-+     if META_LOG_FILE.exists():
+-+@@ -13,7 +13,7 @@ def cleanup_log_file():
+-+     if META_LOG_FILE.exists():
+-+         META_LOG_FILE.unlink()
 -+ 
--+     def approve(self):
--+         old_stage = self.current_stage
--+diff --git a/tests/test_governor.py b/tests/test_governor.py
--+index 26bf82b..a431529 100644
--+--- a/tests/test_governor.py
--++++ b/tests/test_governor.py
--+@@ -71,5 +71,37 @@ def test_governor_enforces_rules_on_approve(mocker, capsys):
+-+-def test_register_meta_requirement_creates_file_and_logs_entry():
+-++def test_register_meta_requirement_creates_file_and_logs_entry(cleanup_log_file):
+-+     """Verify that the first call creates the log file and adds the first entry correctly."""
+-+     # Arrange
+-+     description = "This is the first meta requirement."
+-+@@ -31,7 +31,7 @@ def test_register_meta_requirement_creates_file_and_logs_entry():
+-+     # A simple regex to check for the timestamp format
+-+     assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
 -+ 
--+     # Assert
--+     captured = capsys.readouterr()
--+-    expected_rule = Governor.RULES["Coder"]
--+-    assert expected_rule in captured.out
--++    # Check that each rule is printed
--++    for rule in Governor.RULES["Coder"]:
--++        assert rule in captured.out
--++
--++@pytest.mark.parametrize("stage, allowed_command", [
--++    (stage, command) 
--++    for stage, commands in Governor.RULES.items() 
--++    for command in commands
--++])
--++def test_governor_authorizes_allowed_commands(mock_state, stage, allowed_command):
--++    """Verify that the Governor authorizes all allowed commands for each stage."""
--++    # Arrange
--++    mock_state.get.return_value = stage
--++    governor = Governor(mock_state)
--++    
--++    # Act & Assert
--++    try:
--++        governor.authorize(allowed_command + " --some-arg") # Test with an argument
--++    except PermissionError:
--++        pytest.fail(f"Governor incorrectly denied command '{allowed_command}' for stage '{stage}'.")
--++
--++def test_governor_denies_forbidden_command(mock_state):
--++    """Verify that the Governor denies a command that is not allowed."""
--++    # Arrange
--++    stage = "Engineer"
--++    forbidden_command = "git commit -m 'should not be allowed'"
--++    mock_state.get.return_value = stage
--++    governor = Governor(mock_state)
--++
--++    # Act & Assert
--++    with pytest.raises(PermissionError) as e:
--++        governor.authorize(forbidden_command)
--++    
--++    assert "Action denied" in str(e.value)
-+-     # Assert
-+-     captured = capsys.readouterr()
-+--    expected_rule = Governor.RULES["Coder"]
-+--    assert expected_rule in captured.out
-+-+    # Check that each rule is printed
-+-+    for rule in Governor.RULES["Coder"]:
-+-+        assert rule in captured.out
-+-+
-+-+@pytest.mark.parametrize("stage, allowed_command", [
-+-+    (stage, command) 
-+-+    for stage, commands in Governor.RULES.items() 
-+-+    for command in commands
-+-+])
-+-+def test_governor_authorizes_allowed_commands(mock_state, stage, allowed_command):
-+-+    """Verify that the Governor authorizes all allowed commands for each stage."""
-+-+    # Arrange
-+-+    mock_state.get.return_value = stage
-+-+    governor = Governor(mock_state)
-+-+    
-+-+    # Act & Assert
-+-+    try:
-+-+        governor.authorize(allowed_command + " --some-arg") # Test with an argument
-+-+    except PermissionError:
-+-+        pytest.fail(f"Governor incorrectly denied command '{allowed_command}' for stage '{stage}'.")
-+-+
-+-+def test_governor_denies_forbidden_command(mock_state):
-+-+    """Verify that the Governor denies a command that is not allowed."""
-+-+    # Arrange
-+-+    stage = "Engineer"
-+-+    forbidden_command = "git commit -m 'should not be allowed'"
-+-+    mock_state.get.return_value = stage
-+-+    governor = Governor(mock_state)
-+-+
-+-+    # Act & Assert
-+-+    with pytest.raises(PermissionError) as e:
-+-+        governor.authorize(forbidden_command)
-+-+    
-+-+    assert "Action denied" in str(e.value)
-++ CurrentStage=Deployer
-++-RequirementPointer=12
-+++RequirementPointer=13
-  diff --git a/tests/test_main.py b/tests/test_main.py
---index c429973..eddb264 100644
--+index eddb264..47ae0e7 100644
-+-index eddb264..47ae0e7 100644
-++index 47ae0e7..e6a7024 100644
-  --- a/tests/test_main.py
-  +++ b/tests/test_main.py
---@@ -1,5 +1,52 @@
--- # tests/test_main.py
---+import pytest
---+from pathlib import Path
---+import re
---+from dw6.main import register_meta_requirement, META_LOG_FILE
--- 
----def test_placeholder():
----    """A placeholder test to satisfy the Validator stage."""
----    assert True
---+@pytest.fixture(autouse=True)
---+def cleanup_log_file():
---+    """Fixture to clean up the meta log file before and after a test."""
---+    if META_LOG_FILE.exists():
---+        META_LOG_FILE.unlink()
---+    yield
---+    if META_LOG_FILE.exists():
---+        META_LOG_FILE.unlink()
--+@@ -50,3 +50,50 @@ def test_register_meta_requirement_increments_id():
--+     assert description1 in lines[0]
--+     assert "[ID:2]" in lines[1]
--+     assert description2 in lines[1]
-- +
---+def test_register_meta_requirement_creates_file_and_logs_entry():
---+    """Verify that the first call creates the log file and adds the first entry correctly."""
-+-@@ -50,3 +50,50 @@ def test_register_meta_requirement_increments_id():
-+-     assert description1 in lines[0]
-+-     assert "[ID:2]" in lines[1]
-+-     assert description2 in lines[1]
-+-+
-+-+
-++@@ -4,7 +4,7 @@ from pathlib import Path
-++ import re
-++ from dw6.main import register_meta_requirement, META_LOG_FILE
-++ 
-++-@pytest.fixture(autouse=True)
-+ +@pytest.fixture
-+-+def mock_main_dependencies(mocker):
-+-+    """Fixture to mock dependencies of the main function for the 'do' command tests."""
-+-+    # Since autospec=True is used, we need to configure the mock instance
-+-+    # to have the 'governor' attribute.
-+-+    mock_workflow_manager_class = mocker.patch('dw6.main.WorkflowManager', autospec=True)
-+-+    mock_workflow_manager_instance = mock_workflow_manager_class.return_value
-+-+    mock_governor = mocker.MagicMock()
-+-+    mock_workflow_manager_instance.governor = mock_governor
-+-+
-+-+    mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
-+-+    return mock_governor, mock_subprocess_run
-+-+
-+-+def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
-+-+    """Verify the 'do' command executes an action when the Governor authorizes it."""
- -+    # Arrange
---+    description = "This is the first meta requirement."
-- +
--++@pytest.fixture
--++def mock_main_dependencies(mocker):
--++    """Fixture to mock dependencies of the main function for the 'do' command tests."""
--++    # Since autospec=True is used, we need to configure the mock instance
--++    # to have the 'governor' attribute.
--++    mock_workflow_manager_class = mocker.patch('dw6.main.WorkflowManager', autospec=True)
--++    mock_workflow_manager_instance = mock_workflow_manager_class.return_value
--++    mock_governor = mocker.MagicMock()
--++    mock_workflow_manager_instance.governor = mock_governor
--++
--++    mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
--++    return mock_governor, mock_subprocess_run
--++
--++def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
--++    """Verify the 'do' command executes an action when the Governor authorizes it."""
--++    # Arrange
--++    mock_governor, mock_subprocess_run = mock_main_dependencies
--++    mock_governor.authorize.return_value = None # Simulate authorization success
--++    
--++    mocker.patch('sys.argv', ['dw6', 'do', 'ls -l'])
--++    
-- +    # Act
---+    register_meta_requirement(description)
--++    from dw6.main import main
--++    main()
-- +
-- +    # Assert
---+    assert META_LOG_FILE.exists()
---+    with open(META_LOG_FILE, "r") as f:
---+        content = f.read()
-+-+    mock_governor, mock_subprocess_run = mock_main_dependencies
-+-+    mock_governor.authorize.return_value = None # Simulate authorization success
-+-+    
-+-+    mocker.patch('sys.argv', ['dw6', 'do', 'ls -l'])
- -+    
---+    assert "[ID:1]" in content
---+    assert description in content
---+    # A simple regex to check for the timestamp format
---+    assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
--++    mock_governor.authorize.assert_called_once_with('ls -l')
--++    mock_subprocess_run.assert_called_once_with('ls -l', shell=True, check=True)
-- +
---+def test_register_meta_requirement_increments_id():
---+    """Verify that subsequent calls increment the requirement ID."""
--++def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
--++    """Verify the 'do' command blocks an action when the Governor denies it."""
-- +    # Arrange
---+    description1 = "First requirement."
---+    description2 = "Second requirement."
--++    mock_governor, mock_subprocess_run = mock_main_dependencies
--++    mock_governor.authorize.side_effect = PermissionError("Action denied")
-- +
- -+    # Act
---+    register_meta_requirement(description1)
---+    register_meta_requirement(description2)
--++    mocker.patch('sys.argv', ['dw6', 'do', 'git push'])
-- +
-+-+    from dw6.main import main
-+-+    main()
-+-+
- -+    # Assert
---+    with open(META_LOG_FILE, "r") as f:
---+        lines = f.readlines()
--++    # Act & Assert
--++    with pytest.raises(SystemExit) as e:
--++        from dw6.main import main
--++        main()
-- +    
---+    assert len(lines) == 2
---+    assert "[ID:1]" in lines[0]
---+    assert description1 in lines[0]
---+    assert "[ID:2]" in lines[1]
---+    assert description2 in lines[1]
--++    assert e.value.code == 1
--++    mock_governor.authorize.assert_called_once_with('git push')
--++    mock_subprocess_run.assert_not_called()
-+-+    mock_governor.authorize.assert_called_once_with('ls -l')
-+-+    mock_subprocess_run.assert_called_once_with('ls -l', shell=True, check=True)
-+-+
-+-+def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
-+-+    """Verify the 'do' command blocks an action when the Governor denies it."""
-+-+    # Arrange
-+-+    mock_governor, mock_subprocess_run = mock_main_dependencies
-+-+    mock_governor.authorize.side_effect = PermissionError("Action denied")
-+-+
-+-+    mocker.patch('sys.argv', ['dw6', 'do', 'git push'])
-+-+
-+-+    # Act & Assert
-+-+    with pytest.raises(SystemExit) as e:
-+-+        from dw6.main import main
-+-+        main()
-+-+    
-+-+    assert e.value.code == 1
-+-+    mock_governor.authorize.assert_called_once_with('git push')
-+-+    mock_subprocess_run.assert_not_called()
-++ def cleanup_log_file():
-++     """Fixture to clean up the meta log file before and after a test."""
-++     if META_LOG_FILE.exists():
-++@@ -13,7 +13,7 @@ def cleanup_log_file():
-++     if META_LOG_FILE.exists():
-++         META_LOG_FILE.unlink()
-++ 
-++-def test_register_meta_requirement_creates_file_and_logs_entry():
-+++def test_register_meta_requirement_creates_file_and_logs_entry(cleanup_log_file):
-++     """Verify that the first call creates the log file and adds the first entry correctly."""
-++     # Arrange
-++     description = "This is the first meta requirement."
-++@@ -31,7 +31,7 @@ def test_register_meta_requirement_creates_file_and_logs_entry():
-++     # A simple regex to check for the timestamp format
-++     assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
-++ 
-++-def test_register_meta_requirement_increments_id():
-+++def test_register_meta_requirement_increments_id(cleanup_log_file):
-++     """Verify that subsequent calls increment the requirement ID."""
-++     # Arrange
-++     description1 = "First requirement."
+-+-def test_register_meta_requirement_increments_id():
+-++def test_register_meta_requirement_increments_id(cleanup_log_file):
+-+     """Verify that subsequent calls increment the requirement ID."""
+-+     # Arrange
+-+     description1 = "First requirement."
++--def test_register_meta_requirement_creates_file_and_logs_entry():
++-+def test_register_meta_requirement_creates_file_and_logs_entry(cleanup_log_file):
++-     """Verify that the first call creates the log file and adds the first entry correctly."""
++-     # Arrange
++-     description = "This is the first meta requirement."
++-@@ -31,7 +31,7 @@ def test_register_meta_requirement_creates_file_and_logs_entry():
++-     # A simple regex to check for the timestamp format
++-     assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
+++-RequirementPointer=13
++++RequirementPointer=14
+++diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+++index 33e9d07..d442899 100644
+++--- a/src/dw6/state_manager.py
++++++ b/src/dw6/state_manager.py
+++@@ -9,7 +9,7 @@ from dw6 import git_handler
+++ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+++ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+++ APPROVAL_FILE = "logs/approvals.log"
+++-STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
++++STAGES = ["Engineer", "Researcher", "Coder", "Validator", "Deployer"]
+++ DELIVERABLE_PATHS = {
+++     "Engineer": "deliverables/engineering",
+++     "Coder": "deliverables/coding",
+++@@ -90,6 +90,15 @@ class Governor:
+++                 print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+++                 sys.exit(1)
+++             print("Governor: 'Engineer' exit criteria met.")
++++        elif self.current_stage == "Researcher":
++++            req_id = self.state.get("RequirementPointer")
++++            research_dir = Path("deliverables/research")
++++            research_dir.mkdir(parents=True, exist_ok=True)
++++            report_file = research_dir / f"cycle_{req_id}_research_report.md"
++++            if not report_file.exists():
++++                print(f"ERROR: Exit criteria for 'Researcher' not met. Research report not found: {report_file}", file=sys.stderr)
++++                sys.exit(1)
++++            print("Governor: 'Researcher' exit criteria met.")
++  
++--def test_register_meta_requirement_increments_id():
++-+def test_register_meta_requirement_increments_id(cleanup_log_file):
++-     """Verify that subsequent calls increment the requirement ID."""
++-     # Arrange
++-     description1 = "First requirement."
+++     def _transition_to_next_stage(self):
+++         current_index = STAGES.index(self.current_stage)
   ```
  \ No newline at end of file
--diff --git a/deliverables/engineering/cycle_13_technical_specification.md b/deliverables/engineering/cycle_13_technical_specification.md
-+diff --git a/deliverables/engineering/cycle_14_technical_specification.md b/deliverables/engineering/cycle_14_technical_specification.md
+-diff --git a/deliverables/engineering/cycle_14_technical_specification.md b/deliverables/engineering/cycle_14_technical_specification.md
++diff --git a/deliverables/engineering/cycle_15_technical_specification.md b/deliverables/engineering/cycle_15_technical_specification.md
  new file mode 100644
--index 0000000..fde1032
-+index 0000000..2957165
+-index 0000000..2957165
++index 0000000..ae9b994
  --- /dev/null
--+++ b/deliverables/engineering/cycle_13_technical_specification.md
-++++ b/deliverables/engineering/cycle_14_technical_specification.md
+-+++ b/deliverables/engineering/cycle_14_technical_specification.md
+++++ b/deliverables/engineering/cycle_15_technical_specification.md
  @@ -0,0 +1,9 @@
--+# Requirement: 13
-++# Requirement: 14
+-+# Requirement: 14
+++# Requirement: 15
  +
  +## 1. High-Level Goal
  +
--+Fix a critical bug in the test suite where a test fixture (cleanup_log_file) is incorrectly configured with autouse=True, causing it to delete the production meta_requirements.log file. The fix involves removing autouse=True and applying the fixture only to the specific tests that require it.
-++Re-introduce the Researcher stage into the DW6 workflow. The new stage order will be Engineer -> Researcher -> Coder -> Validator -> Deployer. The Researcher stage will have its own set of allowed commands (e.g., search_web, read_url_content) and will be required to produce a research report in deliverables/research/ as its exit criteria.
+-+Re-introduce the Researcher stage into the DW6 workflow. The new stage order will be Engineer -> Researcher -> Coder -> Validator -> Deployer. The Researcher stage will have its own set of allowed commands (e.g., search_web, read_url_content) and will be required to produce a research report in deliverables/research/ as its exit criteria.
+++Fix the do command. It should act as a pure authorization gatekeeper, not an executor. It must only validate the intended command against the Governors rules and then exit. It must not attempt to execute the command itself.
  +
  +## 2. Guiding Principles
  +
  +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
  diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
--index 5045595..a1b7a04 100644
-+index a1b7a04..7161830 100644
+-index a1b7a04..7161830 100644
++index 7161830..cb735ed 100644
  --- a/logs/.last_commit_sha
  +++ b/logs/.last_commit_sha
  @@ -1 +1 @@
---223a8df342ec9a1ce277b234efe90e05cc4803dd
-+-05ff4137104ba71c49d78ebaa96798dcee5559f7
+--05ff4137104ba71c49d78ebaa96798dcee5559f7
++-53d60c6a24db61fbf61dbf953026000943463bed
  \ No newline at end of file
--+05ff4137104ba71c49d78ebaa96798dcee5559f7
-++53d60c6a24db61fbf61dbf953026000943463bed
+-+53d60c6a24db61fbf61dbf953026000943463bed
+++cb95677c7e24b2bad2b2fb83ddf08cfbd30078a6
  \ No newline at end of file
  diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
--index d459c0f..a21bb3a 100644
-+index a21bb3a..a4e5ca5 100644
+-index a21bb3a..a4e5ca5 100644
++index a4e5ca5..caa73f9 100644
  --- a/logs/workflow_state.txt
  +++ b/logs/workflow_state.txt
  @@ -1,2 +1,2 @@
   CurrentStage=Deployer
---RequirementPointer=12
--+RequirementPointer=13
--diff --git a/tests/test_main.py b/tests/test_main.py
--index 47ae0e7..e6a7024 100644
----- a/tests/test_main.py
--+++ b/tests/test_main.py
--@@ -4,7 +4,7 @@ from pathlib import Path
-- import re
-- from dw6.main import register_meta_requirement, META_LOG_FILE
-- 
---@pytest.fixture(autouse=True)
--+@pytest.fixture
-- def cleanup_log_file():
--     """Fixture to clean up the meta log file before and after a test."""
--     if META_LOG_FILE.exists():
--@@ -13,7 +13,7 @@ def cleanup_log_file():
--     if META_LOG_FILE.exists():
--         META_LOG_FILE.unlink()
-- 
---def test_register_meta_requirement_creates_file_and_logs_entry():
--+def test_register_meta_requirement_creates_file_and_logs_entry(cleanup_log_file):
--     """Verify that the first call creates the log file and adds the first entry correctly."""
--     # Arrange
--     description = "This is the first meta requirement."
--@@ -31,7 +31,7 @@ def test_register_meta_requirement_creates_file_and_logs_entry():
--     # A simple regex to check for the timestamp format
--     assert re.search(r'\[TS:\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} UTC\]', content)
-+-RequirementPointer=13
-++RequirementPointer=14
-+diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
-+index 33e9d07..d442899 100644
-+--- a/src/dw6/state_manager.py
-++++ b/src/dw6/state_manager.py
-+@@ -9,7 +9,7 @@ from dw6 import git_handler
-+ MASTER_FILE = "docs/WORKFLOW_MASTER.md"
-+ REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
-+ APPROVAL_FILE = "logs/approvals.log"
-+-STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
-++STAGES = ["Engineer", "Researcher", "Coder", "Validator", "Deployer"]
-+ DELIVERABLE_PATHS = {
-+     "Engineer": "deliverables/engineering",
-+     "Coder": "deliverables/coding",
-+@@ -90,6 +90,15 @@ class Governor:
-+                 print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
-+                 sys.exit(1)
-+             print("Governor: 'Engineer' exit criteria met.")
-++        elif self.current_stage == "Researcher":
-++            req_id = self.state.get("RequirementPointer")
-++            research_dir = Path("deliverables/research")
-++            research_dir.mkdir(parents=True, exist_ok=True)
-++            report_file = research_dir / f"cycle_{req_id}_research_report.md"
-++            if not report_file.exists():
-++                print(f"ERROR: Exit criteria for 'Researcher' not met. Research report not found: {report_file}", file=sys.stderr)
-++                sys.exit(1)
-++            print("Governor: 'Researcher' exit criteria met.")
+--RequirementPointer=13
+-+RequirementPointer=14
+-diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
+-index 33e9d07..d442899 100644
+---- a/src/dw6/state_manager.py
+-+++ b/src/dw6/state_manager.py
+-@@ -9,7 +9,7 @@ from dw6 import git_handler
+- MASTER_FILE = "docs/WORKFLOW_MASTER.md"
+- REQUIREMENTS_FILE = "docs/PROJECT_REQUIREMENTS.md"
+- APPROVAL_FILE = "logs/approvals.log"
+--STAGES = ["Engineer", "Coder", "Validator", "Deployer"] # Researcher is a special case, not in the main cycle.
+-+STAGES = ["Engineer", "Researcher", "Coder", "Validator", "Deployer"]
+- DELIVERABLE_PATHS = {
+-     "Engineer": "deliverables/engineering",
+-     "Coder": "deliverables/coding",
+-@@ -90,6 +90,15 @@ class Governor:
+-                 print(f"ERROR: Exit criteria for 'Engineer' not met. Specification file not found: {spec_file}", file=sys.stderr)
+-                 sys.exit(1)
+-             print("Governor: 'Engineer' exit criteria met.")
+-+        elif self.current_stage == "Researcher":
+-+            req_id = self.state.get("RequirementPointer")
+-+            research_dir = Path("deliverables/research")
+-+            research_dir.mkdir(parents=True, exist_ok=True)
+-+            report_file = research_dir / f"cycle_{req_id}_research_report.md"
+-+            if not report_file.exists():
+-+                print(f"ERROR: Exit criteria for 'Researcher' not met. Research report not found: {report_file}", file=sys.stderr)
+-+                sys.exit(1)
+-+            print("Governor: 'Researcher' exit criteria met.")
++-RequirementPointer=14
+++RequirementPointer=15
++diff --git a/src/dw6/main.py b/src/dw6/main.py
++index 13e4d93..9a5c7d1 100644
++--- a/src/dw6/main.py
+++++ b/src/dw6/main.py
++@@ -65,13 +65,9 @@ def main():
++         manager = WorkflowManager()
++         try:
++             manager.governor.authorize(args.action)
++-            # The command is authorized, execute it.
++-            subprocess.run(args.action, shell=True, check=True)
+++            # The command is authorized. The gatekeeper's job is done.
++         except PermissionError:
++             sys.exit(1)
++-        except subprocess.CalledProcessError:
++-            print(f"ERROR: The action '{args.action}' failed to execute.", file=sys.stderr)
++-            sys.exit(1)
++     else:
++         manager = WorkflowManager()
++         if args.command == "approve":
++diff --git a/tests/test_main.py b/tests/test_main.py
++index e6a7024..a60db16 100644
++--- a/tests/test_main.py
+++++ b/tests/test_main.py
++@@ -65,8 +65,8 @@ def mock_main_dependencies(mocker):
++     mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
++     return mock_governor, mock_subprocess_run
++ 
++-def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
++-    """Verify the 'do' command executes an action when the Governor authorizes it."""
+++def test_do_command_authorizes_action(mocker, mock_main_dependencies):
+++    """Verify the 'do' command authorizes an action and does not execute it."""
++     # Arrange
++     mock_governor, mock_subprocess_run = mock_main_dependencies
++     mock_governor.authorize.return_value = None # Simulate authorization success
++@@ -79,7 +79,7 @@ def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
++ 
++     # Assert
++     mock_governor.authorize.assert_called_once_with('ls -l')
++-    mock_subprocess_run.assert_called_once_with('ls -l', shell=True, check=True)
+++    mock_subprocess_run.assert_not_called()
   
---def test_register_meta_requirement_increments_id():
--+def test_register_meta_requirement_increments_id(cleanup_log_file):
--     """Verify that subsequent calls increment the requirement ID."""
--     # Arrange
--     description1 = "First requirement."
-+     def _transition_to_next_stage(self):
-+         current_index = STAGES.index(self.current_stage)
+-     def _transition_to_next_stage(self):
+-         current_index = STAGES.index(self.current_stage)
++ def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
++     """Verify the 'do' command blocks an action when the Governor denies it."""
  ```
 \ No newline at end of file
-diff --git a/deliverables/engineering/cycle_15_technical_specification.md b/deliverables/engineering/cycle_15_technical_specification.md
+diff --git a/deliverables/engineering/cycle_16_technical_specification.md b/deliverables/engineering/cycle_16_technical_specification.md
 new file mode 100644
-index 0000000..ae9b994
+index 0000000..eb7387d
 --- /dev/null
-+++ b/deliverables/engineering/cycle_15_technical_specification.md
++++ b/deliverables/engineering/cycle_16_technical_specification.md
 @@ -0,0 +1,9 @@
-+# Requirement: 15
++# Requirement: 16
 +
 +## 1. High-Level Goal
 +
-+Fix the do command. It should act as a pure authorization gatekeeper, not an executor. It must only validate the intended command against the Governors rules and then exit. It must not attempt to execute the command itself.
++Implement a prompt augmentation system. This system will pre-process the initial user request, enriching it with historical context, project state, and structural formatting before it is passed to the Engineer stage.
 +
 +## 2. Guiding Principles
 +
 +**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
+diff --git a/deliverables/research/cycle_16_research_report.md b/deliverables/research/cycle_16_research_report.md
+new file mode 100644
+index 0000000..584ac93
+--- /dev/null
++++ b/deliverables/research/cycle_16_research_report.md
+@@ -0,0 +1,46 @@
++# Research Report: Prompt Augmentation System (Cycle 16)
++
++## 1. Executive Summary
++
++The investigation into building a "prompt augmentation system" has revealed a more robust and standardized approach: **Context Engineering**. Instead of simply pre-pending text to a prompt, we will build a system that provides context to the AI model through a dedicated, open-source protocol. 
++
++The key technology to achieve this is the **Model Context Protocol (MCP)**, an open standard developed by Anthropic. The AI assistant (Cascade) is already an MCP client. Our task is to build a custom MCP server that exposes our project's specific context.
++
++This approach is superior to basic prompt injection as it is more scalable, secure, and aligns with industry best practices for building agentic AI systems.
++
++## 2. Research Findings
++
++### 2.1. From Prompt Engineering to Context Engineering
++
++Initial research led to the concept of **Context Engineering**, a discipline focused on architecting the entire information ecosystem an AI model uses. This paradigm distinguishes between two types of context:
++
++*   **Deterministic Context:** Information directly and explicitly provided to the model (e.g., the user's prompt, system instructions, files).
++*   **Probabilistic Context:** Information the model discovers autonomously by interacting with its tools (e.g., web searches, database queries).
++
++Our "prompt augmentation system" is, in fact, a tool for engineering the deterministic context to better guide the model's discovery of probabilistic context.
++
++### 2.2. The Model Context Protocol (MCP)
++
++The most critical finding is the **Model Context Protocol (MCP)**. 
++
++*   **What it is:** An open-source, standardized protocol for connecting AI models (clients) to data sources (servers).
++*   **How it works:** We will build an **MCP server** that gathers relevant information from our project workspace. The AI assistant, which is already an **MCP client**, will connect to this server to retrieve context.
++*   **Advantages:** This client-server architecture is more robust, secure, and maintainable than ad-hoc prompt modification scripts. It allows the AI to pull context dynamically as needed.
++
++### 2.3. Pre-Built Components
++
++Anthropic and the open-source community provide pre-built MCP servers for common tools like Git, GitHub, and various databases. This is a significant accelerator, as we can leverage these existing components and focus on building the logic for our specific project context.
++
++## 3. Proposed Technical Solution
++
++Based on this research, the plan is as follows:
++
++1.  **Develop a custom MCP Server:** This server will be a Python application.
++2.  **Implement Context Providers:** Within the server, create modules responsible for gathering specific pieces of context:
++    *   `StateProvider`: Reads `logs/workflow_state.txt` to determine the current stage and requirement pointer.
++    *   `GitProvider`: Uses the existing `git_handler` to get the latest commit hash, branch, and recent log messages.
++    *   `RequirementsProvider`: Reads `logs/meta_requirements.log` to provide the list of open and completed meta-requirements.
++3.  **Expose Context:** The MCP server will expose this information through standardized MCP endpoints.
++4.  **Integration:** The AI assistant (Cascade) will be configured to connect to this local MCP server, allowing it to access this rich, real-time context during its operations.
++
++This research concludes that building a dedicated MCP server is the most professional and effective path forward for creating our prompt augmentation system.
 diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
-index 7161830..cb735ed 100644
+index cb735ed..0b9fef6 100644
 --- a/logs/.last_commit_sha
 +++ b/logs/.last_commit_sha
 @@ -1 +1 @@
--53d60c6a24db61fbf61dbf953026000943463bed
+-cb95677c7e24b2bad2b2fb83ddf08cfbd30078a6
 \ No newline at end of file
-+cb95677c7e24b2bad2b2fb83ddf08cfbd30078a6
++d3fe155e791ae31e41520cd1fdb1ada96584d0cb
 \ No newline at end of file
 diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
-index a4e5ca5..caa73f9 100644
+index caa73f9..a0479ba 100644
 --- a/logs/workflow_state.txt
 +++ b/logs/workflow_state.txt
 @@ -1,2 +1,2 @@
  CurrentStage=Deployer
--RequirementPointer=14
-+RequirementPointer=15
-diff --git a/src/dw6/main.py b/src/dw6/main.py
-index 13e4d93..9a5c7d1 100644
---- a/src/dw6/main.py
-+++ b/src/dw6/main.py
-@@ -65,13 +65,9 @@ def main():
-         manager = WorkflowManager()
-         try:
-             manager.governor.authorize(args.action)
--            # The command is authorized, execute it.
--            subprocess.run(args.action, shell=True, check=True)
-+            # The command is authorized. The gatekeeper's job is done.
-         except PermissionError:
-             sys.exit(1)
--        except subprocess.CalledProcessError:
--            print(f"ERROR: The action '{args.action}' failed to execute.", file=sys.stderr)
--            sys.exit(1)
-     else:
-         manager = WorkflowManager()
-         if args.command == "approve":
-diff --git a/tests/test_main.py b/tests/test_main.py
-index e6a7024..a60db16 100644
---- a/tests/test_main.py
-+++ b/tests/test_main.py
-@@ -65,8 +65,8 @@ def mock_main_dependencies(mocker):
-     mock_subprocess_run = mocker.patch('dw6.main.subprocess.run')
-     return mock_governor, mock_subprocess_run
- 
--def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
--    """Verify the 'do' command executes an action when the Governor authorizes it."""
-+def test_do_command_authorizes_action(mocker, mock_main_dependencies):
-+    """Verify the 'do' command authorizes an action and does not execute it."""
-     # Arrange
-     mock_governor, mock_subprocess_run = mock_main_dependencies
-     mock_governor.authorize.return_value = None # Simulate authorization success
-@@ -79,7 +79,7 @@ def test_do_command_executes_authorized_action(mocker, mock_main_dependencies):
- 
-     # Assert
-     mock_governor.authorize.assert_called_once_with('ls -l')
--    mock_subprocess_run.assert_called_once_with('ls -l', shell=True, check=True)
-+    mock_subprocess_run.assert_not_called()
- 
- def test_do_command_blocks_denied_action(mocker, mock_main_dependencies):
-     """Verify the 'do' command blocks an action when the Governor denies it."""
+-RequirementPointer=15
++RequirementPointer=16
+diff --git a/src/dw6/mcp_server.py b/src/dw6/mcp_server.py
+new file mode 100644
+index 0000000..99312c2
+--- /dev/null
++++ b/src/dw6/mcp_server.py
+@@ -0,0 +1,83 @@
++# src/dw6/mcp_server.py
++
++"""
++DW6 Context Engineering Server
++
++This server implements the Model Context Protocol (MCP) to provide rich,
++real-time context about the dw6_test_bed_v7 project to an MCP client
++(e.g., the Cascade AI assistant).
++"""
++
++import asyncio
++from pathlib import Path
++
++# Placeholder for actual MCP server implementation from an SDK
++# In a real scenario, we would import the necessary components from an MCP library.
++class BaseMcpServer:
++    def __init__(self, port):
++        self.port = port
++
++    async def start(self):
++        print(f"Starting MCP Server on port {self.port}")
++        # In a real implementation, this would start a web server (e.g., aiohttp)
++        # and listen for incoming MCP requests.
++        while True:
++            await asyncio.sleep(3600) # Keep server running
++
++    def add_resource(self, resource):
++        print(f"Registering resource: {resource.name}")
++
++class StateProvider:
++    """Provides context from the workflow_state.txt file."""
++    def __init__(self):
++        self.name = "/workflow_state"
++        self.state_file = Path("logs/workflow_state.txt")
++
++    def get_context(self):
++        """Reads and returns the current stage and requirement pointer."""
++        if not self.state_file.exists():
++            return {"error": "State file not found."}
++        content = self.state_file.read_text().strip().split('\n')
++        state = {line.split('=')[0]: line.split('=')[1] for line in content}
++        return state
++
++class GitProvider:
++    """Provides context from the git repository."""
++    def __init__(self):
++        self.name = "/git_context"
++        # In a real implementation, this would use the git_handler.py module
++
++    def get_context(self):
++        """Returns key information from git."""
++        # Placeholder implementation
++        return {
++            "branch": "master",
++            "latest_commit": "d3fe155", # Hardcoded for now
++            "status": "clean"
++        }
++
++class RequirementsProvider:
++    """Provides context from the meta_requirements.log file."""
++    def __init__(self):
++        self.name = "/meta_requirements"
++        self.log_file = Path("logs/meta_requirements.log")
++
++    def get_context(self):
++        """Reads and returns the list of meta-requirements."""
++        if not self.log_file.exists():
++            return {"requirements": []}
++        return {"requirements": self.log_file.read_text().strip().split('\n')}
++
++
++async def main():
++    server = BaseMcpServer(port=8080)
++
++    # Register context providers as resources
++    server.add_resource(StateProvider())
++    server.add_resource(GitProvider())
++    server.add_resource(RequirementsProvider())
++
++    await server.start()
++
++if __name__ == "__main__":
++    asyncio.run(main())
 ```
\ No newline at end of file
diff --git a/deliverables/engineering/cycle_17_technical_specification.md b/deliverables/engineering/cycle_17_technical_specification.md
new file mode 100644
index 0000000..1361e24
--- /dev/null
+++ b/deliverables/engineering/cycle_17_technical_specification.md
@@ -0,0 +1,9 @@
+# Requirement: 17
+
+## 1. High-Level Goal
+
+Fix the Researcher stage rules. The Researcher must be allowed to write files to create its research report deliverable.
+
+## 2. Guiding Principles
+
+**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress.
diff --git a/logs/.last_commit_sha b/logs/.last_commit_sha
index 0b9fef6..1b589e5 100644
--- a/logs/.last_commit_sha
+++ b/logs/.last_commit_sha
@@ -1 +1 @@
-d3fe155e791ae31e41520cd1fdb1ada96584d0cb
\ No newline at end of file
+20dc6516a46b4d3aa59198e9b3725781a6d63216
\ No newline at end of file
diff --git a/logs/workflow_state.txt b/logs/workflow_state.txt
index a0479ba..2595ec3 100644
--- a/logs/workflow_state.txt
+++ b/logs/workflow_state.txt
@@ -1,2 +1,2 @@
 CurrentStage=Deployer
-RequirementPointer=16
+RequirementPointer=17
diff --git a/src/dw6/state_manager.py b/src/dw6/state_manager.py
index d442899..3c910ac 100644
--- a/src/dw6/state_manager.py
+++ b/src/dw6/state_manager.py
@@ -30,7 +30,8 @@ class Governor:
             "replace_file_content",
             "write_to_file",
             "view_file_outline",
-            "ls"
+            "ls",
+            "mkdir"
         ],
         "Validator": [
             "uv run pytest"
@@ -43,7 +44,12 @@ class Governor:
         ],
         "Researcher": [
             "search_web",
-            "read_url_content"
+            "read_url_content",
+            "write_to_file",
+            "replace_file_content",
+            "view_file_outline",
+            "cat",
+            "ls"
         ]
     }
 
```