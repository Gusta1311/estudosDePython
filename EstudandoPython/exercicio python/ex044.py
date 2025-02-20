#💡 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo: Abaixo de 18.5: Abaixo do Peso, Entre 18.5 e 25: Peso ideal, 25 até 30: Sobrepeso, 30 até 40: Obesidade, Acima de 40: Obesidade mórbida
peso = float(input('Digite seu peso(kg): '))
altura = float(input('Digite sua altura(m): '))

#calcular altura ao quadrado
altura_quadrado = altura **2

#fazer formula do imc
imc = peso / altura_quadrado

#deixar o resultado da condição em branco para depois eu mesmo colocar os status
resultado = ''

#Fazer as condiçoes para determinar o status
if imc < 18.5:
    resultado = 'Abaixo do Peso!'
elif 18.5 <= imc < 25:
    resultado = 'Peso Ideal!'
elif 25 <= imc < 30:
    resultado = 'Sobrepeso!'
elif 30 <= imc <= 40:
    resultado = 'Obesidade!'
elif 40 < imc:
    resultado = 'Obesidade Mórbida!'
print(f'Seu imc foi de {imc:.2f}, e seu status é {resultado}!')