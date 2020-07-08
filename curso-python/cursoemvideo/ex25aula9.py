'''Crie um programa que leia o nome de uma pessoa e diga se ela tem Silva no nome'''
nome = str(input('Digite seu nome completo: \n')).strip()
'''silva = nome.upper().split()
vdd = 'SILVA' in silva'''
print('Seu nome contém Silva? {}'.format('SILVA' in nome.upper()))


