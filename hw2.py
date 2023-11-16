class Square:
    def __init__(self, a):
        self.a = a

    def ploshiad(self):
        print(f'Площадь: {self.a * self.a}')

    def perimetr(self):
        print(f'Периметр: {self.a * 4}')


jusi = Square(3)
jusi.ploshiad()
jusi.perimetr()
