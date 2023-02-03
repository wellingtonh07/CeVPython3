'''Melhore esse programa perguntando se a pessoa quer adicionar mais termos
Encerre o programa quando a pessoa dizer que quer ver mais 0 termos'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
#Pra mostrar o termos e contar até 10
termo = primeiro
contador = 1
total = 0
#Simulando como se ele quisesse mais 10 termos
mais = 10
#Enquanto mais for diferente de 0
#Encerra o programa se o resultado da variável mais for = 0
while mais != 0:
    total = total + mais
    #total = porque pode escolher várias vezes enquanto não apertar 0
    #end='' -> para terminar na mesma linha
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razão 
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')