'''Leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
o primeiro valor é  maior
o segundo valor é maior
não existe valor maior, os dois são iguais'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número é o maior!')
elif n2 > n1:
    print('O segundo número é o maior!')
else:
   print('Não existe valor maior, os dois são iguais!')
print('FIM')