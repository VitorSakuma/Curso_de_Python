prova = float(input("Digite a nota na prova do aluno 0 a 70: "))
atividade = float(input("Digite e media das noptas das atividades 0 a 30: "))

#Nota prova = 70% da media final
#Nota atividades = 30% da media final

mediaFinal = prova + atividade
print(mediaFinal)

if mediaFinal>= 50:
    print(f"Aprovado, media final igual {mediaFinal}")
elif mediaFinal>=40:
    print(f"Recuperação, media final igual a {mediaFinal}")
else:
    print(f"Reprovado, media final igual a {mediaFinal}")