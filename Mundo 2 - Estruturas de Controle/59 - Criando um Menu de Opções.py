'''rie um programa que leia dois valores e mostre um menu na tela:
      [ 1 ] somar
      [ 2 ] multiplicar
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''


primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))
opção = 0
#Enquanto a opção for diferente de 5
while opção != 5:
    print(''' [1] Somar
 [2] Multiplicar
 [3] Maior
 [4] Novos números
 [5] Encerrar programa ''')
    print('=-' * 20)
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = primeiro + segundo
        print(f'{primeiro} + {segundo} = {soma}')
    elif opção == 2:
        multiplicação = primeiro * segundo
        print(f'{primeiro} x {segundo} = {multiplicação}')
    elif opção == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print(f'Entre o número {primeiro} e o número {segundo} o maior é o {maior}')
    elif opção == 4:
        #Depois de informar os números de novo, volta pro menu de opções 
        print('Informe os números novamente: ')
        primeiro = int(input('Primeiro número: '))
        segundo = int(input('Segundo número: '))
    elif opção == 5:
        print('=-' * 20)
        print('Encerrando programa...')
        print('Programa finalizado, volte sempre!')
    else:
        print('Opção inválida, tente novamente')
