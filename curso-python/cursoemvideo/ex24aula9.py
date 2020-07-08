'''Leia o nome de uma cidade e diga se ela começa ou não com o nome Santo.'''
cidade = str(input('Digite o nome da sua cidade:\n')).strip()
temsanto = cidade.upper().split()
temsanto1 = temsanto[0]
print(temsanto1 == 'SANTO')
