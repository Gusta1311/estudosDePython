#Escreva um programa que faça o computador "pensar' em um numero inteiro entre 0 e 100 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu
#✅
#Da biblioteca random eu importei o modulo randint que rnadomiza numeros inteiros
from random import randint
from time import sleep
#sendo assim eu coloquei que a variavel do numero escolhido pelo computador, iria ser random entre 0 e 20
numero_computador = randint(0,100)
print('*'*100)
print('Bem vindo ao jogo da Adivinhação. tenet acertar o número...')
print('*'*100)
#aqui eu peço para o usuario escolher um numero para tentar acertar e salvo na variavel do usuario
numero_usuario = int(input("Escolha um numero entre 0 e 100: "))
print('PROCESSANDO...')
sleep(3)
#se o numero que o computador escolheu for igual ao do usuario ele ganha
if numero_computador == numero_usuario:
    print("Parabens, voce acertou!")
#se nao ele perde
else:
    print("Infelizmente você perdeu ja que o numero escolhido pelo computador foi {} e voce escolheu {}".format(numero_computador, numero_usuario))
print('*'*100)
print('FIM DE JOGO!')
print('*'*100)