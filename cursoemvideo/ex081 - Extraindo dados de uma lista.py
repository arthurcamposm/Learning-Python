lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    contin = str(input('Você quer continuar? [S/N] ')).upper()
    if contin == 'N':
        break
lista.sort(reverse=True)
print(f'{len(lista)} números foram digitados\nOs valores em ordem decrescente são {lista}')
if 5 in lista:
    print('O número 5 está na lista.')