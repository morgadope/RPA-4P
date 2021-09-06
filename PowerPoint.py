import pyautogui as pg
import time
from datetime import datetime,timedelta

data = datetime.now()
data+=timedelta(days=-1)
data = (format(data,"%d/%m/%Y"))
book_alvorada= 'Copacol Alvorada'
book_barcelos  = 'Copacol Barcelos'
book_barra = 'Copacol Barra oeste'
book_casa = 'Copacol casa do sabao'
book_compre = 'Copacol Compre mais '
book_gmap = 'Copacol Gmap'
book_guanabara = 'Copacol Guanabara'
book_pd = 'Copacol Pd Fonseca'
book_ramigos = 'Copacol Ramigos'
book_super = 'Copacol Superprix'
book_torre = 'Copacol Torre'
book_prezunic ='Copacol Prezunic'
book_obom = 'Copacol O Bom' 
book_dom = 'Copacol Dom '
book_alvo = 'Copacol Alvo Atacado'

lista_de_books  = [book_alvorada, book_barcelos, book_barra, book_casa, book_compre, book_gmap, book_guanabara, book_pd, book_ramigos, book_super,book_torre, book_prezunic, 
book_obom, book_dom, book_alvo]

#pesquisar  
time.sleep(3)
for books in lista_de_books:
  pg.press('win')
  time.sleep(1)
  pg.write(books)
  pg.press('backspace')
  time.sleep(2)
  pg.press('enter')
  #Nomear 
  time.sleep (2)
  pg.click(x=772, y=380)
  time.sleep(3)
  pg.write(books)
  pg.click(x=928, y=482)
  pg.sleep(2)
  pg.write(data)  #tema
  time.sleep(3)
  pg.click(x=259, y=48)
  time.sleep(2)
  pg.click(x=152, y=97)
  #edição
  pg.click(x=1017, y=609)
  pg.press('delete')
  #salvar arquivo
  pg.click(x=33, y=13)
  #fechar janela
  pg.click(x=1337, y=13)
  time.sleep(5)
