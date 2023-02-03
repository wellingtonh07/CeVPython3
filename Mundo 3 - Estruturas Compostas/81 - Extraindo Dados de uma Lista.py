'''Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, mostre:
a) Quantos números foram digitados
b) Lista de valores ordenada de forma decrescente
c) Se o valor 5 foi digitado e está ou não na lista'''

lista = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
    

print(f'Lista de números digitados: {lista}')
print(f'Quantidade de números digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista de valores ordenados em ordem decrescente: {lista} ')
if 5 in lista:
    print('O número 5 foi digitado')
else:
    print('O número 5 não foi digitado')