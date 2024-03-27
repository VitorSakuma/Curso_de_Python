#Faça um programa que leia uma frase pelo teclado e mostre:

frase = "Curso de Programacao em Python, Professor Pedro Miho".upper()

contaCaracter = frase.count("A")
InicioCaracter = frase.find("A")
ultimoCaracter = frase.rfind("A")

print(f"A letra A apareceu {contaCaracter} vezes")
print(f"A letra A apareceu na {InicioCaracter +1} Posição")
print(f"A letra A apareceu pela ultima vez na {ultimoCaracter +1} posição")

