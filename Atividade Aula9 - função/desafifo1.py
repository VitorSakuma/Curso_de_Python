# DESAFIO 01

# Faça um programa que tenha uma função chamada área(), que
# receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.



def calculaArea(largura, comprimento):
    area = largura * comprimento
    return area
    
largura = int(input("Digite a largura do terreno: "))
comprimento = int(input("Digite a comprimento do terreno: "))

print(f"O terreno tem {calculaArea(largura,comprimento)} m²")
