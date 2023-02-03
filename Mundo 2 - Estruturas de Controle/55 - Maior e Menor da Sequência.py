'''Faça um programa que leia o peso de 5 pessoas.
No final mostre qual foi o maior e menor peso lidos.'''

#Achei mais simples fazer usando lista

#lista = [] -> é uma lista vazia
#lista.append -> adiciona um item na lista
#max(lista) -> maior item de uma lista
#min(lista) -> menor item de uma lista

lista = []

for pessoas in range(1,6):
    lista.append(float(input(f'Peso da {pessoas}ª pessoa em kg: ')))

print(f'O maior peso lido foi {max(lista)} kg')
print(f'O menor peso lido foi {min(lista)} kg')
    
