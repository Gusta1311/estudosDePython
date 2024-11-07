#Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem ou nao formar um triangulo
#
#Pede ao usuario para digitar uma reta
reta1 = float(input('Digite 1° reta:'))

reta2 = float(input('Digite 2°reta:'))

reta3 = float(input('Digite 3° reta: '))

#Verificar se essas retas podem formar um triangulo. De acordo com a inequação triangular (se somar quaisquer dois lados tem que ser maior que o terceiro lado)
if (reta1 + reta2 > reta3) and (reta2 + reta3 > reta1) and (reta3 + reta1 > reta2):
    print('Pode se ser um triangulo: ')
#Se nao seguir a regar acima, printa que nao pode ser um triangulo
else:
    print('Nao pode se formar um triangulo: ')
