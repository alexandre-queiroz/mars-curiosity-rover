from random import uniform, randint

class LixoEspacial:
    def __init__(self):
        self.peso = round(uniform(1.12, 8.55), 2)
        self.diametro = round(uniform(0.1, 0.4), 2)
        self.tipo = randint(0, 1)

    def __repr__(self):
        tipo = "Não metálico"
        if self.tipo == 1:
            tipo = "Metálico"
        return "Tipo " + tipo