#AND

batata  = input("Você comprou batata [S/N]: ").upper()
maionese  = input("Você comprou maionese [S/N]: ").upper()


if batata == "S" and maionese == "S":
    print("TEM SALADA DE MAIONESE")
else:
    print("NÃO VAI TER MAIONESE")
