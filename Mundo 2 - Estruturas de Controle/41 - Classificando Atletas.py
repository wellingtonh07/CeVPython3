'''A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
  - Até 9 anos: MIRIM
  - Até 14 anos: INFANTIL
  - Até 19 anos: JÚNIOR
  - Até 25 anos: SÊNIOR
  - Acima de 25 anos: MASTER'''

nascimento = int(input('Informe o ano do seu nascimento: '))
atual = 2022
idade = atual - nascimento

print(f'Você tem {idade} anos')
if idade <= 9:
    print('Classificação MIRIM')
elif idade > 9 and idade <= 14:
    print('Classificação INFANTIL')
elif idade > 14 and idade <= 19:
    print('Classificação JUNIOR')
elif idade > 19 and idade <= 25:
    print('Classificação SÊNIOR')
else: 
    print('Classificação MASTER')