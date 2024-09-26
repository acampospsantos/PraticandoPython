#Exercício proposto

#Crie um script que peça para o usuário digitar o nome de 5 bebidas favoritas dele, armazenando esses valores em uma lista.

#Na sequência, exiba em tela os elementos da lista em ordem alfabética, um por linha, usando um laço de repetição for.


#RESOLUÇÃO DA QUESTÃO PROPOSTA

lista_bebidas = [] #Criei uma lista para armazenar as bebidas favoritas do usuário

for i in range(0, 5):
    bebida = input("Digite o nome de suas bebidas favorita: ")
    lista_bebidas.append(bebida)
    #lista_bebidas.insert(i,bebida) #Outra forma de fazer a inserção dos elementos na lista - a partir do índice i

#sorted(lista_bebidas)
lista_bebidas.sort() #Ordenação dos elementos da lista

print('\nRanking de bebidas: ')
for bebidas in lista_bebidas: #Iteração da lista utilizando for
    print('-', bebidas)

print('\nAgradeço!')