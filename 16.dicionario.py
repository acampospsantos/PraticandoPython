# Dicionários --> permitem armazenar dados em pares chave valor

# Similares aos arrays associativos (ou Hashmaps)

#Regra: Não pode ter chaves repetidas
# As chaves são imutáveis
# Então tipos mutáveis não podem ser usados. Ex's: Tuplas
elemento  = {
    'nome': 'Sport Club do Recife',
    'dataNasc': 1905,
    'grupo': 'Nordeste',
    'apelido': 'Maior do Nordeste',
    'titulosNacionais': 3
}

print('Time: ', elemento['nome'])
print('Data de fundação ', elemento['dataNasc'])
print('Apelido: ', elemento['apelido'])

#Atualizar uma entrada
elemento['titulosNacionais'] = 'CampeonatosNacionais'
print(elemento)

#Adicionar uma entrada
elemento['serieC'] = 0
print(elemento)

# Exclusão de itens em dicionários
del elemento['titulosNacionais']
print(elemento)

# Deletar todos os itens
elemento.clear
print(elemento)
#Outra forma: del elemento 

print(elemento.items()) #Vai retornar os itens do dicionário(em tuplas)
for i in elemento.itens():
    print(i)

print(elemento.keys()) #Lista com o nome das chaves
for i in elemento.keys():
    print(i)


#Declaração que dados é um dicionário
dados = dict()

#Podemos inserir valores de duas formas:
# I)
dados = { 'nome':'Pedro', 'idade':25 }

# II)
dados = { 'nome': 'Pedro', 
         'idade': 25
}

print(dados['nome'])
print(dados['idade'])

#Criei o elemento sexo que recebe M
dados['sexo'] = 'M'

# Pra eliminar um elemento + estrutura
del dados['idade']


print(dados.values())
#Vai imprimir = o valor das chaves

print(dados.keys())
# Vai imprimir as chaves de elemento = 'nome' e 'sexo'

print(dados.items())
# Vai imprimir as chaves e os valores das chaves

print('O sujeito {} tem {} anos!'.format(dados['nome'], dados['idade']))

for chave in dados.keys():
    print(chave)

for k, v in dados.items():
    print('{} = {}'.format(k , v))

dados['nome'] = 'Anderson'
dados['idade'] = 24

#Se eu quiser adicionar uma nova chave:
dados['peso'] = 92

print(dados)