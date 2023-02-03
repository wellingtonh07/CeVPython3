'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista
No final, mostre
a)Quantas pessoas foram cadastradas 
b)Uma listagem com as pessoas mais pesadas
c)Uma listagem com as pessoas mais leves'''

temp = []
principal = []
maior = menor = 0


while True:
    temp.append(str(input('Nome: ')))
    temp.append(str(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    principal.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
    
print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi {maior}Kg. Peso de: ', end='')

for p in principal:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi de {menor}. Peso de: ', end='')

for p in principal:
    if p[1] == menor:
        print(f'{p[0]}')
print()