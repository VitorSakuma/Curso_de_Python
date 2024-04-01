#DESAFIO 04

#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#AND ou OR, fazer comparação entre varios numeros

#AND, todas as condições tem que ser Verdadeiras
#OR, umas das condições tem que ser verdadeiras
#n1>n2 and n1>n3
#n2>n3 and n2>n1
#n3>n2 and n3>n1

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite um numero: "))
numero3 = int(input("Digite um numero: "))

# valida numero maior
if (numero1 > numero2) and (numero1> numero3):
    print(f"Para os numeros inseridos {numero1} , {numero2} e {numero3} o maior é {numero1}")

if (numero2 > numero3) and (numero2> numero1):
    print(f"Para os numeros inseridos {numero1} , {numero2} e {numero3} o maior é {numero2}")
    
if (numero3 > numero2) and (numero3> numero1):
    print(f"Para os numeros inseridos {numero1} , {numero2} e {numero3} o maior é {numero3}")
    
#valida numero menor
if (numero1 < numero2) and (numero1 < numero3):
    print(f"Para os numeros inseridos {numero1} , {numero2} e {numero3} o menor é {numero1}")

if (numero2 < numero3) and (numero2 < numero1):
    print(f"Para os numeros inseridos {numero1} , {numero2} e {numero3} o menor é {numero2}")
    
if (numero3 < numero2) and (numero3 < numero1):
    print(f"Para os numeros inseridos {numero1} , {numero2} e {numero3} o menor é {numero3}")
    
#CTRL D, seleciona as palavras iguais
