n = int(input('Digite um número inteiro qualquer: '))
n1 = int(input('Digite 1 para converter para binário\nDigite 2 para converter para octal\n'
               'Digite 3 para converter para hexadecimal: '))
if n1 == 1:
    print(bin(n))
elif n1 == 2:
    print(oct(n))
elif n1 == 3:
    print(hex(n))
else:
    print('número inválido')