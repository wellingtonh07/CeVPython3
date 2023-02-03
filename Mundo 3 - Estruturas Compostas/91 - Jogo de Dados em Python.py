'''Crie um programa onde 4 jogadores jogam um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número do dado'''

from random import randint
from time import sleep

#Criando dicionário vazio
jogo = {}
for pos in range(1,5):
    #Adicionando itens no dicionário 
    jogo[f"Jogador{pos}"] = randint(1,6)

for key, value in jogo.items():
    #mostrando o dicionário já formatado, mais bonito
    print(f'{key} tirou {value} no dado')
    sleep(1)

print('-=' * 30)
#Para mostrar ja do vencedor para o último lugar
x = 1

#Retorna o dicionário com os valores do maior para o menor 
for pos in sorted(jogo, reverse=True, key=jogo.get):
    print(f'{x}° Lugar: {pos} com {jogo[pos]}')
    x += 1
    sleep(1)