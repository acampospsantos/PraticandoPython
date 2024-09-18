#print é uma função interna do python

# Sintaxe:
# print(objetos/textos, argumentos)

#mensagem = 'Função print()'
#print(mensagem) 

nome = 'Anderson Santos'
canal = 'Andy Entreteniment'

#Formas de Imprimir:
print('Andy Entreteniment - ', nome)

print(canal, ' - ', nome)

name = input('Digite seu nome: ')
print ('Olá, ', nome, 'Bem vindo ao curso de Python!', end='')#Esse end é pra não ter a quebra da linha!


nome = "Andsu"
idade = 24
msg_formatada = 'O nome dela é {0} e ela tem {1} anos'.format(nome,idade)
print(msg_formatada)

#Outra forma de imprimir
msg = f'Olá, meu nome é {nome} e eu tenho {idade} anos!'
print(msg)