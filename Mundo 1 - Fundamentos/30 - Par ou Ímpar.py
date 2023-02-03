# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número qualquer: '))
resultado = numero % 2

print(f'O resultado é {resultado}')

if resultado == 1:
    print('IMPAR')
else:
    print('PAR')