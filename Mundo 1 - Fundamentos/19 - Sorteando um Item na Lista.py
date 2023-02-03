'''Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

#Biblioteca aleatória(random)
import random

primeiro = input('Primeiro aluno: ')
segundo = input('Segundo aluno: ')
terceiro = input('Terceiro aluno: ')
quarto = input('Quarto aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
#random.choice() -> retorna um item aleatório de uma lista
escolhido = random.choice(lista)

print(f'O escolhido foi {escolhido}')