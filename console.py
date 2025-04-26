#!/usr/bin/python3
"""Defines the HBNBCommand class."""

import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB command line interpreter."""

    def __init__(self):
        """Initializes the interpreter."""
        super().__init__()
        self.prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quits the interpreter."""
        return True

    def do_EOF(self, arg):
        """Exits on Ctrl+D (EOF)."""
        print()
        return True

    def do_help(self, arg):
        """List available commands with "help" or detailed help with "help cmd"."""  # noqa
        super().do_help(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
