#Caso de condição Aninhada : elif
#exemplo:
idade = int(input('Digite sua idade: '))
if idade < 13:
    print('Criança.')
#Condição nova
elif idade < 18:
    print('Adolescente.')
elif idade < 65:
    print("Adulto.")
else:
    print("Idoso.")
