'''Crie um programa que leia o nome completo de uma pessoa e mostre:
     - O nome com todas as letras maiúsculas e minúsculas.
     - Quantas letras ao todo (sem considerar espaços).
     - Quantas letras tem o primeiro nome.'''

#.strip() - elimina os espaços antes e depois do nome.
#nome.count(' ') - eliminando os espaços entre os nomes
#nome.find(' ') - Só mostra quantas letras tem no primeiro nome 

nome = str(input('Digite seu nome completo: ')).strip()
maiusculas = nome.upper()
minusculas = nome.lower()
tamanho = len(nome) - nome.count(' ')
primeiro = nome.find(' ')


print(f'O seu nome em maiúsculas é {maiusculas}')
print(f'O seu nome em minúsculas é {minusculas}')
print(f'O seu nome ao todo tem {tamanho} letras')
print(f'Seu primeiro tem {primeiro} letras') 