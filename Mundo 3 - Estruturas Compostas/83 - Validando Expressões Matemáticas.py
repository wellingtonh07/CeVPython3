'''Crie um programa onde o usuário digita uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parenteses abertos e fechados na ordem correta.'''

expressão = str(input('Digite sua expressão: '))
pilha = []
for símbolo in expressão:
    if símbolo == '(':
        pilha.append('(')
    elif símbolo == ')':
        if len(pilha) > 0:
            #Removendo a última expressão
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão está válida')
else: 
    print('Sua expressão não está válida')