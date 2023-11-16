class CPerson:
    def __init__(self, n, l, s, d, g):
        self.n = n
        self.l = l
        self.s = s
        self.d = d
        self.g = g
    def __del__(self):
        print('Красота')
    def coxr(self):
        print(f'Ваши данные: {self.n} {self.l} {self.s} {self.d} {self.g}')



inf = CPerson(input('Your name: '), input('Your lastname: '), input('Your surname: '), input('Your data: '), input('Your gender: '))
inf.coxr()
