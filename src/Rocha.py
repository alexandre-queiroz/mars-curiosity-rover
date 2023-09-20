import random

class Rocha:
    def __init__(self):
        self.peso = round(random.uniform(0.5, 14.2), 2)
        self.diametro = round(random.uniform(0.3, 0.8), 2)
        self.tipo = random.randint(1, 3)

    def __repr__(self):
        return "Tipo " + str(self.tipo)
