from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\n{max(numeros)} é o maior número e {min(numeros)} é o menor número')
