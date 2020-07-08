n1 = float(input('Digite a nota da 1ª prova: '))
n2 = float(input('Digite a nota da 2ª prova: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m>= 6.0:
    print('A sua média foi boa! Parabéns!')
else:
    print('A sua média foi ruim! Estude mais!')
