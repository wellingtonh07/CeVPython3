'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços organizando os dados em forma tabular'''

#centralizar: :^numero
#colocar a esquerda: :<numero
#Colocar a direita: :>numero

listagem = ('Lápis', 3.75,
            'Caneta' , 4.00,
            'Mochila', 120,
            'Lapiseira', 1.25)

print('-' * 40)
print(f'{"Listagem de preços":^40}') #Centralizando string
print('-' * 40)

for pos in range(0, len(listagem)):
    #mostrando nomes dos produtos a esquerda
    
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end=' ')
    
    #colocando preço dos produtos a direita
    else: 
        print(f'R${listagem[pos]:>7.2f}')
