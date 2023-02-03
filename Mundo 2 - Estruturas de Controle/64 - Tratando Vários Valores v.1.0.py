'''Crie um programa que leia vários numeros inteiros pelo teclado
O programa só vai parar quando o usuário digitar o valor 999 que é a condição de parada
No final, mostre quantos números foram digitados e qual foi a soma entre eles'''

#Pode fazer assim também: número = contador = soma = 0
número = 0
contador = 0
soma = 0
número = int(input('Digite um número [999 para parar]: '))
while número != 999:
    soma = soma + número
    contador = contador + 1
    número = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {contador} números e a soma entre eles foi {soma}')