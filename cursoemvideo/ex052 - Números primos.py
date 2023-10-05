num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\033[m\nO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('Por isso esse número é primo')
else:
    print('Por isso esse número não é primo')
