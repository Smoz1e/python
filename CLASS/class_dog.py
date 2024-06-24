class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
            print(f"{self.name} села")
    def roll_over(self):
            print(f"{self.name} прокрутись")

my_dog =Dog('Bob', 6)
print(f"Мою собаку зовут {my_dog.name}")
print(f'Моей собаке {my_dog.age} лет')
print(my_dog.sit(), my_dog.roll_over())
print()