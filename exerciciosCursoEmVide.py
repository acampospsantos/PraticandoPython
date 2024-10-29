#LISTA DE EXERCÍCIOS PYTHON - CURSO EM VÍDEO
#(MUNDO1 - FUNDAMENTOS)

#Enunciado 1
# Crie um programa que imprime "Olá mundo" na tela
print('Hello World!')


#Enunciado 2
# Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas vindas 
nome = input("Qual é o seu nome? ")
print('Olá, ', nome, '! Prazer em te conhecer.')


#ENUNCIADO 3
# Crie um programa que leia dois números e imprime a soma entre eles
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

soma = n1 + n2

print('A soma entre', n1, 'e', n2, ' é = ', soma)
# print ('A soma entre {} e {} é = {}'.format(n1, n2, soma))

print (soma)


#Enunciado 4
# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possíveis.
variavel = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(variavel))
print('Só tem espaços? ', variavel.isspace)
print('É um número? ', variavel.isnumeric)
print('É alfabético? ', variavel.isalpha())
print('É alfanumérico? ', variavel.isalnum)
print('Está em maiusculo? ', variavel.isupper)
print('Está em minúsculo? ', variavel.islower)
print('Está capitalizada? ', variavel.istitle)


#Enunciado extra
# Faça um programa que leia o dia, o mês e o ano de nascimento de alguém e imprima numa linha de comando
dia = int(input('Digite seu dia de nascimento: '))
mes = int(input('Digite seu mês de nascimento: '))
ano = int(input('Digite seu ano de nascimento: '))

print('Data de nascimento: {}/{}/{}'.format(dia, mes, ano))


#ENUNCIADO 5
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
num = int(input('Digite um número: '))

numSucessor = num + 1
numAntecessor = num - 1

#Há duas formas de impressão:
print('Sucessor de {}: {}, Antecessor de {}: {}'.format(num, numSucessor, num, numAntecessor))

print('Sucessor de {}: {}, Antecessor de {}: {}'.format(num, num+1, num, num-1))


#ENUNCIADO 6
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
import math

num = int(input('Digite um número: '))

numDobro = num * 2

numTriplo = num * 3

numQuadrado = num ** (1/2)
#raizQuadrada = math.sqrt(num)

print('Numero lido: {} , Dobro = {} , Triplo = {} , Raiz Quadrada = {}'.format(num, numDobro, numTriplo, numQuadrado))


#ENUNCIADO 7
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média

nota1 = float(input('Digite a primeira nota do aluno: '))

nota2 = float(input('Digite a segunda nota do aluno: '))

media = (nota1 + nota2)/2

print('A média do aluno foi = {}'.format(media))


#ENUNCIADO 8
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
valorMetros = int(input('Digite um valor inteiro em metros: '))

valorCentimetros = valorMetros * 100

valorMilimetros = valorMetros * 1000

print('Valor em metros = {}m , Valor em centimetros = {}cm , Valor em milimetros = {}mm'.format(valorMetros, valorCentimetros, valorMilimetros))


#ENUNCIADO 9
# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
valor = int(input('Digite um valor: '))

i = 1

#FORMA MANUAL
print('Tabuada do {}\n'.format(valor))
print('{}. {} x 1 = {}'.format(i, valor, valor*1))
print('{}. {} x 2 = {}'.format(i+1, valor, valor*2))
print('{}. {} x 3 = {}'.format(i+2, valor, valor*3))
print('{}. {} x 4 = {}'.format(i+3, valor, valor*4))
print('{}. {} x 5 = {}'.format(i+4,valor, valor*5))
print('{}. {} x 6 = {}'.format(i+5, valor, valor*6))
print('{}. {} x 7 = {}'.format(i+6, valor, valor*7))
print('{}. {} x 8 = {}'.format(i+7, valor, valor*8))
print('{}. {} x 9 = {}'.format(i+8, valor, valor*9))
print('{}. {} x 10 = {}\n'.format(i+9, valor, valor*10))


