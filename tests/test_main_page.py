from locators.MainLocator import StatusLocator
from pages.mainpage import MainPage
import time

def test_cpu_status(browser):
    obj = MainPage(browser)
    text1 = obj._text(StatusLocator.POWER)
    for i in range(3):
        time.sleep(3)
        text2 = obj._text(StatusLocator.POWER)
        if text1 != text2:
            return True
    assert text1 != text2,  f"Проверить обновление загрузки процессора (1: {text1}, 2: {text2})"

def test_temperature_status(browser):
    obj = MainPage(browser)
    text1 = obj._text(StatusLocator.TEMPERATURE)
    for i in range(3):
        time.sleep(3)
        text2 = obj._text(StatusLocator.TEMPERATURE)
        if text1 != text2:
            return True
    assert text1 != text2, f"Проверить обновление температуры процессора (1: {text1}, 2: {text2})"

def test_sip_status(browser):
    obj = MainPage(browser)
    assert obj.or_text(StatusLocator.SIP_REGISTRATION_STATUS, "Not registered"), "Проверить статус регистрации sip"

def test_h323_status(browser):
    obj = MainPage(browser)
    assert obj.or_text(StatusLocator.H323_REGISTRATION_STATUS, "Not registered"), "Проверить статус регистрации h323"