# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.


d = float(input('Quanto de dinheiro você tem na carteira? '))
dolar = d / 5.41
euro = d / 5.61

print(f'Com {d} você vai poder comprar {dolar:.2f} dólares, e em euro {euro:.2f}')

# :.2f é para 2 casas decimais
