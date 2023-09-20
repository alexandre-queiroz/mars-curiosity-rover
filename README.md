# Mars Science Laboratory: Mars Curiosity Rover

![image](https://github.com/alexandre-queiroz/mars-curiosity-rover/assets/54822170/b279a4ab-06d8-419f-8651-70209905c324)

*É importante observar que as funcionalidades descritas neste documento foram criadas apenas para fins acadêmicos e de simulação. Elas não refletem o funcionamento exato do Rover Curiosity da NASA, que é uma missão real em Marte. Para obter informações precisas e atualizadas sobre o Rover Curiosity e suas atividades em Marte, visite o site oficial da NASA em [https://mars.nasa.gov/msl/home](https://mars.nasa.gov/msl/home/).*

**Agradeço por explorar esta simulação do Curiosity e por seu interesse na exploração espacial!**

## Detalhes da missão
## 1. Introdução
A missão do robô Rover Curiosity em Marte começou em 6 de agosto de 2012, quando chegou à cratera Gale. Desde essa data, o robô começou a explorar o território de Marte.

## 2. Características do Curiosity
O Curiosity possui apenas um braço e uma câmera para conduzir a exploração. Ele é capaz de atingir uma velocidade de até 90 m/h, tem uma massa de 899 kg, uma altura de 2,2 m, uma largura de 2,7 m e um comprimento de 3 m. Seu braço pode se estender até 3 m. Além da câmera, o Curiosity também está equipado com uma bateria solar.

## 3. Coleta de Elementos
O Curiosity coleta elementos que encontra no solo de Marte, avalia-os com sua câmera e os armazena em até dois depósitos diferentes. Se o que ele encontra for uma rocha, ela é registrada em um depósito no formato de lista. Se o que for encontrado forem partes de lixo deixado por explorações passadas, esse lixo é armazenado em outro depósito no formato de pilha.

## 4. Políticas de Armazenamento de Rochas
O Curiosity armazena rochas de até 2,5 kg de peso e até 0,74 m de diâmetro. Rochas maiores do que esse peso e dimensão são descartadas. As rochas podem ser classificadas em tipos 1, 2 e 3. Quando a capacidade de armazenamento do Curiosity fica comprometida, o robô avalia a quantidade de rochas em função de seu tipo e elimina as rochas necessárias até alcançar um equilíbrio entre os tipos de rochas.

## 5. Políticas de Armazenamento de Lixo Espacial
Ao mesmo tempo, o robô armazena lixo espacial de até 2,5 kg de peso e até 0,3 m de diâmetro. Lixo espacial que ultrapassa esse peso e dimensão é desconsiderado. O lixo espacial pode ser de tipo metálico ou não metálico. O robô equilibra sua pilha de lixo espacial de modo que, antes de armazenar um determinado tipo de lixo, avalia qual tipo de lixo está no topo da pilha. Se no topo houver lixo metálico, então o novo elemento a ser empilhado deve ser do tipo não metálico, e vice-versa. Caso essa condição não possa ser cumprida, o robô desempilhará até ter, no topo da sua pilha, o tipo de lixo adequado para salvar o novo lixo que pretende armazenar.

## 6. Capacidade de Armazenamento
O Curiosity é capaz de armazenar até 70 kg (somando rochas e lixo) durante uma missão de exploração. Quando a capacidade de armazenamento se vê comprometida, o robô avalia se o equilíbrio de tipos de rochas em sua lista de rochas é o adequado. Se a lista não estiver equilibrada, então ele elimina rochas conforme a política descrita acima. Caso a lista esteja equilibrada e não seja possível inserir mais nenhum elemento (rocha ou lixo) que esteja em avaliação, o robô desconsidera esse elemento e continua a exploração de um novo elemento. Esse processo é repetido até terminar de explorar uma determinada região de Marte.

## 7. Retorno à Estação Espacial
Após o término de uma exploração, o robô precisa retornar a uma estação espacial para liberar os elementos armazenados e iniciar uma nova exploração.

## 8. Implementação em Python
Para simular a exploração do Curiosity em Marte, é necessário construir um sistema em Python que utilize Tipos Abstratos de Dados (TADs). Os TADs a serem implementados são Rocha, Lixo Espacial e Curiosity.

## 9. Simulação da Exploração
Nesta seção, descrevemos como a simulação será realizada, incluindo a criação de listas de rochas e lixo espacial com valores aleatórios.
 ```
from random import randint, uniform

class Rocha:

    def __init__(self):
        self.peso = round(uniform(0.5, 14.2), 2)
        self.diametro = round(uniform(0.3, 0.8), 2)
        self.tipo = randint(1, 3)

    def __repr__(self):
        return "Tipo " + str(self.tipo)

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

class Curiosity:

    def __init__(self):
        self.deposito_rocha = []
        self.exploracao_rocha = []
        self.deposito_lixo = []
        self.exploracao_lixo = []
        self.peso = 0

    def iniciar_exploracao(self):
        x = 0
        while x < 3:
            self.deposito_rocha = []
            self.deposito_lixo = []
            self.peso = 0
            for i in range(randint(30, 120)):
                self.exploracao_rocha.append(Rocha())
                self.exploracao_lixo.append(LixoEspacial())
            self.coleta_materiais()

            tipo1 = 0
            tipo2 = 0
            tipo3 = 0

            for i in range(len(self.deposito_rocha)):
                if self.deposito_rocha[i].tipo == 1:
                    tipo1 += 1
                elif self.deposito_rocha[i].tipo == 2:
                    tipo2 += 1
                else:
                    tipo3 += 1

            m = 0
            n = 0

            for i in range(len(self.deposito_lixo)):
                if self.deposito_lixo[i].tipo == 1:
                    m += 1
                else:
                    n += 1

            print("\nExploração nº: " + str(x + 1) + " finalizada")
            print("Quantidade de rochas do tipo 1: " + str(tipo1) + "\n" +
            "Quantidade de rochas do tipo 2: " + str(tipo2) + '\n' +
            "Quantidade de rochas do tipo 3: " + str(tipo3) + '\n' +
            "\nQuantidade de lixo Metálico: " + str(m) + '\n' +
            "Quantidade de lixo Não Metálico: "  + str(n) + '\n' +
            "\nPeso: " + str(self.peso))
            print("\nCuriosity terminou exploração. Liberando espaço de armazenamento.")
            x += 1

 ```

## 10. Instruções de Uso
Nesta seção, fornecemos instruções básicas de uso do código e como executar a simulação.
 ```
# Exemplo de como usar o código para simular a exploração do Curiosity
curiosity = Curiosity()
curiosity.iniciar_exploracao()
 ```

## 11. Exemplos de Execução
Nesta seção, apresentamos exemplos de execução do código para demonstrar como a simulação funciona na prática.
 ```
# Exemplo de saída da simulação

Exploração nº: 1 finalizada
Quantidade de rochas do tipo 1: 1
Quantidade de rochas do tipo 2: 2
Quantidade de rochas do tipo 3: 2

Quantidade de lixo Metálico: 4
Quantidade de lixo Não Metálico: 3

peso: 21.53

Curiosity terminou exploração. Liberando espaço de armazenamento.

Exploração nº: 2 finalizada
Quantidade de rochas do tipo 1: 4
Quantidade de rochas do tipo 2: 4
Quantidade de rochas do tipo 3: 3

Quantidade de lixo Metálico: 7
Quantidade de lixo Não Metálico: 6

peso: 39.65

Curiosity terminou exploração. Liberando espaço de armazenamento.

Exploração nº: 3 finalizada
Quantidade de rochas do tipo 1: 9
Quantidade de rochas do tipo 2: 6
Quantidade de rochas do tipo 3: 6

Quantidade de lixo Metálico: 10
Quantidade de lixo Não Metálico: 9

peso: 61.30


Curiosity terminou exploração. Liberando espaço de armazenamento.
 ```
