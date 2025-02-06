# Enunciado 115
# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter duas opções: cadastrar e listar todas as pessoas cadastradas.

import arquivoModular

while True:
    print('--- Sistema Modularizado ---')
    print('0 - SAIR DO SISTEMA')
    print('1 - Cadastrar')
    print('2 - Listar cadastrados')
    try:
        opcao = int(input('Qual opção desejada? : '))
    except Exception:
        print('## ERRO: DIGITE UMA OPÇÃO VÁLIDA! ##\n')
    else:
        if(opcao < 0 or opcao > 2):
            print('## ERRO: DIGITE UMA OPÇÃO VÁLIDA! ##\n')
        elif(opcao == 0):
            print('Saindo do programa...')
            break
        else:
            if (opcao == 1):
                arquivoModular.cadastrar()
            elif (opcao == 2):
                arquivoModular.listar()

print('\nATÉ A PRÓXIMA!')