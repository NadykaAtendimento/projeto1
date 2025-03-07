import os
def exibir_nome_do_programa():
    print ('      𝓣𝓮𝓶𝓹𝓮𝓻𝓸 𝓢𝓮𝓬𝓻𝓮𝓽𝓸\n')

def exibir_opções():
    print('1- Cadastrar restaurante')
    print('2- Listar restaurante')
    print('3- Ativar restaurante')
    print('4- Sair\n')

def Encerrando_programa():
    os.system('cls')
    print('Encerrando o programa')



def opcao_invalida():
    print('Opção Inválida!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()


def escolher_opcao():

    opcao_escolhida= int(input('Escolha uma opção: '))
    print (f'Você escolheu a opção: {opcao_escolhida}\n')

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurantes')
    elif opcao_escolhida == 4:
        Encerrando_programa()
    else:
     opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opcao()

if __name__ == '__main__':
    main()