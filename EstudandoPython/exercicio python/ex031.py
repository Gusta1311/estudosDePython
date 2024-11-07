#Crie um programa que mostre um numero qualquer inteiro e diga se ele é par ou impar
#✅
#O usuario escolhe o numero
numero = int(input('Digite um numero: '))
#Aqui eu digo se o numero é divisivel por 2 sem deixar resto, se for ele é par
if numero % 2 == 0:
    print('O numero  {} é par.'.format(numero))
#se nao ele é impar
else:
    print('O numero {} é impar.'.format(numero))
    