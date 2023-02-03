'''Faça um programa que tenha uma função chamada maior, que receba vários parâmetros com valores inteiros
Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''

from time import sleep

#Função que aceita vários parâmetros por causa do *
#Desempacotando números usando o for
def maior(* núm):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    #Para mostrar os valores do programa principal
    for valor in núm:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        
        #Se for o primeiro valor(pode ser o menor também)
        if cont == 0:
            maior = valor
        
        #Se o valor for maior do que o maior valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    
    print(f'Foi informado {cont} valores ao todo')
    print(f'O maior valor foi {maior}')


#Programa principal
maior(2, 4, 5, 7, 9, 1)
maior(4, 7, 8)
maior(1, 2)
maior(6)
maior()