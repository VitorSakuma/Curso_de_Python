#DESAFIO 01

#Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
#da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorCasa = float(input("Valor da Residencia a ser financiada: "))

rendaComprador = float(input("Digite a renda mensal: ")) 

tempoFinanciamento = float(input("Digite a tempo de financiamento em anos: "))



limitePrestação = 0.3

valorPrestação = (valorCasa / (tempoFinanciamento * 12))

percentualSalario = rendaComprador * limitePrestação

if(valorPrestação <= percentualSalario):
    print(f"Seu financiamento foi aprovado")

else:
    print(f"Seu financiamento não foi aprovado")