import random

valor = random.randint(1,20)
print(valor)


print('Gerar cinco números inteiros aleatórios entre 1 e 50: \n')
for i in range(5):
    n = random.randint(1,50)
    print('Número gerado: ', n)


#Gera números float aleatórios (não aceita parâmetros) -
valor = random.random()
print('Número gerado: ', valor*10)


#O método choice pega um número da Lista L que fornecemos
L = [2, 4, 6, 9, 10, 13, 17, 18, 20, 21, 25, 29]
n = random.choice(L)
print('Número escolhido: ', n)

# O método sample pega a lista L e seleciona três números aleatórios dela
n = random.sample(L,3)
print('Números escolhidos: ', n)

#Embaralhar
print ('Exibir a lista original: ', L)
print ('Embaralhar a lista e exibi-la: ')
n = random.shuffle(L) #Recebe a lista como parâmetro e embaralha a lista