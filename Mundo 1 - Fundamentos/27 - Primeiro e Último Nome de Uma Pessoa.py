'''Faça um programa que leia o nome completo de uma pessoa
mostrando em seguido o primeiro e ultimo nome separadamente.'''

nome = str(input('Nome completo: ')).strip()

n = nome.split()
primeiro = n[0]
sobrenome = n[len(n)-1]

print(f'Seu primeiro nome é {primeiro}.')
print(f'Seu sobrenome é: {sobrenome}.')
