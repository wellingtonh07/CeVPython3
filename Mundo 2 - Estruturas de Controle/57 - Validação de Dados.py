'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
Caso esteja errado, peça pra digitar de novo até ter a resposta correta'''

sexo = str(input('Informe seu sexo [M/F] ')).strip().upper()
#Enquanto sexo não estiver em MmFf
#Mm = masculino em maiúsculo e minúsculo
#Ff = Feminino em maiúsculo e minúsculo
while sexo not in 'MmFf':
    print('Dados inválidos, tente novamente')
    sexo = str(input('Por favor, informe seu sexo: [M/F] ')).strip().upper()

print(f'Sexo {sexo} registrado com sucesso ')


