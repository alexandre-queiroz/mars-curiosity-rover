import random

class LixoEspacial:
    def __init__(self):
        self.peso = round(random.uniform(1.12, 8.55), 2)
        self.diametro = round(random.uniform(0.1, 0.4), 2)
        self.tipo = random.randint(0, 1)

    def __repr__(self):
        tipo = "Não metálico" if self.tipo == 0 else "Metálico"
        return "Tipo " + tipo
