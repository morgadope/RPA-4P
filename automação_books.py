from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import timedelta, datetime
from selenium.webdriver.support.expected_conditions import frame_to_be_available_and_switch_to_it
from selenium.webdriver.support.wait import WebDriverWait
import pyautogui as pg

# Definindo driver

driver = webdriver.Chrome()
wdw = WebDriverWait(driver, 10)
driver.get('https://4pmktcompartilhado.umov.me/CenterWeb/managementPanel/list#__main__')
driver.maximize_window()

# Tela de login"

driver.find_element_by_xpath('//*[@id="username"]').send_keys('master')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('iq@4p')
driver.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.ENTER)
time.sleep(5)

# Selecionar book de fotos


driver.find_element_by_xpath("//a[@href='/CenterWeb/ureport']").click()

# Selecionando Filtro copacol


driver.switch_to.frame(0)  # select
driver.find_element_by_xpath('//*[@id="filterPanel"]/div[1]/div[2]/div[2]/div/button').click()  # clicar no filtro
driver.find_element_by_xpath(
    '//*[@id="filterPanel"]/div[1]/div[2]/div[2]/div/ul/li/a/label/input').click()  # Selecionar o filtro

# Definindo data

data = datetime.now()

if datetime.today().weekday() != 0:
    data += timedelta(days=-1)

else:
    data += timedelta(days=-2)

data = (format(data, "%d/%m/%Y"))

driver.find_element_by_xpath('//*[@id="initial-period-filter"]').click()
driver.find_element_by_xpath('//*[@id="initial-period-filter"]').clear()
driver.find_element_by_xpath('//*[@id="initial-period-filter"]').send_keys(data)
driver.find_element_by_xpath('//*[@id="final-period-filter"]').click()
driver.find_element_by_xpath('//*[@id="final-period-filter"]').clear()
driver.find_element_by_xpath('//*[@id="final-period-filter"]').send_keys(data)

# Definindo Local

locais = ["alvorada", "barra oeste ", "barcelos", "casa do sabao", "Compre mais ", "Gmap", "Guanabara", "Padrão",
          "Prezunic", "Ramigos", "Superprix", " Torre"]  # Lista que define endereços nome das lojas

for local in locais:  # para cada local fazer processo
    driver.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/button').click()  # Seleciona local
    driver.find_element_by_xpath(
        '//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[1]/div/input').click()  # seleciona text box local
    driver.find_element_by_xpath('//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[1]/div/input').send_keys(local)
    time.sleep(5)
    for n in range(0, 3):
        driver.find_element_by_xpath(
            '//*[@id="filterPanel"]/div[6]/div[1]/div[2]/div/ul/li[2]/a/label/input').click()  # seleciona

driver.find_element_by_xpath('//*[@id="btnFilter"]').click()  # clicar em filtrar

for n in range(0, 2):
    pg.press('pagedown')  # para viualizar o processo de click nos botões

# Enviando para dowloads

driver.find_element_by_xpath('//*[@id="select_photo"]')  # selecionar todas as fotos

imagens = driver.find_element_by_xpath('//*[@id="countSelectedImages"]')

if imagens > 10:
    driver.find_element_by_xpath(
        '//*[@id="select_all_images"]/a ').click()  # clicar em selecionar mais de 10 fotos (todas as fotos)

driver.find_element_by_xpath(
    '//*[@id="photo"]/div[2]/div[3]/div/div/button').click()  # clicar em agendar books de fotos

time.sleep(3)
driver.back()  # volta para pagina anterior
wdw.until(frame_to_be_available_and_switch_to_it)
driver.switch_to.frame(0)
time.sleep(1)

# for n in range(0,10):
#  driver.find_element_by_xpath("#xpath download") #baixar todos os arquivos gerados
