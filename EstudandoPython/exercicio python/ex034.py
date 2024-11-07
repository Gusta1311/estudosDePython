#Faça um programa que leia 3 numeros e me diga qual o maior e qual é o menor
num1 = int(input('Digite um numero:'))

num2 = int(input('Digite outro numero:'))

num3 = int(input('Digite mais um numero:'))

if num1 > num2 and num1 > num3:
    maior = num1
    
elif num2 > num3 and num2 > num1:
    maior = num2
    
else:
    maior = num3
    
if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num3 and num2 < num1:
    menor = num2
else:
    menor = num3
print('O maior numero foi {}.'.format(maior))
print('O menor numero foi {}.'.format(menor))
    