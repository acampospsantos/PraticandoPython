# Exceção é um objeto que representa um erro que ocorreu ao executar um programa

# Blocos try... except

#Exemplo: Código para divisão de dois números inteiros - utilizando tratamento de exceções
while True:
    try:
        n1 = int(input('Digite um numero inteiro(numerador): '))
        n2 = int(input('Digite um número inteiro(denominador): '))
        break
    except ValueError:
        print('# Ocorreu um erro ao ler o valor! Tente novamente. #')

try:
    r = (n1/n2)
except ZeroDivisionError:
    print('# Não é possível dividir por zero! #')
except:
    print('# Ocorreu um erro desconhecido! #')
else: #Caso ocorra nenhum erro.. será executado oq está no else
    print('Resultado = ', n1, '/', n2, ' = ', r)
finally: #Bloco de código que será executado independentemente de ter dado erro
    print('\nFim de cálculo!') 



# O melhor: tratar cada tipo de exceção separadamente