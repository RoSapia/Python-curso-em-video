'''Leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binario
2 para octal
3 para hexadecimal'''
num = int(input('Digite um número: '))
base = int(input('''Escolha uma das bases para conversão:
[ 1 ] para converter em binário;
[ 2 ] para octal;
[ 3 ] para hexadecimal. \n'''))
if base == 1:
    print('O número {} convertido em binário é {}!'.format(num, bin(num)[2:]))
elif base == 2:
    print('O número {} convertido em octal é {}!'.format(num, oct(num)[2:]))
elif base == 3:
    print('O número {} convertido em hexadecimal é {}'. format(num, hex(num)[2:]))
else:
    print('Opção inválida!')
print('FIM!')