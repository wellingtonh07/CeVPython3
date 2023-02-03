'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
'''

'''Função que retorna o nome e o número de gols que um jogador fez.
nome_jogador = nome, gols = numero_gols'''
def ficha(nome_jogador, numero_gols):
    return f'O jogador {nome_jogador.upper()} fez {numero_gols} gol(s) no campeonato.'


#Programa principal
nome = str(input('Nome do jogador: \n'))
#Se nada for digitado
if len(nome) == 0:
    nome = "<desconhecido>"

gols = str(input('Número de gols: \n'))
#Se o gol for um número
if gols.isnumeric():
    gols = int(gols)
else:
    #Se nada ou 0 for digitado
    gols = 0


print(ficha(nome, gols))
