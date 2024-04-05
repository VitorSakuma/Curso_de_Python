# DESAFIO 03

# Crie um programa que leia vários números inteiros pelo
# teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e o menor valores lidos. O programa
# deve perguntar ao usuário se ele quer ou não continuar a
# digitar valores

numerosInteiros = []

valorUsuario = int(input("Digite um valor: "))

continuar = input("DESEJA CONTINUAR [S/N]: ").upper()

while continuar == 'S':
    
     valorUsuario = int(input("Digite um valor: "))
    
    