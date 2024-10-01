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

