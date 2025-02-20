#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: À vista dinheiro/cheque: 10% de desconto, À vista no cartão: 5% de desconto, Em até 2x no cartão: preço normal, 3x ou mais no cartão: 20% de juros
print('Abrindo Programa de Calculo de Preço de Produto')

#Perguntar o valor do produto
valor = float(input('Valor do produto: '))

#Escolher forma de pagamento
pagamento = str(input('Escolha sua forma de pagamento: 1- Dinheiro, 2- Cartão, 3- 2x, 4-3x: '))

#Fazer valor nomal a vista dinheiro/cheque com 10% de desconto
dinheiro = valor - (valor*10/100)

#Fazer valor normal a vista no cartão com 5% de desconto
cartao_vista = valor - (valor*5/100)
cartao2 = valor 
cartao3 = valor - (valor*20/100)

#fazer as condiçoes de pagamento
if pagamento == 'Dinheiro':
    print(f'O valor em dinheiro foi de {dinheiro} R$ com 10% desconto')
elif pagamento == 'Cartão':
    print (f'O valor no cartão a vista foi de {cartao_vista} R$ com 5% de desconto ')
elif pagamento == '2x':
    print(f'O valor do produto em 2x no cartão foi de {cartao2} R$')
elif pagamento == '3x':
    print(f'O valor no cartão em 3x ou mais no cartão foi de {cartao3} R$ com 20% de juros.')
else:
    print('Opção Inválida.')
print('Fim do programa')

