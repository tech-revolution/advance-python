# Loops / Do not repeat yourself
# while
# 


# i = 0
# while i<len(ls1):
#     print(ls1[i])
#     i+=1

# for loop

# for i in ls1:
#     print(f"Hello My name is {i} and Bye")
#     if i == "Agha":
#         break

# for i in ls1:   
#     if i == "Naveed":
#         continue
#     elif i == "Agha":
#         continue
#     print(f"Hello My name is {i} and Bye")
# for i in range(2, 20, 3):
#     print(i)
# if i > 5:
#     print("i is no more then 20")

"""
Ali 23
Naveed 34

"""

# Nested Loop
# ls1 = ["Ali", "Naveed", "Agha", "Burhan"]
# ls2 = [23, 34, 56, 76]

# for i in ls1:
#     for j in ls2:
#         # print(i, j)
#         pass

for i in range(5):
    for j in range(3):
        print("*", end=" ")
    print()

