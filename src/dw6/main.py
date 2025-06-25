# dw6/main.py
import argparse
import sys
import re
import subprocess
from pathlib import Path
from datetime import datetime, timezone
from dw6.state_manager import WorkflowManager
from dw6.augmenter import process_prompt

META_LOG_FILE = Path("logs/meta_requirements.log")

def register_meta_requirement(description: str):
    """Logs a new meta-requirement to the meta_requirements.log file."""
    META_LOG_FILE.parent.mkdir(exist_ok=True)
    
    last_id = 0
    if META_LOG_FILE.exists():
        with open(META_LOG_FILE, "r") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                match = re.search(r'^\[ID:(\d+)\]', last_line)
                if match:
                    last_id = int(match.group(1))

    new_id = last_id + 1
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    log_entry = f"[ID:{new_id}] [TS:{timestamp}] {description}\n"

    with open(META_LOG_FILE, "a") as f:
        f.write(log_entry)
    
    print(f"Successfully logged meta-requirement {new_id}.")

def main():
    """Main entry point for the DW6 CLI."""
    parser = argparse.ArgumentParser(description="DW6 Workflow Management CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands", required=True)

    # Approve command
    subparsers.add_parser("approve", help="Approve the current stage and move to the next.")

    # New command
    new_parser = subparsers.add_parser("new", help="Create a new requirement specification from a prompt.")
    new_parser.add_argument("prompt", type=str, help="The high-level user prompt.")

    # Meta-req command
    meta_req_parser = subparsers.add_parser("meta-req", help="Register a new meta-requirement for the workflow.")
    meta_req_parser.add_argument("description", type=str, help="The description of the meta-requirement.")

    # Do command
    do_parser = subparsers.add_parser("do", help="Execute a governed action.")
    do_parser.add_argument("action", type=str, help="The action to execute.")

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()
    
    if args.command == "meta-req":
        register_meta_requirement(args.description)
    elif args.command == "do":
        manager = WorkflowManager()
        try:
            manager.governor.authorize(args.action)
            # The command is authorized. The gatekeeper's job is done.
        except PermissionError:
            sys.exit(1)
    else:
        manager = WorkflowManager()
        if args.command == "approve":
            manager.approve()
        elif args.command == "new":
            process_prompt(args.prompt)

if __name__ == "__main__":
    main()
