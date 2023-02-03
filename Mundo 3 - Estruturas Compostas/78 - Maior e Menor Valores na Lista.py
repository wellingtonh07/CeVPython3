'''Crie um programa que leia 5 valores numéricos e os guarde em uma lista.
No final, mostre quais foi o maior e menor valor digitado e as suas respectivas posições na lista.'''

#Adicionando valores na lista
lista = [int(input('Digite um valor para a posição 0: ')), 
int(input('Digite um valor para a posição 1: ')),  
int(input('Digite um valor para a posição 2: ')), 
int(input('Digite um valor para a posição 3: ')), 
int(input('Digite um valor para a posição 4: '))]

for i, v in enumerate(lista):
    if v == max(lista):
        maior = i
    else:
        menor = i

print(f'O maior valor digitado foi: {max(lista)} na posição {maior} e omenor foi: {min(lista)} na posição {menor}')
