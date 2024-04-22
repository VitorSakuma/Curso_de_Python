try:
    with open ("data.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não existe")
except ZeroDivisionError:
    print("Impossivel dividir por um numero por Zero")
finally:
    print("FIM")