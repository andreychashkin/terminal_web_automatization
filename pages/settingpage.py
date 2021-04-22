from pages.basepage import BasePage
from locators.SettingLocator import SettingLocator, SettingLocatorNdi, SettinglocatorScreenSave, SettingLocatorTerminal
from locators.MainLocator import MainLocator
import default_settings, time

class SettingPage(BasePage):

    #метод проверки наличия в списке хотя бы одной камеры
    def search_ndi(self):
        self._open('system/settings')
        self._click(SettingLocator.NDI)
        return self._search_element(SettingLocatorNdi.NDI_CAM)

    # метод установки роли камере
    def set_role_ndi(self, role):
        self._click(SettingLocatorNdi.NDI_CAM)
        if role == 'star':
            self._click(SettingLocatorNdi.NDI_STAR_LABEL)
        elif role == 'presentation':
            self._click(SettingLocatorNdi.NDI_PREZENATION_LABEL)
        self._click(SettingLocatorNdi.NDI_SUBMIT_BUTTON)
        time.sleep(5)
        return

    # метод проверки установленной роли
    def result_set_role_ndi(self, role):
        if role == 'star':
            return self._search_element(SettingLocatorNdi.NDI_ICON_STAR)
        elif role == 'presentation':
            return self._search_element(SettingLocatorNdi.NDI_ICON_PRESENTATION)
        return False

    # метод загрузки картинки
    def download_image(self, input):
        self._open('system/settings')
        self._click(SettingLocator.SCREENSAVE)
        self._click(SettinglocatorScreenSave.DOWNLOAD_BUTTON)
        self._input(SettinglocatorScreenSave.INPUT_FILE, lstr=input)
        self._click(SettinglocatorScreenSave.SUBMIT_BUTTON)
        return

    # метод удаления картинки
    def dell_image(self):
        try:
            while True:
                self._open('system/settings')
                self._click(SettingLocator.SCREENSAVE)
                self._click(SettinglocatorScreenSave.DELL_IMAGE)
                alert = self.driver.switch_to_alert()
                alert.accept()
        except:
            return

    # метод проверки загруженной картинки
    def search_image(self):
        try:
            text = self._text(SettinglocatorScreenSave.ALLERT)
            text = text.split("×\n")[1]
            if text == 'Изображение успешно загружено.' and self._search_element(SettinglocatorScreenSave.IMAGE) == True:
                return True
            return False
        except:
            return False

    #метод поиска сообщения о ошибке загрузки
    def search_err_image(self):
        text = self._text(SettinglocatorScreenSave.ERR_DOWNLOAD)
        text = text.split("×\n")[1]
        if text == 'Неверный файл':
            return True
        return False

    # метод выбора отключеного протокола и вызова по нему
    def off_protocol(self, locator):
        self._click(locator)
        self._click(SettingLocator.SAVE_LOCATOR_BUTTON)
        self._open('')

        if locator == SettingLocatorTerminal.SIP:
            locator = "SIP"
        if locator == SettingLocatorTerminal.H323:
            locator = "H323"
        return locator