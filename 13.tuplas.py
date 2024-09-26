#Tuplas: São imutáveis --> Não pode alterar o valor/conteúdo da tupla, após sua criação

tupla = (2,4,6,7,9)
print(tupla)

print(type(tupla))

#Exemplo
#tupla[1] = 5  --> Vai dar erro, já que não podemos alterar esse valor diretamente

halogenios = ("F", 'Cl', 'Br', 'I', 'At')
print(len(halogenios))
print(halogenios[3]) #Podemos ler os valores a partir do índice

gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')

elementos = halogenios + gases_nobres
print(elementos)

t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)
print(t1.count(3)) #A função count serve para contar quantas vezes o elemento que está sendo passado como parâmetro apareceu na tupla

print(halogenios[0:2]) #Imprime dois elementos a partir de 0 da tupla, ou seja, o elemento 0 e 1

print ('Cl' in halogenios) #Esse in serve para procurar o parâmetro no halogênio --> retorna true ou false

print(sum(t1)) #A função sum vai somar todos os elementos da tupla

print(max(t1)) #A função max retorna o maior valor da tupla

print(min(t1)) #A função min retorna o menor valor da tupla


# Operações não disponíveis em tuplas: .sort() , append() , .reverse(), .pop() , ...
# Ou seja: qualquer operação que possa alterar o valor e as estruturas da tupla não estão disponíveis

for elemento in elementos:
    print('Elemento Químico: ', elemento)

#Podemos criar uma lista a partir de uma tupla:
grupo17 = list(halogenios)
print(grupo17)

#Podemos criar uma tupla a partir de uma lista:
grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alcalinos = tuple(grupo1)