from selenium.webdriver.common.by import By

class SettingLocator:
    NDI = (By.LINK_TEXT, 'NDI')
    SCREENSAVE = (By.CSS_SELECTOR, ".nav.nav-tabs li:nth-child(12)")
    TERMINAL = (By.CSS_SELECTOR, ".nav.nav-tabs li:nth-child(7)")
    SAVE_LOCATOR_BUTTON = (By.CSS_SELECTOR, ".col-md-12 [name='submit']")

class SettingLocatorNdi:
    NDI_SEARCH = (By.CSS_SELECTOR, "#ndiSearch")
    NDI_CAM = (By.CSS_SELECTOR, "#ndiDevices :nth-child(2) a") # первая найденная камера
    NDI_STAR_LABEL = (By.CSS_SELECTOR, "#ndiOptionsMain") # баттон роли основная
    NDI_PREZENATION_LABEL = (By.CSS_SELECTOR, "#ndiOptionsPresentation") # баттон роли презентация
    NDI_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#ndiForm [type='submit']")
    # иконки роли камер
    NDI_ICON_STAR = (By.CSS_SELECTOR, "#ndiDevices .glyphicon-star-empty")
    NDI_ICON_PRESENTATION = (By.CSS_SELECTOR, "#ndiDevices .glyphicon-circle-arrow-up")

class SettinglocatorScreenSave:
    DOWNLOAD_BUTTON = (By.CSS_SELECTOR, "#saverUploadBtn")
    INPUT_FILE = (By.CSS_SELECTOR, "#saverUploadForm input") # педать путь к файлу с картинкой для заставки
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#saverUploadForm [type='submit']") # кнопка подтверждения загрузки картинки
    ALLERT = (By.CSS_SELECTOR, "#msg div") # алерт сообщение о успешной загрузке изображения
    IMAGE = (By.CSS_SELECTOR, "#saverImages li") # первый элемент картинка
    DELL_IMAGE = (By.CSS_SELECTOR, "#saverImages .glyphicon.glyphicon-trash") # кнопка удаления картинки
    ERR_DOWNLOAD = (By.CSS_SELECTOR, "#msg-saver-upload div") # сообщение ошибки загрузки некорректного изображения

class SettingLocatorTerminal:
    SIP = (By.XPATH, "//div[3]/div[10]/div[1]")
    H323 = (By.XPATH, "//div[3]/div[11]/div[1]")