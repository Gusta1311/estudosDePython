#Faça um programa que mostre um ano qualquer e pergunte se ele é um ano bissexto
#
#Pede um ano para ser calculado
ano = int(input('Digite um ano: '))
#Aqui ele calcula se o ano é bissexto, e para descobrir isso primeiro temos que saber e ele é divisivel por 4 e nao por 100/ e se ele for por 100 ele tem que ser divisivel por 400 por isso aquele or no final para tratar da excessão dele ser dividido por 100
if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print('O ano {} é bissexto.'.format(ano))
#se nao ele nao é bissexto    
else:
    print('O ano {} não é bissexto.'.format(ano))

