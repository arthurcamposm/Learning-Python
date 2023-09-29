npedido = 0
while npedido != 5:
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
    npedido = int(input('[1] soma\n'
                        '[2] multiplica\n'
                        '[3] maior\n'
                        '[4] novos números\n'
                        '[5] sair do programa\n'
                        'Escolha uma opção: '))
    if npedido == 1:
        print(f'{n1} + {n2} é igual a {n1 + n2}')
    elif npedido == 2:
        print(f'{n1} x {n2} é igual a {n1 * n2}')
    elif npedido == 3:
        if n1 > n2:
            print(f'{n1} é o maior número')
        else:
            print(f'{n2} é o maior número')
print('Fim do Programa.')