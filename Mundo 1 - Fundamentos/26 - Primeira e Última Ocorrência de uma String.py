'''Faça um programa que leia uma frase pelo teclado e mostre:
       - Quantas vezes aparece a letra 'A'
       - Em que posição ela aparece a primeira vez
       - Em que posição ela aparece a última vez'''


nome = str(input('Informe seu nome: ')).upper().strip()
contar = nome.count('A')
primeira = nome.find('A') + 1
última = nome.rfind('A')


print(f'A letra "A" aparece {contar} vezes')
print(f'A primeira vez aparece na {primeira}ª posição')
print(f'A última vez aparece na {última}ª posição')