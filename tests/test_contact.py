from pages.contactpage import ContactPage
from locators.ContactLocator import  ContactLocator
import pytest, time, default_settings

@pytest.fixture(scope='function')
def add_contacts(browser):
    page = ContactPage(browser)
    page._open('contacts')
    yield browser
    page._open('contacts')
    page.dell_all_contacts()

# тест создания контакта
@pytest.mark.parametrize('protocol', default_settings.test_protocol)
def test_add_contact(add_contacts, protocol):
    obj = ContactPage(add_contacts)
    obj.add_contact(protocol=protocol)
    assert obj.rezult(protocol=protocol) == True, "Ошибка при проверке созданного контакта"

# тест создание одинаковых контактов
@pytest.mark.parametrize('protocol', default_settings.test_protocol)
def test_add_duble(add_contacts, protocol):
    obj = ContactPage(add_contacts)
    obj.add_contact(protocol=protocol)
    obj.add_contact(protocol=protocol)
    assert obj._text(ContactLocator.ERROR_ADD_CONTACT).split("×\n")[1] == "Контакт с таким номером уже существует!", "Нет ошибки при создании одинаковых контактов"
