

nome = input("Qual é o seu nome? ")
altura = float(input('Qual é a sua altura? '))
peso = int(input("Qual é o seu peso? "))
imc = float(peso/altura**2)
if imc < 18.5:
    print('Você está em baixo peso')
elif 18.6 <= imc < 24.9:
    print('Você está com peso normal')
elif 30 <= imc < 34.9:
    print('Você está com Obesidade grau I')
elif 35 <= imc < 39.9:
    print('Você está com obesidade grau II')
else:
    print('Você está com obesidade grau III')
print(f"O índice de massa corporal de {nome} é {imc:.2f}")

