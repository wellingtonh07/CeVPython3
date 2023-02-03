'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e
mantenha tudo funcionando.'''


from ex111_módulo.UtilidadesCeV import moeda

preco = float(input('Informe um preço: R$ '))

moeda.resumo(preco, 70, 10)

