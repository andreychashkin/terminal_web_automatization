from pages import BasePage
from locators.MainLocator import MainLocator
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import default_settings, time

class MainPage(BasePage):

    def call(self, protokol, speed, fps, number=default_settings.test_number, resolution=2,):
        self._select(MainLocator.PROTOCOL, protokol)
        self._input(MainLocator.NUMBER, number)
        self._select(MainLocator.RESOLUTION, resolution)
        self._select(MainLocator.SPEED, speed)
        self._select(MainLocator.FPS, fps)
        self._click(MainLocator.BUTTON_CALL)
        time.sleep(10)
        return

    def call_rezult(self, protocol, number=default_settings.test_number, resolution=None, speed=None, fps=None):
        self._click(MainLocator.INFORMATION_BUTTON)
        time.sleep(10)
        # номер, протокол
        number_rez = self._text(MainLocator.NUMBER_PARTICIPANTS)
        prot, num = str(number_rez).split('/')
        # разрешение
        rezolut = (self._text(MainLocator.INFO_RESOLUTION)).split('/')[1]
        # speed
        spd = (self._text(MainLocator.INFO_SPEED)).split('/')[1]
        spd = int(spd)
        # FPS
        fps_rez = (self._text(MainLocator.INFO_FPS)).split('/')[1]
        fps_rez = int(fps_rez)
        # Закрыть окно информации
        self._click(MainLocator.INFO_BUTTON_CLOSE)
        self.call_off()
        assert (protocol == prot) and (number == num), f"протокол и номер не соответствует вызванным (вызывали: {protocol} / {number}, " \
                                                       f"получили: {prot} / {num} )"
        if resolution != None:
            #resolution = resolution.split(' ')[0]
            assert resolution.find(rezolut) != -1, f"Разрешение не соответствует выбранному(выбирали: {resolution}, " \
                                                   f"получили: {rezolut} )"
        if speed != None:
            speed = int(speed)
            assert spd <= speed, f"Битрейт превышает максимальное допустимое значение (выбирали: {speed}," \
                                 f" получили: {spd} )"
        if fps != None:
            fps = int(fps)
            assert fps_rez <= fps, f"fps превышает максимальное допустимое значение (выбирали: {fps}," \
                                   f" получили: {fps_rez})"

    def call_off(self):
        self._click(MainLocator.BUTTUN_CALL_RED)
        self._click(MainLocator.BUTTUN_CALL_RED_MODAL)
        self._select(MainLocator.PROTOCOL, "H323")
        self._select(MainLocator.RESOLUTION, 3)
        self._select(MainLocator.SPEED, 10)
        self._select(MainLocator.FPS, 5)
        return