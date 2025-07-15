from selenium import webdriver
from urllib.parse import quote
import pyautogui
import time

# ========= Parte Selenium =========

usuario = quote("aflconsultores@HjK#123!")
senha = quote("O#i8Lcr@Ld&bnjRh")

# Cria navegador
navegador = webdriver.Chrome()

# Acessa URL com login
navegador.get(f"https://{usuario}:{senha}@dev.aflconsultores.com.br/admin")

# Maximiza
navegador.maximize_window()

# Espera a página carregar
time.sleep(5)

# ========= Parte PyAutoGUI =========

# Espera um tempo antes de começar a automação desktop
time.sleep(2)

# Exemplo: mover mouse para posição (x, y) e clicar
# Suponha que queremos clicar em algum botão na tela, fora do navegador (ex: abrir Notepad)

# Primeiro, podemos ver a posição atual do mouse:
print(pyautogui.position())

time.sleep(3)  # Mova o mouse manualmente para onde quer clicar, e olhe no console

# Exemplo genérico: mover para x=500, y=500 e clicar
pyautogui.moveTo(500, 500, duration=0.5)
pyautogui.click()

# Exemplo: digitar algo
pyautogui.write("Testando automação desktop!", interval=0.1)

# Exemplo: apertar Enter
pyautogui.press("enter")

# ========= Continua Selenium (se quiser) =========

# Exemplo: voltar e clicar em outro botão na web
# navegador.find_element('xpath', '//*[@id="outro-botao"]').click()

# Fecha navegador
time.sleep(5)
navegador.quit()
