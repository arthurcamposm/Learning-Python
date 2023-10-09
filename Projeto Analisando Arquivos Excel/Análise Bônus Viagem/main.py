import pandas as pd
from twilio.rest import Client

account_sid = "AC80bc9bf30bb49df0c02813dd5f58173a"
auth_token = "b89a6554c98bc2aa017da5833a296bbf"

client = Client(account_sid, auth_token)


lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Abrir os 6 arquivos em excel

# Para cada arquivo, verificar se algum valor na coluna vendas no arquivo é maior que 55.000
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to="xxxxxxxxxxxxx",
            from_="+12512552771",
            body=f"Olá {vendedor}! Você ganhou uma bonificação de uma viagem por ter vendido R${vendas}"
                 f" no mês de {mes}!")

        print(message.sid)
# Se for maior do que 55.000 -> Envia um SMS com o nome, o mes e as vendas do vendedor
