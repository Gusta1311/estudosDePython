#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno,cosseno e tangente desse 
#importar biblioteca e modulos
from math import sin,cos,tan,radians

angulo = float(input("Digite um angulo qualquer: ")) #pedindo o angulo

angulo_radians = radians(angulo)#transformando em raidando ja que o seno,cosseno e tangente so ler em radiando
# colocando o angulo em cada posição
seno = sin(angulo_radians)
cosseno = cos(angulo_radians)
tangente = tan(angulo_radians)
print('O seno de {}° é {:.2f}\no cosseno de {} é {:.2f}\ne a tangente de {} é {:.2f}.'.format(angulo,seno,angulo,cosseno,angulo,tangente)) #printando eles formatado