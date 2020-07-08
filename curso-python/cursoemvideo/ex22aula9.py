'''Leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minusculas
Quantas letras ao todo, sem considerar os espaços
Quantas letras tem o primeiro nome'''
nome = str(input('Escreva seu nome: ')).strip()
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
#print(len(nome.replace(' ', '')))
'''dividido = nome.split()'''
'''dividido2 = dividido[0]'''
'''print(len(dividido[0]))'''
print(nome.find(' '))
