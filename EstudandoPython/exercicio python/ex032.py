#Desenvolva um programa que pergunte a distancia de uma viagem em Km.Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de ate 200Km e R$0,45 para viagens mais longas
#✅
#Digite quantos ele quer fazer
viagem = float(input('Quantos km você quer fazer? '))
#Se a viagem for menos de 200 ou 200km ele pagar um valor x
if viagem <= 200:
    preco = viagem * 0.50
# se nao ele vai pagar outro valor
else:
    preco = viagem * 0.45
#printando a resposta com o valor da passagem final de acordo com a kilometragem feita
print('O preço da passagem ficou de R${}'.format(preco))