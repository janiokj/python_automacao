import yfinance
import pyautogui
import pyperclip
import webbrowser
import time

ticker = input("Informe a ação de sejada. Ex. PETR4.SA:")

dados = yfinance.Ticker(ticker).history(start="2023-01-01", end="2023-12-31") # Captura o histórico de uma ação direto da base do yahoo finantial
fechamento = (dados.Close) # Nome da coluna que se quer usar
fechamento.plot() #Aqui já usa a finção plot do matplotlib

maximo = round(fechamento.max(),2) # round faz o arredondamento
minimo = round(fechamento.min(),2)
media = round(fechamento.mean(),2)

print("Maior Cotação:", maximo)
print("Menor Cotação:", minimo)
print("Média das Cotações:", media)


destinatario = "tamarawkipfer@gmail.com"
assunto = f"Cotação da Ação {ticker}"
# caso eu queira concatenar variáveis em um texto string basta digitar f no início do texto e colocar a váriáveis dentro de {chaves}
mensagem = f'''
Prezado Gerente,

Seguem as análises solicitadas da ação {ticker}:

Cotação Máxima no Período: R$ {maximo}
Cotação Mínima no Período: R$ {minimo}
Valor Médio das Cotações: R$ {media}

Dúvidas estou à disposição.

Atenciosamente,

Jânio

'''

# Abrir o navegador e ir para o gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

pyautogui.PAUSE = 2 #Define uma pausa padrão de 03 segundos antes de cada comando do pyautogui

# Clicar no botão escrever
pyautogui.click(x=80, y=252)

# Digitar o E-mail
pyperclip.copy(destinatario) # comando para copiar algo para memória do PC
pyautogui.hotkey("ctrl", "v") # Excecuta atalhos no teclado
pyautogui.hotkey("tab")

# Digitar o Assunto
pyperclip.copy(assunto) # comando para copiar algo para memória do PC
pyautogui.hotkey("ctrl", "v") # Excecuta atalhos no teclado
pyautogui.hotkey("tab")

# Digitar a Mensagem
pyperclip.copy(mensagem) # comando para copiar algo para memória do PC
pyautogui.hotkey("ctrl", "v") # Excecuta atalhos no teclado
pyautogui.hotkey("tab")

# O Gmail tem um atalho para enviar o e-mail aberto (ctrl + enter)... como ele salva o rascunho uso o shift+tab para voltar para o corpo do email
pyautogui.hotkey("shift", "tab")
pyautogui.hotkey("ctrl", "enter")

# Fechar uma aba do navegador
pyautogui.hotkey("ctrl", "f4")

print("Email enviado com sucesso.")