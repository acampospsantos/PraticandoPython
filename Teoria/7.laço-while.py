#Estrutura de Repetição/Laço - While

num = 1

while (num <= 10):
    print(num)
    num = num + 1



#1º Forma
nome = None #Convenção pra dizer que a variável é vazia
nome = input('Digite seu nome: ')
while (nome != 'x' or nome != 'X'):
    nome = input('Digite seu nome: ')

print('# Programa encerrado! #')


#2º Forma 
while true:
    nome = input('Digite seu nome: ')
    if(nome == 'x' or nome == 'X'):
        break

print('# Programa encerrado! #')