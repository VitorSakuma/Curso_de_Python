bacalhau = input("Você comprou bacalhau [S/N]: ").upper()
sardinha = input("Você comprou sardinha [S/N]: ").upper()

if bacalhau == "S" or sardinha == "S":
    print("TEM PEIXE NA SEXTA-FEIRA SANTA")
else:
    print("NÃO VAI TER PEIXE NA SEXTA-FEIRA SANTA")
    