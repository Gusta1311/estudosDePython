#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
from math import sqrt
cateto_oposto = float(input('Digite o angulo do cateto oposto: '))
cateto_adjacente = float(input('Digite um angulo do cateto adjacente: '))
hipotenusa = sqrt(cateto_oposto**2 + (cateto_adjacente**2))
print('O comprimento da hipotenusa vale {}.'.format((hipotenusa)))

#Pode fazer dessa forma tambem
from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjaccente: '))
hi = hypot(ca,co)
print =('A hipotenusa foi de {}.'.format(hi)) 