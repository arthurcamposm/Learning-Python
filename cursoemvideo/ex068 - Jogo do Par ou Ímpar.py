from random import randint
from time import sleep
cont = 0
while True:
    print('=' * 10, 'JOGO DO PAR OU ÍMPAR!', '=' * 10)
    esc = ' '
    while esc not in 'pi':
        esc = str(input('Par ou Ímpar[P/I]? ')).lower().strip()
    num = int(input('Escolha um número: '))
    sleep(1)
    numpc = randint(0, 11)
    print(f'O PC escolheu \033[32m{numpc}\033[m')
    sleep(1)
    soma = num + numpc
    if soma % 2 == 0 and esc == 'i' or soma % 2 != 0 and esc == 'p':
        break
    else:
        print('Você Ganhou!')
        cont += 1
print(f'Você perdeu e ganhou {cont} consecutivas!')
