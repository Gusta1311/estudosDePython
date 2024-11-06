#Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome "Santo"✅

cidade = str(input('Digite o nome de uma Cidade: '))

cidade_autenticador = 'Santos' in cidade

print('O nome da cidade é {}.'.format(cidade))
print('Ela tem Santos? {}'.format(cidade_autenticador))