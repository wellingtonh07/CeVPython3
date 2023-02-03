'''rie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
e o outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
'''


def fatorial(num, show=False):
    '''
    Calcula o fatorial de um número.
    :parâmetro num: o número a ser calculado
    :parâmetro show: (opcional), para mostrar ou não a conta
    :return O valor do fatorial de um número num
    '''
    fatorial = 1
    #range(início, fim, passo)
    for i in range(num, 0, -1):
        #Se show for verdade, mostra a conta
        if show:
            print(i, end="")
            #Pra mostrar o sinal de igualdade no fim do cálculo da fatorial
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    #Calculando e retornando a fatorial    
        fatorial *= i
    return fatorial


numero = int(input("Digite um número par saber o fatorial: \n"))
#Mostrando a fatorial com a conta
print(fatorial(numero, show=True))