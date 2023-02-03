'''Crie um programa que tenha a função leia_int(), 
que vai funcionar de forma semelhante à função input do Python,
só que fazendo a validação para aceitar apenas um valor numérico.
ex.:
n = leia_int("Digite um n")
'''


def leia_int(entrada_usuario):
    is_ok = False
    valor = None
    while True:
        numero = input(f'{entrada_usuario} \n')
        #Se número for número mesmo
        if numero.isnumeric():
            valor = numero
            is_ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        #Se estiver tudo bem, sai do loop
        if is_ok:
            break
    #Retorna o número
    return valor

#n = entrada_usuario da função leia_int
n = leia_int('Digite um número:')
print(f'Você acabou de digitar o número {n}.')
