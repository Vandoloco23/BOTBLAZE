from importlib import reload
from pickle import NONE
from sqlite3 import Time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import telebot
import time
import bd
from datetime import datetime,timedelta 
import os

############################ Por informações do seu bot.##########################
api_key = '5685103429:AAGEP5thqPQ1EcX3zcWl7WZ1yXVKnZzFZ_g'  # TOKEN DO SEU BOT    
chat_id = '-1001885454057'                        
bot = telebot.TeleBot(token=api_key)
bot.send_message(chat_id=chat_id, text= ''' 🚦 BOT ATIVADO 🚦
⚪️ Proteja o Branco Pela Lista ⚪️ ''')

##################################################################################

options = webdriver.ChromeOptions()
options.add_argument('--headless')
nav = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), chrome_options=options)

nav.get('https://blaze.com/pt/games/double')
link_blaze = '[🔥 APOSTE AQUI 🔥](https://blaze.com/pt/games/double)'  # LINK DO APOSTE

def qualnum(x):
    if x == '0':
        return 0

    if x == '1':
        return 1

    if x == '2':
        return 2

    if x == '3':
        return 3

    if x == '4':
        return 4

    if x == '5':
        return 5

    if x == '6':
        return 6

    if x == '7':
        return 7

    if x == '8':
        return 8

    if x == '9':
        return 9

    if x == '10':
        return 10

    if x == '11':
        return 11

    if x == '12':
        return 12

    if x == '13':
        return 13

    if x == '14':
        return 14


def qualcor(x):
    if x == '0':
        return 'B'

    if x == '1':
        return 'V'

    if x == '2':
        return 'V'

    if x == '3':
        return 'V'

    if x == '4':
        return 'V'

    if x == '5':
        return 'V'

    if x == '6':
        return 'V'

    if x == '7':
        return 'V'

    if x == '8':
        return 'P'

    if x == '9':
        return 'P'

    if x == '10':
        return 'P'

    if x == '11':
        return 'P'

    if x == '12':
        return 'P'

    if x == '13':
        return 'P'

    if x == '14':
        return 'P'


def reset():
    bd.estrategy_name = 'TRUE'
    bd.direction_color = 'NULL'
    bd.analisar = 0
    bd.gale_atual = 0
    
################################################## WIN NO BRANCO #####################################################
def martingales():
    def very_gale(num):
        if num[0:1] == [0]:
            if bd.gale_atual == 0: 
                b = bd.Win + bd.Branco
                if(bd.Win + bd.Branco + bd.Loss)!=0:
                    a=100/(bd.Win + bd.Branco + bd.Loss)*b
                else:
                    a=0
                bd.Win_hat = (f'{a:,.2f}%') # PORCENTAGEM
                bd.Branco += 1
                bd.Branco1 += 1               
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf4pjjAVWjRRrNJnu2gK5KmVC9ekK6gACuQMAAn4cwUQtQdOVzqh2GisE')
      
                
                
                reset()
                return

            if bd.gale_atual == 1:
                bd.Branco += 1
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf4pjjAVWjRRrNJnu2gK5KmVC9ekK6gACuQMAAn4cwUQtQdOVzqh2GisE')  
          
                
                reset()
                return

            if bd.gale_atual == 2:
                bd.Branco += 1
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf4pjjAVWjRRrNJnu2gK5KmVC9ekK6gACuQMAAn4cwUQtQdOVzqh2GisE')
          
                
                reset()
                return

