class Restoran():

    def __init__(self,restoran_name, cuisine_typ):
        self.restoran_name = restoran_name
        self.cuisine_typ = cuisine_typ

    def describe_restoran(self):
        print(f"{self.restoran_name} {self.cuisine_typ}")

    def open_restoran(self):
        print(f"{self.restoran_name} открыт")

my_restoran = Restoran('Jass','Open')

print(my_restoran.restoran_name, my_restoran.cuisine_typ)