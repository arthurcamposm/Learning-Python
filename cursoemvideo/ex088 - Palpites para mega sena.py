from time import sleep
from random import randint
print('-' * 30)
print('      JOGA NA MEGA SENA')
print('-' * 30)
qnt_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {qnt_jogos} JOGOS =-=-=-')
sleep(1.25)
lista = list()
jogos = list()
tot = 1
while tot <= qnt_jogos:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(0.5)