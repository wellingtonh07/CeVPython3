'''Faça um programa que calcula a soma entre todos os números ímpares
que são multiplos de 3 e que se encontram em un intervalo entre 1 e 500.'''

soma = 0
contador = 0
for i in range(1, 501, 2):
    # % = divisão. vendo se um número é divisível por 3.
    if i % 3 == 0:
        contador = contador + 1
        soma = soma + i
print(f'A soma entre todos os {contador} valores é {soma}')