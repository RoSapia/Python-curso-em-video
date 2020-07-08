'''Leia um ano qualquer e mostre se ele é bissexto'''
from datetime import date
anobi = int(input('Digite um ano com 4 digitos "aaaa", para saber se é bissexto: \nColoque 0 p/ analizar o ano atual!'))
if anobi == 0:
    anobi = date.today().year


if anobi % 400 == 0 or anobi % 4 == 0 and anobi % 100 != 0:
    print('O ano {} é bissexto!'.format(anobi))
else:
    print('O ano {} não é bissexto!'.format(anobi))
print('=====Fim=====')