#!/usr/bin/python3
"""
Module console
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit the command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel,
        saves it (to the JSON file) and prints the id\n"""
        if not arg:
            print('** class name missing **')
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print('** class doesn\'t exist **')

    def do_show(self, arg):
        """Print the string representation of an instance
        based on the class name and id\n"""
        if not arg:
            print("** class name missing **")
            return

        li_arg = arg.split()
        if len(li_arg) == 1:
            print("** instance id missing **")
            return

        try:
            statement = f"{li_arg[0]}.{li_arg[1]}"
            print(storage.all()[statement])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return

        li_arg = arg.split()
        if len(li_arg) == 1:
            print("** instance id missing **")

        try:
            statement = f"{li_arg[0]}.{li_arg[1]}"
            del storage.all()[statement]
            storage.save()
        except KeyError:
            print("** no instance found")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        if not arg:
            for obj in storage.all():
                print(storage.all()[obj].__str__())
            return

        try: 
            cls_name = eval(arg).__name__
        except NameError:
            print("** class doesn't exist **")
            return

        for obj in storage.all():
            if obj.startswith(f"{cls_name}."):
                print(storage.all()[obj].__str__())

    def do_update(self, arg):
        """Updates an instance based on the class name and if
        by adding or updating attribute (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return

        li_arg = arg.split()
        if len(li_arg) == 1:
            print("** instance id missing **")
            return

        try:
            statement = f"{li_arg[0]}.{li_arg[1]}"
            storage.all()[statement]
        except KeyError:
            print("** no instance found **")
            return

        if len(li_arg) == 2:
            print("** attribute name missing **")
            return

        if len(li_arg) == 3:
            print("** value missing **")
            return

        try:
            statement = f"{li_arg[0]}.{li_arg[1]}"
            obj = storage.all()[statement]
            if li_arg[3].startswith('"') and li_arg[3].endswith('"'):
                li_arg[3] = li_arg[3][1:-1]
            setattr(obj, li_arg[2], li_arg[3])
            obj.save()
        except Exception:
            print("** value missing **")

    def emptyline(self):
        """Do nothing when hit enters\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
