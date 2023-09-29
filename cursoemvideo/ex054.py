from datetime import date
atual = date.today().year
cont = 0
cont1 = 0
for c in range(0, 7):
    anonasc = int(input('Digite o ano de nascimento: '))
    idade = atual - anonasc
    if idade >= 21:
        cont += 1
    else:
        cont1 += 1
print(f'{cont} pessoa(s) já atingiram a maioridade e {cont1} pessoa(s) ainda não atingiram a maioridade.')

