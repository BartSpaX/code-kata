import random


class Robot:
    created_names = []
    def __init__(self):
        self.name = self.__generate_new_name()
        Robot.created_names.append(self.name)
    
    def __generate_new_name(self):
        new_name = "".join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        new_name += "".join(random.choices('0123456789', k=3))
        while new_name in Robot.created_names:
            new_name = "".join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
            new_name += "".join(random.choices('0123456789', k=3))
        return new_name
    
    def reset(self):
        Robot.__init__(self)
