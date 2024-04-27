from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from django.contrib.auth.models import User
from todo_app.models import Skill

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

browser = webdriver.FireFox(
    service=FireFoxService(GeckoDriverManager().install()))

browser.get('https://www.selenium.dev/documentation/')
assert 'selenium' in browser.title 

elem = browser.find_element(By.NAME, 'p')
elem.send_keys('seleniumhq' + Keys.RETURN)

browser.quit()