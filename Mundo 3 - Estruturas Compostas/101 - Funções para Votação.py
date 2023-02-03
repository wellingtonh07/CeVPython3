'''Crie um programa que tenha uma função chamada voto()
que vai receber como parâmetro o ano de nascimento de uma pessoa, 
retornando um valor literal indicando se uma pessoa tem voto 
NEGADO, OPCIONAL ou OBRIGATORIO nas eleições.
'''

def voto(ano):
    #importando a biblioteca date para pegar uma data
    from datetime import date
    #Pegando o ano atual
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos de idade: VOTO NEGADO'
    elif idade < 18 or idade >= 65:
        return f'Com {idade} anos de idade: VOTO OPCIONAL'
    elif idade < 65:
        return f'Com {idade} anos de idade: VOTO OBRIGATÓRIO'


ano_nasc = int(input('Em qual ano você nasceu?\n> '))
print(voto(ano_nasc))