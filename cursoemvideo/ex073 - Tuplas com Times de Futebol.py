brasileirao = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fluminense', 'Atlético-MG', 'Athletico-PR',
               'Fortaleza', 'São Paulo', 'Cuiabá', 'Cruzeiro', 'Corinthians', 'Internacional', 'Santos', 'Vasco',
               'Goiás', 'Bahia', 'América-MG', 'Coritiba')
print('-=' * 15)
print(f'Os times são {brasileirao}')
print('-=' * 15)
print(f'Os cinco primeiros são {brasileirao[0:5]}')
print('-=' * 15)
print(f'Os quatro últimos são {brasileirao[-4:]}')
print('-=' * 15)
print(f'Em ordem alfabética: {sorted(brasileirao)}')
print('-=' * 15)
print(f'O Athletico-PR está na {brasileirao.index("Athletico-PR")+1}ª posição da tabela')
print('-=' * 15)
