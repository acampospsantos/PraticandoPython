# Operadores - Aritméticos:
# +     Soma
# -     Subtração
# *     Multiplicação
# /     Divisão real
# //    Divisão inteira
# %     Módulo (MOD)
# **    Potenciação

a = 20
b = 5
c = 2

print ('Soma = ', a + b) # Adição
print ('Subtracao = ', a - b) # Subtração
print ('Multiplicacao = ', a * b) # Multiplicação
print ('Divisao = ', a/c) # Divisão
#print ('Divisão inteira', a//c) #divisão inteira

print ('Potenciacao = ', a ** c) # Potenciação 

print ('Calculo: a + b * c = ', a + b * c) #Ordem das operações: multiplicação - soma


x = y = 0
#A função input recebe o valor digitado pelo usuário em String --> Dessa forma a seguir convertemos para int:
x = int (input('Digite o valor de x: ')) 
y = int (input('Digite o valor de y: '))
z = x + y
print('x + y = ', z)