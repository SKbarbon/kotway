"""
Manage the 'kotway' commands on terminal.
"""
from .create_project import create_project
from .run_project import run_project
from .build_static_web import build_static_web

def commands_manager (commands: list[str]):
    if len(commands) < 1:
        raise Exception("You need to provide a kotway command name.")

    command_name: str = commands[1]
    command_args: list[str] = []
    if len(commands) > 2: command_args = commands[2:]

    if command_name == "create":
        create_project(command_args)
    elif command_name == "run":
        run_project(command_args)
    elif command_name == "build":
        build_static_web(command_args)