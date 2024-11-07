#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento. Para salarios superiores a R$1.250.00 calcule um aumento de 10%. para os inferiores ou igual o aumneto é de 15%
#
#Pergunte ao usuario o valor do salario
salario = float(input('Quanto é seu salario:'))

#Verifica se o salario é superior a R$1.250.00
if salario <= 1.250:
    #Calcula o aumento de 15%
    aumento = (salario *15)/100
else:
    #Calcula o aumento de 10%
    aumento = (salario *10)/100
    
print('O aumento do seu salario foi de R${}'.format(aumento))