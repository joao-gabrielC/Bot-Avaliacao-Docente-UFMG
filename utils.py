import sys, os, time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def clickableByXpath(browser: webdriver, Xpath, tempoExplicity=10):
    return WebDriverWait(browser, tempoExplicity).until(EC.element_to_be_clickable((By.XPATH, Xpath)))

def presenceByXpath(browser: webdriver, Xpath, tempoExplicity=10):
    return WebDriverWait(browser, tempoExplicity).until(EC.presence_of_element_located((By.XPATH, Xpath)))
