while True:
    nome = input('Nome: ')
    nota_1 = float(input('Primeira nota: '))
    nota_2 = float(input('Segunda nota: '))
    resp = input('Quer continuar? [S/N] ').upper()
    if resp == 'N':
        break