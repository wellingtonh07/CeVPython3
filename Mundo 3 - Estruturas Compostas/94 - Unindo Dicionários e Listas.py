'''Crie um programa que leia nome, sexo e idade de várias pessoas
Guarde esses dados em um dicionário e todos os dicionários em uma lista
No final, mostre:
a) Quantas pessoas foram cadastradas
b) Media de idade
c) Uma lista com as mulheres
d) Uma lista de pessoas com idade acima da média'''

#Criando dicionário vazio e adicionando dados a ele
pessoa = {}
galera = []
soma = media = 0

while True: 
    pessoa['nome'] = str(input('Nome da pessoa: '))

#Validação para caso a pessoa digite outra letra que não seja M ou F
    while True:
        #Limpando o dicionário pessoa antes de colocar os dados na lista galera
        pessoa.clear()
        pessoa['sexo'] = str(input('Sexo da pessoa: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ERRO. Tente novamente...')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    #Copia do dos dados do dicionário pessoas guardados em uma lista
    galera.append(pessoa.copy())
    
    #Outra validação, para caso a pessoa digite qualquer outra letra
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Tente novamente...')
    if resp == 'N':
        break

#Respondendo letra A
print(f'Ao todo temos {len(galera)} pessoas cadastradas')

#Letra B
media = soma / len(galera)
print(f'A média de idade é de {media:5.2f}')

#Letra C
print('As mulheres cadastradas foram: ')
for p in galera:
    if p['sexo'] in 'F':
        print(f"{p['nome']} ")

print()
