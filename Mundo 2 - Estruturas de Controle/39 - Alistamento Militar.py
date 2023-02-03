'''Faça um programa que leia o ano de nascimento de um jovem
e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''


atual = 2022
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')

if idade == 18:
    #igual a 18 anos
    print('Você já pode se alistar')
elif idade < 18:
    #menor de 18 anos
    saldo = 18 - idade
    print(f'Você ainda não tem 18 anos. Ainda faltam {saldo} anos para o alistamento.')
else:
    #maior de 18 anos
    saldo = idade - 18
    print(f'Você já deveria ter se alistado há {saldo} anos.')  

