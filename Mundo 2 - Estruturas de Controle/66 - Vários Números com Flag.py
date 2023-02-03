'''Crie um programa que leia números inteiros pelo teclado
O programa só vai parar quando apertar 999
No final mostre a soma e o valor entre eles'''

número = 0
soma = 0
contador = 0
while True:
    número = int(input('Digite um número [999 para parar]: '))
    if número == 999:
        break
    contador = contador + 1
    soma = soma + número
print(f'Você digitou {contador} números, e a soma entre eles é {soma}')