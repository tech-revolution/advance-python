# Multiple Inheritance

class Mamal:
    def mamal_info(self):
        print("Mamal Function")

class wingedAnimal:
    def winged_info(self):
        print("Winged Function")

class sparrow(Mamal, wingedAnimal):
    def sparrow_info(self):
        print("Mamal Function")

obj1 = sparrow()

print(obj1.mamal_info())

# Multilevel Ineritance

class GrandFather:
    def Grand_Father_info(self):
        print("Grand Father class")

class Father(GrandFather):
    def info(self):
        print("Father class")

class Mother:
    def Mother_info(self):
        print("Mother class")

class Son(Father, Mother):
    def info(self):
        print("Son class")

class Daughter(Father, Mother):
    pass

son1 = Son()
sister1 = Daughter()

print(son1.info())
# print(sister1.Grand_Father_info())
# print(sister1.Mother_info())
