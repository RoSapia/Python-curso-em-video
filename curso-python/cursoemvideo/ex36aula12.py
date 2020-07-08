'''Programa aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o
valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela nã pode esceder 30% do salário ou então o empréstimo
será negado '''
precoCasa = float(input('Qual o preço da casa? '))
salario = float(input('Qual o seu salário? '))
parcelas = int(input('Em quantas parcelas pretende pagar o empréstimo? '))
prestacao = (precoCasa / parcelas)
print('Uma casa de {:.2f}, paga em {} parcelas, custa R${:.2f} mensal'.format(precoCasa, parcelas, prestacao))
if prestacao >= (salario * (30/100)):
    print('Empréstimo bancário negado! Seu salário não atingiu a renda mínima necessária!')
else:
    print('Empréstimo concedido! O valor das parcelar é de R${:.2f}'.format(prestacao))