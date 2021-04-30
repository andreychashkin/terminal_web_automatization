from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pytest
import time
import default_settings


@pytest.fixture()
def browser():
    link = 'https://' + default_settings.terminal_ip
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome("./chromedriver.exe", options=options)
    browser.get(link)
    time.sleep(1.5)
    lang = Select(browser.find_element(By.CSS_SELECTOR, '#language')).select_by_value('ru')
    browser.refresh()
    name = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    button = browser.find_element(By.CLASS_NAME, "form__btn")
    time.sleep(2)
    password.send_keys('123')
    name.send_keys('admin')
    button.click()
    browser.refresh()
    time.sleep(1)
    yield browser
    browser.quit()
