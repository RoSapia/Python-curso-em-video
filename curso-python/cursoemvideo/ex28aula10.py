'''Faça o computador pensar em um número entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela
se o usuário venceu ou perdeu'''
from random import randint
from time import sleep
randomico = randint(0,5)
print('-=*' * 30)
print('Adivinhe o número escolhido pelo computador (0 a 5)!')
print('-=*' * 30
      )
num = int(input('Eu escolho o: '))
print('Processando...')
sleep(3)
if num == randomico:
    print('Você digitou {} e... '.format(num))
    sleep(2)
    print('Acertô miseravi!')
else:
    print('EEEErroooooo! O computador escolheu: {}'.format(randomico))
print('=====Fim do jogo=====')
