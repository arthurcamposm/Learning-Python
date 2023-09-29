import time
import random
print('JOKENPÔ COM O PC')
time.sleep(1)
player = str(input('Escolha entre PEDRA, PAPEL ou TESOURA: ')).capitalize().strip()
pc = random.choice(['Pedra', 'Papel', 'Tesoura'])
print('...')
time.sleep(2)
print(f'O PC escolheu {pc}!')
time.sleep(2)
if pc == 'Pedra' and player == 'Pedra':
    print('EMPATE')
elif pc == 'Pedra' and player == 'Papel':
    print('VOCÊ GANHOU! PARABÉNS')
elif pc == 'Pedra' and player == 'Tesoura':
    print('VOCÊ PERDEU! HAHAHA')
elif pc == 'Papel' and player == 'Papel':
    print('EMPATE')
elif pc == 'Papel' and player == 'Pedra':
    print('VOCÊ PERDEU! HAHAHA')
elif pc == 'Papel' and player == 'Tesoura':
    print('VOCÊ GANHOU! PARABÉNS')
elif pc == 'Tesoura' and player == 'Tesoura':
    print('EMPATE')
elif pc == 'Tesoura' and player == 'Papel':
    print('VOCÊ PERDEU! HAHAHA')
elif pc == 'Tesoura' and player == 'Pedra':
    print('VOCÊ GANHOU! PARABÉNS')