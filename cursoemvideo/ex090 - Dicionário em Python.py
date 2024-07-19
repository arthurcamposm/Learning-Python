dados_aluno = dict()
dados_aluno['nome'] = str(input('Nome: '))
dados_aluno['média'] = float(input('Média: '))
if dados_aluno['média'] >= 7:
    dados_aluno['situação'] = 'Aprovado'
else:
    dados_aluno['situação'] = 'Reprovado'
print(f"Nome é igual a {dados_aluno['nome']}\nMédia é igual a {dados_aluno['média']}\nSituação é igual a {dados_aluno['situação']}")