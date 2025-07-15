from selenium import webdriver
import time

#abrir o navegador
navegador = webdriver.Chrome()

#acessar um site
navegador.get("https://dev.aflconsultores.com.br/admin")

#colocar navegador em tela cheia
navegador.maximize_window()

#Selecionar um elemento na tela
navegador.find_element('')

time.sleep(10)