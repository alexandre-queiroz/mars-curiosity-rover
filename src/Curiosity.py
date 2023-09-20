import random
from src.Rocha import Rocha
from src.LixoEspacial import LixoEspacial

class Curiosity:
    """
    A classe Curiosity simula as operações de exploração do rover Curiosity em Marte.
    O Curiosity coleta rochas e lixo espacial durante suas explorações e realiza a organização
    desses materiais de acordo com seu peso e tipo para otimizar o armazenamento.

    Attributes:
        deposito_rocha (list): Lista para armazenar rochas coletadas.
        exploracao_rocha (list): Lista temporária de rochas encontradas durante a exploração.
        deposito_lixo (list): Lista para armazenar lixo espacial coletado.
        exploracao_lixo (list): Lista temporária de lixo espacial encontrado durante a exploração.
        peso (float): Peso total dos materiais armazenados.

    Methods:
        iniciar_exploracao: Inicia a simulação de exploração do Curiosity.
        coletar_rocha: Coleta uma rocha e a adiciona ao depósito, se atender aos critérios de tamanho.
        coletar_lixo: Coleta lixo espacial e o adiciona ao depósito, se atender aos critérios de tamanho.
        coleta_materiais: Realiza a coleta de materiais durante a exploração.
        organizar_rochas: Organiza as rochas no depósito, equilibrando os tipos e mantendo o peso dentro dos limites.
    """
    def __init__(self):
        self.deposito_rocha = []
        self.exploracao_rocha = []
        self.deposito_lixo = []
        self.exploracao_lixo = []
        self.peso = 0

    def iniciar_exploracao(self):
        """
        Inicia a simulação de exploração do Curiosity.
        """
        x = 0
        while x < 3:
            self.deposito_rocha = []
            self.exploracao_rocha = []
            self.deposito_lixo = []
            self.exploracao_lixo = []
            self.peso = 0

            for i in range(random.randint(90, 400)):
                self.exploracao_rocha.append(Rocha())
                self.exploracao_lixo.append(LixoEspacial())

            self.coleta_materiais()
            self.organizar_rochas()
            x += 1

            tipo1 = sum(1 for rocha in self.deposito_rocha if rocha.tipo == 1)
            tipo2 = sum(1 for rocha in self.deposito_rocha if rocha.tipo == 2)
            tipo3 = len(self.deposito_rocha) - tipo1 - tipo2

            m = sum(1 for lixo in self.deposito_lixo if lixo.tipo == 1)
            n = len(self.deposito_lixo) - m

            print("\nExploração nº: " + str(x) + " finalizada")
            print("Quantidade de rochas do tipo 1: " + str(tipo1))
            print("Quantidade de rochas do tipo 2: " + str(tipo2))
            print("Quantidade de rochas do tipo 3: " + str(tipo3))
            print("\nQuantidade de lixo Metálico: " + str(m))
            print("Quantidade de lixo Não Metálico: " + str(n))
            print("\nPeso total: " + str(self.peso))
            print("\nCuriosity terminou exploração. Liberando espaço de armazenamento.")

    def coletar_rocha(self, rocha):
        """
        Coleta uma rocha e a adiciona ao depósito, se atender aos critérios de tamanho.

        Args:
            rocha (Rocha): A rocha a ser coletada.
        """
        if rocha.peso <= 2.5 and rocha.diametro <= 0.74:
            self.peso += rocha.peso
            self.deposito_rocha.append(rocha)

    def coletar_lixo(self, lixo):
        """
        Coleta lixo espacial e o adiciona ao depósito, se atender aos critérios de tamanho.

        Args:
            lixo (LixoEspacial): O lixo espacial a ser coletado.
        """
        if lixo.peso <= 2.5 and lixo.diametro <= 0.3:
            if not self.deposito_lixo or self.deposito_lixo[-1].tipo != lixo.tipo:
                self.peso += lixo.peso
                self.deposito_lixo.append(lixo)

    def coleta_materiais(self):
        """
        Realiza a coleta de materiais durante a exploração.
        """
        for i in range(len(self.exploracao_rocha)):
            if self.peso < 70.0:
                self.coletar_rocha(self.exploracao_rocha[i])
                self.coletar_lixo(self.exploracao_lixo[i])
            else:
                self.organizar_rochas()
        self.organizar_rochas()

    def organizar_rochas(self):
        """
        Organiza as rochas no depósito, equilibrando os tipos e mantendo o peso dentro dos limites.
        """
        tipo1 = sum(1 for rocha in self.deposito_rocha if rocha.tipo == 1)
        tipo2 = sum(1 for rocha in self.deposito_rocha if rocha.tipo == 2)
        tipo3 = sum(1 for rocha in self.deposito_rocha if rocha.tipo == 3)

        while tipo1 != tipo2 or tipo2 != tipo3:
            if tipo1 > tipo2:
                for i, rocha in enumerate(self.deposito_rocha):
                    if rocha.tipo == 1:
                        tipo1 -= 1
                        self.peso -= rocha.peso
                        self.deposito_rocha.pop(i)
                        break
            elif tipo2 > tipo3:
                for i, rocha in enumerate(self.deposito_rocha):
                    if rocha.tipo == 2:
                        tipo2 -= 1
                        self.peso -= rocha.peso
                        self.deposito_rocha.pop(i)
                        break
            elif tipo3 > tipo1:
                for i, rocha in enumerate(self.deposito_rocha):
                    if rocha.tipo == 3:
                        tipo3 -= 1
                        self.peso -= rocha.peso
                        self.deposito_rocha.pop(i)
                        break

        while self.peso > 70:
            if self.deposito_rocha:
                self.peso -= self.deposito_rocha[-1].peso
                self.deposito_rocha.pop()
            elif self.deposito_lixo:
                self.peso -= self.deposito_lixo[-1].peso
                self.deposito_lixo.pop()