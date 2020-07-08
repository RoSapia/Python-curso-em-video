'''Leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra A,
Em que posição ela aparece a primeira vez
Em que posição ela aparece a ultima vez'''
frase = str(input('Digite uma frase: \n')).strip().upper()
a = frase.count('A')
a1 = frase.find('A')
afinal = frase.rfind('A')
print('A letra A aparece {} vezes na frase!'.format(a))
print('A letra A aparece primeiro na posição {}!'.format(a1+1))
print('A letra A aparece pela última vez na posição {}!'.format(afinal+1))