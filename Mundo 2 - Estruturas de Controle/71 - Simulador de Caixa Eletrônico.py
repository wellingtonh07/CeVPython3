'''#Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro)
E o programa vai perguntar quantas cédulas de cada valor serão entregues
Obs: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1'''

valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    #Verificando quantas vezes da pra tirar R$ 50 do total
    if total >= céd:
        total -= céd
        totcéd += 1
    #Verificando a cédula atual
    else:
        print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:   #
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        #Saindo do loop
        if total == 0:
            break

print('Encerrando programa')