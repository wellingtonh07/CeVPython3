'''Crie um programa que leia varios números inteiros pelo teclado
No final, mostre a media entre todos os valores e qual foi o maior e menor valores lidos
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores'''

resp = 'S'
soma = 0
media = 0
quantidade = 0
maior = 0
menor = 0
while resp in 'Ss':
    número = int(input('Digite um número: '))
    soma = soma + número
    quantidade = quantidade + 1
    #por exemplo: foi digitado o numero 5.
    #Ele é o maior e menor número até agora
    if quantidade == 1:
        maior = menor = número   
    else:
        #Verificando o maior e menor número
        if número > maior:
            maior = número
        else:
            menor = número 
   
    resp = str(input('Deseja continuar? [S/N] ')).upper()
   
media = soma / quantidade    
print(f'Você digitou {quantidade} números e a média foi {media}')
print(f'O maior número foi {maior} e o menor foi {menor}')
   
