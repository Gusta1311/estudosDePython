#Faça um programa que leia uma frase pelo teclado e mostre✅
#1- Quantas vezes aparece o 'A'.
#2- em que posição ela aparece a primeira vez
#3-em que posição ela aparece pela ultima vez

frase = str(input('Digite uma frase:  '))
frase_vezes =  frase.lower().count('a')
frase_primeira = frase.lower().find('a')
frase_ultima = frase.lower().rfind('a')
print('A letra (a) aparece {} vezes.'.format(frase_vezes))
print('A primeira vez que o (a) aparece é na posição {}°.'.format(frase_primeira))
print('E a ultima vez é na posição {}°.'.format(frase_ultima))



