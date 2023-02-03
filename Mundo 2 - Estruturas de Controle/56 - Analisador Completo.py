'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas
No final do programa mostre: a media de idade do grupo
Nome do homem mais velho
Quantas mulheres tem menos de 20 anos'''

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulheres_20 = 0
for pessoas in range(1,5):
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): ')).strip()
    print('-=' * 10)
    somaidade += idade
#in = para ser maiúsculo ou minúsculo 
    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
#Verificar quem é o homem mais velho
    elif sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
#Verificar se tem mulheres com menos de 20 anos
    elif sexo in 'Ff' and idade < 20:
        mulheres_20 += 1

mediaidade = somaidade / 4
    
    
    
print(f'A média de idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {mulheres_20} mulheres com menos de 20 anos')


