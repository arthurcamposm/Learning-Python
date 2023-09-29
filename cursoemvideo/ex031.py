d = int(input('Qual a distancia da viagem em Km? '))
if d <= 200:
    p = 0.5 * d
else:
    p = 0.45 * d
print(f'O preço da passagem ficou {p} reais')