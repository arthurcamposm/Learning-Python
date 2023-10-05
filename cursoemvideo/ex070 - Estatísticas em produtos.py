soma = 0
totmaisdemil = 0
maisbarato = 0
nomemaisb = ''
totprod = 0
while True:
    nomeprod = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: '))
    perg = ' '
    while perg not in 'SN':
        perg = str(input('Você quer continuar[S/N]? ')).upper().strip()[0]
    soma += preço
    totprod += 1
    if totprod == 1:
        maisbarato = preço
        nomemaisb = nomeprod
    else:
        if preço < maisbarato:
            maisbarato = preço
            nomemaisb = nomeprod
    if preço > 1000:
        totmaisdemil += 1
    if perg == 'N':
        break
print(f'O total gasto foi R${soma:.2f}, {totmaisdemil} produtos custaram mais que mil reais e '
      f'{nomemaisb} foi o produto mais barato.')
