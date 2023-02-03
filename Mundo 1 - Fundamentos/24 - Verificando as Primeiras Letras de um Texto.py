'''Faça um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "Santos"'''


#[:5] - So as 5 primeiras letras
#.strip() - Eliminando espacos antes e depois do nome
#upper() - Letras maiúsculas


cidade = str(input('Em que cidade você nasceu? ')).strip()
print(cidade[:5].upper() == 'SANTO')