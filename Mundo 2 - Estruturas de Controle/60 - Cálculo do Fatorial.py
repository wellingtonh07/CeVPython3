#Faça um programa que leia um número inteiro qualquer e mostre seu fatorial.

from math import factorial

numero = int(input('Fatorial de que: '))
fatorial = factorial(numero)
print(f'A fatorial de {numero} é: {fatorial}')

