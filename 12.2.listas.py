#Listas que armazenam listas

galera = [['Anderson', 24] , ['Vivian', 25] , ['Geórgia', 57] , ['Giovanna' , 24]]

#Nesse caso estamos pedindo pro prog imprimir o nome das listas internas em galera
for pessoa in galera:
    print(pessoa[0])

#Nesse caso estamos pedindo pro prog imprimir as idades das listas internas em galera
for pessoa in galera:
    print(pessoa[1])

#Varredura na lista e imprimeira
for pessoa in galera:
    print('{} tem {} anos de idade!'.format(pessoa[0], pessoa[1]))


grupo = []
dado = []

for c in range(0,3):
    nome = input('Digite seu nome: ')
    dado.append(nome)
    idade = input('Digite sua idade: ')
    dado.append(idade)
    grupo.append(dado[:]) #Fazendo uma cópia da lista dado pra lista grupo --> sem ter que correlacionar as listas 
    dado.clear()

print(grupo)


# Vamos para o caso de termos uma lista inserida na outra
# E queremos imprimir o nome das pessoas com mais de 20 anos: 
grupo = []
dados = []

for i in range(0,3):
    nome = input('Digite seu nome: ')
    dados.append(nome)
    idade = int(input('Digite sua idade: '))
    dados.append(idade)
    grupo.append(dados[:])
    dados.clear()

for i in grupo:
    if(i[1] > 20):
        print('{} tem mais de 20 anos!'.format(i[0]))
    elif(i[1] == 20):
        print('{} tem 20 anos!'.format(i[0]))
    else: #i[1] < 20
        print('{} tem menos de 20 anos!'.format(i[0]))