#Um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada(n**(1/2)
n = int(input('Digite um número: '))
print('Digitou {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é: {:.2f}'.format(n, (n*2), (n*3), pow(n,(1/2))))