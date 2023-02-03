'''Escreva um programa que leia um número inteiro N qualquer
E mostre na tela os N primeiros elementos de uma sequência de Fibonacci.
Sequência de fibonacci, é uma sequencia de números inteiros, começando por 0 e 1
Na qual cada termo seguinte, corresponde a soma dos 2 anteriores. ex: 0, 1, 1, 2, 3, 5, 8...'''


print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
número = int(input('Quantos termos você quer mostrar? '))

#Primeiro e segundo termos são definidos automaticamente
t1 = 0
t2 = 1
print('~' * 30)
print(f'{t1} -> {t2}', end='')

#Como ja tem 2 termos, o contador ajuda a não deixar o programa muito grande
contador = 3
while contador <= número:
    t3 = t1 + t2
    print(f' -> {t3}', end='')
    #Para apresentar os termos corretamente
    t1 = t2
    t2 = t3
    contador = contador + 1
print(' -> FIM')