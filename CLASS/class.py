class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        def sit(self):
            print(f'{self.name} сейчас сидит')

        def roll_over(self):
            print(f"{self.name} делает перекат")
    ...
my_dog = Dog('Williw', 6)
print(f"Имя моей собаки :{my_dog.name}")
print(f"Возраст моей собаки:{my_dog.age}")