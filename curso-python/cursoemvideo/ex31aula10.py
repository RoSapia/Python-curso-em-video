'''PErgunte a distancia de uma viagem em km. Calcule o preço da passagem, cobrando
R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas'''
distancia = float(input('Qual a distância em Km, até o seu destino: \n'))

if distancia <= 200:
    print('O preço da passagem para o seu destino é R${:.2f}'.format(distancia * 0.5))
else:
    print('O preço da passagem para o seu destino é R${:.2f}'.format(distancia * 0.45))
print('=====Fim=====')