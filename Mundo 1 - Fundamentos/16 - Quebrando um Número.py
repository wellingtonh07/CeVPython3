# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math
num = float(input('Digite um número: '))
int = math.trunc(num)

print(f'O número {num} tem a parte inteira {int}')