#Utilizando for
print('Tabuada do {}\n'.format(valor))
for i in range(1,11):
    print('{}. {} x {} = {}'.format(i, valor, i, valor*i))



#ENUNCIADO 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$ 1.00 = R$3,27
carteira = float(input('Digite seu saldo na carteira: '))

dolares = carteira/3.27

print('Quantidade em dólares que se pode comprar = US${}'.format(dolares))


#Enunciado 11
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
altura = int(input('Digite a altura da parede(em m): '))

largura = int(input('Digite a largura da parede(em m): '))

area = altura * largura #m²

qtdTinta = area/2

print('Area da parede = {}m², Quantidade de tinta = {}L'.format(area, qtdTinta))
#Cada litro de tinta - 2m²

# 1L - 2m² 
# xL - area m²

# 2*x = area
# x = area / 2


# Enunciado 12
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
precoProduto = int(input('Digite o preço do produto: '))

desconto = precoProduto * (5/100) # 5%

novoPreco = precoProduto - desconto

print('Preço do produto: R${}, Preço após desconto = R${}'.format(precoProduto, novoPreco))


# Enunciado 13
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salarioInicial = int(input('Digite seu salário inicial: '))

aumento = salarioInicial * (15/100)

salarioFinal = salarioInicial + aumento

print('Salário Inicial = R${} , Salário pós aumento = R${}'.format(salarioInicial, salarioFinal))


# Enunciado 14
# Faça um conversor de temperatura: de celsius para farenheit
tempCelsius = float(input('Digite a temperatura em celsius: '))

tempFarenheit = ((9 * tempCelsius)/5) + 32

print('A temperatura de {}ºF = {}ºC'.format(tempFarenheit, tempCelsius))


# Enunciado 15
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
kmRodados = int(input('Digite a quantidade de km rodados pelo carro: '))

diasAlugado = int(input('Quantidade de dias alugado: '))

valorDiasAlugado = 60 * diasAlugado

valorKmRodado = 0.15 * kmRodados

valorTotal = valorDiasAlugado + valorKmRodado

print('Valor Total = R${}'.format(valorTotal))


# Enunciado 16
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
num = float(input('Digite um número inteiro: '))

numInteiro = math.trunc(num)
print('{} em sua versão inteira = {}'.format(num, numInteiro))


# Enunciado 17
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
import math
catetoOposto = int(input('Digite o valor do cateto oposto: '))

catetoAdjacente = int(input('Digite o valor do cateto adjacente: '))

#hipotenusa² = catetoAdjacente² + catetoOposto²

hipotenusa = math.sqrt((catetoOposto**2) + (catetoAdjacente**2))

hipotenusa2 = ((catetoOposto**2) + (catetoAdjacente**2))**(1/2)

print(hipotenusa)

print(hipotenusa2)


# Enunciado 18
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Digite o angulo da circuferencia: '))

#Calculo seno
seno = math.sin(math.radians(angulo))
print('O ângulo de {} tem o seno de {}'.format(angulo,seno))
#Calculo Cosseno
cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o cosseno de {}'.format(angulo,cosseno))
#Calculo Tangente
tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a tangente de {}'.format(angulo, tangente))


# Enunciado 19
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

#Seleção aleatória do aluno
alunoEscolhido = random.randint(1,4)

print('\n### Seleção aleatória dos alunos ### ')
if(alunoEscolhido == 1):
    print('Aluno escolhido foi: {}'.format(aluno1))
elif(alunoEscolhido == 2):
    print('Aluno escolhido foi: {}'.format(aluno2))
elif(alunoEscolhido == 3):
    print('Aluno escolhido: {}'.format(aluno3))
elif(alunoEscolhido == 4):
    print('Aluno escolhido foi: {}'.format(aluno4))

# Outra forma de solução
lista = [aluno1, aluno2, aluno3, aluno4]
escollhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escollhido))


