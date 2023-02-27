#!/usr/bin/python3
"""
clase HBNBCommand este sera el interprete de comandos:
encargado de crear actualizar y destruir clases y objetos
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """field to clase HBNBComman """
    prompt = '(hbnb) '
    classes = ["BaseModel"]
    error_messages = {'missing_class': '** class name missing **',
                      'dont_exists_class': "** class doesn't exist **",
                      'missing_id': '** instance id missing **',
                      'dont_exists_id': '** no instance found **',
                      'missing_attribute': '** attribute name missing **',
                      'missing_value': '** value missing **'}

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel """
        if not arg:
            print(self.error_messages['missing_class'])
        elif arg not in self.classes:
            print(self.error_messages['dont_exists_class'])
        else:
            _class = globals().get(arg)
            obj = _class()
            storage.new(obj)
            storage.save()
            print(obj.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not arg:
            print(self.error_messages['missing_class'])
        elif args[0] not in self.classes:
            print(self.error_messages['dont_exists_class'])
        elif len(args) == 1:
            print(self.error_messages['missing_id'])
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print(self.error_messages['dont_exists_id'])
            else:
                print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print(self.error_messages['missing_class'])
        elif args[0] not in self.classes:
            print(self.error_messages['dont_exists_class'])
        elif len(args) == 1:
            print(self.error_messages['missing_id'])
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print(self.error_messages['dont_exists_id'])
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        if not arg:
            print([str(v) for k, v in storage.all().items()])
        elif args[0] not in self.classes:
            print(self.error_messages['dont_exists_class'])
        else:
            objects = storage.all()
            objs_list = [str(objs) for objs in objects.values()]
            print(objs_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print(self.error_messages['missing_class'])
        elif args[0] not in self.classes:
            print(self.error_messages['dont_exists_class'])
        elif len(args) == 1:
            print(self.error_messages['missing_id'])
        elif len(args) == 2:
            print(self.error_messages['missing_attribute'])
        elif len(args) == 3:
            print(self.error_messages['missing_value'])
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print(self.error_messages['dont_exists_id'])
            else:
                setattr(storage.all()[key], args[2], args[3])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
