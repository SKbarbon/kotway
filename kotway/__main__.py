import sys
from .cmd.commands_manager import commands_manager

# If this is running by a kotway command.
if len(sys.argv) > 1:
    commands_manager(sys.argv)