#Enunciado 20
# O mesmo professor do exercício anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

listaAlunos = [aluno1, aluno2, aluno3, aluno4]
listaSorteada = []

print(listaAlunos, '\n')
print('Lista aleatória:')
for i in range(1,5):
    escolhido = random.choice(listaAlunos)
    listaSorteada.append(escolhido)
    listaAlunos.remove(escolhido)

print(listaSorteada)

#Outra forma de fazer:
print('A ordem de apresentação será:')
random.shuffle(listaAlunos)
 

# Enunciado 21 
# Faça um programa que abra e reproduza o aúdio de um arquivo mp3
# importar a biblioteca pygame
from pygame import mixer

# uma forma de implementar o código
mixer.init()

# substitua o nome do arquivo "musica.mp3" pelo seu arquivo mp3
mixer.music.load('audio.mp3')
mixer.music.play()
x = input('Digite algo para parar...')


# Enunciado 22
# Crie um programa que leia o nome completo de uma pessoa e mostre:
#I) - O nome com todas as letras maiúsculas
#II) - O nome com todas as letras minúsculas
#III) - Quantas letras ao todo (sem considerar espaços)
#IV) - Quantas letras tem o primeiro nome

nomeCompleto = input('Digite seu nome completo: ')

nomeMaiusculo = nomeCompleto.upper()
nomeMinusculo = nomeCompleto.lower()

listaNomes = nomeCompleto.split()
qtdPrimeiroNome = len(listaNomes[0])

qtdTotalLetras = 0
variavel = len(listaNomes)

for i in range(0, variavel):
    qtdTotalLetras = qtdTotalLetras + len(listaNomes[i])

print('Nome em maiúsculo: {}'.format(nomeMaiusculo))
print('Nome em minúsculo: {}'.format(nomeMinusculo))
print('Nome tem ao todo {} letras'.format(qtdTotalLetras))
print('Primeiro nome: {} , tem {} letras'.format(listaNomes[0], qtdPrimeiroNome))


# Enunciado 23
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = input('Digite um número: ')

separacao = len(numero)

if (separacao == 1):
    print('Unidade: {}'.format(numero))

if (separacao == 2):
    for i in range(0, separacao):
        if(i == 0):
            print('Dezena: {}'.format(numero[i]))
        elif(i == 1):
            print('Unidade: {}'.format(numero[i]))


if (separacao == 3):
    for i in range(0, separacao):
        if(i == 0):
            print('Centena: {}'.format(numero[i]))
        elif(i == 1):
            print('Dezena: {}'.format(numero[i]))
        elif(i == 2):
            print('Unidade: {}'.format(numero[i]))

if(separacao == 4):
    for i in range(0, separacao):
        if(i == 0):
            print('Milhar: {}'.format(numero[i]))
        elif(i == 1):
            print('Centena: {}'.format(numero[i]))
        elif(i == 2):
            print('Dezena: {}'.format(numero[i]))
        elif(i == 3):
            print('Unidade: {}'.format(numero[i]))


#Forma matemática
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))


# Enunciado 24
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = input('Digite o nome da sua cidade: ')

cidadeAtualizada = cidade.upper()

encontrar = cidadeAtualizada.find('SANTO')

if(encontrar != 0):
    print('Sua cidade não começa com SANTO')
elif(encontrar == 0):
    print('Sua cidade começa com SANTO')


#Enunciado 25
# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'SILVA' no nome.
nome = input('Digite seu nome: ')

nome = nome.upper()

encontrar = nome.find('SILVA')

if (encontrar == -1):
    print('{} não tem Silva!'.format(nome))
else:
    print('{} tem Silva!'.format(nome))


# Enunciado 26
# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A"
# - Em que posição ela aparece a primeira vez
# - Em que posição ela aparece a última vez
frase = input('Digite uma frase: ')

frase = frase.upper()

QtdA = frase.count('A')

encontrar = frase.find('A')


