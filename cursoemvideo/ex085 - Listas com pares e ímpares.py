pares = list()
ímpares = list()
números = list()
números.append(pares)
números.append(ímpares)
for c in range(1, 8):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        ímpares.append(num)
pares.sort()
ímpares.sort()
print(f'Os valores pares digitados em ordem crescente são: {pares}\nOs valores ímpares digitados em ordem crescente são: {ímpares}')
