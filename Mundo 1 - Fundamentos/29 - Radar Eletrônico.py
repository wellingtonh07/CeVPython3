'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.'''


from time import sleep

carro = int(input('Qual a velocidade do seu carro? em KM/h: '))
multa = 7 * (carro - 80)

'''por ex: a resposta é 81, a variável carro se transforma em 81
então (81 - 80) = 1. 
7 * 1 = 7. Então a multa seria de 7 reais.'''

print('PROCESSANDO...')
sleep(2)

if carro < 80:
    print('Tudo bem, prossiga!')
else:
    print(f'Você foi multado, sua multa é de {multa} reais.')