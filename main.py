class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        if type(name) == type(''):
            self.__name = name
        else:
            print("Недопустимый параметр")