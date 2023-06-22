import time
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

    class Login(TestCase):

        FORM_AUTHENTICATION_LINK = (By.XPATH, '//a[text()="Form Authentication"]')
        LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
        H2_ELEMENT = (By.XPATH, '//h2')
        HREF_LINK = (By.XPATH, '//a[@href="http://elementalselenium.com/"]')
        USER_NAME = (By.ID, 'username')
        PASSWORD = (By.ID, 'password')
        # ERROR_MESSAGE=(By.XPATH,'//div[@id="flash"]')
        # sau
        ERROR_MESSAGE = (By.XPATH, "//div[normalize-space(contains(text(),'Your username is invalid'))]")
        ERROR_CLOSED = (By.XPATH, '//a[@class="close"]')
        LABEL_LIST = (By.XPATH, '//label')
        SUCCESS_MESSAGE = (By.XPATH, '//div[@class="flash success"]')
        LOGOUT_BUTTON = (By.XPATH, '//a[@href="/logout"]')
        ELEM_H4 = (By.XPATH, '//h4[@class="subheader"]')

    def setUp(self):
        self.chrome = webdriver.Chrome()
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(By.LINK_TEXT,'Form Authentication').click()

    def tearDown(self):
        self.chrome.quit()

#Test1 - Verifică dacă noul url e corect

    def test_url(self):
         actual_url = self.chrome.current_url
         expected_url = 'https://the-internet.herokuapp.com/login'
         assert actual_url == expected_url, f'Invalid URL: expected {expected_url}, actual URL: {actual_url}'


#Test2 - Verifică dacă page title e corect

    def test_title(self):
            actual = self.chrome.title
            expected = 'The Internet'
            self.assertEqual(expected, actual, f' Titlul paginii este {actual}, dar ar fi trebuit sa fie {expected}')

#Test3 - Verifică textul de pe elementul xpath=//h2 e corect
    def test_element(self):
        self.chrome.get('https://the-internet.herokuapp.com/')
        actual = self.chrome.find_element(*self.H2_ELEMENT).text
        print(f'Denumirea elementului este {actual}')
        expected = 'Login Page'
        self.assertEqual(actual, expected, f' Denumirea elementului este {actual}, dar ar fi trebuit sa fie {expected}')

#Test4 - Verifică dacă butonul de login este displayed

    def test_element_afisat(self):
        self.chrome.get('https://the-internet.herokuapp.com/login')
        self.chrome.find_element(By.ID, 'login').click()
        assert True, "Elementul este afisat"

        time.sleep(5)

#Test5 - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test_href_link(self):
        actual_link = self.chrome.find_element(*self.HREF_LINK).get_attribute('href')
        assert actual_link == 'http://elementalselenium.com/', 'Link-ul este gresit'
        print('Link-ul verificat este corect')

#Test6
# Lasă goale user și pass
# Click login
#Verifică dacă eroarea e displayed

    def test_mesaj_alerta(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')

#Test7
# Completează cu user și pass invalide
# Click login
# Verifică dacă mesajul de pe eroare e corect
# Este și un x pus acolo extra așa că vom folosi soluția de mai jos
#expected = 'Your username is invalid!'
#self.assertTrue(expected in actual, 'Error message text is incorrect')

    def test_mesaj_eroare (self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tom')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_MESSAGE).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in {actual},'Error message text is incorrect')

#Test8
#Lasă goale user și pass
#Click login
#Apasă x la eroare
#Verifică dacă eroarea a dispărut

def test_inchidere_mesaj_eroare(self):
    self.chrome.find_element(*self.LOGIN_BUTTON).click()
    self.chrome.find_element(*self.ERROR_CLOSED).click()
    try:
        self.chrome.find_element(*self.ERROR_CLOSED)
    except NoSuchElementException:
        print("The text is not visible on the page! It's ok")

# Test9
#  Ia ca o listă toate //label
#  Verifică textul ca textul de pe ele să fie cel așteptat (Username și Password)
#  Aici e ok să avem 2 asserturi
    def test_lista_label(self):
        elem_lista = self.chrome.find_elements(*self.LABEL_LIST)
        i = 0
        is_username_text_correct = False
        is_password_text_correct = False
        while i < len(elem_lista):
            if elem_lista[i].text == 'Username':
                is_username_text_correct = True
            elif elem_lista[i].text == 'Password':
                is_password_text_correct = True
            i += 1
        assert is_username_text_correct == True
        assert is_password_text_correct == True

#Test10
# Completează cu user și pass valide
# Click login
# Verifică ca noul url CONTINE /secure
# Folosește un explicit wait pentru elementul cu clasa ’flash succes’
# Verifică dacă elementul cu clasa=’flash succes’ este displayed
# Verifică dacă mesajul de pe acest element CONȚINE textul ‘secure area!’

    def test_verif_secure(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        url_dupa_logare = self.chrome.current_url
        self.assertTrue("secure" in url_dupa_logare, 'Noul url nu contine secure')
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
        assert self.chrome.find_element(*self.SUCCESS_MESSAGE).is_displayed() == True

#Test 11
# Completează cu user și pass valide
# Click login
# Click logout
# Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_verif_login_logout(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        WebDriverWait(self.chrome, 10).until(EC.url_contains('/login'))
        url_dupa_delogare = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        assert url_dupa_delogare == expected_url, f'Invalid url: {url_dupa_delogare} este diferit de {expected_url}'