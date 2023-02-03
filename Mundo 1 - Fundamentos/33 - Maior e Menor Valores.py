# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#Forma mais simples de resolver 

primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
terceiro = int(input('Terceiro número: '))
numeros = [primeiro, segundo, terceiro]

print(f'O maior numero digitado foi {max(numeros)}')
print(f'O menor número digitado foi {min(numeros)}')