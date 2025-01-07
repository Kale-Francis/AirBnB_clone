#!/usr/bin/python3
"""Command interpreter for AirBnB clone project"""
import cmd
import json
import os
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for AirBnB clone"""
    prompt = "(hbnb) "

    def quit(self, arg):
        """Quit command to exit the program"""
        return True

    def EOF(self, arg):
        """Handles EOF (Ctrl+D) to exit the program"""
        print()
        return True

    def emptyline + ENTER(self):
        """Do nothing on empty input"""
        pass

    def do_create(self, args):
        """Creates a new instance of a class"""
        if not args:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

def do_show(self, args):
    """Shows an instance by its ID"""
    if len(args) < 1:
        print("** class name missing **")
        return
    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    instance_id = args[1]
    key = f"{class_name}.{instance_id}"
    instance = storage.all().get(key)
    if not instance:
        print("** no instance found **")
        return
    print(instance)

def do_destroy(self, args):
    """Destroys an instance by its ID"""
    if len(args) < 1:
        print("** class name missing **")
        return
    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    instance_id = args[1]
    key = f"{class_name}.{instance_id}"
    instance = storage.all().get(key)
    if not instance:
        print("** no instance found **")
        return
    storage.delete(instance)
    storage.save()
    print(f"{class_name} instance {instance_id} destroyed.")


    def do_all(self, args):
        """Shows all instances or those of a specific class"""
        if len(args) < 1:
            print("** class name missing **")
        return
        class_name = args[0]
        if class_name not in self.classes:
         print("** class doesn't exist **")
        return
        instances = storage.all(class_name)
        for instance in instances.values():
            print(instance)

    def do_count(self, args):
        """Counts all instances of a class"""
    if len(args) < 1:
        print("** class name missing **")
        return
    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return
    instances = storage.all(class_name)
    print(len(instances))


def do_update(self, args):
    """Updates an instance by its ID"""
    if len(args) < 1:
        print("** class name missing **")
        return
    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    instance_id = args[1]
    key = f"{class_name}.{instance_id}"
    instance = storage.all().get(key)
    if not instance:
        print("** no instance found **")
        return
    if len(args) < 3:
        print("** attribute name missing **")
        return
    attribute_name = args[2]
    if len(args) < 4:
        print("** value missing **")
        return
    value = args[3]
    setattr(instance, attribute_name, value)
    instance.save()

    """Updates an instance using a dictionary"""
    if len(args) < 1:
        print("** class name missing **")
        return
    class_name = args[0]
    if class_name not in self.classes:
        print("** class doesn't exist **")
        return
    if len(args) < 2:
        print("** instance id missing **")
        return
    instance_id = args[1]
    key = f"{class_name}.{instance_id}"
    instance = storage.all().get(key)
    if not instance:
        print("** no instance found **")
        return
    if len(args) < 3:
        print("** dictionary missing **")
        return
    dictionary = eval(args[2])  # Convert string representation of dictionary
    for key, value in dictionary.items():
        setattr(instance, key, value)
    instance.save()


    def do_count(self, args):
        """Counts all instances of a class"""
        if len(args) < 1:
            print("** class name missing **")
        return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
        return
        instances = storage.all(class_name)
        print(len(instances))



if __name__ == '__main__':
    HBNBCommand().cmdloop()
