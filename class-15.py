# Functions
# print()
# def my_fun():
#     print("Hello")

# my_fun()

# def print_name(fname):
#     print(f"My name is {fname}")


# var1 = input("Enter your name: ")
# print_name(var1)


# def print_details(fname, lname, age, email):
#     print(f"My name is {fname} {lname} and my age is {age} also my email is {email}")


# fname = input("Enter your first name: ")
# lname = input("Enter your last name: ")
# age = int(input("Enter your age: "))
# email = input("Enter your email: ")


# print_details(fname, lname, age, email)


# void type 
# def sum(a, b, c):
#     print(a+b+c)

# sum(4, 5, 6)
# def sum(a, b):
#     return f"The result of two numbers is {a+b}"

# res = sum(3,5)
# print(res)

# args and kwargs

# def sum(para, *para1):
#     print(para)
#     sum = 0
#     for i in para1:
#         sum = sum+i
#     print(f"Sum is : {sum}")

# sum("This is sum function")

# **kwargs[]
def print_dict(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


fname = input("Enter first name")
lname = input("Enter last name")
age = int(input("Enter age"))
print_dict(firstname=fname, lastname=lname, stdage=age)