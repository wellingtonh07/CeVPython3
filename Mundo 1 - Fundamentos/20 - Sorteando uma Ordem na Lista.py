'''O mesmo professor do desafio 019 quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa que
leia o nome dos quatro alunos e mostre a ordem sorteada.'''

#random.shuffle(embaralha e retorna uma nova lista)

import random

primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
ordem = random.shuffle(lista)

print(f'A ordem escolhida é {lista}')