print('A letra ''A'' aparece: {} vezes'.format(QtdA))
print('A letra ''A'' aparece pela primeira vez na posição: '.format(encontrar))
print('A letra ''A'' aparece pela última vez na posição: '.format(frase.rfind('A')+1))


# Enunciado 27
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = input('Digite seu nome completo: ')

nomeSplit = nome.split()

nomeTamanho = len(nomeSplit)

primeiroNome = nomeSplit[0]

UltimoNome = nomeSplit[nomeTamanho-1]

print('Nome completo: {}'.format(nome))

print('Primeiro: {}'.format(primeiroNome))

print('Último: {}'.format(UltimoNome))


# Enunciado 28
# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time
numeroAleatorio = random.randint(0, 5) #Computador vai escolher um número entre 0 e 5

print('----- Tente adivinhar o número escolhido pelo computador! -----')
numeroUsuario = int(input('Digite um número entre 0 e 5: '))
print('\nProcessando....\n')
time.sleep(2)
print('\nNúmero escolhido: {} x {} :Número aleatório'.format(numeroUsuario, numeroAleatorio))

if(numeroUsuario == numeroAleatorio):
    print('--- Usuário venceu! ---')
else:
    print('--- Usuário perdeu! ---')


# Enunciado 29
# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.
velocidadeCarro = int(input('Digite a velocidade do carro: '))
velocidadePermitida = 80

print('\nVelocidade permitida: {}km/h x {}km/h :Velocidade do veículo'.format(velocidadePermitida, velocidadeCarro))

if(velocidadeCarro > 80):
    velocidadeExcedente = velocidadeCarro - velocidadePermitida
    multa = velocidadeExcedente * 7.00
    print('Você foi multado!')
    print('Excendente de velocidade = {}km/h'.format(velocidadeExcedente))
    print('Valor da Multa = R${}'.format(multa))
else:
    print('Velocidade dentro do permitido!')


# Enunciado 30
# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
numero = int(input('Digite um número: '))

restoDiv = numero % 2

if(restoDiv == 1):
    print('{} é ÍMPAR!'.format(numero))
else: #restoDiv == 0
    print('{} é PAR!'.format(numero))


# Enunciado 31
# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.
distancia = float(input('Digite a distancia de sua viagem(em Km): '))

precoPassagem = 0.0

if(distancia <= 200):
    precoPassagem = 0.5 * distancia
else: # distancia > 200
    precoPassagem = 0.45 * distancia

print('Preço da Passagem = R${}'.format(precoPassagem)) 


# Enunciado 32
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('Digite o ano a ser consultado: '))

if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print('O ano {} é bissexto!'.format(ano))
else: 
    print('O ano {} não é bissexto!'.format(ano))


# Enunciado 33
# Faça um programa que leia três números e mostre qual é o maior e qual o menor.
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

numeroMaior = numero1
numeroMenor = numero1

#Condição: numero1 x numero2
if(numeroMaior < numero2):
    numeroMaior = numero2
    #numeroMenor continua sendo numero1
else: #numeroMaior > numero2
    #numeroMaior continua sendo numero1
    numeroMenor = numero2 

#Condição numero1 e numero2 x numero3
if(numeroMaior < numero3):
    numeroMaior = numero3

#Condição numero1 e numero2 x numero3
if (numeroMenor > numero3):
    numeroMenor = numero3

print('\nMaior número = {}'.format(numeroMaior))
print('Menor número = {}'.format(numeroMenor))


# Enunciado 34
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1250,00 , calcule um aumento de 10%
# Para inferiores ou iguais, o aumento é de 15%
salario = float(input('Digite seu salário: R$'))

if(salario > 1250.0):
    print('Por ser mais que R$1250, o acréscimo é de 10%')
    salarioAtualizado = salario + (salario*0.1)
    print('Salário atualizado = R${}'.format(salarioAtualizado))
