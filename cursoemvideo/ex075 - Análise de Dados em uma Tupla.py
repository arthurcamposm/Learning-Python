n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))
numeros = (n1, n2, n3, n4)
pares = []
qntdnove = numeros.count(9)
for cont in range(0, len(numeros)):
    if numeros[cont] == 3:
        postres = cont
    if numeros[cont] % 2 == 0:
        pares += [numeros[cont]]
print(f"quantidade de noves é {qntdnove}, posição do primeiro três é {postres} e {pares} são os números pares")