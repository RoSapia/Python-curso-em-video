'''Leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo
sobrenome separadamente. EX.: Primeiro: Roberta, Ultimo: Sapia'''
nome = str(input('Digite seu nome completo: \n')).strip()
separado = nome.split()
print('Seu primeiro nome é: {}'.format(separado[0]))
print('Seu Último sobrenome é: {}'.format(separado[-1]))