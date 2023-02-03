'''Faça um programa que leia uma função chamada área (), que receba as dimensões...
de um terreno retangular(largura e comprimento) e mostre a área do terreno.'''

def area():
    print('Controle de terrenos')
    print('=' * 20)
    largura = float(input('Largura: (m) '))
    comprimento = float(input('Comprimento: (m) '))
    area_terreno = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area_terreno}m²')

area()