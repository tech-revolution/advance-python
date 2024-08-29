# for i in range(10):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# for i in range(10):
#     print()
#     for j in range(10-i):
#         print("*",end = " ")

# for i in range(10,0):
#     for j in range(10-i):
#         print(" ",end = " ")
#     for j in range(i):
#         print("*",end = " ")
#     print()
        
# for i in range(0,10):
#     for j in range(0,10-i-1):
#         print(" ",end = " ")
#     for k in range(0,i+1):
#             print("*",end = " ")
#     print()

# Fibonacci Series 
# 0 1 1 2 3
'''
-1 enter positive number
0
1 
n1, n2 = 0 , 1
print(n1)
nth = n1 + n2
n1 = n2
n2 = nth


[[0,0,0,0], [0,1,2,3]]
'''
# row_in = int(input("Enter Row: "))
# col_in = int(input("Enter Column: "))

# list1 = [[0 for col in range(col_in)] for row in range(row_in)]

# for row in range(row_in):
#     for col in range(col_in):
#         list1[row][col] = row * col

# print(list1)
"""
Student management system
1. Press 1 for create a new student
    1. Enter student name
    2. enter student age
    3. enter email
    4. enter class name
    Student created successfuly
    press 1 for view students list
    press 2 for main menu
press 2 for delete student
press 3 for exit program
Thank you for using our system


"""

# Camera Assignment

# import cv2
# import numpy as np
# ip = "http://192.168.1.29:8080"
# ac = cv2.VideoCapture(ip)
# while(True):
#     camera, frame = ac.read()
#     if frame is not None:
#         cv2.imshow("Frame", frame)
#     q = cv2.waitKey(1)
#     if q==ord("q"):
#         break
# cv2.destroyAllWindows()








# def convert_roman(r):
#     r=r.upper()
#     roman_dic={"I": 1,"V": 5,"X": 10,"L": 50,"C": 100,"D": 500,"M": 1000}
#     decimal=0
#     length_of_roman=len(r)
#     for i in range(length_of_roman):
#         if r[i] not in roman_dic:
#              print("wrong numerals.....")
#         current=roman_dic[r[i]]

#         if i<length_of_roman-1 and roman_dic[r[i]]< roman_dic[r[i+1]]:
#              decimal-=current
#             # decimal-=roman_dic[roman[i+1]]-roman_dic[roman[i]]
#         else:
#                 decimal += current
    
#     return decimal

# r=input("enter roman number :")
# print(f"the decimal value is: {convert_roman(r)}")

# q------2
# import  random
# def die_roll(n):
#         random_number=random.randint(1,n)
#         return random_number
# n=int(input("Enter no of sides of a die you want "))
# print("after rolling",die_roll(n))



# import random

# def dice_roll(dice,sides):
#     roll = []

#     for i in range(0,dice):
#       face = random.randint(1,sides)
#       roll.append(face)
#     return roll  

# dice = int(input("Dice: "))

# if (dice <=0):
#     print("Must have at least one dice")
#     quit()


# sides = int(input("Sides: "))
# if (sides <=0):


#     print("Must have one side: ")
#     quit()

# roll = dice_roll(dice, sides)

# print(roll)  

# def main():
#     while True:
#         input("Press 'Enter' to roll the dice or type 'quit' to exit:")
#         if input().lower() == "quit":
#             break  
# if __name__ == "__main__":
#         main()