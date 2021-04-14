from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  default_settings
import time
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def __element(self, locator, index: int):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator),
                                                        message="Элемент не найден")
        return elements[index]

    def _click(self, locator, index=0):
        return self.__element(locator, index).click()

    def _input(self, locator, lstr: str, index=0):
        self.__element(locator, index).clear()
        return self.__element(locator, index).send_keys(lstr)

    def _select(self, locator, value=None, visible_text=None):
        if type(value) == int:
            return Select(self.__element(locator, 0)).select_by_index(value)
        if type(value) == str:
            return Select(self.__element(locator, 0)).select_by_value(value)
        if visible_text is not None:
            return Select(self.__element(locator, 0)).select_by_visible_text(visible_text)
        return "Error: Невозможно выбрать эллемент"

    def _text(self, locator, index=0):
        return self.__element(locator, index).text

    def _open(self, url):
        return self.driver.open("https://" + default_settings.terminal_ip + '/' + url)
