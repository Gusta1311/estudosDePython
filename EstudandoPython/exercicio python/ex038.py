#Escreva um programa que peça para o usuario escrever um numero inteiro qualquer e peça para o ususario escolher qual ser a base de conversao. 1- base binaria, 2 base octal, 3 base hexidecimal
print('Conversão de Bases Numéricas.')

#Pedi numero para o usuario
num = int(input('Digite um numero inteiro qualquer: '))

#Mostrar opçoes de conversao

print('\nEscolha sua base de conversão: ')
print('1- Base Binária.')
print('2- Base Octal.')
print('3- Base Hexadecimal.')
#Ele escolhe a base que ele quer
opcao = int(input("Opção desejada(1, 2, 3):"))

#Condições de cada uma acontecer
if opcao == 1:
    print(f'O número {num} em binário é {bin(num)[2:]}')
elif opcao == 2:
     print(f'O número {num} em binário é {oct(num)[2:]}')
elif opcao == 3:
      print(f'O número {num} em binário é {hex(num)[2:].upper()}')
else:
     print('❌ Opção Inválida. Escolha 1, 2 ou 3.')