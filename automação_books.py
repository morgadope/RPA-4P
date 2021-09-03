

from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time
from datetime import timedelta,datetime
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it 
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui as pg 

# Definindo Locais

locais = ["SUPERMARTKET - ALOVORADA","SUPERNARKET - BARRA OESTE","BARCELOS","CASA DO SABÃO"] # Lista que define endereços nome das lojas

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



navegador.switch_to_frame('//*[@id="iFrameResizer0"]') #select 
navegador.find_element_by_xpath('') # clicar no filtro
navegador.find_element_by_xpath('') # Selecionar o filtro

# Definindo data

#corrigir data 
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
    navegador.find_element_by_xpath('#definir xpath de text box ').send_keys(local)
    time.sleep(5)
    navegador.find_element_by_xpath('#clicar no check box do local').click()
    navegador.find_element_by_xpath('#clicar em filtrar').click()
    time.sleep(5)  
    #Enviando para dowloads
    navegador.find_element_by_xpath('#clicar em selecionar fotos').click()    #clicar em selecionar
    #podem ou não existir mais de 10 fotos
    navegador.find_element_by_xpath('#clicar em selecionar mais de 10 fotos ').click()    #clicar em selecionar
    navegador.find_element_by_xpath('#clicar em agendar books de fotos').click()    #clicar em agendar books de fotos
    time.sleep(3)
    navegador.back() # volta para pagina anterior
    navegador.switch_to_frame(0)
    time.sleep(2)
    