from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def esperar_elemento(driver, by, valor, tiempo=10):
    return WebDriverWait(driver, tiempo).until(
        EC.presence_of_element_located((by, valor))
    )