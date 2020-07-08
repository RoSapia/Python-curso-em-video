''' Leia tres numeros e mostre qual é o maior e qual é o menor'''
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
'''if num1 < num2 and num1 < num3:
    print('Menor número é o primeiro: {}'.format(num1))
elif num2 < num1 and num2 < num3:
    print('Menor número é o segundo: {}'.format(num2))
else:
    print('Menor número é o terceiro: {}'.format(num3))

if num1 > num2 and num1 > num3:
    print('Maior número é o primeiro: {}'.format(num1))
elif num2 > num1 and num2 > num3:
    print('Maior número é o segundo: {}'.format(num2))
else:
    print('Maior número é o terceiro: {}'.format(num3))
'''
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O maior número é o ', maior)
print('O menor número é o ', menor)

print('=====Fim=====')