# DESAFIO 01

# Escreva um programa que peça ao usuário para digitar dois
# números e divida o primeiro número pelo segundo. Certifique-se
# de lidar com a possibilidade de divisão por zero.

while True:
    try:
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
    
        divisao = n1/n2
        #print(divisao)
    except ZeroDivisionError:
        print("Não existe divisão por ZERO")
    
    except ValueError:
        print("Digite um valor Numerico")
    
    else:
        print(f"O valor da divisão foi {divisao}")
        break
        
     