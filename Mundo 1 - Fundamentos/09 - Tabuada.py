# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.


#Tabuada de uma forma mais simples

numero = int(input('Tabuada de que? '))

for n in range(11):
    print(f'{numero} x {n} é igual a {numero * n}')
    
    