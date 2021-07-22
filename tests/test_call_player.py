from pages.videopage import VideoPage
from pages.mainpage import MainPage
import pytest


@pytest.fixture(scope='function')
def player(browser):
    page = VideoPage(browser)
    page._open("system/video")
    page.add_video()
    page._open("")
    yield browser
    page._open("system/video")
    page.dell_all_video()

# тест загрузки ролика
def test_call_player(player):
    obj = MainPage(player)
    obj.call_rolik()
    assert obj.call_off(), "Проблемы с вызовом ролика"

# тест удаления плеера
def test_dell_player(player):
    obj = MainPage(player)
    assert obj.dell_player_main() == True, "Не удалось удалить добавленный ролик"
