'''
Importamos uma função do python que gera números aleatórios
'''
from random import randint, uniform

'''
Criamos uma classe para representar as rochas que são recolhidas pelo Curiosity.
Ela possui como atributos: peso, diametro e tipo
'''
class Rocha:

    def __init__(self):
        self.peso = round(uniform(0.5, 14.2),2) # tivemos que definir aleatoriamento o peso das rochas no intervalo de
        # 0.5 até 14.2, e ainda arrendondamos o peso para duas casas decimais.
        self.diametro = round(uniform(0.3, 0.8),2) # tivemos que definir aleatoriamento o diametro das rochas no intervalo de
        # 0.3 até 2.0, e ainda arrendondamos o diametro para duas casas decimais.
        self.tipo = randint(1, 3) # e o tipo é escolhido aleatoriamente também no intervalo de 1 até 3. 

    def __repr__(self): # serve para representar um objeto como uma string
        return "Tipo " + str(self.tipo) # representando o objeto tipo como uma string

'''
Criamos uma classe para representar a Lixo espacial que é recoliho pelo Curiosity.
Ela possui como atributos: peso, diametro e tipo
'''
class LixoEspacial:

    def __init__(self):
        self.peso = round(uniform(1.12, 8.55), 2) # tivemos que definir aleatoriamento o peso dos lixos no intervalo de
        # 1.12 até 8.55, e ainda arrendondamos o peso para duas casas decimais.
        self.diametro = round(uniform(0.1, 0.4), 2) # tivemos que definir aleatoriamento o diametro dos lixos no intervalo de
        # 0.1 até 0.4, e ainda arrendondamos o diametro para duas casas decimais.
        self.tipo = randint(0, 1) # e o tipo do lixo é escolhido aleatoriamente também no intervalo de 0 até 1. 

    def __repr__(self): # serve para representar um objeto como uma string
        tipo = "Não metálico" # se o tipo escolhido aleatoriamente for igual a 2 ou 3 ele é do tipo Não metálico. Com o repr 
            # conseguimos transformar o número do tipo em string para o usuário.
        if self.tipo == 1: # se o tipo escolhido aleatoriamente for igual a 1 ele é do tipo Metálico. Com o repr 
            # conseguimos transformar o número do tipo em string para o usuário.
            tipo = "Metálico"

        return "Tipo " + tipo # retorna o tipo
