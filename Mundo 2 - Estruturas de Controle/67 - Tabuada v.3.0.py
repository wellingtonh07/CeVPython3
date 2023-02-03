'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor gerado pelo usuário
O programa será interrompido quando o valor solicitado for 0 ou negativo.'''


tabuada = 1
print('Informe um número e veja a tabuada dele. Se desejar sair digite 0 ou número negativo')

while True:
    print('=-' * 20)
    número = int(input('Qual tabuada você quer ver? '))
    #Para encerrar o programa. 0 ou menos que 0 ou seja, um número negativo
    if número <= 0:
        break
    else:
        #Para mostrar a tabuada, for é a melhor opção
        for tabuada in range (1, 11):
            print(f'{número} x {tabuada} = {número * tabuada}')
print('Encerrando programa...')
        	
    