#Fatiamento

#digitei uma frase e guardei em uma variavel chamada frase
frase = 'Curso em video Python'

#chamei em uma lista o 9 caractere da variavel frase
frase[9]# Sendo assim o V

#outro exemplo
#ele pega do 9 caractere ate o 12 ele exclui o 13
frase[9:13] #Sendo assim o V,I,D,E

#outra forma
#ele mostra de 2 em 2 ate o 21(que seria o 20 ja que ele come o ultimo)
frase[9:21:2] #Sendo assim V,D,O,P,T,O (Lembrando que nos renders(que é o nome desse fatiamento de outras manipulações) o espaços vazios que sao os espaços que voce da tbm conta na hora de contar as letras)

#outra
#mostra so onde termina mas nao mostra de onde começa ou seja ele SEMPRE vai começar do 0 e vai ate o 5(4)
frase[:5]#Sendo Assim C,U,R,S,O

#outra forma ( vou para de repetir isso ja)
#voce ja deve saber a esse ponto oq isso significa... nao? ok vamos la, significa que ele vai começar a mostrar do 15 caracter ate o final, mas dessa vez sem excluir nada ja que so exclui na hora de parar e nao começar
frase[15:]#Sendo assim P,Y,T,H,O,N

#Ele começa no 9 e pula de 3 em 3
frase[9::3]#Sendo assim V,E,P,H

#Analise

#ve o tamanho da frase e quantos caracteres ele ocupa
len(frase)#No caso 21 caracteres

#Vai contar quantas daquela letra mencionada tem no caso o (e tem que dizer se quer maiuscula ou minuscula, nesse caso ele so conta os o minusculo se quisesse o grande tinha que ser 'O' e fosse os 2 juntos, 'O,o')
frase.count('o')#Sendo 3 nessa frase

#Vai contar quanto o tem ja com fatiamento(Ou seja so vai contar do 0 ate o 13 que é 12)
frase.count('o',0,13)#Sendo assim so tem 1

#ele encontra a primeira ocorrencia da letra/frase
frase.find()

#Msotrando a ultima vez que foi encontrado aquela letra/frase
frase.rfind()

#ele vai procurar a frase android na frase
frase.find('android')#Não encontrará nenhuma e ele retornara -1 (ou seja ele ta dizendo que nao existe)

#Voce pergunta se existe essa palavra na frase
'Curso' in frase#nesse caso, sim existe a palavra curso na frase

#Transformação

#Voce pede para ele trocar a palavra python com android
frase.replace('pytho','android')#Ficaria assim: Curso em Video Android

#ele transforma as palavras em maiusculo(o que ja for, continua em maiusculo)
frase.upper()#Sendo assim ficaria: CURSO EM VIDEO PYTHON

#é literalmente ao contrario do upper, ele mantem oq esta minusculo e oq nao, fica em maiusculo
frase.lower()#Sendo assim ficaria:curso em video python

#ele joga todos os caracteres para minusculo e joga a primeira letra para maisuculo
frase.capitalize()#Sendo assim ficaria:Curso em video python

#ele da uma lida na frase para descobri onde tem letra e onde começa e termina uma frase( ele faz essa conta pela quantidade espaços)e vai deixar todas as primeiras letras em maiusculo
frase.title()#Sendo assim ficaria:Curso Em Video Python


#Mudando de frase
frase = '   Aprenda Python   '#os espaços sao propositais

#ele remove todos os espaços inuteis, tanto no inicio quanto no final da string, os espaços do meio ele mantém
frase.strip()#Ajeitando a palavra para 'Aprenda Python'

#ele remove somente os ultimos espaços(o da direita)
frase.rstrip()#Sendo assim fica: '   Aprenda Python'

#mesma coisa mas gaora removendo os espaços so da esquerda(os inicias)
frase.lstrip()#Sendo assim ficaria:'Aprenda Python   '


#Voltando a string normal agora ('Curso em Video python)

#Divisão

#ele dividi a palavra e gera uma lista para cada nova palavra
frase.split()#Sendo assim ficaria: ['Curso', 'Em', 'Video','Python']

#vc pode colocar o split em uma variavel e depois so pedi uma frase em especifico ou ate uma letra daquela frase
dividido = frase.split()
print(dividido[2],[2])#Aqui sendo a 3 frase com [2] lembrando que começa no 0 e a 3 letra co [2] lembrando dnv que começa no 0

#Junção

#voce usa todos os elementos da frase, juntando-os e gerando um - entre as palavras
'-'.join(frase)#ou seja ficaria: Curso-em-Video-python


