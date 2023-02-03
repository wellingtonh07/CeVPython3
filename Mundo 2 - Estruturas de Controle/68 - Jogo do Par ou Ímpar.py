'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

v = 0
while True:
    jogador = int(input('Você joga qual número: '))
    computador = randint(0,10)
    total = jogador + computador
    print('=-' * 10)
    tipo = str(input('PAR OU ÍMPAR? ')).strip().upper()[0]
    print(f'Você jogou {jogador}, computador jogou {computador}')
        
    if tipo == 'P':
        if total % 2 == 0:
            print(f'Deu {total}, É PAR, VOCÊ VENCEU!!!')
            v = v + 1
        else:
            print('Deu ÍMPAR, VOCÊ PERDEU')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print(f'Deu {total}, é ÍMPAR, VOCÊ VENCEU!!')
            v = v + 1
        else:
            print('Deu PAR, VOCÊ PERDEU')
            break
    print('-=' * 10)
    novamente = str(input('Vamos jogar novamente? ')).strip().upper()[0]
    if novamente == 'N':
        break
print(f'GAME OVER! Você venceu {v} vezes!')