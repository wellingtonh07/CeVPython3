'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome e quantas partidas ele jogou, depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos em um campeonato.'''

#Criando lista e dicionário vazio
dados = {}
gols = []

#Adicionando itens no dicionário 
dados['Nome'] = str(input('Nome do jogador: '))
dados['Partidas'] = int(input('Quantas partidas jogadas? '))

#Pegando a quantidade de gols que o jogador fez na partida
for c in range(1, dados['Partidas'] + 1):
    gols.append(int(input(f'Quantos gols na partida {c} ? ')))

#Adicionando a lista de gols no mesmo dicionário
#E somando o total de gols
dados['Gols'] = gols
total = sum(gols)    
print(f'{dados} total: {total} ')

print('-=' * 30)

#Fazendo agora formatado
for key, value in dados.items():
    print(f'{key} = {value}')
print(f'Total: {total}')


