#Refaça o exercício 51, pegaando 10 termos de uma PA mas dessa vez usando o while

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
#Pra mostrar o termos e contar até 10
termo = primeiro
contador = 1

#end='' -> para terminar na mesma linha
while contador <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razão 
    contador = contador + 1

print('FIM')