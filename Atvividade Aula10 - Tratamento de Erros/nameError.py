try:
    nome = int(input("Digite um nome: "))
    print(nome) #quando não tem a variavel"NOME"
except NameError:
    print("Não tem como, Chamar uma variavel que não existe")