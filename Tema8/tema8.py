import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/form')

# selectare dupa ID

chrome.find_element(By.ID,'first-name').send_keys('Teodora')
chrome.find_element(By.ID,'last-name').send_keys('Socol')
chrome.find_element(By.ID,'job-title').send_keys('Coordonator logistic')

time.sleep(5)
chrome.quit()

from datetime import time

# selectare dupa link text si partial text

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/')

chrome.find_element(By.LINK_TEXT, 'Autocomplete').click()
time.sleep(3)

chrome.find_element(By.ID,'logo').click()
time.sleep(3)

chrome.find_element(By.LINK_TEXT,'Buttons').click()
time.sleep(3)

chrome.find_element(By.ID, 'logo').click()
time.sleep(3)

chrome.find_element(By.LINK_TEXT,'Datepicker').click()
time.sleep(3)

chrome.find_element(By.PARTIAL_LINK_TEXT, 'Enabled').click()
time.sleep(3)

chrome.find_element(By.ID, 'logo').click()
time.sleep(3)

chrome.find_element(By.PARTIAL_LINK_TEXT, 'Radio').click()
time.sleep(3)

chrome.find_element(By.ID, 'logo').click()
time.sleep(3)

chrome.find_element(By.PARTIAL_LINK_TEXT, 'Key').click()
time.sleep(3)

chrome.quit()

# selectare dupa name

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get('https://www.seleniumframework.com/practiceform/')
chrome.find_element(By.NAME, 'country').send_keys('Romania')
chrome.find_element(By.NAME, 'telephone').send_keys('0123456789')
chrome.find_element(By.NAME, 'message').send_keys('Blablabla')

time.sleep(3)
chrome.quit()

# pentru tag

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/form')

chrome.find_element(By.TAG_NAME, 'input').send_keys('Teodora')
time.sleep(3)
chrome.find_element(By.TAG_NAME, 'body').send_keys('radio-button')
time.sleep(3)
chrome.find_element(By.TAG_NAME, 'body').send_keys('h1')

time.sleep(3)
chrome.quit()

#pentru class name

import time
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
chrome = webdriver.Chrome()
chrome.get('https://formy-project.herokuapp.com/form')

# chrome.find_element(By.CLASS_NAME,'form-control').send_keys('FIRST_NAME_BY_CLASS')
# time.sleep(3)
# chrome.find_elements(By.CLASS_NAME,'form-control')[1].send_keys('LAST_NAME_BY_CLASS')
# time.sleep(3)
chrome.find_elements(By.CLASS_NAME,'form-control')[2].send_keys('JOB_BY_CLASS')
time.sleep(3)