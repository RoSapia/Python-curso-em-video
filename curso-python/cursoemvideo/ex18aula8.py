#Leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
angulo = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('Para o angulo {:.2f}º, o seno é: {:.2f}; cosseno é: {:.2f} e a tangente: {:.2f}'.format(angulo, seno, cosseno, tangente))
