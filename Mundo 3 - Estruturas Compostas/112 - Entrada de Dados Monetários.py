'''Exercício Python 111 - Transformando módulos em pacotes
Dentro do pacote que criamos no desafio 111, temos um módulo chamado dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imput(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.'''

from ex112_módulo.UtilidadesCeV import moeda
from ex112_módulo.UtilidadesCeV import dado

preco = dado.leiaDinheiro('Informe um preço: R$ ')

moeda.resumo(preco, 65, 25)