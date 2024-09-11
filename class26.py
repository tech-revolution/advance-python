"""
Ezaan 200
Ali Ahmad 200
Nouman 200
Rehan 200
Kaif 200
Ali Raza 200
Iqra 200
Eman 200

"""

# File I/O in Python

# f = open("demo.txt", "r") # not truncated
# f = open("test.txt", "w") # truncated
# f = open("test.txt", "a") # 
# f = open("test.txt", "r+") # 
# f = open("test.txt", "w+") 
# f.write("Ezaan")
# print(f.read())
# print(f.readlines()[1])
# print(f.read())
# print(f.readline())
# print(f.readline())

# import os as a

# f = open("demo.txt", "a+") 
# # f.write("This is Python")
# del f
# # a.remove("test.txt")

# f.close()
import pandas as pd

list_of_students = []

def get_student_data():
    name = input("Enter your Name: \n")
    roll_no = input("Enter your Roll Number: \n")
    age = input("Enter your Age: \n")
    phone = input("Enter your Phone: \n")

    student = {
        "Name": name,
        "Roll Number": roll_no,
        "Age": age,
        "Phone": phone
    }

    list_of_students.append(student)

def excel_save(file_name):
    df = pd.DataFrame(list_of_students)
    df.to_excel(file_name, index=False, engine='openpyxl')

while True:
    get_student_data()

    next = input("Do you want to add another student info press y/n").lower()

    if next != 'y':
        break

excel_save('Student_Data.xlsx')

