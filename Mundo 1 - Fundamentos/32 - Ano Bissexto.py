# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.


from calendar import isleap

ano = int(input('Digite o ano: '))
bissexto = isleap(ano) #Verificar se o ano é bissexto

if bissexto is True:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')