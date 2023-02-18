#!/usr/bin/python3
"""
Module console
"""
import cmd
from models.base_model import BaseModel
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
            statement = "{}.{}".format(li_arg[0], li_arg[1])
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
            statement = "{}.{}".format(li_arg[0], li_arg[1])
            del storage.all()[statement]
            storage.save()
        except KeyError:
            print("** no instance found")

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        if not arg:
            for obj in storage.all():
                print(str(storage.all()[obj]))
            return

        try: 
            cls_name = eval(arg).__name__
        except NameError:
            print("** class doesn't exist **")
            return

        for obj in storage.all():
            if obj.startswith(cls_name + "."):
                print(str(storage.all()[obj]))

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
        
        statement = "{}.{}".format(li_arg[0], li_arg[1])
        if statement not in storage.all():
            print("** no instance found **")
            return

        if len(li_arg) == 2:
            print("** attribute name missing **")
            return

        if len(li_arg) == 3:
            print("** value missing **")
            return

        if len(li_arg) > 4:
            print("Unknown command")
            return

        try:
            value = type(eval(li_arg[3]))(li_arg[3])
        except(NameError, ValueError):
            value = li_arg[3]
        
        setattr(storage.all(), li_arg[2], value)
        storage.all()[statement].save()
        storage.save()

    def emptyline(self):
        """Do nothing when hit enters\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
