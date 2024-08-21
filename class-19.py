# Inheritance

class Animal:
    def __init__(self, animal_name, animal_category, animal_age):
        self.name = animal_name
        self.cat = animal_category
        self.age = animal_age

    def animal_details(self):
        return f"Animal name is {self.name} category is {self.cat} and age is {self.age}"

    
    
class Dog(Animal):
    def __init__(self, animal_name, animal_category, animal_age, shape):
        super().__init__(animal_name, animal_category, animal_age)
        self.shape = shape

    

class Cat(Animal):
    def __init__(self, animal_name, animal_category, animal_age):
        super().__init__(animal_name, animal_category, animal_age)

    

# animal1 = Animal("Persian Cat", "Cats", 2)

dog1 = Dog("Pakistani Dog","Dog", 3, "Any")
print(dog1.shape)
# print(dog1.animal_details())

# details = animal1.animal_details()
# print(details)

# def prnit_name(name):
#     pass

# prnit_name()