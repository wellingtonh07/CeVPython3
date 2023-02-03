'''Crie um programa que leia nome e 2 notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente'''

lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    #Criando uma lista composta com os dados apresentados
    lista.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break

print('-=' * 30)
#:<4 E 10 alinha os caracteres a esquerda
#:>8 Alinha os caracteres a direita
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
#i = índice
#a = aluno

for i, a in enumerate(lista):
    #a[0] = nome , #a[1] = notas, a[2] = media
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-' * 35)
    opção = int(input('Quer mostrar notas de qual aluno? (999 para): '))
    if opção == 999:
        print('FINALIZANDO...')
        break
    #Se for menor ou igual que o tamanho da lista - 1
    if opção <= len(lista) - 1:
        print(f'Notas de {lista[opção][0]} são {lista[opção][1]}')
        
print('<<< Volte Sempre >>>')
