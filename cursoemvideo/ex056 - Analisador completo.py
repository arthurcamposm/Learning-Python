soma = 0
mvelho = 0
cont = 0
nomemvelho = ''
for c in range(1, 5):
    print(f'-----{c}ª PESSOA-----')
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo: ')).strip().capitalize()
    soma += idade
    if c == 1 and sexo == 'Masculino':
        mvelho = idade
        nomemvelho = nome
    else:
        if idade > mvelho and sexo == 'Masculino':
            mvelho = idade
            nomemvelho = nome
    if idade < 20 and sexo == 'Feminino':
        cont += 1
media = soma / 4
print(f'A média de idade do grupo é {media} anos.\n'
      f'O homem mais velho se chama {nomemvelho} e tem {mvelho} anos')
if cont == 1:
    print(f'{cont} mulher tem menos de 20 anos.')
else:
    print(f'{cont} mulheres têm menos de 20 anos.')