else :
    print('Por ser menos que R$1250, o acréscimo é de 15%')
    salarioAtualizado = salario + (salario*0.15)
    print('Salário atualizado = R${}'.format(salarioAtualizado))



#Enunciado 35
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um triângulo.

#Condição de existência:
#um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois lados.
lado1 = int(input('Digite o lado1 do triângulo: '))
lado2 = int(input('Digite o lado2 do triângulo: '))
lado3 = int(input('Digite o lado3 do triângulo: '))

principio1 = False
principio2 = False
principio3 = False

if ( (abs(lado1 - lado2) < lado3) and ((lado1 + lado2) > lado3) ):
    #print('Verdadeiro!')
    principio1 = True

if ( (abs(lado1 - lado3) < lado2) and ((lado1 + lado3) > lado2) ):
    #print('Verdadeiro!')
    principio2 = True

if ( (abs(lado2 - lado3) < lado1) and ((lado2 + lado3) > lado1) ):
    #print('Verdadeiro!')
    principio3 = True


if((principio1 == True) and (principio2 == True) and (principio3 == True)):
    print('--- PODE FORMAR UM TRIÂNGULO! ---')
else:
    print('--- NÃO PODE FORMAR UM TRIÂNGULO! ---')



#(MUNDO2 - ESTRUTURAS DE CONTROLE)

#Enunciado 36
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input('Digite o valor da casa: '))

SalarioComprador = float(input('Digite o salário do comprador: '))

QtdAnosPagamento = float(input('Digite em quantos anos ele vai pagar: '))

qtdMesesPagamento = QtdAnosPagamento * 12

valorPrestacaoMensal = valorCasa/qtdMesesPagamento

emprestimoMaximo = SalarioComprador*0.3 #Valor máximo de pagamento por mês (30% do salário)

print('Salário do comprador = R${} , Valor Máximo do empréstimo = R${} , valor prestação mensal = R${}'.format(SalarioComprador, emprestimoMaximo, valorPrestacaoMensal))

if(valorPrestacaoMensal > emprestimoMaximo):
    print('Valor da prestação excedeu os 30% de salário do comprador!')
    print('----- EMPRÉSTIMO NEGADO! -----')
else:
    print('----- EMPRÉSTIMO APROVADO! -----')


#Enunciado 37
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 Binário
# 2 Octal
#3 Hexadecimal
numero = int(input('Digite um número: '))

print('1 - Binário, 2 - Octal , 3 - Hexadecimal')

opcao = input('Você deseja converter para qual base de conversão? : ')

if(opcao == 1):
    print('{} convertido para Binário = {}'.format(numero, bin(numero)[2:]))
elif(opcao == 2):
    print('{} convertido para Octal  = {}'.format(numero, oct(numero)[2:]))
else: #opcao == 3
    print('{} convertido para HexaDecimal = {}'.format(numero, hex(numero)[2:]))


# Enunciado 38
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: 
# - O primeiro valor é maior
# - O segundo valor é maior 
# - NÃO EXISTE valor maior, os dois são iguais
numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

print('Numero 1: {} x {} :Numero 2'.format(numero1, numero2))

if(numero1 > numero2):
    print('--- O primeiro valor é maior! ---')
elif(numero1 < numero2):
    print('-- O segundo valor é maior! ---')
else: #numero1 == numero2
    print('--- OS DOIS TEM O MESMO VALOR! ---')


#Enunciado 39
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
anoNascimento = int(input('Digite seu ano de nascimento: '))

idade = 2024 - anoNascimento

print('Idade = {} anos'.format(idade))

if(anoNascimento>18):
    print('Já passou do tempo de alistamento, há {} anos!'.format(idade-18))
elif(anoNascimento == 18):
    print('Idade para se alistar')
else: #anoNascimento < 18
    print('O jovem ainda vai se alistar daqui a {} anos'.format(18-idade))


# Enunciado 40
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5: REPROVADO
# - Média entre 5 e 6.9: RECUPERAÇÃO
# - Media 7 ou superior: APROVADO
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

