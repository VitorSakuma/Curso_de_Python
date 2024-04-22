# DESAFIO 01

# Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def calculaArea(largura, comprimento):
    area = largura * comprimento
    print(area)
    
largura = int(input("Digite a largura: "))
comprimento = int(input("Digite a comprimento: "))

calculaArea(largura,comprimento)
