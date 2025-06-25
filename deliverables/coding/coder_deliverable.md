# Coder Deliverable

## Changed Files

- `src/dw6/augmenter.py`
- `src/dw6/main.py`

## Git Diff

```diff
diff --git a/src/dw6/augmenter.py b/src/dw6/augmenter.py
new file mode 100644
index 0000000..c1614f0
--- /dev/null
+++ b/src/dw6/augmenter.py
@@ -0,0 +1,26 @@
+# src/dw6/augmenter.py
+
+import os
+from .state_manager import get_current_requirement_id
+
+WORKING_PHILOSOPHY = """**Working Philosophy:** We always look to granularize projects into small, atomic requirements and sub-requirements. The more granular the requirement, the easier it is to scope, implement, test, and validate. This iterative approach minimizes risk and ensures steady, verifiable progress."""
+
+def process_prompt(prompt_text: str):
+    """
+    Augments a raw user prompt and generates a formal technical specification markdown file.
+    """
+    requirement_id = get_current_requirement_id()
+    file_path = f"deliverables/engineering/cycle_{requirement_id}_technical_specification.md"
+
+    content = f"# Requirement: {requirement_id}\n\n"
+    content += f"## 1. High-Level Goal\n\n{prompt_text}\n\n"
+    content += f"## 2. Guiding Principles\n\n{WORKING_PHILOSOPHY}\n"
+
+    try:
+        os.makedirs(os.path.dirname(file_path), exist_ok=True)
+        with open(file_path, 'w') as f:
+            f.write(content)
+        print(f"Successfully created specification: {file_path}")
+    except IOError as e:
+        print(f"ERROR: Could not write to file {file_path}.\n{e}", file=sys.stderr)
+        sys.exit(1)
diff --git a/src/dw6/main.py b/src/dw6/main.py
index 7bbd031..a55f148 100644
--- a/src/dw6/main.py
+++ b/src/dw6/main.py
@@ -2,6 +2,7 @@
 import argparse
 import sys
 from dw6.state_manager import StateManager
+from dw6.augmenter import process_prompt
 
 def main():
     """Main entry point for the DW6 CLI."""
@@ -15,6 +16,10 @@ def main():
     # Approve command
     subparsers.add_parser("approve", help="Approve the current stage and move to the next.")
 
+    # New command
+    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
+    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")
+
     if len(sys.argv) == 1:
         parser.print_help(sys.stderr)
         sys.exit(1)
@@ -27,6 +32,8 @@ def main():
         manager.review()
     elif args.command == "approve":
         manager.approve()
+    elif args.command == "new":
+        process_prompt(args.prompt)
 
 if __name__ == "__main__":
     main()
```