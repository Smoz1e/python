
class gaz():
    def __init__(self, a = None, b = None, c = None):
        self.a = a
        self.b = b
        self.c = c
    
    def tig(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a == 0 and b == 0 and c == 0:
            print(f'Из отрезков с длиной a = {self.a}, b = {self.b}, с = {self.c} треугольник построить нельзя')


t  = gaz('0','0','0')
print(t.tig)
        
