'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso de zero até 20
Seu programa deverá ler o número pelo teclado(entre 0 e 20) e mostra-lo por extenso.'''

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    número = int(input('Digite um número entre 0 e 20: '))
    if número >= 0 and número <= 20:
        print(f'O número digitado foi {cont[número]}')
        resp = str(input('Continua? ')).strip().upper()[0]
        if resp == 'N':
           break
    else:
        print('Número inválido, tente novamente. ')

print('Encerrando programa...')