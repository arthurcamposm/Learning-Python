from random import randint
n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)
numeros = (n1, n2, n3, n4, n5)
print(numeros)
maior = sorted(numeros)[4]
menor = sorted(numeros)[0]
print(f'{maior} é o maior número e {menor} é o menor número')
