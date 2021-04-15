from pages.contactpage import ContactPage
import pytest, time, default_settings

@pytest.fixture(scope='function')
def add_contacts(browser):
    page = ContactPage(browser)
    page._open('contacts')
    yield browser
    page._open('contacts')
    page.dell_all_contacts()

@pytest.mark.parametrize('protocol', default_settings.test_protocol)
def test_add_contact(add_contacts, protocol):
    obj = ContactPage(add_contacts)
    obj.add_contact(protocol=protocol)
    assert obj.rezult(protocol=protocol) == True, "Ошибка при проверке созданного контакта"