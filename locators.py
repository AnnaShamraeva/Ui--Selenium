from selenium.webdriver.common.by import By

class Locators:
    # локаторы для регистрации:
    REG_BUTTON = (By.XPATH, ".//a[@class='header__auth-link']") # Кнопка "Зарегистрироваться" 
    REG_POPUP = (By.XPATH, ".//p[@class='popup__status-message']")
    REG_EMAIL = (By.ID, 'email') #  Поле ввода почты
    REG_PASSWORD = (By.ID, 'password') #  Поле ввода пароля
    
    # локаторы для изменения аватара:
    PROFILE_IMAGE = (By.XPATH, "//div[@class='profile__image']")
    AVATAR_INPUT = (By.ID, 'owner-avatar' )
    UPDATE_AVATAR_BUTTON = (By.XPATH, "//form[@name='edit-avatar']/button[@class='button popup__button']")
    CARDS = (By.CLASS_NAME, 'card__image')