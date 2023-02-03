# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.


produto = float(input('Preço do produto: '))
desconto = produto * 5/100
final = produto - desconto

print(f'O produto custa {produto} e com o novo desconto de 5% é: {final}')