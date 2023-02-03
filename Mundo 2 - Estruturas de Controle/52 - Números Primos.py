#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo


# += é como se fosse: contador = contador + 1 ...
numero = int(input('Digite um número: '))
contador = 0

for i in range(2, numero):
    if numero % i == 0:
        contador += 1
if numero == 1:
    print('Esse número NÃO é primo')
elif contador == 0:
    print('Esse número É primo')
else: 
    print('Esse número NÃO é primo')