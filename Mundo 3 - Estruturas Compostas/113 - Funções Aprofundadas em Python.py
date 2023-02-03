'''Funções aprofundadas em Python
Reescreva a função lerInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite e crie também uma função lerFloat() com a mesma funcionalidade.'''

def lerInteiro():
    while True:
        try:
            número = int(input('Digite um número inteiro: '))
        #Quando digitar qualquer outra coisa que não seja um número inteiro
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número inteiro válido\033[m')
        else:
            return número 


def lerFloat():
    while True:
        try:
            número = float(input('Digite um número real: '))
        #Quando digitar qualquer outra coisa que não seja um número real
        except (ValueError, TypeError):
            print('\033[31mErro! Por favor digite um número real válido\033[m')
        else:
            return número 

#Programa principal
num1 = lerInteiro()
num2 = lerFloat()

print('-'*20)
print(f'''Número Inteiro: {num1}
Número real: {num2}''')
print('-'*20)
