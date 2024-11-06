#Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva no nome✅

nome = str(input('Digite seu nome aqui: '))
nome_autenticador = 'Silva' in nome
print('O nome da pessoa é {}.'.format(nome))
print('Ela tem Silva ? {}'.format(nome_autenticador))