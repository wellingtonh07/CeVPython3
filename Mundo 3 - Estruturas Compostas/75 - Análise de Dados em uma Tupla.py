'''Desenvolva um programa que leia quatro valores pelo teclado e os guarde em uma tupla.
No final, mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os números pares'''


val = (int(input('Insira um número: ')),
int(input('Insira um número: ')),
int(input('Insira um número: ')),
int(input('Insira um número: ')))

print(f'Os números inseridos foram: {val}')
print(f'O valor 9 apareceu {val.count(9)} vezes')
if 3 in val:
    print(f'O valor 3 aparece na {val.index(3)+1}ª posição')
else:
    print('O número 3 não aparece em nenhuma posição ')
    
print('Os números pares foram: ', end=' ')
for n in val:
    if n % 2 == 0:
        print(n, end=' ')