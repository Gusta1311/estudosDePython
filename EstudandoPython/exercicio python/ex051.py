from random import randint
from time import sleep
print('*'*100)
print('Bem vindo ao jogo de Adivinhação!')
print('*'*100)
tentativas = 0
numero_usuario = -0
numero_comp =  randint(0,10)
print('Vamos ver se você descobre o número que estou pensando!')
sleep(2)
print('PROCESSANDO...')
sleep(3)
while numero_comp != numero_usuario:
    print('Você não acertou, tente novamente!')
    numero_usuario = int(input('Escolha um numero de 0 a 10: '))
    tentativas += 1
    
    if numero_usuario > numero_comp:
        print('MENOS... o número é menor.')
    elif numero_usuario < numero_comp:
        print('MAIOR... o número é MAIOR.')
        
print(f'PARABÉNS!, Você acertou na {tentativas} tentativa. O número era {numero_comp}! ')
    
    

