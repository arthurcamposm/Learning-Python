matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
soma_terc_col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if matriz[l][c] == matriz[l][2]:
            soma_terc_col += matriz[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)
print(f'A soma de todos os valores pares é {soma_pares}.\nA soma dos valores da terceira coluna é {soma_terc_col}\nO maior valor da segunda linha é {max(matriz[1])}')
