'''Desenvolva um programa que leia 6 numeros inteiros e mostre a soma apenas daqueles que forem pares
Se o valor digitado for ímpar, desconsidere-o'''

soma = 0
contador = 0
for i in range(1, 7):
    numero = int(input('Digite um número: '))
    #Se for par, soma
    if numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1
print(f'Você me mostrou {contador} números PARES e a soma entre eles é {soma}')