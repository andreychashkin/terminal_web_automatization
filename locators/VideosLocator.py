from selenium.webdriver.common.by import By

class Videoslocators:
    OPEN_ADD_VIDEO_FORM = (By.CSS_SELECTOR, "#nav-control span")
    TITLE_VIDEO = (By.CSS_SELECTOR, "#titleVideo")
    DESCRIPTION_VIDEO = (By.CSS_SELECTOR, "#descriptionVideo")
    INPUT_VIDEO = (By.CSS_SELECTOR, "#fileVideo") # в этот локатор мы должны кейсом передать путь к файлу
    ADD_VIDEO_BUTTON = (By.CSS_SELECTOR, "#addVideo")# кнопка подтверждения загрузки видео на терминал
    # удаление ролика

    OPEN_DELL_MODAL = (By.CSS_SELECTOR, "#video ul li:nth-child(2)")
    DELL_BUTTON = (By.CSS_SELECTOR, "#deleteVideoBtn")