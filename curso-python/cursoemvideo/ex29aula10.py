'''Leia a velocidade de uma carro. Se ele ultrapassar 80km/h, mostre uma msg
dizendo que ele foi multado. A multa vai custar R$ 7,00 cada km acima do limite'''
velocidade = int(input('Qual a velocidade do carro? \n'))

if velocidade > 80:
    print('Você está acima do limite de velocidade permitido, e foi multado em R${:.2f}!'.format((velocidade - 80) * 7))
else:
    print('Você está dentro do limite de velocidade permitido!')
print('===Fim===')