'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''


valor_casa = float(input('Qual é o valor da casa? '))
salário = float(input('Quanto você ganha? '))
anos = int(input('Quantos anos de financiamento? '))
prestação = valor_casa / (anos * 12)
mínimo = salário * 30 / 100
print(f'Para pagar uma casa de R${valor_casa:.2f} em {anos} anos, a prestação será de R${prestação:.2f}')

if prestação <= mínimo:
    print('Empréstimo pode ser concedido!')
else:
    print('Emprestimo NEGADO!')