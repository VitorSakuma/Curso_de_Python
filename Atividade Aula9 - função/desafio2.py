# DESAFIO 02

# Faça um programa que tenha uma função chamada escreva(), que
# receba um texto qualquer como parâmetro e mostre uma mensagem com
# tamanho adaptável.

# Ex:

# escreva(‘Olá, mundo!!’)

# Saída

# -----------------------------------

# Olá, mundo

# -----------------------------------

# def escreva(texto):
#     print ("-" *20)
#     print(texto)
#     print ("-" *20)
    
# escreva("Olá, mundo!!!")
    
#Pedro

texto = input("Digite um texto: ")

def escreva(texto):
    tamanhoTexto = len(texto) 
    
    print ("-" *tamanhoTexto)
    print(texto)
    print ("-" *tamanhoTexto)
    
escreva(texto)