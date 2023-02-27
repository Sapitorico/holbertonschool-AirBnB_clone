#!/usr/bin/python3
"""
clase HBNBCommand este sera el interprete de comandos:
encargado de crear actualizar y destruir clases y objetos
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """field to clase HBNBComman """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
