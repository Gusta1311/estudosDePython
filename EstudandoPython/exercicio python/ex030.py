#Escreva um programa que leia a velocidade de um carro.Se ele ultrapassar 80Km/H, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do 
#✅
#Dizendo a velocidade que o carro estava
velocidade = float(input('Digite a sua velocidade: '))
#se ele estiver acima de 80 vai pagar um valor de 7 vezes a diferença da velocidade dele - 80, ou seja  a velocidade a mais que ele estava e printando que ele foi multado e o valor da multa
if velocidade > 80:
    multa = (velocidade - 80) *7
    print('Você estava acima do limite de velocidade e a multa é de R${:.2f} pelo excesso de velocidade.'.format(multa))
#se nao ele se safa
else:
    print('Deu sorte maloqueiro,se liga em!')