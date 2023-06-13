from funcoes import *

while True:
    escolha = escolher_opcoes()
    if escolha == 'parar':
        break
    processar_escolhas()
    salvar_em_txt()
