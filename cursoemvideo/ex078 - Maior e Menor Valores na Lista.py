valores = []
for posiçao in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {posiçao}: ')))
maior_valor = max(valores)
menor_valor = min(valores)
print(f'Os valores digitados foram {valores}')
print(f'O maior valor foi {maior_valor} encontrado na posição ', end='')
for posiçao, valor in enumerate(valores):
    if valor == maior_valor:
        print(posiçao, end='... ',)
print(f'\nO menor valor foi {menor_valor} encontrado na posição ', end='')
for posiçao, valor in enumerate(valores):
    if valor == menor_valor:
        print(posiçao, end='... ')