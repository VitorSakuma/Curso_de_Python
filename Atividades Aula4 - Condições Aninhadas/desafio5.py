#DESAFIO 05
#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
	
#Equilátero: Todos os lados iguais
#Isósceles: Dois lados iguais
#Escaleno: Todos os lados diferentes

reta1 = int(input("Digite um numero: ")) #a
reta2 = int(input("Digite um numero: ")) #b
reta3 = int(input("Digite um numero: ")) #c

# Condições Necessárias:
# a + b > c
# a + c > b
# b + c > a

ab = reta1 + reta2
ac = reta1 + reta3
bc = reta2 + reta3


if (ab>reta3) and (ac>reta2) and (bc>reta1):
    
    if reta1 == reta2 == reta3:
        print("o triangulo formado foi um Equilatero")
        
    elif reta1 != reta2 != reta3 != reta1 :
        print("O triangulo formado foi o Escaleno")
    
    else:
        print( "O triangulo formado é p Isosceles")
    
else:
    print(f"Não é posiivel forma um triangulo")
