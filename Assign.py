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
row_in = int(input("Enter Row: "))
col_in = int(input("Enter Column: "))

list1 = [[0 for col in range(col_in)] for row in range(row_in)]

for row in range(row_in):
    for col in range(col_in):
        list1[row][col] = row * col

print(list1)
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