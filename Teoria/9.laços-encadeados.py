#Encadeamento de Laços de repetição

#Um laço que tá dentro de outro laço

#Primeiro exemplo
#for contador_externo in range(1,6):
#    print('\nRodada: ', contador_externo)
#    for contador_interno in range(5, 0, -1):
#        print ('Contador : ', contador_interno)

#print('\nFim dos laços!')

#Segundo exemplo
import random

for A in range(1,6):
    print('\nConjunto ', A)
    for B in range(5):
        num = random.randint(1,100) #num recebe valores aleatórios de 1 a 100
        print('Valor: ', num)