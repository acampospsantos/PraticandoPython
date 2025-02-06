#Funções builtin

valores = [2,5,8,-1,0,11,7,-6]
print(max(valores))
print(min(valores))

a = -5
b = 4

print (abs(a)) #Retorna o valor em módulo

print(pow(a,b)) #Exponenciação: os parâmetros a ser passados são base e expoente

c = 2.789011 
print(round(c,3)) ##A função round se passa o valor e a quantidade de casa decimais que serão usadas


#Módulo Math
import math

x = 8
y = 100

#Vamos extrair a raiz quadrada
raiz_quadrada = math.sqrt(x)
print(raiz_quadrada) # = 2.8
math.ceil(raiz_quadrada) #Arredonda pro inteiro mais próximo(pra cima) = 3
math.floor(raiz_quadrada) #Arredonda pro inteiro mais próximo(pra baixo) = 2

logaritmo = math.log10(y)
print(logaritmo)

print(math.pi) #Essa função diz o valor de π com a maior precisão possível

print(math.factorial(x)) #Calcula o fatorial do parâmetro