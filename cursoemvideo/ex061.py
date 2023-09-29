termo1 = float(input("Digite o primeiro termo da pa: "))
razao = float(input("Digite a razão da pa: "))
pa = 0
while pa != termo1 + (10 - 1) * razao:
    pa = pa + razao
    print(pa)
