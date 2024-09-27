#Strings: conjuntos de caracteres
#Características: também são imutáveis, mas é possível aceitar partes isoladas por meio de variáveis

nome = 'Anderson'
letra = nome[2] #É possível captar um caractere de uma string a partir do índice

print(letra)

print(len(nome)) #Possível calcular o comprimento da String

curso = 'Ciência da Computação'

print(nome, ' - ', curso)

#Exemplo de manipulação de Strings
email = input('Digite seu endereço de email: ')
arroba = email.find('@')
print(arroba)
usuario = email[0:arroba]
dominio = email[arroba+1:]
print(usuario)
print(dominio)

#Manipulação utilizando operadores de associação
produtos = 'Carbonato de sódio e óxido de zinco'
print('sódio' in produtos)
print('magnésio' not in produtos)


item = 'hipoclorito'
pos = item.find('clor')
print(pos)
pos = item.find('flu')
print(pos)

#Upper e Lower case
objeto_celeste = 'galáxia esPiral M31'
print(objeto_celeste)
print(objeto_celeste.upper())
print(objeto_celeste.lower())

#Substituição de caracteres dentro da string
suplemento = 'cloreto de magnésio'
n_suplemento = suplemento.replace('magnésio', 'zinco')
print(suplemento)
print(n_suplemento)

frase = '       Ômega 3 é bom pra saúde!               '
print(frase)
print(frase.Istrip()) #Elimina os espaços a mais da esquerda
print(frase.rstrip()) #Elimina os espaços a mais da direita
print(frase.strip()) #Elimina os espaços a mais da esquerda e direita


fruta = 'Abacate'
print(fruta)
print(fruta.rjust())