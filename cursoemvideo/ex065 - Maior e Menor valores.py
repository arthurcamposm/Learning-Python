contin = 'sim'
soma = 0
cont = 0
maior = 0
menor = 0
while contin == "sim":
    n = int(input('Digite um número inteiro: '))
    contin = str(input('Você quer continuar? ')).lower().strip()
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print(f'A média de todos os números digitados é {media}, o maior número é {maior} e o menor número é {menor}')

