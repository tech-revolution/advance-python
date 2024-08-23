# Polymorphism in python

# a = 5
# a = 6
# # print(a+b)



# class parent:
#     def info(self):
#         print("Parent")

# class Son(parent):
#     def info(self):
#         print("Son")

# class Daughter(parent):
#     def info(self):
#         print("Daughter")

from multipledispatch import dispatch

# class test_class:
#     @dispatch(int, int)
#     def test(x,y):
#         print(x+y)

#     @dispatch(int, int, int)
#     def test(x,y,z):
#         print(x+y+z)

# class derivedClass1(test_class):
#     @dispatch(int, int, int, int)
#     def test(x,y,z,a):
#         print(x+y+z+a)

# person1 = test_class()
# person2 = derivedClass1()
# print(person2.test(2,3))

# obj1 = test_class()
# obj2 = test_class()

# print(obj1.test(23,12))
# print(obj1.test(23,12,45))

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

class Hr_Employee(Employee):
    def __init__(self, name, age):
        super().__init__(name, age)
        
# obj1 = Hr_Employee("Ali", 23)

