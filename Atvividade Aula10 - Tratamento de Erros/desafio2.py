# DESAFIO 02

# Escreva um programa que leia um arquivo de texto chamado
# "dados.txt" e exiba seu conteúdo. Certifique-se de lidar com o
# erro caso o arquivo não exista.

try:
    with open ("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não existe")
except ZeroDivisionError:
    print("Impossivel dividir por um numero por Zero")
finally:
    print("FIM")