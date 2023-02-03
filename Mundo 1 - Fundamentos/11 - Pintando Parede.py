'''Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''


Largura = float(input('Largua da Parede: '))
Altura = float(input('Altura da Parede: '))
area = Largura * Altura
tinta = area / 2

print(f'Sua parede tem a dimensão de {Largura}x{Altura} e sua área é de {area}m²')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta')