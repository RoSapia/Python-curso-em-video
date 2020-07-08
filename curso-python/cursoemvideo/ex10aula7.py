#Leia quanto dinheiro uma pessoa tem e mostre quantos dólares ela pode comprar dolar 3,27

real = float(input('Quantos R$ você tem na carteira? R$'))
dolar = (real / 3.27)
print('Você tem R${:.2f} na carteira e pode comprar US${:.2f}!'. format(real, dolar))