'''Crie um programa que tenha uma tupla com várias palavras(Não usar acentos)
Depois disso você deve mostrar para cada palavra, quais são suas vogais'''

palavras = ('Vai', 'Corinthians', 'Real', 'Madrid')
for p in palavras:
    #Exibindo as palavras
    print(f'\n Na palavra {p.upper()} temos: ', end=' ')
    
    #Para exibir as letras
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
