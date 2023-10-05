termo1 = float(input("Digite o primeiro termo da pa: "))
razao = float(input("Digite a razão da pa: "))
pa = 0
qnttermos = 1
novapa = 0
while pa != termo1 + (10 - 1) * razao:
    pa = pa + razao
    print(pa)
while qnttermos != 0:
    qnttermos = int(input("Você quer mostrar mais quantos termos? "))
    novapa = qnttermos * razao + pa
    while pa != novapa:
        pa = pa + razao
        print(pa)
print('Fim do Programa.')

