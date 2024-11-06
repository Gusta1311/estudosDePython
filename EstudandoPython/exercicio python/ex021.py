#O mesmo professor do desafio anterior quer sortear a ordem de apresentação dos alunos.Faça um rpograma que leia o nome dos quatros alunos e mostre a ordem sorteada
from random import shuffle
n1 = input('Digite o Nome do Aluno: ')
n2 = input('Digite o nome do outro Aluno: ')
n3 = input('Digite o nome de mais um Aluno: ')
n4 = input('Digite o nome do ultimo aluno: ')
aluno = [n1,n2,n3,n4]
shuffle(aluno)
print('A ordem da Apresentação será 1°{0}\n2° {1}\n3° {2}\n4° {3}'.format(aluno[0],aluno[1],aluno[2],aluno[3]))