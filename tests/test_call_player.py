from pages.mainpage import MainPage
from random import randint as rand
import pytest, time, default_settings

@pytest.fixture
def add_player():
    return