# Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

#Obs: Achei mais fácil copiar o que ja tinha feito no exercício 9, pois é mais simples.

numero = int(input('Tabuada de que? '))

for n in range(11):
    print(f'{numero} x {n} é igual a {numero * n}')
    