# Dictionary
# name = "Ali"
# name = "ahmed"
# dict1 = {
#     "fname": "Bilal",
#     "lname": "Ahmad",
#     "age": 23,
#     # "hobby": ["Football", "Reading Books"],
#     "hobby": name
# }
# name = input("Enter name")
# dict1["fname"] = "anmol"

# # a = dict1["age"]
# # a = dict1.get("hobby")
# # a = dict1.keys()
# a = dict1.values()
# print(a)

# dict1 = {
#     "fname": "ali",
#     "lname": "Ahmad",
#     "age": 23,
#     "hobby": ["Football", "Reading Books"]
# }
# dict1.update({"email":"example@gmail.com"})
# print(dict1)
# dict1.pop("age")
# dict1.popitem()
# del dict1
# print(dict1)

# a = dict1.items()
# print(a)
# if "fname" in dict1:
#     print("yes")

# dict1.clear()
# print(type(dict1))
# for i in dict1.values():
#     print(i)
# for i in dict1:
#     print(i)
# for i, j in dict1.items():
#     print(i, j)
# dict2 = dict1.copy()
# print(dict1)
# print(dict2)

adv_py = {
    "std1":{
        "name": "Kainat",
        "age":34
    },
    "std2":{
        "name": "anmol",
        "age":45
    }
}
for i, j in adv_py.items():
    print(i)
    for y in j:
        print(y , j[y])

# print(adv_py["std1"]["name"])


