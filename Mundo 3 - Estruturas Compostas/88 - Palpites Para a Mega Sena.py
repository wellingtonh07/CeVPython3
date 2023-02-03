'''Faça um programa que ajude um jogador da Mega Sena a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo
Cadastrando tudo em uma lista composta'''

from random import sample
for x in range(int(input('Quantos jogos você quer fazer? '))):
    print(f'Jogo {x+1}: {sample(range(1,60),6)}')
