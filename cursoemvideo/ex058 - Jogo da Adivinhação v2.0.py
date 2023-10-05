from random import randint
from time import sleep
print('Pensando em um número de 0 a 10...')
sleep(2)
n = randint(0, 10)
x = 0
tent = 0
while x != n:
    x = int(input('Adivinhe o número: '))
    if x != n:
        print('ERROU! TENTE NOVAMENTE')
    tent += 1
if tent == 1:
    print(f'ACERTOU! DEPOIS DE {tent} TENTATIVA')
else:
    print(f'ACERTOU! DEPOIS DE {tent} TENTATIVAS')
