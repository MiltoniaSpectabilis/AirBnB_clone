#!/usr/bin/python3
"""
HBNB command interpreter
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    HBNB command interpreter class
    """

    prompt = '(hbnb) '

    def precmd(self, line):
        """Print a new line before the prompt in non-interactive mode"""
        if not sys.stdin.isatty():
            print()
        return line

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of a class, save it, and print the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            cls = globals()[arg]
            new_instance = cls()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = globals()[args[0]]
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = globals()[args[0]]
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        if arg:
            try:
                cls = globals()[arg]
                instances = [str(obj) for key, obj in storage.all().items() if arg in key]
                print(instances)
            except KeyError:
                print("** class doesn't exist **")
        else:
            instances = [str(obj) for key, obj in storage.all().items()]
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = globals()[args[0]]
            if len(args) < 2:
                print("** instance id missing **")
                return
            key = "{}.{}".format(args[0], args[1])
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            obj = storage.all()[key]
            setattr(obj, args[2], args[3].strip('"'))
            obj.save()
        except KeyError:
            print("** class doesn't exist **")

    def do_help(self, arg):
        """List available commands with 'help' or detailed help with 'help cmd'."""
        if arg:
            # Try to execute parent class do_help() method
            try:
                func = getattr(self, 'help_' + arg)
            except AttributeError:
                try:
                    doc = getattr(self, 'do_' + arg).__doc__
                    if doc:
                        self.stdout.write("%s\n" % str(doc))
                        return
                except AttributeError:
                    pass
                self.stdout.write("%s\n" % str(self.nohelp % (arg,)))
                return
            func()
        else:
            if not sys.stdin.isatty():
                print()
                print("Documented commands (type help <topic>):")
                print("========================================")
                commands = [name[3:] for name in dir(self) if name.startswith('do_')]
                print(" ".join(commands))
            else:
                print()
                print("Documented commands (type help <topic>):")
                print("========================================")
                commands = [name[3:] for name in dir(self) if name.startswith('do_')]
                print(" ".join(commands))
                print()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

