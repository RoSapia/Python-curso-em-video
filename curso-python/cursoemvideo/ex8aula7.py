#Escreva um programa que leia um valor em metros e o exiba convertido e cm e mm
m = float(input('Digite um valor em metros: '))
dm = (m * 10)
cm = (m * 100)
mm = (m * 1000)
km = (m / 1000)
hm = (m / 100)
dam = (m / 10)

print('A medida de {}m em \ncm é {:.0f} e \nem mm é {:.0f}'.format(m, cm, mm))
print('em km é {}, em hectometro é {} e decametro é {}'.format(km, hm, dam))