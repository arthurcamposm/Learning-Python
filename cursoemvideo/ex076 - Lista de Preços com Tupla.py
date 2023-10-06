listagem = ('Lápis', 1.75
            , 'Borracha', 2
            , 'Caderno', 15.9
            , 'Estojo', 25
            , 'Transferidor', 4.2
            , 'Compasso', 9.99
            , 'Mochila', 120.32
            , 'Canetas', 22.3
            , 'Livro', 34.9)
print('=' * 39)
print(f'{"LISTAGEM":^39}')
print('=' * 39)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R$ {listagem[pos]:>6.2f}')
print('=' * 39)