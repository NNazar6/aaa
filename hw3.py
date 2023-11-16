class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimetr(self):
        print(f'Периметр: {self.a + self.b + ((self.a ** 2 + self.b ** 2) ** 0.5)}')

    def ploshaid(self):
        print(f'Площадь: {self.a * 0.5 * self.b}')


P1usi = Triangle(3, 5)
P1usi.perimetr()
P1usi.ploshaid()
