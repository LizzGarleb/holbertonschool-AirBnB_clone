#!/usr/bin/python3
"""Module console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit the command to exit the program\n'"""
        Return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when hit enters"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
