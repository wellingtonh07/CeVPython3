'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e indique o menor e maior valores na tupla.'''

from random import sample

while True:
    #Numeros aleatórios até 10 colocados na tupla
    números = tuple(sample(range(10), 5))
    print(números)
    print('-=' * 20)
    print(f'O maior número é {max(números)} e o menor é {min(números)}')
    print('-=' * 20)
    resp = str(input('Quer ver de novo? ')).strip().upper()[0]
    if resp == 'N':
        break
print('Encerrando programa...')