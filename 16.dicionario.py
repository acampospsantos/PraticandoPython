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