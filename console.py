#!/usr/bin/python3
"""Defines the HBNBCommand class."""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """HBNB command line interpreter."""

    # i'll be adding more names later
    cls_names = {
        'BaseModel': BaseModel,
        'User': User,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review,
        'State': State
    }

    def __init__(self, stdin=None, stdout=None):
        """Initializes the interpreter."""
        super().__init__(stdin=stdin, stdout=stdout)
        self.prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.cls_names:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.cls_names[args[0]]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Shows an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in HBNBCommand.cls_names:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        cls_id = args[1]
        objects = storage.all()
        key = f"{cls_name}.{cls_id}"
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroys an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in HBNBCommand.cls_names:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        cls_id = args[1]
        objects = storage.all()
        key = f"{cls_name}.{cls_id}"
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Shows all instances."""
        if arg and arg not in HBNBCommand.cls_names:
            print("** class doesn't exist **")
            return
        args = arg.split()
        objects = storage.all()
        list_objects = []
        if args and args[0] in HBNBCommand.cls_names:
            for obj in objects.values():
                if obj.__class__.__name__ == args[0]:
                    list_objects.append(str(obj))
        else:
            for obj in objects.values():
                list_objects.append(str(obj))
        print(list_objects)

    def do_update(self, arg):
        """Updates an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        cls_name = args[0]
        if cls_name not in HBNBCommand.cls_names:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        cls_id = args[1]
        objects = storage.all()
        key = f"{cls_name}.{cls_id}"
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) == 3:
            print("** value missing **")
            return
        attr_value = args[3]
        setattr(objects[key], attr_name, attr_value[1:-1])
        storage.save()

    def default(self, line):
        """Shows all instances of a class using ".all()"."""
        split_line = line.split()
        cmd = split_line[0].split(".")
        if len(cmd) < 2:
            return
        cls_name = cmd[0]
        cls_method = cmd[1]
        if cls_name not in HBNBCommand.cls_names:
            return
        if cls_method != "all()":
            return
        objects = storage.all()
        instances = ""
        for k, v in objects.items():
            if cls_name in k:
                instances += str(v)
        print(f"[{instances}]")

    def do_quit(self, arg):
        """Quits the interpreter."""
        return True

    def do_EOF(self, arg):
        """Exits on Ctrl+D (EOF)."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
