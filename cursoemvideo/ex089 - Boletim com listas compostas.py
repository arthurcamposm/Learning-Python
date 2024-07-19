boletim = list()
while True:
    nome = input('Nome: ')
    nota_1 = float(input('Primeira nota: '))
    nota_2 = float(input('Segunda nota: '))
    media = (nota_1 + nota_2) / 2
    boletim.append([nome, [nota_1, nota_2], media])
    resposta = input('Quer continuar? [S/N] ').upper()
    if resposta == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(boletim):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    numero_aluno = (input('Você quer ver as notas de qual aluno? (999 interrompe) '))
    if numero_aluno == 999:
        break
    if numero_aluno <= len(boletim) - 1:
        print(f'Notas de {boletim[numero_aluno][0]} são {boletim[numero_aluno][1]}')