################################################### SE DEU WIN ##########################################################

        if num[0:1] > [0] and num[0:1] <= [7]   and bd.direction_color == '🟥':
            if bd.gale_atual == 0:
                b = bd.Win + bd.Branco
                if(bd.Win + bd.Branco + bd.Loss)!=0:
                    a=100/(bd.Win + bd.Branco + bd.Loss)*b
                else:
                    a=0
                bd.Win_hat = (f'{a:,.2f}%') # PORCENTAGEM
                bd.Win+=1
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf45jjAWF9ghaBZMGfFUlvxS13T4pmgACjwIAAszPyUSvS8rr2dknKisE')
                bot.send_message(chat_id=chat_id, text = ("✅ = %i | ⚪️ = %i | ❌ = %i | 🧮 = %s"%(bd.Win, bd.Branco, bd.Loss, bd.Win_hat)))                
                reset()
                
                return
                

            if bd.gale_atual == 1:
                b = bd.Win + bd.Branco
                if(bd.Win + bd.Branco + bd.Loss)!=0:
                    a=100/(bd.Win + bd.Branco + bd.Loss)*b
                else:
                    a=0
                bd.Win_hat = (f'{a:,.2f}%') # PORCENTAGEM
                bd.Win+=1
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf45jjAWF9ghaBZMGfFUlvxS13T4pmgACjwIAAszPyUSvS8rr2dknKisE')
                bot.send_message(chat_id=chat_id, text = ("✅ = %i | ⚪️ = %i | ❌ = %i | 🧮 = %s"%(bd.Win, bd.Branco, bd.Loss, bd.Win_hat)))
                
                reset()
                
                return
                

            if bd.gale_atual == 2:
                
                bd.Win+=1
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf45jjAWF9ghaBZMGfFUlvxS13T4pmgACjwIAAszPyUSvS8rr2dknKisE')
                bot.send_message(chat_id=chat_id, text = ("✅ = %i | ⚪️ = %i | ❌ = %i | 🧮 = %s"%(bd.Win, bd.Branco, bd.Loss, bd.Win_hat)))
                
                reset()
                
                return

            
            

        if num[0:1] >= [8] and num[0:1] <= [14] and bd.direction_color == '⬛️':
            if bd.gale_atual == 0:
                bd.Win+=1
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf45jjAWF9ghaBZMGfFUlvxS13T4pmgACjwIAAszPyUSvS8rr2dknKisE')
                bot.send_message(chat_id=chat_id, text = ("✅ = %i| ⚪️ = %i| ❌ = %i| 🧮 = %s"%(bd.Win, bd.Branco, bd.Loss, bd.Win_hat)))
                
                reset()
                
                return
            

            if bd.gale_atual == 1:
                bd.Win+=1
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf45jjAWF9ghaBZMGfFUlvxS13T4pmgACjwIAAszPyUSvS8rr2dknKisE')
                bot.send_message(chat_id=chat_id, text = ("✅ = %i | ⚪️ = %i | ❌ = %i | 🧮 = %s"%(bd.Win, bd.Branco, bd.Loss, bd.Win_hat)))
                
                reset()
                
                return
            
            if bd.gale_atual == 2:
                bd.Win+=1              
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf45jjAWF9ghaBZMGfFUlvxS13T4pmgACjwIAAszPyUSvS8rr2dknKisE')
                bot.send_message(chat_id=chat_id, text = ("✅ = %i | ⚪️ = %i | ❌ = %i | 🧮 = %s"%(bd.Win, bd.Branco, bd.Loss, bd.Win_hat)))
                reset()
                
                return

################################################## SE DEU GALE ###########################################################

        if num[0:1] >= [8] and num[0:1] <= [14] and bd.direction_color == '🟥':
            if bd.gale_atual == 0:
                bd.gale_atual += 1
                print('Vamos pro gale 1')
                #bot.send_message(chat_id=chat_id, text=''' 🚨 ATENÇÃO G1 🚨''')
                return

            if bd.gale_atual == 1:
                bd.gale_atual += 1               
                print('Vamos pro gale 2')
                #bot.send_message(chat_id=chat_id, text=''' 🚨🚨 ATENÇÃO G2 🚨🚨''')
                return

            if bd.gale_atual == 2:                
                b = bd.Win + bd.Branco
                if(bd.Win + bd.Branco + bd.Loss)!=0:
                    a=100/(bd.Win + bd.Branco + bd.Loss)*b
                else:
                    a=0
                bd.Win_hat = (f'{a:,.2f}%') # PORCENTAGEM
                bd.Loss +=1
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf5JjjAWltgL08_ovwNDjyIkEAfBmJAACvgIAAs8JwUQ0kYGUDoRZPSsE')##AQUI É LOSS
                #bot.send_message(chat_id=chat_id, text = ("✅ = %i | ⚪️ = %i | ❌ = %i | 🧮 = %s"%(bd.Win, bd.Branco, bd.Loss, bd.Win_hat)))
                print("deu loss")
                reset()
                return
    
        if num[0:1] > [0] and num[0:1] <= [7 ] and bd.direction_color == '⬛️':
            if bd.gale_atual == 0:
                bd.gale_atual += 1
                print('Vamos pro gale 1')
                #bot.send_message(chat_id=chat_id, text=''' 🚨 ATENÇÃO G1 🚨''')
                return

            if bd.gale_atual == 1:
                bd.gale_atual += 1               
                print('Vamos pro gale 2')
                #bot.send_message(chat_id=chat_id, text=''' 🚨🚨 ATENÇÃO G2 🚨🚨''')
                return 

            if bd.gale_atual == 2:               
                b = bd.Win + bd.Branco
                if(bd.Win + bd.Branco + bd.Loss)!=0:
                    a=100/(bd.Win + bd.Branco + bd.Loss)*b
                else:
                    a=0
                bd.Win_hat = (f'{a:,.2f}%') # PORCENTAGEM
                bd.Loss +=1
                bot.send_sticker(chat_id,sticker='CAACAgEAAxkBAAEBf5JjjAWltgL08_ovwNDjyIkEAfBmJAACvgIAAs8JwUQ0kYGUDoRZPSsE')## AQUI É
                #bot.send_message(chat_id=chat_id, text = ("✅ = %i | ⚪️ = %i | ❌ = %i | 🧮 = %s"%(bd.Win, bd.Branco, bd.Loss, bd.Win_hat)))
                print("deu loss")
                reset()
                return
            
    very_gale(bd.finalnum)
    return        
    

        
