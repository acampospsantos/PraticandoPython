#Listas: Representa uma sequência de valores (pode aumentar e diminuir valores a depender da necessidade) --> podemos armazenar vários elementos dentro de uma única estrutura

# Sintaxe: nome_lista = [valores]

notas = [5, 7, 8, 6, 9]
print(notas)

n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 4]

valores = n1 + n2 #Criei uma variável e concatenou as duas listas(n1 e n2) em uma única lista
print(type(valores)) #É possível ver que a variável valores é do tipo Lista 
print(valores)

variavel = valores[6] #Podemos acessar os elementos da lista a partir do índice --> nesse caso estamos resgatando o elemento de indice 1 da lista valores
print(valores) 

print(len(valores)) #Imprime o tamanho da lista(len = length)

print(sorted(valores)) #A função sorted ordena os elementos da lista

print(sorted(valores, reverse=True)) #A função sorted ordena os elementos da lista, o parâmetro reverse faz a ordenação ser invertida

print(sum(valores)) #A função soma os elementos da lista

print(min(valores)) #A função min capta o menor elemento da lista

print(max(valores)) #A função max capta o maior elemento da lista


valores.append(13) #O append acrescenta um valor(do parâmetro) ao fim da lista

valores.pop() #O pop retira por padrão o último elemento da lista

valores.pop(3) #Nesse caso o pop retira o elemento de índice 3

valores.insert(3,21) #A função insert recebe dois parâmetros(posição e valor do elemento) - após isso, a função faz a inserção

print(12 in valores) #O 'in' nesse caso faz a procura do elemento na lista

planetas = ['Mercúrio', 'Vênus', 'Marte', 'Saturno', 'Urano', 'Netuno'] #Iteração da lista
for planeta in planetas:
    print(planeta)