'''Exercício Python 109 - Formatando Moedas
Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,  
Informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.'''

from ex109_módulo import moeda

valor = float(input('Informe um valor: R$ '))

print(f'Aumento de 10%: {moeda.aumentar(valor, 10, True)}')
print(f'Reduzindo 15%: {moeda.diminuir(valor, 15, True)}')
print(f'O dobro de {moeda.moeda(valor)} é: {moeda.dobro(valor)}')
print(f'A metade de {moeda.moeda(valor)}: {moeda.metade(valor)}')

