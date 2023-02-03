#Funções para sortear e somar
'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e soma_par(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista 
e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
'''
from random import randint
from time import sleep

def sorteia():
    #Criando lista na variável números
    numeros = list()
    for n in range(0, 5):
        #Adicionando números aleatórios entre 0 e 99
        numeros.append(randint(0, 99))
    print(f'Sorteando {len(numeros)} valores da lista: ', end='')
    #Mostrando os 5 números sorteados
    for i in numeros:
        print(f'{i} ', end='', flush=True)
        sleep(0.5)
    return numeros


def soma_par(lista_numeros):
    pares = list()
    for n in lista_numeros:
        #Adicionando os números pares
        if n % 2 == 0:
            pares.append(n)
    print(f'\nOs valores pares da lista são: ', end='')
    print(f'{pares}', end='')
    print(f'\nE o resultado da soma deles é: {sum(pares)}')


# sorteia()
# soma_par(numeros)

#Função dentro de outra função 
soma_par(sorteia())