pn = float(input('Digite o preço normal do produto: '))
print('Digite [1] para pagar à vista cheque/dinheiro\n'
      'Digite [2] para pagar à vista no cartão\n'
      'Digite [3] para pagar em 2x no cartão\n'
      'Digite [4] para pagar em 3x ou mais no cartão')
cp = int(input('Digite a condição de pagamento: '))
if cp == 1:
    vp = pn - pn * 10/100
    print(f'O valor a ser pago será R${vp:.2f}')
elif cp == 2:
    vp = pn - pn * 5/100
    print(f'O valor a ser pago será R${vp:.2f}')
elif cp == 3:
    mens = pn / 2
    print(f'O valor a ser pago será R${pn:.2f} e será dividido em 2x de R${mens:.2f}')
elif cp == 4:
    parc = int(input('Quantas parcelas vão ser? '))
    vp = pn + 20/100 * pn
    mens = vp / parc
    print(f'Sua compra será parcelada em {parc}x de R${mens:.2f} com Juros.\n'
          f'Sua compra de R${pn:.2f} vai custa R${vp:.2f} no final.')
