import pandas as pd
from twilio.rest import Client

account_sid = {{ACCOUNT_TWILLIO}}
auth_token  = {{TOKEN_TWILLIO}}

client = Client(account_sid, auth_token)

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabelas_vendas = pd.read_excel (f'{mes}.xlsx')
    if (tabelas_vendas ['Vendas'] > 55000) .any():
        vendedor = tabelas_vendas.loc [tabelas_vendas ['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabelas_vendas.loc [tabelas_vendas ['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to={{PHONE_NUMBER}},
            from_={{PHONE_NUMBER}},
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')

print(message.sid)
