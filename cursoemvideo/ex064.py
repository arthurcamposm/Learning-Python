n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
print(f'Você digitou {cont - 1} números e a soma desses números é {soma - 999}.')