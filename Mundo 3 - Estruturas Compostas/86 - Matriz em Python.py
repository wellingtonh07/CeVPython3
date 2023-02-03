'''Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
'''Matriz é 0,1,2. 3 colunas e 3 linhas
Fazendo a matriz de linhas'''
for l in range(0,3):
    #Fazendo a matriz de colunas
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)
#Para mostrar a estrutura na tela
for l in range(0,3):
    for c in range(0,3):
        #Resultado centralizado para caso o usuário digite número com mais digitos
        print(f'[{matriz[l][c]:^5}]', end='')
    #Para quebrar linha e assim formar a matriz
    print()