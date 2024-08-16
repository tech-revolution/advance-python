# Recursive functions
# def my_rec(a):
#     if a>0:
#         res = a + my_rec(a-1)
#         # print(res)
#     else:
#         res = 0
#     return res

# print(my_rec(2))

# def fact(a):
#     if a == 1:
#         return 1
#     elif a == 0:
#         return 1
#     else:
#         return a*fact(a-1)
    
# print(fact(0))
# import math

# print(math.factorial(5))

# Lambda Functions

# a = lambda b : b*2
# print(a(3))
# def my_fun(a):
#     return lambda b:b+a

# var1 = my_fun(2)
# print(var1(3))

# a = lambda b, c, d : b+c+d
# print(a(3, 4, 7))



# Try and Except
# print(x)
# x = 6
# try:
#     print(x)
# except:
#     print("Variable is not defined")
# finally:
#     print(2+2)
# else:
#     print("Thanks")

try:
    f = open("sample.txt")
    try:
        f.write("Hello world")
    except:
        print("File not open")
    finally:
        f.close()
except:
    print("File does not exist")  
