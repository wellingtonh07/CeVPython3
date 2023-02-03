'''Crie um programa onde o usuário possa digitar 7 valores numéricos.
Cadastre em uma lista única que mantenha separado os valores pares e ímpares 
No final, mostre os valores pares e ímpares em ordem crescente.'''

núm = [[], []]
valor = 0
for i in range(1,8):
    valor = int(input(f'Digite o {i}° valor: '))
    #Se for par, adiciona na primeira lista
    if valor % 2 == 0:
        núm[0].append(valor)
    #Caso contrário, adiciona na segunda lista
    else:
        núm[1].append(valor)

print('-=' * 30)
#Deixando em ordem crescente
núm[0].sort()
núm[1].sort()
print(f'Valores pares: {núm[0]}')
print(f'Valores ímpares: {núm[1]}')