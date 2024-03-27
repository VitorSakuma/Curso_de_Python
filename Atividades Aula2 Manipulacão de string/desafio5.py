nomeCompleto = input("Digite seu nome completo: ")

divideNome = nomeCompleto.split()
totalItem = len(divideNome)
primerioNome = divideNome[0]
ultimoNome = divideNome[-1]

print(f"o primeiro nome é {primerioNome}")
print(f"O ultimo nome é {divideNome[totalItem-1]}")
