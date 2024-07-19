dados = dict()
dados['Nome'] = str(input("Insira o nome: "))
dados['Qnt_Partidas'] = int(input("Insira a quantidade de partidas: "))
dados['Total_Gols'] = 0
for c in range(1, dados['Qnt_Partidas'] + 1):
    dados[f'Partida_{c}'] = int(input(f'Quantidade de gols da {c}ª partida: '))
    dados['Total_Gols'] = dados['Total_Gols'] + dados[f'Partida_{c}']

print(f'-=' * 30)
print(dados)
for k, v in dados.items():
    print(f'-{k} tem o valor {v}')
