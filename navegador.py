import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

def navegador():
    time.sleep(2)
    #chromeOptions = webdriver.ChromeOptions()
    #prefs = {'profile.managed_default_content_settings.images':2, 
    # 'profile.default_content_setting_values.geolocation':2, 
    # 'disk-cache-size':4096}
    #chromeOptions.add_experimental_option('prefs', prefs)
    #chromeOptions.add_argument('disable-extensions')
    #chromeOptions.add_argument('disable-popup-blocking')
    #chromeOptions.add_argument('--window-size=1200,1200')
    browser = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))
    browser.get('https://sistemas.ufmg.br/aluno-grad-avaliacao/acessoquestionarios/acessarQuestionarios.seam')
    return browser
