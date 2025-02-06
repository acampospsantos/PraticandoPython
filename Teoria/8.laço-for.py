#Estrutura de Repetição/Laço - for

lista = [2,6,9,4,0,12,3,7]

#for item in lista: #Podemos entender como: para cada item dentro da lista faço algo com esse item
#    print(item)


#Outro exemplo
#palavra = 'Anderson'
#for letra in palavra:
#    print (letra)


#Outro exemplo
nome = input('Digite seu nome: ')
for x in range(10):
    print(x+1, ' - ', nome)


#range é uma função do python que pode receber até três valores
#range(valor_inical, valor_final, incremento)
for x in range(2, 20): #O último valor (nesse caso 20) não entra na contagem, ou seja, esse range vai de 2 até 19
    print(x)


#Outro exemplo: (recebo uma lista com nome de rochas, mas não quero que o 'quartzo' seja impresso)
pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')
for pedra in pedras:
    if (pedra == 'Quartzo'):
        continue #Instrução que encerra a interação atual do laço, ou seja,  a instrução seguinte do laço não será executada
    print (pedra)