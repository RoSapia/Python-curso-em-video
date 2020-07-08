#Leia o salário de um funcionario e mostre seu novo salário com 15% de aumento
salario = float(input('Digite o salário atual: R$'))
salarionovo = salario + salario * 15 / 100
print('Parabéns! Você teve um aumento de 15%!')
print('Seu salário antes era R${:.2f}, agora é R${:.2f} :D'.format(salario, salarionovo))