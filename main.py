from utils import presenceByXpath, clickableByXpath
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.by import By
import navegador
import selenium
import time

input('Aperte enter para iniciar')
browser=navegador.navegador()
input('\n\nEntre na conta e aperte enter para continuar')
print('Execução do programa\n\n')

while True:
    try:
        try:
            elem = presenceByXpath(browser, '//*[contains(text(), "preenchido")]/../a', 10)
        except selenium.common.exceptions.TimeoutException:
            elem = presenceByXpath(browser, '//*[@id="formPesquisa:tabEntidade:scrollerDaTabela_table"]/tbody/tr/td[6]')
            browser.execute_script("arguments[0].scrollIntoView();", elem)
            time.sleep(1)
            elem.click()
            elem = presenceByXpath(browser, '//*[contains(text(), "preenchido")]/../a', 10)
        browser.execute_script("arguments[0].scrollIntoView();", elem)
        print(f'Professor: {elem.text}') 
        time.sleep(1)
        elem.click()
        elem = clickableByXpath(browser, '//*[@id="formCadastro:AcaoResponderQuestionario_situacaoQueroResponder:1"]', 2000)
        elem.click()
        time.sleep(1)
    except Exception as e:
        print(f'\n!\n! Erro detectado: {e}. Deseja retomar execução?\n[Enter]: sim\n[Ctrl-C]: não')
        input('# ')
