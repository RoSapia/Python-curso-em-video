'''Leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
com a media atingida:
media abaixo de 5.0 REPROVADO
media entre 5 e 6.9 RECUPERAÇÃO
media 7 ou superior APROVADO'''
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2
if media < 5.0:
    print('A média do aluno foi {}.Aluno reprovado!'.format(media))
elif media >= 5 or media < 7:
    print('A média do aluno foi {}. Aluno em recuperação!'.format(media))
else:
    print('A média do aluno foi {}. Aluno aprovado!'.format(media))