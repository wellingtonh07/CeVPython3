'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, #   mostrando no final
quantos palpites foram necessários para vencer.'''



from random import randint
computador = randint(0, 10)
print('Olá, sou seu computador e eu pensei em um número entre 0 e 10')
print('Será que você consegue adivinhar em que número eu pensei?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    #Para validar em quantas tentativas você acertou
    palpites = palpites + 1
    #Se o jogador jogou igual ao computador
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... ')
        else: 
            print('Menos... ')

print(f'Você acertou!!! Com {palpites} tentativas, PARABÉNS!')



 