

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
from datetime import timedelta,datetime
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it 
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui as pg 

# Definindo Locais

locais = ["alvorada", "barra oeste ","barcelos","casa do sabao","Compre mais ", "Gmap", "Guanabara", "Padrão", "Prezunic", "Ramigos", "Superprix"," Torre"] # Lista que define endereços nome das lojas 

# Definindo navegador

navegador = webdriver.Chrome()
wdw = WebDriverWait(navegador, 10) 
navegador.get('https://4pmktcompartilhado.umov.me/CenterWeb/managementPanel/list#__main__')
navegador.maximize_window()
wdw = WebDriverWait(navegador,60)

# Tela de login"

navegador.find_element_by_xpath('//*[@id="username"]').send_keys('master')
navegador.find_element_by_xpath('//*[@id="password"]').send_keys('iq@4p')
navegador.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
time.sleep(5)

# Selecionar book de fotos


navegador.find_element_by_xpath("//a[@href='/CenterWeb/ureport']").click()

# Selecionando Filtro copacol

wdw.until(frame_to_be_available_and_switch_to_it)
navegador.switch_to_frame(0) #select 
navegador.find_element_by_xpath('//*[@id="filterPanel"]/div[1]/div[2]/div[2]/div/button/span').click() # clicar no filtro
navegador.find_element_by_xpath('//*[@id="filterPanel"]/div[1]/div[2]/div[2]/div/ul/li/a/label/input').click() # Selecionar o filtro

# Definindo data

data = datetime.now()

if datetime.today().weekday() != 0 :
    data+=timedelta(days=-1)

else:
    data+=timedelta(days=-2)
    
data = (format(data,"%d/%m/%Y"))
    
    
wdw.until(frame_to_be_available_and_switch_to_it)
navegador.switch_to_frame(0)
navegador.find_element_by_xpath('#initial-period-filter').clear()
navegador.find_element_by_xpath('#initial-period-filter').send_keys(data)
navegador.find_element_by_xpath('#final-period-filter').clear
navegador.find_element_by_xpath('#initial-period-filter').send_keys(data)

# Definindo Local

for local in locais: # para cada local fazer processo 
    navegador.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/button') # Seleciona local
    navegador.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[1]/div/input').click() # seleciona text box local
    navegador.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[1]/div/input').send_keys(local)
    Navegador.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[2]/a/label/input').click() # seleciona
    Navegador.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[2]/a/label/input').click() # tira a seleção
    Navegador.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[2]/a/label/input').click() # seleciona  novamente
    navegador.find_element_by_xpath('//*[@id="btnFilter"]').click()#clicar em filtrar
    pg.press('pagedown')
    pg.press('pagedown')
    #Enviando para dowloads 
    
    Navegador.find_element_by_xpath('//*[@id="select_photo"]') #selecionar todas as fotos 

    imagens = navegador.find_element_by_xpath('//*[@id="countSelectedImages"]')
    
    if imagens > 10 :
        navegador.find_element_by_xpath('//*[@id="select_all_images"]/a ').click() #clicar em selecionar mais de 10 fotos (todas as fotos)
        navegador.find_element_by_xpath('//*[@id="photo"]/div[2]/div[3]/div/div/button').click()  #clicar em agendar books de fotos
        time.sleep(2)
        navegador.back() # volta para pagina anterior
        wdw.until(frame_to_be_available_and_switch_to_it)
        navegador.switch_to_frame(0)
        time.sleep(2)
    
    else:    
        navegador.find_element_by_xpath('//*[@id="photo"]/div[2]/div[3]/div/div/button').click()  #clicar em agendar books de fotos
        navegador.back() # volta para pagina anterior
        wdw.until(frame_to_be_available_and_switch_to_it)
        navegador.switch_to_frame(0)
        time.sleep(2)
    