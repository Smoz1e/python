class House():
    """описание дома"""
    def __init__(self, street_name, number):
        self.street = street_name
        self.num = number
        self.age = 0

    def build(self):
        """Строт дом"""
        print(f"Дом на улице {self.street} построин, его номер {self.num}")
    
    def old(self, old):
        self.age += old


    
House1 = House("Московская", "1")
print (House1.num)

House1.build()

print(House1.age)

House1.old(5)

print(f"Возраст дома составляет {House1.age}")

# Класс потомок 

class Prospect_house(House):
    """Дома на проспекте"""
    def __init__(self, street_name, number, dor="0"):
        super().__init__(street_name, number)
        self.dor = dor
        



hous2 = Prospect_house("Московская", "1","10")
print(hous2.dor)