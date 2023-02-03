# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


salario = float(input('Qual é o seu salário? '))
aumento = salario * 15 / 100
novo_salario = salario + aumento

print(f'Você ganha {salario:.2f}, com 15% de aumento, passa a receber R${novo_salario:.2f}.')