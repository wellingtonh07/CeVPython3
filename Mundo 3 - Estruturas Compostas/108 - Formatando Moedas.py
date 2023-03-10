'''Exercício Python 108 - Formatando Moedas
Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os
números como um valor monetário formatado.'''

from ex108_módulo import moeda

valor = float(input('Informe um valor: R$ '))

print(f'Aumento de 10%: {moeda.aumentar(valor, 10)}')
print(f'Reduzindo 15%: {moeda.diminuir(valor, 15)}')
print(f'O dobro de {moeda.moeda(valor, "$")} é: {moeda.dobro(valor)}')
print(f'A metade de {moeda.moeda(valor)} é: {moeda.metade(valor)}')