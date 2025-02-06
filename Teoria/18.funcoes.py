#Funções: Bloco de código que executa determinada tarefa

#VANTAGENS: Modularização, promove o reúso de código, Legibilidade

#Funções definidas pelo usuário X Funções internas do Python

# Estrutura
#def <nome_função> (argumentos):
#    <instruções>

def mensagem():
    print('Anderson Campos P Santos')
    print('Aprendendo Python')

mensagem()


def soma(a, b):
    total = a + b
    print('Soma = ', total)

soma(20, 10)


def multiplicacao(a, b):
    resultado = a * b
    return resultado

c = 20
d = 40
e = multiplicacao(c, d)
print(e)

def divisao(k, j):
    if (j != 0):
        return k/j
    else:
        return 'Impossível dividir por zero!'

resultadoDivisao = divisao(c, d)
print(c , ' dividido por ', d, ' = ',  resultadoDivisao)


# Função com parâmetros indefinidos
def contador(* num):
    tamanho = len(num)
    print('Parâmetros = {} , Qtd de Parâmetros = {}'.format(num, tamanho))

contador(5, 8, 10, 20)
contador(2)
contador(19 , 20, 30, 51, 80, 90, 100)


# Dobrando os valores de uma lista
def dobra(lista):
    pos = 0
    while(pos < len(lista)):
        lista[pos] = lista[pos] * 2
        pos = pos + 1
    print(lista)

lista = [10, 20, 30, 40, 50]

dobra(lista)