'''
Criamos uma classe para representar o robo Curiosity.
Ela possui como atributos: quatro listas vazias deposito_rocha e exploracao_rocha usadas para armazenar e coletar as rochas que serão
recolhidas durantes as três expediões do Curiosity que vamos simular.
Outras duas listas vazias que serão utilizadas deposito_lixo e exploracao_lixo usadas para armazenar e coletar os lixos que serão
recolhidas durantes as três expediões do Curiosity que vamos simular.
E ainda tem o atributo peso que representa a soma total dos pesos dos lixos e rochas que o Curiosity recolheu durante suas três expedções
Tem os métodos: Iniciar exploração, Coleta Materiais, Coletar Rocha, Coletar Lixo e Organizar Rochas
'''
class Curiosity:

    def __init__(self):
        self.deposito_rocha = [] 
        self.exploracao_rocha = []
        self.deposito_lixo = [] 
        self.exploracao_lixo = []
        self.peso = 0
        
    '''
    Função que coleta os lixos e as rochas do Curiosity durante as suas três exepedições
    '''
    def iniciar_exploracao(self):
        x = 0
        while x < 3:
            self.deposito_rocha = [] # lista agora vazia, mas logo abaixo será utilizada para armazenar as rochas
            self.deposito_lixo = [] # lista agora vazia, mas logo abaixo será utilizada para armazenar os lixos
            self.peso = 0 # variável criada para ser incrementada com a soma do peso do lixo e das rochas coletadas pelo Curiosity
            # Para cada i no intervalo aleatório de 30 até 120 ele vai armazenar as rochas e lixos coletados pelos robos
            for i in range(randint(30, 120)):
                self.exploracao_rocha.append(Rocha()) # armazena as rochas coletadas pelo Curiosity
                self.exploracao_lixo.append(LixoEspacial()) # armazena os lixos coletados pelo Curiosity
            self.coleta_materiais() # chamamos a função Coleta Materias que permite que o Curiosity armazene rochas e lixos até não comprometer
            # sua capacidade limite que é de 70 quilogramas.

            tipo1 = 0 # rocha do tipo 1
            tipo2 = 0 # rocha do tipo 2
            tipo3 = 0 # rocha do tipo 3

            #Percorremos a lista depósito rocha lendo quantos valores ela possui
            # para cada i dentro do tamanho da lista fazemos a contagem da quantidade de cada tipo de rocha
            for i in range(len(self.deposito_rocha)):
                if self.deposito_rocha[i].tipo == 1:
                    tipo1 += 1  # incrementa a quantidade de cada rocha do tipo 1
                elif self.deposito_rocha[i].tipo == 2:
                    tipo2 += 1 # incrementa a quantidade de cada rocha do tipo 2
                else:
                    tipo3 += 1 # incrementa a quantidade de cada rocha do tipo 3

            m = 0
            n = 0
            #Percorremos a lista depósito lixo lendo quantos valores ela possui
            # para cada i dentro do tamanho da lista fazemos a contagem da quantidade de cada tipo de lixo
            for i in range(len(self.deposito_lixo)):
                if self.deposito_lixo[i].tipo == 1:
                    m += 1 # incrementa a quantidade de cada lixo do tipo Metálico
                else:
                    n += 1 # incrementa a quantidade de cada lixo do tipo Não Metálico

            print("\nExploração nº: " + str(x + 1) + " finalizada") # mostrar a primeira, depois a segunda e a terceira
            # expedição do Curiosity
            print("Quantidade de rochas do tipo 1: " + str(tipo1) + "\n" + # mostra a contagem de rocha do tipo 1 que
            # o Curiosity está armazenando
            "Quantidade de rochas do tipo 2: " + str(tipo2) + '\n' + # mostra a contagem de rocha do tipo 2 que
            # o Curiosity está armazenando
            "Quantidade de rochas do tipo 3: " + str(tipo3) + '\n' + # mostra a contagem de rocha do tipo 3 que
            # o Curiosity está armazenando
            "\nQuantidade de lixo Metálico: " + str(m) + '\n' + # mostra a contagem de lixo do tipo Metálico que
            # o Curiosity está armazenando
            "Quantidade de lixo Não Metálico: "  + str(n) + '\n' + # mostra a contagem de lixo do tipo Não Metálico que
            # o Curiosity está armazenando
            "\npeso: " + str(self.peso))  # mostra o peso total que o Curiosity está armazenando
            print("\nCuriosity terminou exploração. Liberando espaço de armazenamento.") # a cada término da exploração do
            # Curiosity mostra "Curiosity terminou exploração. Liberando espaço de armazenamento"
            x += 1 # aqui vai incrementar três vezes

    '''
    O Curiosity salva rochas de ate 2,5kg de peso e de até 0,74m de diâmetro. Rochas maiores
    a esse peso e diametro, são desconsideradas pelo Curiosity. As rochas podem ser dos tipos 1, 2 e 3.
    Quando capacidade de armazenamento do Curiosity fica comprometida ele avalia a quantidade de rochas
    em função do seu tipo e elimina as rochas necessárias até ter uma quantidade mais ou menos equilibrada
    de tipos de rochas.
    '''
    def coletar_rocha(self, rocha:Rocha):
        if rocha.peso <= 2.5 and rocha.diametro <= 0.74: # avalia se a rocha está no peso e diametro que ele
            #pode armazenar
            self.peso += rocha.peso # incrementa o peso das rochas coletadas
            self.deposito_rocha.append(rocha) # armazena as rochas coletadas

    '''
    O Curiosity salva lixo espacial de até 2,5kg de peso e de até 0,3m de diâmetro.
    Lixo espacial que ultrapasse esse peso e dimensão são desconsiderados pelo Curiosity. 
    Lixo espacial pode ser de tipo metálico e não metálico. 
    O Curiosity equilibra sua pilha de lixo espacial seguindo a seguinte política:
    Antes de armazenar o tipo de lixo
    ele avalia qual tipo de lixo está no topo da pilha
    Se no topo houver lixo do tipo metálico o novo elemento a
    ser empilhado precisa ser do tipo não metálico.
    Se for do Não Metálico, o próximo elemento a ser empilhado precisa ser do tipo Metálico.
    Caso essa condição não possa ser cumprida o robô ira desempilhar os lixos até no seu topo
    ter o tipo de lixo Metálico.
    '''
    def coletar_lixo(self, lixo: LixoEspacial):
        # Verifica se existe pelo menos um lixo na pilha
        if len(self.deposito_lixo) > 0:
            # Recebe o tipo do último lixo
            ultimo_tipo = self.deposito_lixo[-1].tipo
        # Caso não tenha 1 ou mais na pilha
        else:
            # "Seta" a variavel para um valor fora do range de tipos
            ultimo_tipo = 3
        # Verifica o peso e diametro do lixo
        if lixo.peso <= 2.5 and lixo.diametro <= 0.3:
            # Adiciona o lixo se o ultimo tipo não for igual 
            if lixo.tipo != ultimo_tipo:
                self.peso += lixo.peso
                self.deposito_lixo.append(lixo)
            # Remove o lixo anterior e adiciona o novo se o tipo for igual
            else:
                self.peso -= self.deposito_lixo[-1].peso
                self.deposito_lixo.pop()
                self.peso += lixo.peso
                self.deposito_lixo.append(lixo)
    '''
    O Curiosity consegue armazenar até 70kg (somando rochas e lixo) durante sua missão de exploração.
    '''
    def coleta_materiais(self):
        # Percorre o campo de exploração
        for i in range(len(self.exploracao_rocha)):
            # Verifica se o peso é maior que 70 
            if self.peso < 70.0:
                # Coleta as pedras
                self.coletar_rocha(self.exploracao_rocha[i])
                # Coleta os lixos
                self.coletar_lixo(self.exploracao_lixo[i])
            else:
                # Organiza o espaço caso o peso seja maior que 70
                self.organizar_rochas()
        # Ao final organiza o espaço
        self.organizar_rochas()

    '''
    Quando a capacidade de armazenamento se vê comprometida ele
    avalia se o equilíbrio de tipos de rochas na sua lista de rochas é o adequado para ele armazenar.
    Se a lista de rochas não estiver equilibrada,ele elimina rochas.
    Quando a lista estiver equilibrada e não seja possível inserir mais nenhum elemento do tipo rocha
    ou lixo que esteja em avaliação.
    O Curiosity desconsidera esse elemento e continua a exploração de um novo elemento.
    Esse processo é repetido até terminar de explorar uma determinada região de Marte.
    '''
    def organizar_rochas(self):
        tipo1 = 0
        tipo2 = 0
        tipo3 = 0
        tipo_do_menor = 0

        # Separa as pedras por tipos
        for i in range(len(self.deposito_rocha)):
            if self.deposito_rocha[i].tipo == 1:
                tipo1 += 1
            elif self.deposito_rocha[i].tipo == 2:
                tipo2 += 1
            else:
                tipo3 += 1


        menor = 0
        # Conta a quantidade de pedras por tipo
        if tipo1 < tipo2 and tipo1 < tipo3:
            menor = tipo1
            tipo_do_menor = 1
        if tipo2 < tipo1 and tipo2 < tipo3:
            menor = tipo2
            tipo_do_menor = 2
        if tipo3 < tipo1 and tipo3 < tipo2:
            menor = tipo3
            tipo_do_menor = 3

        x = 0
        # Realiza o loop enquanto os valores forem diferentes
        while tipo1 != tipo2 and tipo2 != tipo3 :
            # Verifica se o tamanho do deposito de rochas é menor que o contador 
            if len(self.deposito_rocha) > x:
                # Verifica se esta rocha não é do tipo que tem menos
                if self.deposito_rocha[x].tipo != tipo_do_menor:
                    # Remove a rocha caso seja do(s) tipo(s) que possuem quantidades excedentes
                    if self.deposito_rocha[x].tipo == 1:
                        tipo1 -= 1
                        self.peso -= self.deposito_rocha[x].peso
                    elif self.deposito_rocha[x].tipo == 2:
                        tipo2 -= 1
                        self.peso -= self.deposito_rocha[x].peso
                    else:
                        tipo3 -= 1
                        self.peso -= self.deposito_rocha[x].peso
                    self.deposito_rocha.pop(x)
                else:
                    # Caso seja do tipo que tem menos passa para o próximo elemento
                    x += 1
            # Caso o contador seja maior para o loop
            else:
                break

        # Remoção de itens adicionais caso ultrapasse o valor
        while self.peso > 70:
            if len(self.deposito_rocha) >= 1:
                self.peso -= self.deposito_rocha[-1].peso
                self.deposito_rocha.pop()
            else:
                self.peso -= self.deposito_lixo[-1].peso
                self.deposito_lixo.pop()

Curiosity().iniciar_exploracao()
