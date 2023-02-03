'''Faça um programa que leia algo pelo teclado
e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.'''



#Tipo primitivo: type()
#Espaços: isspace()
#Numero: isnumeric()
#Alfabetico: isalpha()
#Alfanumérico: isalnum()
#Maiúsculas: isupper()
#Minusculas: islower()
#Capitalizado(começa com maiúscula): istitle()

algo = input('Digite algo: ')
print(f'O tipo primitivo desse valor é: {type(algo)}')
print(f'Esse valor só tem espaços? {algo.isspace()}')
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
print(f'Está capitalizado? {algo.istitle()}')