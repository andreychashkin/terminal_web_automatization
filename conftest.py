from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.fixture()
def browser():
    link = 'https://10.1.0.129'
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome("./chromedriver", options=options)
    browser.get(link)
    time.sleep(1.5)
    name = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    button = browser.find_element(By.CLASS_NAME, "form__btn")
    password.send_keys('123')
    name.send_keys('admin')
    button.click()
    browser.refresh()
    time.sleep(1)
    yield browser
    browser.quit()
