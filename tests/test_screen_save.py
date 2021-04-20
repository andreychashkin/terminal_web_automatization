from pages.settingpage import SettingPage
import pytest, default_settings

@pytest.fixture(scope='function')
def open_image(browser):
    image = SettingPage(browser)
    image._open('system/settings')
    yield image
    image.dell_image()
    browser.close()

# тест загрузки изображения
def test_download_image(open_image):
    open_image.download_image(default_settings.picture)
    assert open_image.search_image() == True, "Не найдена загруженная картинка"

# тест загрузки меньшего изображения
@pytest.mark.parametrize('way', default_settings.picture_err)
def test_download_image_err(open_image, way):
    open_image.download_image(way)
    assert open_image.search_err_image() == True and open_image.search_image() == False, "Неверное изображение было загружено"