################################################# CHECANDO A ROLETA ##########################################################

while True:
    
    try:
        resulROOL = nav.find_element(
            By.XPATH, '//*[@id="roulette-timer"]/div[1]').text
    except NameError as erro:
        continue
    except Exception as erro:
        continue

    if resulROOL == 'Girando...':
        bd.analisar_open = 1
        print('Analisando')
        time.sleep(13)
        c = nav.page_source
        bd.resultsDouble.clear()
        os.system("cls")
        soup = BeautifulSoup(c, 'html.parser')
        go = soup.find('div', class_="entries main")
        for i in go:
            if i.getText():
                bd.resultsDouble.append(i.getText())
            else:
                bd.resultsDouble.append('0')

        bd.resultsDouble = bd.resultsDouble[:-1]

        if bd.analisar_open == 1:

            default = bd.resultsDouble[0:14]

            mapeando = map(qualnum, default)
            mapeando2 = map(qualcor, default)
            bd.finalnum = list(mapeando)
            bd.finalcor = list(mapeando2)
            print(bd.finalnum)
            print(bd.finalcor)
            print(bd.estrategy_name)    
            
######################################################### ESTRATÉGIAS #######################################################

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name == 'E1':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA PRETO-
            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:8] == ['P', 'P', 'P', 'P', 'V', 'P', 'V', 'V']:
                        bd.estrategy_name = 'E3'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E3 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if num[0:8] == ['P', 'P', 'V', 'V', 'P','P', 'V', 'V']:
                        bd.estrategy_name = 'E3'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E30 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto .
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name == 'E2':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA PRETO-

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:8] == ['V', 'V', 'P', 'P', 'V','V', 'P', 'P']:
                        bd.estrategy_name = 'E3'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E3 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if num[0:8] == ['P', 'V', 'P', 'V', 'P','V', 'P', 'V']:
                        bd.estrategy_name = 'E3'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E30 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho .
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name == 'E3':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA PRETO-

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:8] == ['V', 'P', 'V', 'P', 'V','P', 'V', 'P']:
                        bd.estrategy_name = 'E3'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E3 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if num[0:8] == ['V', 'V', 'V', 'P', 'V','V', 'V', 'P']:
                        bd.estrategy_name = 'E3'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E30 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho .
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name == 'E4':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA VERMELHO-

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:8] == ['P', 'P', 'P', 'V', 'P','P', 'P', 'V']:
                        bd.estrategy_name = 'E4'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E4 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if num[0:8] == ['V', 'V', 'P', 'V', 'V','P', 'P', 'V']:
                        bd.estrategy_name = 'E4'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E40 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name == 'E5':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA VERMELHO-

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:8] == ['P', 'P', 'V', 'P', 'P','V', 'V', 'P']:
                        bd.estrategy_name = 'E5'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E5 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if num[0:8] == ['P', 'P', 'P', 'P', 'P','P', 'P', 'P']:
                        bd.estrategy_name = 'E5'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E50 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name == 'E6':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA VERMELHO-

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:8] == ['V', 'V', 'V', 'V', 'V','V', 'V', 'V']:
                        bd.estrategy_name = 'E6'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E6 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if num[0:8] == ['P', 'P', 'P', 'P', 'V','P', 'V', 'V']:
                        bd.estrategy_name = 'E6'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E60 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION(bd.finalcor)

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name == 'E7':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA VERMELHO-

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:8] == ['P','V','P','V','P','P','P','P']:
                        bd.estrategy_name = 'E7'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E7 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if num[0:8] == ['P','V','P','P','V','B','P','P']:
                        bd.estrategy_name = 'E7'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada E70 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
