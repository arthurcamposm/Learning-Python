casa = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o salário do comprador? '))
anos = int(input('Vai pagar em quantos anos? '))
meses = anos * 12
prest = casa / meses
print(f'Você terá que pagar R${prest:.2f} por mês.')
if prest <= sal * 0.3:
    print('Empréstimo aprovado!')
else:
    print('Empréstimo negado.')