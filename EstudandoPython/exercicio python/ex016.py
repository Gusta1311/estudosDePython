carro = int(input("Quantos dias vocês ficaram com o carro? "))
km = float(input('Quantos kilômetros foi percorrido com o carro nesses dias? '))
Pago = (carro * 60) + (km * 0.15)
print('O total a se pagar foi de R${:.2f}'.format(Pago))