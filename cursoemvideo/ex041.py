from datetime import date
atual = date.today().year
ano = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - ano
if idade <= 9:
    print("CATEGORIA MIRIM")
elif 9 < idade <= 14:
    print("CATEGORIA INFANTIL")
elif 14 < idade <= 19:
    print("CATEGORIA JUNIOR")
elif 19 < idade <= 20:
    print("CATEGORIA SÊNIOR")
else:
    print("CATEGORIA MASTER")
