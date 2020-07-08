# -*- coding: utf-8 -*-
'''Leia a data de nascimento de um jovem e informe, de acordo com a sua idade:
se ele ainda vai se alistar ao exército
se é a hora de se alistar
se já passou do tempo do alistamento
mostre o tempo que falta ou que já passou do prazo '''
from datetime import date
from dateutil.relativedelta import relativedelta
hoje = date.today()
print('Digite a sua data de nascimento:')
dia = int(input('DIA: '))
mes = int(input('MÊS: '))
ano = int(input('ANO: '))
nascimento = date(ano, mes, dia)
idade = relativedelta(hoje, nascimento).years
if idade < 18:
    print('Você ainda vai se alistar no exército. Faltam {} anos'.format(18 - idade))
elif idade == 18:
    print('É a hora de se alistar!')
elif idade > 18:
    print('Já passou do tempo de alistamento! Passaram-se {} anos'.format(idade - 18))
