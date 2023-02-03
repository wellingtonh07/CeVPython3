'''Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista,
já na posição correta da inserção, sem usar o sort()
No final, mostre a lista ordenada na tela'''


lista = []
for i in range(0,5):
    n = int(input('Digite um número: '))
    if i == 0 or n > max(lista):
        lista.append(n)
        print('Adicionado ao fim da lista')
    else:
        
        #Para ver a posição do número adicionado
        for p, item in enumerate(lista):
            if n < item: #item = lista
                #inserindo um número em uma posição
                lista.insert(p, n)
                print(f'Adicionado a posição {p} da lista')
                break
    

print(f'Números adicionados: {lista}')