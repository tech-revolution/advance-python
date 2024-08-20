# OOP
# Object Oriented Programing
'''
1. Ineritance
2. Encapsulation
3. Polymorphism
4. Abstraction

'''
# name = "Ali"
# class Student:
#     fname = "Ali"
#     lname = "Ahmed"
#     course = "Python"

#     def print_details(self):
#         print(f"Hello my name is {Student.fname}")

# std1 = Student()
# std2 = Student()

# print(std2.print_details())

class Student:
    def __init__(self, name, age, course)-> None:
        self.fullname = name
        self.student_age = age
        self.course_program = course

    def print_details(self):
        print(f"Hello my name is {self.fullname} and my age is {self.student_age} my course is {self.course_program}")
    


std1 = Student("Salman Sabir", 56, "Python")
std2 = Student("Anmol", 67, "Web")

print(std1.print_details())
