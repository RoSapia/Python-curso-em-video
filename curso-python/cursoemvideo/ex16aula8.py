#crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
'''import math
num = float(input('Digite um número: '))
porint = math.trunc(num)
print(porint)'''
num = float(input('Digite um número: '))
print('O número que você digitou é {} e sua parte inteira é {}'.format(num, int(num)))