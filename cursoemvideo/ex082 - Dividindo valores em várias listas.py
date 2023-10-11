lista = list()
pares = list()
impares = list()
while True:
    numero = int(input('Digite um número: '))
    resp = str(input('Você quer continuar? [S/N] ')).upper()
    lista.append(numero)
    if resp == 'N':
        break
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print(f'Os números foram {lista}\nOs pares foram {pares}\nOs ímpares foram {impares}')