# TaxHub Bot - Monitoramento e Alertas

Este projeto consiste em um bot para monitoramento automático da API TaxHub, com envio de alerta por e-mail em caso de resposta inesperada. Todas as credenciais e configurações sensíveis são carregadas via arquivo `.env` para maior segurança e flexibilidade.

## Funcionalidades

- Consome a API TaxHub periodicamente ou sob demanda.
- Verifica se a resposta é igual ao padrão esperado.
- Caso a resposta seja diferente do esperado, envia um alerta por e-mail.
- Mantém registro (log) local das verificações e dos alertas enviados.

---

## Estrutura
.
├── consumir_taxhub.py # Função para consumir a API TaxHub
├── send_mail.py # Função para envio de e-mails
├── bot.py # Orquestrador: chama os módulos, faz verificações e logging
├── .env # Variáveis sensíveis de ambiente (NÃO versionar)
├── bot_taxhub.log # Log local das operações (gerado automaticamente)


---

## Configuração

### 1. Instale as dependências

```sh
pip install -r requeriments.txt
```

### 2. Configure o arquivo .env
- Crie um arquivo .env na raiz do projeto com o seguinte conteúdo, personalizando conforme necessário:

```sh
TAXHUB_URL=http://192.168.1.2:8189/atosdata/TaxCalc
TAXHUB_AUTHORIZATION=Basic <SEU_TOKEN_AQUI>

SMTP_SSL_HOST=mail.cafeutam.com.br
SMTP_SSL_PORT=465
SMTP_USERNAME=utambot@cafeutam.com.br
SMTP_PASSWORD=<SENHA_SUA>
SMTP_FROM_ADDR=ubot@cafeutam.com.br

ALERTA_EMAILS=email1@dominio.com,email2@dominio.com
```

### 3. Ajuste os destinatários de alerta.
- Edite o campo ALERTA_EMAILS para os responsáveis pelo monitoramento.

## Uso
- Execute o bot manualmente:
```sh
python bot.py
```
- Você pode agendar execuções periódicas (por exemplo, com cron no Linux ou Agendador de Tarefas no Windows).

## Logs
- O arquivo bot_taxhub.log registra todas as verificações realizadas, com data e hora, bem como os alertas enviados.

## Dependências
- requests
- python-dotenv
- Python 3.10+