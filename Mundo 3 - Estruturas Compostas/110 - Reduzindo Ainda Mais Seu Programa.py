'''Exercício Python 110 - Reduzindo ainda mais seu programa
Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela
algumas informações geradas pelas funções que já temos no módulo criado até aqui.'''

from ex110_módulo import moeda

preço = float(input('Informe um preço: R$'))

moeda.resumo(preço, 80, 30)