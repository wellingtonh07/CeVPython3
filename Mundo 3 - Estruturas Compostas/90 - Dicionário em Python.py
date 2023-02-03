'''Faça um programa que leia nome e média de um aluno e guarde em um dicionário.
No final, mostre o conteúdo da estrutura na tela'''

#Criando um dicionário 
aluno = {}

#Adicionando itens no dicionário 
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Média'] = float(input(f'Média do {aluno["Nome"]} '))

#Adicionando mais um item(Situação)
#Verificando se o aluno está aprovado, em recuperação ou reprovado
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado(a)'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado(a)'

print('-=' * 30)

#key = chave , value = valor
# {"key": valor}
#.items() - Retorna a chave e o valor do dicionário
for key, value in aluno.items():
    print(f'{key} = {value}')