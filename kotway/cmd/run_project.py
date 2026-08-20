import os, subprocess, sys

def run_project (command_args: list[str]):
    """Run a kotway project."""
    # STEP: Get target path.
    selected_path: str = "./" # The path where the project folder is at.

    if len(command_args) >= 1:
        selected_path = ""
        index = 0
        for p in command_args[0:]:
            selected_path = selected_path + p
            if index >= len(command_args): selected_path = selected_path + " "
            index = index + 1
    # validate the selected path.
    if not os.path.isdir (selected_path):
        raise Exception(f"The provided path `{selected_path}` is not a folder.")

    result = subprocess.run(
        [sys.executable, "main.py"],
        cwd=os.path.join(selected_path)
    )
    print(f"Process exited with code: {result.returncode}")