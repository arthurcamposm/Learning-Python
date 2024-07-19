from datetime import datetime

cadastro = dict()

cadastro['Nome'] = input("Insira o nome: ")
ano_nascimento = (int(input("Insira o ano do nascimento: ")))
cadastro['Idade'] = datetime.now().year - ano_nascimento
cadastro['CTPS'] = int(input("Insira a Carteira de Trabalho (0 não tem): "))

if cadastro['CTPS'] != 0:
    cadastro['Ano_Contratação'] = int(input("Insira o ano de contratação: "))
    cadastro['Salário'] = float(input("Insira o salário: R$ "))
    cadastro['Aposentadoria']= cadastro['Ano_Contratação'] + 35 - ano_nascimento

print(f'-=' * 30)
print(cadastro)
for k, v in cadastro.items():
    print(f'{k} tem o valor {v}')
