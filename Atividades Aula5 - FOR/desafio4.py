#DESAFIO 04

#Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input("Digite qual a tabuada a ser feita: "))

for elemento in range (0, 11, 1):
    print(f" {tabuada} x {elemento} = {tabuada * elemento}")
    

#Professor Pedro
 
numero = int(input("Digite um numero: "))

for elemento in range (1, 11):
    resultado = elemento * numero
    print(f" {numero} * {elemento} = {resultado} ")