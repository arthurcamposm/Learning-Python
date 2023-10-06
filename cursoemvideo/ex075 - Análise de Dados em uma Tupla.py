n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
numeros = (n1, n2, n3, n4)
print(f"A quantidade de noves é {numeros.count(9)}")
if 3 in numeros:
    print(f'A posição do primeiro três é {numeros.index(3)}')
print('Os números pares foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')