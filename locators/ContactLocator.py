from selenium.webdriver.common.by import By

class ContactLocator:
    ADD_CONTACT = (By.CSS_SELECTOR, "#nav-control ul li:nth-child(1) span")
    IMPORT_CONTACTS = (By.CSS_SELECTOR, "#nav-control ul li:nth-child(2) span")
    EXPORT_CONTACTS = (By.CSS_SELECTOR, "#nav-control ul li:nth-child(3) span")
    NAME_CONTACT = (By.CSS_SELECTOR, "[name='name']")
    TYPE_PROTOCOL = (By.CSS_SELECTOR, "[name='type']")
    NUMBER = (By.CSS_SELECTOR, "[name='number']")
    FAVORITE = (By.CSS_SELECTOR, ".form-group div")
    BUTTON_SUBMITE = (By.CSS_SELECTOR, "button[name='submit']")
    # локаторы для проверки создания контакта
    NAME_CONTACT_REZULT = (By.XPATH, "//table[@id='table']/tbody/tr[1]/td[3]")
    NUMBER_CONTACT_REZULT = (By.XPATH, "//table[@id='table']/tbody/tr[1]/td[4]")
    PROTOCOL_CONTACT_REZULT = (By.XPATH, "//table[@id='table']/tbody/tr[1]/td[5]")

    DELL_CONTACT = (By.XPATH, "//tbody/tr[1]/td[8]/a[2]/span[@class='fa fa-trash fa-custom']")
    DELL_CONTACT_OK = (By.XPATH, "//button[@class='btn btn-warning load']")

    ERROR_ADD_CONTACT = (By.CSS_SELECTOR, "#msg-add div")
