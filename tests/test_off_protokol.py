import time

from locators.MainLocator import MainLocator
from pages.settingpage import SettingPage
from locators.SettingLocator import SettingLocator, SettingLocatorTerminal
import pytest
@pytest.fixture(scope='function')
def open_terminal(browser):
    obj = SettingPage(browser)
    obj._open('system/settings')
    obj._click(SettingLocator.TERMINAL)
    yield obj
    browser.close()

@pytest.mark.parametrize('protocol', [SettingLocatorTerminal.H323, SettingLocatorTerminal.SIP])
def test_off_protocol(open_terminal, protocol):
    protocol_rezult = open_terminal.off_protocol(protocol)
    open_terminal._select(MainLocator.PROTOCOL, protocol_rezult)
    open_terminal._input(MainLocator.NUMBER, "10.1.0.11")
    open_terminal._click(MainLocator.BUTTON_CALL); time.sleep(3)
    rezult = open_terminal._text(MainLocator.OFF_PROTOCOL_LABEL)

    open_terminal._open('system/settings')
    open_terminal._click(SettingLocator.TERMINAL)
    open_terminal._click(protocol)
    open_terminal._click(SettingLocator.SAVE_LOCATOR_BUTTON)
    assert rezult.find("протокол отключен в настройках устройства!") != -1, \
        f"Отсутствует сообщение о отключении протокола, отображается = ({rezult})"
