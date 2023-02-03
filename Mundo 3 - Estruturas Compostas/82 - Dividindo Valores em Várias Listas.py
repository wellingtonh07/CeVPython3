'''Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, crie 2 listas extras que vão conter apenas os valores pares e os valores ímpares
Ao final, mostre o conteúdo das 3 linhas digitadas'''

lista = []
par = []
ímpar = []

while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
    else:
        if n % 2 == 0:
            par.append(n)
        else:
            ímpar.append(n)

print(f'A lista completa é: {lista}')
print(f'A lista de pares é: {par}')
print(f'A lista de ímpares é: {ímpar}')