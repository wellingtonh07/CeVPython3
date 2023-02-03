'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA
No final mostre os 10 primeiros termos dessa progressão'''

primeiro = int(input('Primeiro número: '))
razao = int(input('Razão: '))
#Calculo da PA para os 10 primeiros termos
decimo = primeiro + (11-1) * razao

for i in range(primeiro, decimo, razao):
    print(i)

