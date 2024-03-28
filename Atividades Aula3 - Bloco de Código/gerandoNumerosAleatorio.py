import random

nota1 = random.randint(1,10)
nota2 = random.randint(1,10)

media = (nota1 + nota2) / 2

print("Nota tirada {nota1}")
print("Nota tirada {nota2}")

if media >= 7:
    print("Aluno Aprovado")
else:
    print("Aluno Reprovado")
    
