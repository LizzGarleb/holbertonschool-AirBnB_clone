#!/usr/bin/python3
"""
Module console
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand
    """
    prompt = '(hbnb) '
    valid_cls = ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]

    def do_quit(self, arg):
        """Quit the command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        return True

    def do_create(self, arg):
        """Create a new instance of BaseMod~el,
        saves it (to the JSON file) and prints the id\n"""
        
        if not arg:
            print('** class name missing **')
            return

        args = arg.split()
        if args[0] not in self.valid_cls:
            print("** class doesn't exist **")
            return

        obj = eval(args[0])()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance
        based on the class name and id\n"""
        if not arg:
            print("** class name missing **")
            return

        li_arg = arg.split()
        try:
            model = storage.all()[f"{li_arg[0]}.{li_arg[1]}"]
            print(model)
        except KeyError:
            print("** no instance found **")
        except IndexError:
            if li_arg[0] not in self.valid_cls:
                print("** class doesn't exist **")
            elif len(li_arg) == 1:
                print("** instance id missing **")
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return

        li_arg = arg.split()

        try:
            model = storage.all()[f"{li_arg[0]}.{li_arg[1]}"]
            del model
            storage.save()
        except KeyError:
            print("** no instance found **")
        except IndexError:
            if len(li_arg) == 1:
                print("** instance id missing **")

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

        try:
            model = storage.all()[f"{li_arg[0]}.{li_arg[1]}"]
            if li_arg[3].startswith('"') and li_arg[3].endswith('"'):
                li_arg[3] = li_arg[3][1:-1]
            setattr(model, li_arg[2], li_arg[3])
            model.save()
        except KeyError:
            print("** no instance found **")
        except IndexError:
            if len(li_arg) == 1:
                print("** instance id missing **")
            elif len(li_arg) == 2:
                print("** attribute name missing **")
            elif len(li_arg) == 3:
                print("** value missing **")

    def emptyline(self):
        """Do nothing when hit enters\n"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
