import os
import datetime
from request_taxCalc import consumir_taxhub
from eng_email import send_mail

# ALERTA_EMAILS=seu@email.com,outro@email.com # no .env

def salvar_log(texto):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('bot_taxhub.log', 'a') as f:
        f.write(f'{now} - {texto}\n')

def main():
    resultado = consumir_taxhub()
    esperado = {'itemTaxResponse': [{'id': '0', 'taxes': []}]}
    
    if resultado != esperado:
        assunto = 'Alerta TaxHub: resposta inesperada'
        corpo = f'Foi recebida uma resposta inesperada da TaxHub:\n\n{resultado}'
        # Para: ler do .env ou fixar em uma variável
        destinatarios = os.environ.get('ALERTA_EMAILS', 'seu@email.com').split(',')
        send_mail(corpo, assunto, destinatarios)
        salvar_log(f'ALERTA ENVIADO - Resposta inesperada: {resultado}')
    else:
        salvar_log('TaxHub OK - resposta esperada')

if __name__ == '__main__':
    main()