listaCadastrados = []
pessoa = {}

def cadastrar():
    print('\n--- CADASTRO ---')
    while True:
        try:
            pessoa['nome'] = input('Digite seu nome: ')
        except Exception:
            print('## ERRO: DIGITE UM NOME VÁLIDO! ##')
        else:
            break
    while True:
        try:
            pessoa['idade'] = int(input('Digite sua idade: '))
        except Exception:
            print('## ERRO: DIGITE UM NÚMERO VÁLIDO! ## ')
        else:
            print('- Cadastro de {} efetuado com sucesso! -\n'.format(pessoa['nome']))
            listaCadastrados.append(pessoa.copy())
            break 


def listar():
    if(len(listaCadastrados) == 0):
        print('\n--- NÃO HÁ PESSOAS CADASTRADAS ---\n')
    else: 
        print('\n--- LISTA CADASTRADOS ---')
        for i in range(len(listaCadastrados)):
            print('{}. {} - {} anos'.format(i+1,listaCadastrados[i]['nome'],listaCadastrados[i]['idade']))
        print('----------------------\n')