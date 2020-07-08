#um professor quer sortear un dos seus quatro alunos para apagar o quadro. Ajude lendo o nome dos alunos e escrevendo o escolhido
from random import choice
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
sorteio = choice([aluno1, aluno2, aluno3, aluno4])
print('O aluno sorteado é: {}'.format(sorteio))
