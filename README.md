# mars-curiosity-rover

![image](https://github.com/alexandre-queiroz/mars-curiosity-rover/assets/54822170/b279a4ab-06d8-419f-8651-70209905c324)

## Detalhes da missão
## 1. Introdução
A missão do robô Rover Curiosity em Marte começou em 6 de agosto de 2012, quando chegou à cratera Gale. Desde essa data, o robô começou a explorar o território de Marte.

## 2. Características do Curiosity
O Curiosity possui apenas um braço e uma câmera para conduzir a exploração. Ele é capaz de atingir uma velocidade de até 90 m/h, tem uma massa de 899 kg, uma altura de 2,2 m, uma largura de 2,7 m e um comprimento de 3 m. Seu braço pode se estender até 3 m. Além da câmera, o Curiosity também está equipado com uma bateria solar.

## 3. Coleta de Elementos
O Curiosity coleta elementos que encontra no solo de Marte, avalia-os com sua câmera e os armazena em até dois depósitos diferentes. Se o que ele encontra for uma rocha, ela é registrada em um depósito no formato de lista. Se o que for encontrado forem partes de lixo deixado por explorações passadas, esse lixo é armazenado em outro depósito no formato de pilha.

## 4. Políticas de Armazenamento
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

## 10. Acompanhamento da Exploração
Nesta seção, descrevemos como o progresso da exploração será acompanhado por meio de mensagens durante o processo.

## 11. Finalização da Exploração
Nesta seção, detalhamos o que acontecerá quando o Curiosity atingir sua capacidade máxima de armazenamento ou quando não houver mais elementos para coletar.

## 12. Instruções de Uso
Nesta seção, fornecemos instruções básicas de uso do código e como executar a simulação.

## 13. Exemplos de Execução
Nesta seção, apresentamos exemplos de execução do código para demonstrar como a simulação funciona na prática.

## 14. Conclusão
Encerramos o README com uma conclusão geral e informações adicionais, se necessário.
