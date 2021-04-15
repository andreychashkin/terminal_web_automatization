from locators.ContactLocator import ContactLocator
from pages import BasePage
import default_settings, time

class ContactPage(BasePage):

    # метод создания контакта для теста
    def add_contact(self, number=default_settings.test_number, protocol='SIP', name=default_settings.test_name):
        self._open('contacts')
        self._click(ContactLocator.ADD_CONTACT)
        self._input(ContactLocator.NAME_CONTACT, name)
        self._select(ContactLocator.TYPE_PROTOCOL, protocol)
        self._input(ContactLocator.NUMBER, number)
        self._click(ContactLocator.BUTTON_SUBMITE)

    # проверка результата создания контакта
    def rezult(self, number=default_settings.test_number, protocol='SIP', name=default_settings.test_name):
        self._open('contacts')
        name_rezult = self._text(ContactLocator.NAME_CONTACT_REZULT)
        number_rezult = self._text(ContactLocator.NUMBER_CONTACT_REZULT)
        protocol_rezult = self._text(ContactLocator.PROTOCOL_CONTACT_REZULT)
        if name_rezult == name and number_rezult == number and protocol_rezult == protocol:
            return True
        return False

    # удаление контакта
    def dell_all_contacts(self):
        try:
            while True:
                self._click(ContactLocator.DELL_CONTACT)
                self._click(ContactLocator.DELL_CONTACT_OK)
        except:
            return