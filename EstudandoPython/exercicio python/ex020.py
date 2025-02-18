#Um professor que sortear um de seus alunos para apagar a lousa.Faça um programa que ajude ele, lendo o nome do escolhido
from random import choice
n1 = input('Digite um nome para ser Sorteado: ')
n2 = input('Digite o segundo nome a ser sorteado: ')
n3 = input ('Digite o terceiro nome a ser sorteado: ')
n4 = input('Digte o quarto nome a ser sorteado: ')

alunos = [n1,n2,n3,n4]
aluno_random = choice(alunos)

print('O aluno que vou escolher para apagar a lousa vai ser {}!'.format(aluno_random))
 
 