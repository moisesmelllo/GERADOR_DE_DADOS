from random import randint


def criar_telefone():
    telefone_lista = []
    for c in range(0, 8):
        numero = randint(0, 9)
        telefone_lista.append(str(numero))
    telefone = '55119' + ''.join(telefone_lista)
    return telefone


nomes = ['moises', 'marcos', 'julio', 'matheus', 'antonio']
emails = ['moises@gmail.com', 'marcos@gmail.com', 'julinho@hotmail.com', 'matheus.farias@yahoo.com',
          'antonio311@hotmail.com']

telefones = [criar_telefone()]
cidades = ['sao paulo', 'guarulhos', 'manaus', 'castro', 'caichoeirinha']
estados = ['sao paulo', 'rio de janeiro', 'acre', 'amazonas', 'pernambuco', 'paraiba']

base_de_dados = nomes, emails, telefones, cidades, estados

