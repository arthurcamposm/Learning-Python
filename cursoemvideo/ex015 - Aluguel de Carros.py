d = int(input('Quantos dias o carro foi usado? '))
km = int(input('O carro rodou quantos km? '))
p = d * 60 + km * 0.15
print(f'O preço a pagar pelo aluguel do carro é R${p:.2f}')
