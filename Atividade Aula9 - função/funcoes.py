def calculaArea(largura, altura):
    area = largura * altura
    print(area)
    
def calculoPerimetro (largura, altura):
    perimetro = (2*largura) + (2*altura)
    return perimetro

largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

print(calculoPerimetro(5,3))
calculaArea(altura, largura)

