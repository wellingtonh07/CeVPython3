'''Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
  - Média abaixo de 5.0: REPROVADO
  - Média entre 5.0 e 6.9: RECUPERAÇÃO
  - Média 7.0 ou superior: APROVADO'''


primeira = float(input('Digite a primeira nota: '))
segunda = float(input('Digite a segunda nota: '))
media = (primeira + segunda) / 2

if media < 5:
    print(f'A média foi {media}. Então, o aluno está REPROVADO!')
if media >= 5 and media <= 6.9:
    print(f'A média foi {media}. Então, o aluno ficou de RECUPERAÇÃO!')
elif media >= 7 : 
    print(f'A média foi {media}. Então, o aluno está APROVADO')