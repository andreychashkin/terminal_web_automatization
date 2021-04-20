from pages.settingpage import SettingPage
import time, pytest

@pytest.fixture(scope='function')
def open_ndi(browser):
    ndi = SettingPage(browser)
    ndi.search_ndi()
    yield ndi
    browser.close()

#тест проверки нахождения камеры
def test_search_ndi(open_ndi):
    assert open_ndi.search_ndi() == True, "Ndi камеры не найдены"

# тест назначения роли камере ndi
@pytest.mark.parametrize('role', ['star', 'presentation'])
def test_role_ndi(open_ndi, role):
    open_ndi.set_role_ndi(role)
    assert open_ndi.result_set_role_ndi(role) == True, "Роль NDI не соответствует заданной или не назначена"