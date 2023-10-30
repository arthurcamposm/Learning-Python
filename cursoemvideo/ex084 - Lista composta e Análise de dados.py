lista = list()
pessoas = list()
tot_pessoas = 0
maior_peso = 0
menor_peso = 0
while True:
    lista.append(str(input('Digite o nome da pessoa: ')))
    peso = float(input('Digite o peso da pessoa: '))
    lista.append(peso)
    pessoas.append(lista[:])
    lista.clear()
    tot_pessoas += 1
    if tot_pessoas == 1:
        maior_peso = menor_peso = peso
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
    while True:
        resp = str(input('Você quer continuar? [S/N] ')).upper()
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        break
mais_pesadas = list()
mais_leves = list()
for c in range(0, len(pessoas)):
    if pessoas[c][1] == maior_peso:
        mais_pesadas.append(pessoas[c][0])
    if pessoas[c][1] == menor_peso:
        mais_leves.append(pessoas[c][0])
print(f'Ao todo você cadastrou {tot_pessoas} pessoas.\nO maior peso foi {maior_peso}Kg. Peso de {mais_pesadas}')
print(f'O menor peso foi {menor_peso}Kg. Peso de {mais_leves}')