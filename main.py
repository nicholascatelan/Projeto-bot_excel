#Bot Excel
'''
-A PLANILHA UTILIZADA NÃO PODE CONTER A PRIMEIRA COLUNA E LINHA EM BRANCO

-CASO APARECER POP UP NA JANELA DO WHATSAPP WEB, FECHAR PARA PODER EXECUTAR PERFEITAMENTE

-CUIDADO NO TEMPO DE ESPERA CASO AUMENTAR PODE CORRER RISCOS DE BANIMENTO DO WHATSAPP
'''

#Bibliotecas usadas 
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
from urllib.parse import quote
import time


# Ler a planilha
df = pd.read_excel(r'')   # <------ por endereço da planilha

# Padronizar colunas
df.columns = df.columns.str.strip().str.lower()

# Inicializar o navegador
driver = webdriver.Chrome()   

# Acessar o WhatsApp Web
driver.get('https://web.whatsapp.com')
input('Escaneie o QR Code e pressione Enter para continuar...')

# Iterar sobre os contatos da planilha
for index, row in df.iterrows():
    nome = row['nome']
    telefone = f"+{int(row['telefone'])}"
    data_vencimento = pd.to_datetime(row['data de vencimento']).date()
    valor= row['valor']
    

    # Lógica das mensagens
    hoje = pd.Timestamp.today().date()
    dias_para_vencimento = (data_vencimento - hoje).days
    
    
    #Mensagem de vencimento
    if dias_para_vencimento < 0:
        mensagem = f"Frase desejada"
    #mensagem de vencimento do dia    
    elif dias_para_vencimento == 0:
        mensagem = f"Frase desejada"
    #mensagem de aviso previo     
    elif dias_para_vencimento == 2:
        mensagem = f"Frase desejada"
    else:
        # Se está em dia e não precisa mandar mensagem, pula para o próximo contato
        print(f"pular")
        continue
    
    # atualizando usuario do que esta sendo feito!    
    print(f"\nEnviando para {nome} ({telefone}):\n {mensagem}\n")

    # Codificar a mensagem para URL
    mensagem_codificada = quote(mensagem)

    # Montar URL para envio
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={mensagem_codificada}"

    # Acessar o link do contato
    driver.get(link)
    time.sleep(12)  # Aguarda carregar a conversa (ajuste se a internet for lenta)

    try:
        # Clicar no botão de enviar
        campo_mensagem = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        campo_mensagem.send_keys(Keys.ENTER)
        print(f"Mensagem enviada para {nome}")
    except Exception as e:
        print(f"Não foi possível enviar para {nome}: {e}")

   #!!! PAUSA ENTRE AS MENSAGENS !!!
    time.sleep(90)#<----Segundos  

print("Mensagens enviadas para todos os contatos!")
driver.quit()