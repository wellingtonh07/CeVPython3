'''Crie um programa que leia o ano de nascimento de 7 pessoas.
No final mostre quantas pessoas atingiram ainda não atingiram a maioridade 
E quantas já são maiores'''

from datetime import date

#Para saber em que ano estamos
atual = date.today().year
maior = 0
menor = 0

for i in range(1,8):
    nascimento = int(input(f'Em que ano a pessoa {i} nasceu? '))
    idade = atual - nascimento
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
        
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E também tivemos {menor} pessoas menores de idade')