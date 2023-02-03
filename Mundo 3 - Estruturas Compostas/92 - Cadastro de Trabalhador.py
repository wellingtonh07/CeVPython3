'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o(com idade) em um dicionário.
Se o CPTS for diferente de 0, o dicionário receberá também o ano de contratação e o salário
Calcule e acrescente com a idade, quantos anos a pessoa vai se aposentar'''

from datetime import datetime
#Criando um dicionário vazio
dados = {}

#Adicionando dados(exceto ano de nascimento)
dados['Nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = 2023 - nasc
dados['CTPS'] = int(input('Carteira de trabalho: (0 não tem): '))

#Adicionando mais dados
if dados ['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] + (dados['Contratação'] + 35 - datetime.now().year)

print('-=' * 30)

#Mostrando o dicionário formatado
for key, value in dados.items():
    print(f' - {key} tem o valor {value}')