media = (nota1 + nota2)/2

if(media < 5):
    print('REPROVADO!')
elif(media >= 5 and media <= 6.9):
    print('RECUPERAÇÃO!')
else : #media >= 7
    print('APROVADO!')


# Enunciado 41
# A confederação nacional de natação precisa de um programa que leia o ano de nascimentode um atleta e mostre sua categoria, de acordo com sua idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL 
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER
anoNascimento = int(input('Digite seu ano de nascimento: '))

anoAtual = 2024

idade = anoAtual - anoNascimento

if(idade <= 9):
    print('MIRIM')
elif(idade <= 14):
    print('INFANTIL')
elif(idade <= 19):
    print('JUNIOR')
elif(idade <= 20):
    print('SÊNIOR')
else: #idade > 20
    print('MASTER')


# Enunciado 42
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados são iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes
lado1 = int(input('Digite o lado1 do triângulo: '))
lado2 = int(input('Digite o lado2 do triângulo: '))
lado3 = int(input('Digite o lado3 do triângulo: '))

principio1 = False
principio2 = False
principio3 = False
principioTriangulo = False

if ( (abs(lado1 - lado2) < lado3) and ((lado1 + lado2) > lado3) ):
    #print('Verdadeiro!')
    principio1 = True

if ( (abs(lado1 - lado3) < lado2) and ((lado1 + lado3) > lado2) ):
    #print('Verdadeiro!')
    principio2 = True

if ( (abs(lado2 - lado3) < lado1) and ((lado2 + lado3) > lado1) ):
    #print('Verdadeiro!')
    principio3 = True


if((principio1 == True) and (principio2 == True) and (principio3 == True)):
    principioTriangulo = True
else:
    print('--- NÃO PODE FORMAR UM TRIÂNGULO! ---')


if(principioTriangulo == True):
    if(lado1 == lado2 == lado3):
        print('--- O TRIÂNGULO É EQUILÁTERO! ---')
    elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
        print('O TRIÂNGULO É ISÓSCELES! ---')
    elif(lado1 != lado2 != lado3):
        print('--- O TRIÂNGULO É ESCALENO! ---')


# Enunciado 43
# Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida
peso = float(input('Digite seu peso(em Kg): '))
altura = float(input('Digite sua altura(em metros): '))

imc = peso/(altura**2)

print('O IMC é = {}'.format(imc))
if(imc < 18.5):
    print('--- Abaixo do peso! ---')
elif (imc >= 18.5 and imc <= 25):
    print('--- Peso está ideal! ---')
elif(imc > 25 and imc <= 30):
    print('--- Sobrepreso! ---')
elif(imc > 30 and imc <= 40):
    print('--- Obesidade! ---')
else: #imc > 40
    print('--- Obesidade mórbida! ---')


# Enunciado 44
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros
precoNormal = float(input('Digite o preço normal do produto: '))

print('----- Condição de pagamento -----')
print('1. - a vista dinheiro/cheque - 10% de desconto')
print('2. - a vista no cartão - 5% de desconto')
print('3. - em até 2x no cartão - preço normal')
print('4. - 3x ou mais no cartão - 20% de juros\n')
opcao = int(input('Digite a opção que deseja: '))

precoFinal = precoNormal

if(opcao == 1):
    precoFinal = precoNormal - (precoNormal*0.1)
elif(opcao == 2):
    precoFinal = precoNormal - (precoNormal*0.05)
elif(opcao == 3):
    precoFinal = precoNormal
else: #opcao == 4
    precoFinal = precoNormal + (precoNormal*0.2)

print('Preco Normal = {} , Preco Final = {}'.format(precoNormal, precoFinal))


# Enunciado 45
# Crie um programa que faça o computador jogar Pedra, Papel e Tesoura com você.
import random

lista = ['Pedra', 'Papel', 'Tesoura']

