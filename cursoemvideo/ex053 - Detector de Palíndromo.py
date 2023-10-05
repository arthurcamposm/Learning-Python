frase = str(input('Digite uma frase: ')).strip().replace(' ', '').upper()
inverso = frase[::-1]
'''inverso = ''
for letra in range(len(frase) - 1, - 1, - 1):
    inverso += frase[letra] <- usando a estrutura FOR, mas nesse caso é melhor o fatiamento por ser mais enxuto'''
if inverso == frase:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')


