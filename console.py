#!/usr/bin/python3
"""
Module console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class HBNBCommand
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit the command to exit the program\n"""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        print()
        exit()

    def emptyline(self):
        """Do nothing when hit enters\n"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
