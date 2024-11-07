#indentação
carro.siga()
if carro.esquerda():#carro andar pela esquerda
    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
else:#se nao ele faz outro caminho
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
    carro.esquerda()
    carro.siga()
    carro.direita()
    carro.siga()
carro.pare #o carro.siga e o pare da primeira e ultima linha estao encostado pq eles sempre vao contecer os outros estao no meio pq depende cada cso e so aconteceram nos if e else de cada um se for escolhido
   
#condição booleana (sim e nao)
if carro.esquerda():
    bloco_de_comando = True
else:
    bloco_de_comando = False
    
#Programa exemplo: better-comments.tags
tempo = int(input('Quantos anos tem seu carro?: '))
if tempo <=3:
    print('Seu carro está novo.')
else:
    print('Seu carro está velho.')
print('---FIM--- ')   


 
 
    