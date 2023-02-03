'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final mostre:
A) Quantas pessoas tem mais de 18 anos
B) Quantos homens foram cadastrados
C) Quantas mulheres tem menos de 20 anos'''

tot18 = homens = mulheres = 0

while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resposta == 'N':
        break       
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')