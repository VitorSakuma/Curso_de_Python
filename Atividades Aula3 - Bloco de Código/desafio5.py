# #DESAFIO 05

# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.



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

print(ab)
print(ac)
print(bc)


if (ab>reta3) and (ac>reta2) and (bc>reta1):
    print("é um triangulo")
else:
    print("não é um triangulo")
