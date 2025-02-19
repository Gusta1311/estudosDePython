#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
#Entrada de Dados
print('Bem Vindo ao empréstimo Bancário.')
valor_casa = int(input("Qual o valor da sua casa?:"))
salario = int(input("Valor do salario: "))
anos = int(input("Quantas vezes: "))
#Calcular prestação e 30% do salario
meses = anos * 12
prestacao = valor_casa/ (anos * 12)
salario = salario * 0.3
print(f"A prestacao da casa foi de {prestacao:.2f} Reais, em {meses} vezes no cartão.")

if prestacao > salario:
    print("❌ Emprestimo não foi Aprovado.😔 ")
else:
    print("✅ Emprestimo Aprovado. 💸")