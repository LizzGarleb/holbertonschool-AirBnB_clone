#!/usr/bin/python3
import cmd, sys

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit the command to exit the program\n'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        print()
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
