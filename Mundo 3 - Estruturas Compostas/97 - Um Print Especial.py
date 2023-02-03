'''Faça um programa que tenha uma função especial chamada escreva()...
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

#A msg dentro de escreva vai para o parâmetro da função escreva
#É como se ficasse: def escreva('Vai Corinthians')
def escreva(msg):
    tam = len(msg)
    print('~' * tam)
    print(msg)
    print('~' * tam)
    
    
escreva('Vai Corinthians')