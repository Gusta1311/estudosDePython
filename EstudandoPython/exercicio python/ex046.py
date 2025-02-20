#Crie um programa que faça o computador jogar Jokenpô com você
from random import choice
print('Vamos jogar Jokenpô')
amauri = str(input('Escolha entre pedra papel e tesoura: '))

computador = ['pedra', 'papel', 'tesoura']
escolha = choice(computador)

if amauri == escolha:
    print('Empate')
elif amauri == 'pedra' and escolha == 'tesoura':
    print('Você ganhou!')
elif amauri == 'tesoura' and escolha == 'papel':
    print('Você ganhou!')
elif amauri == 'papel' and escolha == 'pedra':
    print('Você ganhou!')
else:
    print('Você perdeu!')
    print(f'Você escolheu {amauri} e o computador escolheu {escolha}!')
print('Fim de jogo!')

