class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def names(self):
        print(f"Вас зовут{self.name}")
    
    def ages(self):
        print(f"{self.age} вам лет")

ban = Human('Ban', 15)

print(f"{ban.name}")
print(f'{ban.age}')
