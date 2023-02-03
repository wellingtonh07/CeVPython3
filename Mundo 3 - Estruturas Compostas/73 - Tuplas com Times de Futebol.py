'''Crie uma tupla preenchida com os 20 primeiros times do Brasileirão 2022. Na ordem de colocação.
Depois mostre:
a) Os 5 primeiros
b) Os 5 últimos
c) Times em ordem alfabética
d) Em que posição está o Corinthians'''

times = ('Pal', 'Int', 'Flu', 'Cor', 'Fla', 'Ath-PR', 'Galo', 'Fort', 'SPO', 'Coelho', 'Bota', 'Santos', 'Goi',
	 'Bra', 'Coxa', 'Cuia', 'Cea', 'Atl-Go', 'Avai', 'Juve')

#letra a
print('-=' * 20)
print('Os 5 primeiros times: ')
print(times[0:5])

#letra b
print('-=' * 20)
print('Os 4 últimos times: ')
print(times[16:])

#letra c
print('-=' * 20)
print('Em ordem alfabética: ')
print(sorted(times))

#letra d
print('-=' * 20)
print('Posição que o Corinthians ocupa')
print(times.index('Cor')+1)
