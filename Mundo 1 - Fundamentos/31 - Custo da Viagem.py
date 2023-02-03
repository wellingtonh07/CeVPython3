'''Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
200Km e R$0,45 parta viagens mais longas.'''


distancia = float(input('Qual a distância da sua viagem? '))
print(f'Você está começando uma viagem de {distancia} km, boa sorte.')

if distancia <= 200:
    preco = distancia * 0.50
    print(f'O valor da sua passagem é de {preco} reais.')
else:
    preco = distancia * 0.45
    print(f'O valor da sua passagem é de {preco} reais.')