opcaoComputador = random.choice(lista)

opcaoJogador = input('Pedra, Papel ou Tesoura? : ')
opcaoJogador = opcaoJogador.title()

print('\nOpcao do Jogador = {} x {} = Opcao do Computador'.format(opcaoJogador, opcaoComputador))

if(opcaoJogador == 'Pedra'):
    if(opcaoComputador == 'Papel'):
        print('--- VITÓRIA DO COMPUTADOR ---')
    elif(opcaoComputador == 'Tesoura'):
        print('--- VITÓRIA DO JOGADOR ---')
    elif(opcaoComputador == 'Pedra'):
        print('--- EMPATE ---')

elif(opcaoJogador == 'Papel'):
    if(opcaoComputador == 'Pedra'):
        print('--- VITÓRIA DO JOGADOR ---')
    elif(opcaoComputador == 'Tesoura'):
        print('--- VITÓRIA DO COMPUTADOR ---')
    elif(opcaoComputador == 'Papel'):
        print('--- EMPATE ---')

elif(opcaoJogador == 'Tesoura'):
    if(opcaoComputador == 'Papel'):
        print('--- VITÓRIA DO JOGADOR ---')
    elif(opcaoComputador == 'Pedra'):
        print('--- VITÓRIA DO COMPUTADOR ---')
    elif(opcaoComputador == 'Tesoura'):
        print('--- EMPATE ---')

    
# Enunciado 46
# Faça um programa que mpstre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de um segundo entre eles.
import time

print('----- CONTAGEM REGRESSIVA -----')
for i in range(10, -1, -1):
    print(i)
    time.sleep(1)

print('\n--- Fogos !!!!!!! ---')


#Enunciado 47
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
listaPares = []

print('--- Números pares entre 1 e 50 ---')
for i in range(1, 51, 1):
    if( i % 2 == 0):
        print(i)
        listaPares.append(i)

print(listaPares)


# Enunciado 48
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
somatorio = 0
qtd = 0

for i in range(1, 501, 2): # Nesse for eu excluo os números pares
    if(i%3 == 0):
        qtd = qtd + 1
        somatorio = somatorio + i

print('Somatório dos {} ímpares múltiplos de 3 (de 1 até 500) = {}'.format(qtd, somatorio))


# Enunciado 49
# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
valor = int(input('Digite um valor: '))

for i in range(0,11):
    print('{}. {} x {} = {}'.format(i,valor, i, valor*i))


# Enunciado 50
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
import random

somatorio = 0

for i in range(1,7):
    numero = random.randint(1, 1000)
    print('{}. número: {}'.format(i, numero))
    if(numero%2 == 0):
        somatorio = somatorio + numero

print('Somatório = {}'.format(somatorio))


# Enunciado 51
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
#Formula: termoGeral = primeiroTermo + (posicaoTermo - 1)razao

primeiroTermo = int(input('Digite o primeiro termo: '))

razao = int(input('Digite a razão da PA: '))

#Mostre os dez primeiros termos da progressão
for i in range(1, 11):
    termoGeral = primeiroTermo + (razao*(i - 1))
    print('{}º Termo = {}'.format(i, termoGeral)) 


# Enunciado 52
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
numero = int(input('Digite um número: '))

for i in range (2, numero+1):
    if(i == numero):
        print('--- {} É PRIMO!! ---'.format(numero))
    if(numero%i == 0):
        print('{} é divisível por: {}'.format(numero,i))
        print('--- {} NÃO É PRIMO ---'.format(numero))


# Enunciado 53
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite uma frase: ')

frase = frase.lower()

frase = frase.split()
tamanhoFrase = len(frase)

fraseJunta = ''

for i in range(0, tamanhoFrase):
    fraseJunta = fraseJunta + frase[i] #Tô concatendo as Strings

fraseNova = ''

for i in range(len(fraseJunta)-1, -1, -1):
    fraseNova = fraseNova + fraseJunta[i] #Tô concatendo os caracteres da frase original, mas de maneira inversa

