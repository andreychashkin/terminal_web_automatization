from pages import BasePage
from locators.MainLocator import MainLocator
import default_settings, time

class MainPage(BasePage):

    # вызов абонента
    def call(self, protokol='H323', speed=10, fps=5, number=default_settings.test_number, resolution=2,):
        self._select(MainLocator.PROTOCOL, protokol)
        self._input(MainLocator.NUMBER, number)
        self._select(MainLocator.RESOLUTION, resolution)
        self._select(MainLocator.SPEED, speed)
        self._select(MainLocator.FPS, fps)
        self._click(MainLocator.BUTTON_CALL)
        time.sleep(10)
        return

    # проверка результата вызова
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
            # resolution = resolution.split(' ')[0]
            assert resolution.find(rezolut) != -1, f"Разрешение не соответствует выбранному(выбирали: {resolution}, " \
                                                   f"получили: {rezolut} )"
        if speed != None:
            speed = int(speed)
            assert spd <= speed+100, f"Битрейт превышает максимальное допустимое значение (выбирали: {speed}," \
                                 f" получили: {spd} )"
        if fps != None:
            fps = int(fps)
            assert fps_rez <= fps, f"fps превышает максимальное допустимое значение (выбирали: {fps}," \
                                   f" получили: {fps_rez})"

    # сброс вызова и установка стандартного значения
    def call_off(self):
        self._click(MainLocator.BUTTUN_CALL_RED)
        self._click(MainLocator.BUTTUN_CALL_RED_MODAL)
        self._select(MainLocator.PROTOCOL, "H323")
        self._select(MainLocator.RESOLUTION, 3)
        self._select(MainLocator.SPEED, 10)
        self._select(MainLocator.FPS, 5)
        return True

    # вызов ролика
    def call_rolik(self):
        self._click(MainLocator.ADD_ROLIK)
        self._select(MainLocator.SELECT_ROLIK, 0)
        self._click(MainLocator.AUTO_PLAY)
        self._click(MainLocator.ADD_PLAYER_BUTTON)
        self._click(MainLocator.PLAYERS)
        self._click(MainLocator.CALL_PLAYER_BUTTON)
        return True

    # функция сверки текста локатора с эталоном
    def or_text(self, locator, etalon):
        if self._text(locator) == str(etalon):
            return True
        return False

    # удаление добавленного плеера
    def dell_player_main(self):
        try:
            self._click(MainLocator.ADD_ROLIK)
            self._select(MainLocator.SELECT_ROLIK, 0)
            self._click(MainLocator.AUTO_PLAY)
            self._click(MainLocator.ADD_PLAYER_BUTTON)
            self._click(MainLocator.PLAYERS)
            self._click(MainLocator.DELL_ROLIC_BUTTON)
            return True
        except:
            return False