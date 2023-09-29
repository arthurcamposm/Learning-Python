totdmaior = 0
tothom = 0
totmulmenor = 0
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = ' '
    perg = ' '
    while sexo not in 'HM':
        sexo = str(input('Digite o sexo da pessoa [H/M]: ')).upper().strip()[0]
    while perg not in 'SN':
        perg = str(input('Você quer continuar a cadastrar pessoas [S/N]? ')).upper().strip()[0]
    if perg == 'N':
        break
    if idade > 18:
        totdmaior += 1
    if sexo == 'H':
        tothom += 1
    if sexo == 'M' and idade < 20:
        totmulmenor += 1
print(f'{totdmaior} pessoas tem mais que 18 anos, {tothom} são homens e {totmulmenor} são mulheres com menos de 20 '
      f'anos')
