nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota1 + nota2)/2
if media < 5:
    print("REPROVADO")
elif 5 <= media <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")
