# Operadores - Relacionais:
# ==     Igual a
# !=     Diferente de
# >      Maior que
# <      Menor que
# >=     Maior ou igual a
# <=     Menor ou igual a

# Comparação entre valores: e o resultado é um valor lógico(true ou false)

# Exemplo
a = 5
b = 6

#print (a == 5)

#print (b == 6)

#print (a == b)

#print (b == a + 1) #Operação aritmética é prioridade

#print (a * 2 >= b)

# Exemplo 2
x = y = z = False
n1 = n2 = 0

print('Digite um valor para n1: ')
n1 = int(input())
## Duas formas de pedir inserção de valores para o usuário
n2 = int(input('Digite um valor para n2: '))

x = (n1 == n2)
print (n1, ' e ', n2, 'são iguais ? = ', x, '\n')

y = (n1 > n2)
# print ('n1 é maior q n2? ', y)
print (n1, ' é maior que ', n2, ' ? = ', y, '\n')

z = (n1 != n2)
print(n1, ' é diferente de', n2, ' ? = ' + str(z), '\n') #Nesse caso foi convertido o valor de z(Boolean) para String