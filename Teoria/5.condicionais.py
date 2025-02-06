# Estruturas Condicionais
#|--> Simples, Composto, Encadeado : if, elif, else

n1 = n2 = 0.0
media = 0.0

n1 = float(input("Digite a primeira nota: "))

n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2)/2

print('Média do aluno: ', media)

if (media >= 7):
    print('\n Aluno Aprovado!')
    print('Parabéns!! \n')
elif (media >=5): #Faz papel do else if
    print('\n Aluno em Recuperação')
    print('Vamos lá! \n')
else:
    print('\n Aluno Reprovado!')
    print('Lamentável \n')

    # : é um caractere para delimitação de bloco, é a antiga {}