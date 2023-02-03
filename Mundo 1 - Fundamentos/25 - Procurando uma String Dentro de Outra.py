'''Faça um programa que leia o nome de uma pessoa
e diga se ela tem "Silva" no nome.'''


nome = str(input('Qual é seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {'silva' in nome.lower()}')