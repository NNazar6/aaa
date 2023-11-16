class Phone:
    def __init__(self, number, model, weight):
        self.number = number
        self.model = model
        self.weight = weight

    def reciveCall(self, name):
        print(f'Звонит: {name}')

    def getNumber(self, number):
        print(number)
