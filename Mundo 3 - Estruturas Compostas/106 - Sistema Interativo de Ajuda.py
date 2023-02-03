'''Faça um minissistema que utilize o interactive help do Python
O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra "FIM", o programa se encerrará!.
OBS: use cores.'''

from time import sleep


def escreva(texto):
    #Enfeitando o texto
    tamanho = len(texto) + 4
    print('~' * tamanho)
    print(f'  {texto}')
    print('~' * tamanho)


def pyhelp(comando):
    help(comando)


def default_loop():
    while True:
        escreva('Sistema de ajuda PyHELP')
        funcao_ou_lib = input('Função ou Biblioteca > ')
        #Sai do loop e encerra o programa
        if funcao_ou_lib.upper() == 'FIM':
            break
        #Mostra a doc da função ou programa
        else:
            pyhelp(funcao_ou_lib)


default_loop()