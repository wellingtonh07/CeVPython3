'''Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
      - à vista dinheiro/cheque: 10% de desconto
      - à vista no cartão: 5% de desconto
      - em até 2x no cartão: preço formal
      - 3x ou mais no cartão: 20% de juros'''

print('Bem vindos a loja do Wellington')
preco = float(input('Preço das compras: R$ '))
print(''' FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
	''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em {2}x de R${parcela}')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    parcelas_total = int(input('Quantas parcelas? '))
    parcela = total / parcelas_total
    print(f'Sua compra será parcelada em {parcelas_total} de {parcela:.2f} COM JUROS') 
else:
    total = preco
    print('Opção INVÁLIDA de pagamento.')  
print(f'Sua compra de {preco:.2f} vai custar R${total:.2f} no final')
