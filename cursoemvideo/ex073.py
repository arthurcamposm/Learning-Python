brasileirao = ('Botafogo', 'Bragantino', 'Grêmio', 'Palmeiras', 'Flamengo', 'Fluminense', 'Atlético-MG', 'Athletico-PR',
               'Fortaleza', 'São Paulo', 'Cuiabá', 'Cruzeiro', 'Corinthians', 'Internacional', 'Santos', 'Vasco',
               'Goiás', 'Bahia', 'América-MG', 'Coritiba')
print(f'Os cinco primeiros são {brasileirao[0:5]}')
print(f'Os quatro últimos são {brasileirao[16:20]}')
print(f'Em ordem alfabética: {sorted(brasileirao)}')
for cont in range(0, len(brasileirao)):
    if cont == 7:
        print(f'O {brasileirao[cont]} está na posição {cont + 1} da tabela')
