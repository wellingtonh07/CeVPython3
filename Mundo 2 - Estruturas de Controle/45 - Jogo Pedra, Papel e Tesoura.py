# Crie um programa que faça o computador jogar Pedra, papel e tesoura com você.


#Pode ter if dentro de if
from random import randint
from time import sleep

print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
itens = ('Pedra' , 'Papel' , 'Tesoura')
computador = randint(0, 2)
jogador = int(input('Qual é a sua jogada? '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')

print('-=' * 11)
#Substitui o número por Pedra, Papel e Tesoura
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)

if computador == 0: #Jogou Pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Inválida')
elif computador == 1: #Jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Inválida')
elif computador == 2: #Jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada Inválida')
