import cmd
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, line):
        return True
    
    def do_quit(self, line):
        return True
    
    def do_help(self, arg):
        return super().do_help(arg)
    
    def emptyline(self):
        return
    
    def do_create(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            instance = 'BaseModel()'
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        elif arg == "BaseModel" and not arg:
            print("** instance id missing **")
        else:
            print("** no instance found **")
        
    def do_destroy(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        elif arg == "BaseModel" and not arg:
            print("** instance id missing **")
        else:
            print("** no instance found **")

    def do_all(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        else:
            print("** no instance found **")
    
    def d0_update(self, arg):
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        elif arg == "BaseModel" and not arg:
            print("** instance id missing **")
        elif arg == "BaseModel" and not arg:
            print("** attribute name missing **")
        elif arg == "BaseModel" and not arg:
            print("** value missing **")
        else:
            print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()