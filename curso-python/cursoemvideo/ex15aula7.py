#Pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais
#ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 p/dia e R$ 0,15 por km rodado
dias = int(input('Por quantos dias o carro foi alugado? '))
km =  int(input('Quantos km rodados? '))
pagar = (dias*60) + (km*0.15)
print('O total a pagar é R${:.2f} !'.format(pagar) )