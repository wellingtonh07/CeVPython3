'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já esteja lá dentro, ele não será adicionado
No final serão exibidos todos os valores únicos digitados em ordem crescente'''
    
números = list()
while True:
    n = int(input('Digite um número: '))
    
    #Verificando se n já está na lista
    #Se não estiver, adiciona
    if n not in números:
        números.append(n)
        print('Número adicionado com sucesso')
    else:
        print('Número duplicado, não vou adicionar')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

#Deixando em ordem crescente
números.sort()
print(f'Os números adicionados em ordem crescente foi {números}')
