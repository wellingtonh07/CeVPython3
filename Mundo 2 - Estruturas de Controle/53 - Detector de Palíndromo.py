
'''Palíndromo - Quando tanto a palavra escrita normalmente e de trás pra frente são iguais
Crie uma frase que leia uma frase qualquer e diga se ela é um Palíndromo, desconsiderando os espaços.'''


# [::-1] = o primeiro : representa o comeco de uma frase, o segundo : representa o final
# -1 representa a frase ou palavra de trás pra frente, do final para o começo.
#Obs: achei bem difícil esse exercício usando o for, então vou fazer de um jeito mais simples


frase = str(input('Digite uma frase: ')).upper().replace(' ', ' ')
print(frase)
print(frase[::-1])
if frase == frase [::-1]:
    print('É um palíndromo')
else:
    print('Não é um palíndromo') 
