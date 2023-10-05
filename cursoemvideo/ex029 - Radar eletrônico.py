v = int(input('Velocidade do carro em Km/h: '))
m = (v - 80) * 7
if v > 80:
    print(f'Você foi multado, o valor da multa ficou {m} reais')
else:
    print('Você está dentro do limite de velocidade')
