'''Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar. No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$ 1000
C) Qual é o nome do produto mais barato'''

total = 0
tot1000 = 0
menor = 0
contador = 0
barato = ' '

while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    contador += 1
    total += preço       #Letra A
    if preço > 1000:     #Letra B
        tot1000 += 1
    if contador == 1 or preço < menor:    #Letra C
        menor = preço 
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi {total:.2f} reais.')
print(f'Temos {tot1000} produtos custando mais de R$ 1000')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')