🎲 Proteção no ⚪️ Branco.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION(bd.finalcor) 

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name == 'E8':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA VERMELHO-

            def CHECK_VERSION(num):

                if bd.analisar == 0:
                    if num[0:4] == ['V','V','V','V']:
                        time.sleep(60)
                        
                        return
                    if num[0:4] == ['P','P','P','P']:
                        time.sleep(60)
                        bd.analisar = 1                        
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION(bd.finalcor)   
######################################################## ESTRATÉGIAS COM 2 NÚMEROS ############################################ 
        
        if bd.estrategy_name == 'FALSE' or bd.estrategy_name ==  'D1':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0] >= 8:
                        bd.estrategy_name = 'D1'
                        bd.direction_color = '🟥'
                        bd.analisar = 1                        
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada D1 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0] <= 7:
                        bd.estrategy_name = 'D1'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1                       
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada D3 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                        
                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION() 

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name ==  'D3':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0:2] == ('4','4'):
                        bd.estrategy_name = 'D3'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada D4 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0:2] == ('5','5'):
                        bd.estrategy_name = 'D3'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada D5 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION()                             

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name ==  'D5':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0:2] == ('7','7'):
                        bd.estrategy_name = 'D5'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada D7 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0:2] == ('8','8'):
                        bd.estrategy_name = 'D5'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada D6 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION() 

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name ==  'D7':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0:2] == ('10','10'):
                        bd.estrategy_name = 'D7'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada D10 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0:2] == ('13','13'):
                        bd.estrategy_name = 'D7'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada D8 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION()     

        if bd.estrategy_name == 'FALSE' or bd.estrategy_name ==  'D9':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0:2] == ('14','14'):
                        bd.estrategy_name = 'D9'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada D9 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0:2] == ('1','0'):
                        bd.estrategy_name = 'D9'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada D10 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION()    
       
######################################################## ESTRATÉGIAS COM 1 NÚMERO ############################################

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'C1':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0] == 1 :
                        bd.estrategy_name = 'C1'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1                        
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C1 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0] == 2:
                        bd.estrategy_name = 'C1'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1                       
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C2 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                        
                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION() 

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'C3':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0] == 3:
                        bd.estrategy_name = 'C3'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C3 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0] == 4:
                        bd.estrategy_name = 'C3'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C4 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION()                             

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'C5':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0] == 5:
                        bd.estrategy_name = 'C5'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C5 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0] == 6:
                        bd.estrategy_name = 'C5'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C6 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION() 

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'C7':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0] == 7:
                        bd.estrategy_name = 'C7'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C7 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0] == 8:
                        bd.estrategy_name = 'C7'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C8 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION()     

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'C9':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0] == 9:
                        bd.estrategy_name = 'C9'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C9 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0] == 10:
                        bd.estrategy_name = 'C9'
                        bd.direction_color = '🟥'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C10 Confirmada 🚥
🎲 Entrar no: 🟥 Vermelho.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION()    

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'C11':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0] == 11:
                        bd.estrategy_name = 'C11'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C11 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0] ==12:
                        bd.estrategy_name = 'C11'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C12 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION()  

        if bd.estrategy_name == 'TRUE' or bd.estrategy_name == 'C13':   # (TRUE) ATIVADA  (FALSE) DESATIVADA -ESTRATÉGIA N°-

            def CHECK_VERSION():

                if bd.analisar == 0:
                    if bd.finalnum[0] ==13:
                        bd.estrategy_name = 'C13'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C13 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return
                    if bd.finalnum[0] == 14:
                        bd.estrategy_name = 'C13'
                        bd.direction_color = '⬛️'
                        bd.analisar = 1
                        bot.send_message(chat_id=chat_id, text=('''
🚥 Entrada C14 Confirmada 🚥
🎲 Entrar no: ⬛️ Preto.
🎲 Realizar Máximo 2 Gales.
⚪️ Check a Lista para o ⚪️.
'''f'{link_blaze}''''

'''),
    parse_mode='Markdown',
    disable_web_page_preview=True)
                        
                        return

                elif bd.analisar == 1:
                    martingales()
                    return

            checkVersion=CHECK_VERSION() 
     
######################################################## ESTRATÉGIAS LISTA DE BRANCO ############################################        
                
        

            