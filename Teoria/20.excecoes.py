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


try: # Bloco de código que será executado
    a = int(input('Digite o primeiro valor:  '))
    b = int(input('Digite o segundo valor: '))
    r = a/b
except (ValueError, TypeError):
    print('## Ocorreu um erro com os tipos de dados que você digitou! ##')
except ZeroDivisionError:
    print('## Não é possível dividir por zero!! ##')
except KeyboardInterrupt:
    print('## O usuário preferiu não informar os dados! ##')
except Exception as erro: #Erro genérico
    print('## O erro encontrado foi {erro.__cause__} ##')
else: #Bloco de código que será executado caso não dê erro
    print('O valor divisão {}/{} = {}'.format(a,b,r))
finally: # Bloco de código que será executado independente de ter dado certo ou erro
    print('Fim do programa')