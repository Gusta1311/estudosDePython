#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
quantidade_maiores = 0
quantidade_menores = 0
nomes_maiores = []
nomes_menores = []

for i in range(2):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    if idade >= 18:
        print('Parabéns, você é maior de idade!')
        quantidade_maiores += 1
        nomes_maiores.append(nome)
    else:
        print('Infelizmente, você é menor de idade.')
        quantidade_menores += 1
        nomes_menores.append(nome)

print()

if quantidade_maiores >= 1:
    print(f"As pessoas maiores de idade são: {', '.join(nomes_maiores)}.")
else:
    print('Não teve pessoas de maioridade.')

if quantidade_menores >= 1:
    print(f"As pessoas menores de idade são: {', '.join(nomes_menores)}.")
else:
    print('Não teve pessoas de menoridade.')

        
   

        
        
    
                  
    