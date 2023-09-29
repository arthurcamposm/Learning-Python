cidade = input('Digite o nome de uma cidade:')
cs = cidade.upper().strip().split()
x = 'SANTO' in cs[0]
print(f'Começa com Santo? {x}')
