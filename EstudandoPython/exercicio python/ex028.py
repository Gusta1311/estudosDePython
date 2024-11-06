#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente✅
#Ex Ana Maria de Souza
#Primeiro:Ana
#Ultimo:Souza

nome = str(input('Digite eu Nome: '))

nome_separado = nome.split()

primeiro_nome = nome_separado[0]
ultimo_nome = nome_separado[-1]
print("Primeiro Nome {}.".format(primeiro_nome))
print('Ultimo Nome {}'.format(ultimo_nome))