# mars-curiosity-rover

## Detalhes da missão
A missão do robô Rover Curiosity chegou à cratera Gale de
Marte o 6 de agosto de 2012. Desde essa data, o robô começou
a explorar o território de Marte. O robô tem, apenas, um braço
e uma câmera para fazer a exploração. O Curiosity chega a
correr a uma velocidade de até 90 m/h, tem uma massa de 899
kg, uma altura de 2,2m, uma largura de 2,7m e um
cumprimento de 3m. Seu braço se estica até 3m. Além da
câmera, conta também com uma bateria solar.
O Curiosity pega elementos que encontra no solo de Marte,
os avalia com sua câmera e os salva em até 2 depósitos
diferentes. Se o que ele encontra é avaliado como uma rocha,
então tal rocha é salva num depósito em formato de lista. Se
o que for encontrado trata-se de partes de lixo deixado por explorações passadas, então
esse lixo é salvo num outro depósito em formato de pilha.
O Curiosity salva rochas de ate 2,5kg de peso e de até 0,74m de diâmetro. Rochas maiores
a esse peso e dimensão, são desconsideradas. Rochas podem ser dos tipos 1, 2 e 3. Se a
capacidade de armazenamento do Curiosity fica comprometida, o robô avalia a
quantidade de rochas em função do seu tipo e, rejeita (elimina) as rochas necessárias até
ter uma quantidade mais ou menos equilibrada de tipos de rochas.
Ao mesmo tempo, o robô salva lixo espacial de até 2,5kg de peso e de até 0,3m de
diâmetro. Lixo espacial que ultrapasse esse peso e dimensão, é desconsiderado. Lixo
espacial pode ser de tipo metálico e não metálico. O robô equilibra sua pilha de lixo
espacial de maneira que, antes de armazenar um determinado tipo de lixo, avalia qual tipo
de lixo está no topo da pilha. Se no topo houver lixo metálico, então o novo elemento a
ser empilhado deve ser do tipo não metálico, e vice versa. Caso essa condição não possa
ser cumprida, o robô ira desempilhar até ter, no topo da sua pilha, o tipo de lixo adequado
para salvar o novo lixo que pretende salvar.
O Curiosity, consegue armazenar até 70kg (somando rochas e lixo) durante uma missão
de exploração. Quando a capacidade de armazenamento se vê comprometida, o robô
avalia se o equilíbrio de tipos de rochas na sua lista de rochas é o adequado. Se a lista não
estiver equilibrada, então elimina rochas conforme a política descrita acima. Caso a lista
estiver equilibrada e não seja possível inserir mais nenhum elemento (rocha ou lixo) que
esteja em avaliação, o robô desconsidera esse elemento e continua a exploração de um
novo elemento. Esse processo é repetido até terminar de explorar uma determinada região
de Marte.
Após o término de uma exploração, o robô precisa voltar até uma estação espacial para
liberar os elementos armazenada e iniciar com uma nova exploração.

Requerer-se que você construa um sistema em Python que, usando TADs, simule a
exploração do Curiosity em Marte. Assim, construa um TAD Rocha, um TAD
LixoEspacial, e um TAD Curiosity. Para sua simulação, crie uma lista de tamanho 30 ≤
N ≤ 120 para o TAD Rocha e uma segunda lista para o TAD LixoEspacial, também de
tamanho N. O valor de N é gerado aleatoriamente. Preencha os atributos de cada elemento
dessas duas listas com valores aleatórios. Considere que as rochas em Marte têm pesos
que vão desde 0,5kg até 14,2kg; enquanto há registros de que o lixo espacial em Marte
deve pesar entre 1,12kg e 8,55Kg.
Com essas duas listas criadas, você irá percorrê-las ao mesmo tempo e irá inserir no
Curiosity, uma rocha e um lixo por vez, seguindo as políticas descritas acima. Considere
que ambas listas correspondem ao total de elementos a serem explorados pelo robô, isto
é, percorrer ambas listas corresponde a uma exploração realizada pelo Curiosity.
Mostre mensagens que permitam fazer seguimento do passo a passo das ações do
Curiosity. Quando o armazenamento do Curiosity estiver totalmente preenchido, ou
simplesmente não houver mais rochas ou lixos a serem armazenados. Você deverá
mostrar na tela o reporte completo da lista e pilha do Curiosity e a mensagem dizendo
“Curiosity terminou exploração. Liberando espaço de armazenamento”.
Fazer a simulação para três (3) explorações do Curiosity.
