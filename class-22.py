# Doc String

# def my_fun():
#     """
#     This function print hello World
#     """
#     print("Hello World")


# print(my_fun.__doc__)


# Operator overloading
# print(10+30)

# print(int.__add__(10+30))

class A:
    def __init__(self, x):
        self.a = x

    def __add__(self, other):
        return self.a + other.c
    
        

class B:
    def __init__(self, x):
        self.c = x
a = A(5, )
b = B(4)

print(a+b) # int.__add__(a+b)
# A.__add__(a, b)

