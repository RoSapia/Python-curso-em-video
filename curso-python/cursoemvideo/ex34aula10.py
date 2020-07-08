'''Pergunte o salário de um funcionário e calcule o valor de seu aumento
Para salários superiores a R$1250,00  calcule um aumento de 10%
Para os inferiores ou iguais o aumento é de 15%.'''
salarioini = float(input('Qual o seu salário atual: \t'))
if salarioini > 1250:
    print('O seu salário aumentou 10% e agora passa a receber: {:.2f}'.format(salarioini * 1.1))
else:
    print('O seu salário aumentou 15% e agora passa a receber: {:.2f}'.format(salarioini * 1.15))
print('=====Fim=====')