'''Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.'''

#importando biblioteca matemática (math)

import math
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
#importando dessa biblioteca a hipotenusa 
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa vai medir {hipotenusa:.2f}')