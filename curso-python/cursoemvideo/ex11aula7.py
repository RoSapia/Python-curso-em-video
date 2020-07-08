#Leia a altura e a largura de uma parede em metros, calcule a sua area e a quntidade
# necessária de tinta para pinta-la, sabendo que cada l pinta 2m²
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parece em metros: '))
mquadrado = altura * largura
tinta = mquadrado / 2
print('A quantidade de tinta necessária para pintar {:.2f}m² é {:.2f}l!'. format(mquadrado,tinta))