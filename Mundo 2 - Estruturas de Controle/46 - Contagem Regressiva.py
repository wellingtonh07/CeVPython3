'''Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''



#Sobre o for:
#c = variável, 10 = início, 0 = fim e -1 é pra ir voltando de 1 em 1

from time import sleep

print('Contagem regressiva para o estouro de fogos de artifício ')

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('BUM! BUM! POW!')