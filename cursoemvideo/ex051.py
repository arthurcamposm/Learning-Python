t1 = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
t10 = t1 + (10 - 1) * razao
for c in range(t1, t10, razao):
    print(c, end=' -> ')
print('ACABOU-SE')