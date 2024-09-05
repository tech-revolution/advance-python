# Static Methods in python

class myClass:
    # fname = "Asad"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def pname(self):
        print(f"Hello {self.fname}")

    # @staticmethod
    # def add(a, b):
    #     return a+b

    # @classmethod
    # def change_value(cls, newval):
    #     cls.fname = newval


obj1 = myClass("Ali-")
# print(obj1.name)
# print(obj1.pname())
# print(obj1.add(1,2))

# myClass.fname = "Bilal"
# print(obj1.fname)
# obj1.change_value("Bilal")
# print(obj1.pname())
# print(myClass.fname)