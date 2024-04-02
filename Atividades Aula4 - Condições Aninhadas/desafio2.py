#DESAFIO 02

#Escreva um programa que leia dois números inteiros e compare- os, mostrando na tela uma mensagem:

#O primeiro valor é maior

#O segundo valor é maior

#Não existe valor maior, os dois são iguais
 
valor1 = int(input("Digite um numero inteiro: "))

valor2 = int(input("Digite um numero inteiro: "))

if valor1 == valor2:
    print(f"Os valores {valor1} e {valor2} são Iguais: ")

elif valor1 > valor2:
    print(f"O primeiro valor {valor1} é maior: ")
    
else:
    print(f"O segundo 10 valor {valor2} é maior ")