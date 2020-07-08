#Leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco = int(input('Digite o preço do produto: '))
npreco = (preco - (preco * 5 / 100))
print('O produto de R${:.2f}, com o desconto de 5% fica: R${:.2f}'.format(preco, npreco))