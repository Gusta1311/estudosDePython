#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira. Ex: Digite um número:6.127/ O número 6.127 tem a parte inteira 6
from math import trunc
num = float(input('Digite um número: '))
inteiro = trunc(num)
print('O numero digitado {} tem o inteiro {}'.format(num,trunc(inteiro)))

#pode fazer dessa forma tbm
num = float(input('Digite um numero qualquer: '))
print('O numero digitado {} tem o inteiro {}'.format(num,int(num))) #usando o int ja que todo int é inteiro