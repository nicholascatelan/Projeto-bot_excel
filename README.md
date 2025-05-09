# 💬 Bot de Cobrança via WhatsApp com Python e Selenium

Este projeto automatiza o envio de mensagens de cobrança via WhatsApp Web usando Python, Selenium e uma planilha Excel com os dados dos clientes.

## 📋 Funcionalidades

- Leitura de dados de uma planilha Excel (`.xlsx`)
- Cálculo de dias para o vencimento do plano
- Geração personalizada de mensagens com base na data de vencimento
- Abertura automática do WhatsApp Web no navegador
- Envio automatizado das mensagens para cada contato

## 🧰 Tecnologias utilizadas

- Python 3.x 
- [Pandas]
- [Selenium]
- [Webdriver Manager]
- [ChromeDriver]


✅ Requisitos
- Python 3.10 ou superior instalado.
- Google Chrome instalado.
- Conta no WhatsApp com acesso ao WhatsApp Web.


## 🗂️ Estrutura da planilha esperada

A planilha deve conter as seguintes colunas:

| Nome           | Telefone     | Data de Vencimento | Valor     |
|----------------|--------------|---------------------|-----------|
| João da Silva  | 5511999998888| 2025-05-10           |R$ 39.90     |
| Maria Oliveira | 34123456789  | 2025-05-06           |R$ 49.90     |

⚠️ Por DDD Internacinal na parte de "Telefone" Excel junto com o numero.

> O script automaticamente padroniza os nomes das colunas (deixa tudo em minúsculas e remove espaços extras).

Como Criar ambiente virtual ---> [Ambiente Virtual](https://www.notion.so/Bot_excel-1ec3097df4af806ead86de9261f152b4?pvs=4)


## 🚀 Executando o Bot
1. Edite o código do main.py e coloque o caminho da planilha:

- df = pd.read_excel(r'C:\caminho\para\sua\planilha.xlsx')

🧼 Finalizando
- Após o envio para todos os contatos, o navegador será fechado automaticamente.

## 👥 Desenvolvedores

- [Nicholas Catealn de Góes](https://github.com/nicholascatelan)  
- [David Lucas Rodrigues Antunes](https://github.com/imdevdavi)
