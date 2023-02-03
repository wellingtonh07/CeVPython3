'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
e mostre seu status, de acordo com a tabela abaixo:
      - IMC abaixo de 18,5: Abaixo do Peso
      - Entre 18,5 e 25: Peso Ideal
      - 25 até 30: Sobrepeso
      - 30 até 40: Obesidade
      - Acima de 40: Obesidade Mórbida'''

peso = float(input('Qual é o seu peso? '))
altura = float(input('Qual é sua altura? (metros) '))
imc = peso / (altura ** 2)
print(f'O seu imc é {imc:.1f}')


if imc < 18.5:
    print('ABAIXO DO PESO NORMAL!')
elif imc >= 18.5 and imc <= 25:
    print('PESO NORMAL. PARABÉNS!!!')
elif imc > 25 and imc <= 30:
    print('SOBREPESO')
elif imc > 30 and imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
 
