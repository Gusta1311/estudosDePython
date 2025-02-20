#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: Equilátero: todos os lados iguais, Isósceles: dois lados iguais, Escaleno: todos os lados diferentes.

triangulo1 = float(input('Digite o primeiro lado do triangulo: '))
triangulo2 = float(input('Digite o segundo lado do triangulo: '))
triangulo3 = float(input('Digite o terceiro lado do triangulo: '))

resultado = ''

if(triangulo1 != triangulo2 and triangulo1 != triangulo3 and triangulo2 != triangulo3):
    resultado = "Escaleno"
elif(triangulo1 == triangulo2 and triangulo1 == triangulo3 and triangulo2 == triangulo3):
    resultado = "Equiátero"
elif(triangulo1 == triangulo2 or triangulo1 == triangulo3 or triangulo2 == triangulo3) and (triangulo1 != triangulo2 or triangulo1 != triangulo3 or triangulo2 != triangulo3):
    resultado = "Isóceles"
else:
    print('Você é burro!')
print(resultado)


