'''Aprimore o desafio anterior, mostrando no final:
a)A soma de todos os valores digitados
b)A soma dos valores da 3 coluna
c)O maior valor da segunda linha'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_par = terceira_coluna = maior = 0
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
        #a) soma dos pares
        if matriz[l][c] % 2 == 0:
            soma_par += matriz[l][c]
    #Para quebrar linha e assim formar a matriz
    print()
print('-=' * 30)
print(f'A soma dos valores pares é: {soma_par}')
#b) Soma dos valores da 3 coluna
for l in range(0,3):
    terceira_coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é: {terceira_coluna}')

#c) O maior valor da segunda linha
for c in range(0,3):
    if c == 0:
        maior = matriz[1][c]
    elif matriz [1][c] > maior:
        maior = matriz[1][c]

print(f'O maior valor da segunda linha é: {maior}')
