'''Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem
ou não formar um triangulo'''
print('\033[7;31m Para saber se é triângulo!')
reta1 = float(input('Informe o comprimento da primeira reta: '))
reta2 = float(input('Informe o comprimento da segunda reta: '))
reta3 = float(input('Informe o comprimento da terceira reta: '))
if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print('Forma triângulo!')
else:
    print('Não forma triângulo!' )
print('='*5, 'Fim', '='*5)

