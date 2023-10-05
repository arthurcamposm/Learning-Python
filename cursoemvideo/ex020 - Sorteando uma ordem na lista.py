import random
al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
deck = f'{al1} {al2} {al3} {al4}' .split()
random.shuffle(deck)
print(f'A ordem de apresentação será: {deck}')

