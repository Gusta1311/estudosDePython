from time import sleep
valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor: '))
opcao = 0
while opcao != 5:
  
    print('''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
       O que você deseja fazer com os números {} e {}?
         [ 1 ] Somar
         [ 2 ] Multiplicar
         [ 3 ] Ver qual é o maior
         [ 4 ] Digitar novos números
         [ 5 ] Sair do programa
    '''.format(valor1, valor2))
    
    opcao = int(input('>>>>>> Escolha sua opção: '))
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
    sleep(2)
    match opcao:
         
         case 1: 
             soma = valor1 + valor2
             print(f'O resultado da soma de {valor1} + {valor2} é igual a {soma}')
                   
                   
         case 2:
                produto = valor1 * valor2
                print(f'O resultado da multiplicação de {valor1} * {valor2} é igual a {produto}')
                
         case 3: 
                if valor1 > valor2:
                    print(f'O resultado entre {valor1} e {valor2}, o maior número é {valor1}')
                elif valor2 > valor1:
                    print(f'O resultado entre {valor1} e {valor2},o maior número é {valor2} ')
                else:
                    print('Os dois números são iguais.')
                    
         case 4 :
             print('Certo, Insira novos valores.')
             valor1 = float(input('Digite o novo valor aqui: '))
             valor2 = float(input('Digite o outro novo valor aqui: '))
             
         case 5 :
                print('Finalizando Sistema...')
                
         case _:
             print( 'Opção Inválida, Tente Novamente...')
             sleep(2)
print('Programa Encerrado, Volte Sempre!')
                    

