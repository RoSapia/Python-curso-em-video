
#Leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
#a2 = b2 + c2 o quadrado da hipotenusa equivale à soma dos quadrados dos catetos
'''coposto = float(input('Digite o comprimento do cateto oposto: '))
cadjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = (coposto**2+cadjacente**2)**(1/2)
print('A hipotenusa é {:.2f}'.format(hipotenusa))'''
'''import math
coposto = float(input('Digite o comprimento do cateto oposto: '))
cadjacente = float(input('Digite o comprimento do cateto adjacente: '))
antes = pow(coposto, 2) + pow(cadjacente, 2)
hipotenusa = math.sqrt(antes)
print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))'''
from math import hypot
coposto = float(input('Digite o comprimento do cateto oposto: '))
cadjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(coposto, cadjacente)
print('A hipotenusa é {:.2f}'.format(hipotenusa))