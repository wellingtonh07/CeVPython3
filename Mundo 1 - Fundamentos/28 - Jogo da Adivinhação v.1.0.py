'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

import random
from time import sleep

print('Bem vindo ao jogo da Adivinhação: ')
numero = int(input('Vou pensar em um número entre 0 e 5, tente adivinhar... '))
#computador gera um numero aleatório entre 0 e 5
computador = random.randint(0,5)
print('PROCESSANDO...')
sleep(3) #Para fazer o computador "pensar"

if numero == computador:
    print('Você me ganhou, parabéns!')

else:
    print(f'A máquina sempre ganha!!! Eu pensei no número {computador} e não no {numero}')
