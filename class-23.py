# 
# def welcome(abc):
#     def xyz():
#         print("Welcome to our Program")
#         abc()
#         print("Thanks for using our Program")
#     return xyz


# @welcome
# def sum():
#     print("Hello")

# @welcome
# def test():
#     print("This is testing")


# sum()
# test()
# welcome(sum)() optional


class myclass:
    def __init__(self, a):
        self._a = a

    def print_details(self):
        print("The value of a is ", self._a)

    @property
    def get_value(self):
        return self._a

    @get_value.setter
    def set_value(self, new):
        self._a = new

        

ob1 = myclass(5)
ob1._a = 10
print(ob1._a)

