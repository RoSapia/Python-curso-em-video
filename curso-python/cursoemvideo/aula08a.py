from math import sqrt, floor
#import math
num = int(input('Digite um número: '))
raiz = sqrt(num)
#raiz = math.sqrt(num)
#print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))