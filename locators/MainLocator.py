from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class MainLocator:
    PROTOCOL = (By.NAME, "protocol")
    NUMBER = (By.NAME, "number")
    RESOLUTION = (By.NAME, "resolution")
    SPEED = (By.NAME, "speed")
    FPS = (By.NAME, "fps")
    BUTTON_CALL = (By.CSS_SELECTOR, ".app__btn.btn.btn-success")
    # сброс вызова
    BUTTUN_CALL_RED = (By.CSS_SELECTOR, ".app__btn.app__btn_red.btn.btn-danger")
    BUTTUN_CALL_RED_MODAL = (By.XPATH, "//button[@class='btn btn-danger']")
    #локаторы для проверки выполнения вызова
    INFORMATION_BUTTON = (By.XPATH, "//div[@class='participants__actions-left']/a[@class='btn btn-xs btn-default']")
    NUMBER_PARTICIPANTS = (By.XPATH, "//div[@id='mainStats']/table[@class='table table-striped']/tbody/tr[2]/td[2]")
    INFO_RESOLUTION = (By.XPATH, "//div[@id='mainStats']/table[@class='table table-striped']/tbody/tr[3]/td[2]")
    INFO_SPEED = (By.XPATH, "//div[@id='mainStats']/table[@class='table table-striped']/tbody/tr[6]/td[2]")
    INFO_FPS = (By.XPATH, "//div[@id='mainStats']/table[@class='table table-striped']/tbody/tr[7]/td[2]")
    INFO_BUTTON_CLOSE = (By.XPATH, "//div[@class='modal-lg modal-dialog']/div[@class='modal-content']"
                                   "/div[@class='modal-footer']/button[@class='btn btn-default']")

class MenuLocator:
    LOGO = (By.CSS_SELECTOR, "#logo")
    TERMINAL = (By.CSS_SELECTOR, "#menu :nth-child(1)")
    CONTACTS = (By.CSS_SELECTOR, "#menu :nth-child(2)")
    LOGS = (By.CSS_SELECTOR, "#menu :nth-child(3)")
    LOGS_LOGS = (By.CSS_SELECTOR, "#menu :nth-child(3) li:nth-child(1)")
    LOGS_SISTEM = (By.CSS_SELECTOR, "#menu :nth-child(3) li:nth-child(2)")
    LOGS_BAGS = (By.CSS_SELECTOR, "#menu :nth-child(3) li:nth-child(3)")
    SISTEM = (By.CSS_SELECTOR, "#menu :nth-child(4)")
    SISTEM_STATUS = (By.CSS_SELECTOR, "#menu :nth-child(4) li:nth-child(1)")
    SISTEM_VIDEO = (By.CSS_SELECTOR, "#menu :nth-child(4) li:nth-child(2)")
    SISTEM_SETTINGS = (By.CSS_SELECTOR, "#menu :nth-child(4) li:nth-child(3)")
    SISTEM_LICENCE = (By.CSS_SELECTOR, "#menu :nth-child(4) li:nth-child(4)")
    SISTEM_UPDATE = (By.CSS_SELECTOR, "#menu :nth-child(4) li:nth-child(5)")