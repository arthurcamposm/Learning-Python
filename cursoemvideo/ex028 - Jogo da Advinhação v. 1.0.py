from random import randint
from time import sleep
print('Pensando em um número de 0 a 5...')
sleep(2)
n = randint(0, 5)
a = int(input('Pronto... agora adivinhe o número: '))
if a == n:
    print('Você venceu!!!!!')
else:
    print('GAME OVER')


