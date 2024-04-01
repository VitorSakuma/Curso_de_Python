#DESAFIO 03

#Crie um programa que leia duas notas entre 0 a 10 de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida.

#Média abaixo de 5.0: REPROVADO

#Média entre 5.0 a 6.9: RECUPERAÇÃO

#Média igual ou superior a 7.0: APROVADO

nota1 = float(input("Digite um numero inteiro: "))
nota2 = float(input("Digite um numero inteiro: "))

mediaAluno = (nota1 +nota2) / 2

if mediaAluno < 5.0:
    print(f"Aluno Reprovado: ")

elif mediaAluno <= 6.9:
    print(f"Aluno em Recuperação: ") 

else:
    print(f"Aluno Aprovado")
 
