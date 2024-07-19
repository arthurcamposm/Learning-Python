from random import randint
from operator import itemgetter

# Montando o dicionário
jogo = {'jogador_1': randint(1, 6),
        'jogador_2': randint(1, 6),
        'jogador_3': randint(1, 6),
        'jogador_4': randint(1, 6)}

# Ordenando do maior para o menor
ranking = list()
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

# Mostrando o resultado
print(ranking)
print(jogo)
for i, v in enumerate(ranking):
    print(f'{i+1}º {v[0]}: {v[1]}')