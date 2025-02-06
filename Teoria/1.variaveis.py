# Variáveis: local reservado na memório do computador - dados que o programa utiliza
#Variável - Tipo de variável - tamanho na memória - valor

nome = 'Anderson'   #String 
idade = 24          #int
media = 6.5         #float
status = True       #Boolean

n1 = n2 = n3 = n4 = 0.0 #É possível inicializar diferentes varíaveis, mas com mesmo valor, na mesma linha

nome_aluno, idade = 'Antsu', 24 #Outra forma de fazer inicializações de variáveis

print(nome) #Imprime o conteúdo da variável nome 

# Função type() --> Função que diz o tipo de uma variável
print(type(idade))
print(type(nome_aluno))
print(type(status))

# Função isinstance() --> Função que retorna true ou false se a variável for do tipo que passamos de parâmetro
a = 10
b = 'Sol'
print(isinstance(a,int))
print(isinstance(b, float))