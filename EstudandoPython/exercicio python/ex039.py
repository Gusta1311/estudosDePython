#Escreva dois numeros inteiros e compare-os mostrando na tela a seguinte mensagem. - o primeiro é o maior valor, - o segundo é o maior valor, - os dois valores são iguais
numero_1 = int(input('Escreva o primeiro valor: '))
numero_2 = int(input('Escreva o segundo valor: '))

if numero_1 > numero_2:
    print(f'O primeiro valor {numero_1} é o maior.')
elif numero_1 < numero_2:
    print(f'O segundo valor {numero_2} é maior.')
else: 
    print('os dois valores são iguais.')