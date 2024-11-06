#Crie um programa que leia o nome  completo de uma pessoa e mostre:
#1-O nome com todas as letras maiusculas✅
#2-Nome com todas minusculas✅
#3-Quantas letras ao todos (sem considerar os espaços)✅
#4-Quantas letras tem o primeiro nome.✅

frase = 'Gustavo Carvalho Cruz'
print(frase.upper())
print(frase.lower())

frase_s_espaço = frase.replace('','')
frase_contar = len(frase_s_espaço)
print('A sua frase tem {} letras!'.format(frase_contar))

frase_primeira = frase.split()[0]
frase_primeira_contar = len(frase_primeira)
print('A sua primeira frase tem {} letras!'.format(frase_primeira_contar))