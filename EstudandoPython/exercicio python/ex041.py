#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: Média abaixo de 5.0 : REPROVADO, Média entre 5.0 e 6.9 : RECUPERAÇÃO, Média 7.0 ou superior : APROVADO
nome = str(input('Digite seu nome: '))
nota_1 = float(input('Digite sua nota: '))
nota_2 = float(input('Digite sua segunda nota: '))

media = (nota_1 + nota_2)/2
if media < 5:
    print(f'{nome} você está reprovado!')
elif media > 5 and media < 6.9:
    print(f'{nome}, você está de Recuperação!')
elif media >= 7 and media <=10:
    print(f'{nome}, você está aprovado!')
else:
    print(f'{nome}, essa média total está fora do nosso sistema!')
     