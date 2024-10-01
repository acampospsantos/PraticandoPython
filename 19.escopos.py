#Escopo Global e Local
# Escopo global - variáveis que podem ser acessadas por todo o programa
# Escopo local - variáveis que só podem ser acessadas em rotinas locais(funções em que foram criadas

var_global = 'Curso em Python'

def escreve_texto():
    var_local = "Anderson Campos"
    print('VarGlobal: ', var_global, '- VarLocal: ', var_local)

print ("Executar a função escreve_texto()")
escreve_texto()

#Tentando acessar uma variável local
print(var_local) # 'Is not Defined' --> Pq? Pois essa variável só pode ser usada dentro da função escreve_texto()