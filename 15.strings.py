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

# O find vai dizer em qual posição inicia a cadeia passada dos parâmetros
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


#Lembrando: a contagem da cadeia começa em 0
frase = 'Curso em Video'

#Curso em video (0-13) -> len = 14
print(frase[1:5]) #--> vai imprimir do 1ºcaractere ao 4ºcaractere (um por um)

print(frase[1::5]) #--> vai imprimir do 1ºcaractere até o final (pulando de 5 em 5)

print(frase[0:10:2])#--> vai imprimir do 0ºcaractere até o 9º caractere(pulando de dois em dois)

print(frase.count('o')) #--> vai dizer a quantidade de vezes que tem o caractere passado como parâmetro

print(len(frase)) #--> vai dizer o tamanho da cadeia de caracteres

frase.replace('Python','Android') #--> Vai substituir a String Android pela string Python

frase.capitalize() #--> Vai pôr o PRIMEIRO caractere da cadeia como maiúsculo, os demais ficarão em minúsculo
#Exemplo: frase = 'Curso em video'

frase.title() #--> Vai pôr o primeiro caractere de cada palavra da cadeia como maiúsculo
#Exemplo: frase = 'Curso Em Video'

#É possível combinar manipulações:
print(frase.lower().find('video')) #Eu tô transformando toda a cadeia em minuscula para achar o paramentro em  find() - retorna em valor booleano

print(frase.upper().find('CURSO')) #Transformei toda a cadeia em maiuscula para achar o parametro em find() - retorna em valor booleano

dividido = frase.split() #dividido é uma lista que tem 4 elementos = [curso, em, video]
print(dividido[0])
print(dividido[2][3]) #vai pegar o 3ºcaractere do 2º elemento da lista