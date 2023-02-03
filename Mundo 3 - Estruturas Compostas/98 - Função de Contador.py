'''Faça um programa que tenha a função chamada de contador()...
que receba 3 parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada
A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
C) Uma contagem personalizada'''

from time import sleep
#flush=True -> Para auxiliar a função sleep na contagem
def contador(início, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {início} até {fim} de {passo} em {passo}')

    if início < fim:
        cont = início 
        #Enquanto o início for menor ou igual ao fim
        #Pra contar do menor para o maior
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print('FIM')
    else:
        cont = início 
        #Enquanto o início for maior ou igual ao fim
        #Para contar do maior para o menor
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= passo
        print('FIM')
        
        
#Programa principal

#Esses números e variáveis, substituem os parâmetros da função contador
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)