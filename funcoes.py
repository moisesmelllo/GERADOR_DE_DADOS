import os
from random import randint, choice
from constants import *


def escolher_opcoes():
    global opcoes
    opcoes = input('''=========================================================
GERADOR DE DADOS - PARA INTERROMPER, 'DIGITE PARAR'
=========================================================
[1] NOMES
[2] E-MAILS
[3] TELEFONES
[4] CIDADES
[5] ESTADOS
digite o numero referente as opções desejadas: ''')
    print('')
    return opcoes


def processar_escolhas():
    global escolhas
    escolhas = []
    escolhas.clear()
    lista_de_escolhas = opcoes.split(',')
    for item in lista_de_escolhas:
        try:
            escolhas.append(choice(base_de_dados[int(item) - 1]))
        except:
            print('\033[0;31mdigite apenas numeros dentro do range acima e separados por virgula ou para '
                  'interromper, digite "parar"!\033[m')
            print()

    if len(escolhas) > 0:
        print('*'*50)
        for escolha in escolhas:
            print(escolha)
        print('*' * 50)
        # except Exception as error:
        #     print(error)


def salvar_em_txt():
    if len(escolhas) > 0:
        salvar = input('gostaria de salvar suas escolhas? (sim/não): ').lower().strip()
        if salvar in 'sim':
            with open('dados.txt', 'a', newline='') as file:
                for escolha in escolhas:
                    file.write(escolha + os.linesep)
                file.close()
                print()
                print('\033[32mescolhas salvas com sucesso em seu arquivo dados.txt\033[m')
                print()
        else:
            print()
            print('\033[31mescolhas nao salvas em seu arquivo dados.txt\033[m')
            print()


