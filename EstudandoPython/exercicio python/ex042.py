#💡 A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:Até 9 anos: MIRIM, Até 14 anos: INFANTIL, Até 19 anos: JÚNIOR, Até 20 anos: SÊNIOR, Acima: MASTER.
idade = int(input('Digite sua idade: '))
if idade <= 9:
    print('Sua categoria é a Mirim que vai até os 9 anos.')
elif 9 < idade <= 14:
    print('Sua categoria é a Infantil que vai até os 14 anos.')
elif 14 < idade <= 19:
    print('Sua categoria é a Júnior que vai até os 19 anos,')
elif 19 < idade == 20:
    print('Sua categoria é a Sênior que vai até os 20 anos. ')  
else:
    print('Sua categoria é a Master que é para pessoas acima dos 20 anos.')        