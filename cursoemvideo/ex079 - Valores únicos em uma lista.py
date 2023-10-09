lista = []
while True:
    numero = (int(input('Digite um número: ')))
    if numero not in lista:
        lista.append(numero)
        print('Valor adicionado com sucesso!')
    elif numero in lista:
        print('Valor duplicado! Não vou adicionar...')
    continu_programa = str(input('Quer continuar? [S/N] ')).upper()
    if continu_programa == 'N':
        break
print('Você digitou os valores: ', end='')
for valores in sorted(lista):
    print(valores, end=' ')