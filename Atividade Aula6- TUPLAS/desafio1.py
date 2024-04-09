# DESAFIO 01

# Crie um programa que tenha uma tupla totalmente preenchida com
# uma contagem por extenso, de zero até vinte.

# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
# mostra-lo por extenso.

numerosExtenso = ("zero" , "um" , "dois" , "tres" , "quatro" , "cinco" , "seis" , "sete" , "oito" , "nove" , "dez" , "onze" , "doze" , "treze" , "quatorze" , "quinze" , "dezeseis" , "dezesete", "dezoito" , "dezenove" , "vinte").upper()

numero = int(input("Digite um numero de 0 à 20: "))

print(numerosExtenso[numero])