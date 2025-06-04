soma_idade = 0
nome_homem_mais_velho = ''
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(4):
    print(f'\nPessoa {i+1}')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    soma_idade += idade

    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
    elif sexo == 'F':
        if idade < 20:
            mulheres_menos_20 += 1

media_idade = soma_idade / 4

print('\nResultado:')
print(f'A média de idade do grupo é {media_idade:.1f} anos.')
if nome_homem_mais_velho:
    print(f'O homem mais velho é {nome_homem_mais_velho} com {idade_homem_mais_velho} anos.')
else:
    print('Não houve homens no grupo.')
print(f'Ao todo são {mulheres_menos_20} mulher(es) com menos de 20 anos.')
