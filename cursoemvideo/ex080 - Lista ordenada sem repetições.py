lista = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))

    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print(f'O número {valor} foi adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'O número {valor} foi adicionado na posição {pos} da lista...')
                break
            pos += 1
     
print(lista)