print(fraseJunta)
print(fraseNova)

if(fraseJunta == fraseNova):
    print('--- A frase {} É um Palíndromo! ---'.format(fraseJunta))
else:
    print('--- A frase {} NÃO É um Palíndromo! ---'.format(fraseJunta))


# Enunciado 54
# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
listaDataNascimento = []

for i in range(1,8):
    pessoa = int(input('Digite seu ano de nascimento: '))
    pessoaIdade = 2024 - pessoa
    listaDataNascimento.append(pessoaIdade)

#listaDataNascimento = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5, pessoa6, pessoa7]

print(listaDataNascimento)

maioridade = []
menoridade = []

for i in range(0,len(listaDataNascimento)):
    if(listaDataNascimento[i] >= 18):
        maioridade.append(listaDataNascimento[i])
    else: # <18
        menoridade.append(listaDataNascimento[i])

print('Quantidade de pessoas que ATINGIU A MAIORIDADE = {}'.format(len(maioridade)))

print('Quantidade de pessoas que NÃO ATINGIU A MAIORIDADE = {}'.format(len(menoridade)))

print('Lista Maioridade = {}'.format(maioridade))
print('Lista Menoridade = {}'.format(menoridade))



# Enunciado 55
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

listaPeso = []

for i in range(1, 6):
    peso = int(input('Digite seu peso: '))
    listaPeso.append(peso)

listaPeso.sort()

menorPeso = listaPeso[0]
maiorPeso = listaPeso[len(listaPeso)-1]

print('\n--- MAIOR E MENOR PESO ---')
print('Maior peso = {}Kg'.format(maiorPeso))
print('Menor peso = {}Kg'.format(menorPeso))
#----------------------------------------------------------#
#Outra forma de fazer (sem usar listas)
maiorPeso = 0
menorPeso = 300

for i in range(1, 6):
    peso = int(input('Digite seu peso em Kg: '))
    if(peso > maiorPeso):
        maiorPeso = peso
    if(peso < menorPeso):
        menorPeso = peso

print('\n--- MAIOR E MENOR PESO ---')
print('Maior peso = {}Kg'.format(maiorPeso))
print('Menor peso = {}Kg'.format(menorPeso))

# Enunciado 56
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo. 
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos
listaNome = []
listaIdade = []
listaSexo = []

for i in range(0, 4):
    nome = input('\nDigite o nome da pessoa: ')
    listaNome.append(nome)

    idade = int(input('Digite a idade da pessoa: '))
    listaIdade.append(idade)

    sexo = input('Digite o sexo da pessoa: ')
    listaSexo.append(sexo)

# I)
idade = 0
for i in range(0, 4):
    idade = idade + listaIdade[i]

mediaIdade = idade/len(listaIdade)
print('\nA média de idade do grupo é = {} anos'.format(mediaIdade))

# II)
idadeMaisVelho = listaIdade[0]
nomeMaisVelho = listaNome[0]
for i in range(0,4):
    if(listaSexo[i] == 'Masculino'):
        if(listaIdade[i] > idadeMaisVelho):
            idadeMaisVelho = listaIdade[i]
            nomeMaisVelho = listaNome[i]

print('O nome do homem mais velho é {} com = {} anos'.format(nomeMaisVelho,idadeMaisVelho))

# III)
menoridadeMulheres = 0
maioridadeMulheres = 0
listaMenoridade = {}

for i in range(0,4):
    if(listaSexo[i] == 'Feminino'):
        if(listaIdade[i] < 20):
            menoridadeMulheres = menoridadeMulheres + 1
            listaMenoridade = listaNome[i]
        else: #> 20
            maioridadeMulheres = maioridadeMulheres + 1

print('Quantidade de mulheres com menos de 20 anos = {} mulheres'.format(menoridadeMulheres))
print('São ela(s): {}'.format(listaMenoridade))
