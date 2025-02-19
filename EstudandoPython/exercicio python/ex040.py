#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade. Se ele ainda vai servir o exercito, se é hora de se alistar, se ja passou do tempo de se alistar. Seu programa devera tambem mostrar o tempo que ainda falta para o alistamento ou o tempo que passou.
from datetime import date
#Pegar ano atual
ano_atual = date.today().year
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print('Bem Vindo ao Alistamento Militar!')
#Solicitar nome e ano de nascimento
nome = str(input('Seu nome: '))
ano  = int(input('Seu ano de nascimento: '))
#Calcular idade
idade = ano_atual - ano
#Define idade de alistamento
ano_alistamento = 18
#Calcular diferença para dizer se ja passou ou ainda falta tempo
diferença = idade - ano_alistamento
#Verificar situação do alistamento
if idade < ano_alistamento:
    print(f'{nome} ainda não pode se alistar no exército')
    print(f'Faltam {abs(diferença)} anos para você se alistar.') #abs deixa o numero absoluto assim ,não permitindo ter número negativos quando for dizer quanto tempo falta
elif idade == ano_alistamento:
    print(f'{nome} você DEVE se alistar no exército')
else:
    print(f'{nome} você já passou do tempo de se alistar no exército.')
    print(f'Já se passaram {diferença} anos que era para você ter se alistado.')
print('Fim do Programa!')
print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
     

