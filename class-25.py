# Access Specifier

class Student:
    def __init__(self):
        self.__name = "name"

    def __print_name(self):
        print(self.__name)
    
    def hello(self):
        return self.__print_name()

class Chemistry(Student):
    pass
obj1 = Student()
print(obj1.hello())
# Student.__name = "Ali"
# # print(obj1._Student__name)
# print(obj1.__dir__())