import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import esperar_elemento

def hacer_login(driver):
    driver.get("https://www.saucedemo.com/")
    esperar_elemento(driver, By.ID, "user-name").send_keys("standard_user")
    esperar_elemento(driver, By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

def test_automatizacion_de_login(driver):
    hacer_login(driver)
    
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
    assert "/inventory.html" in driver.current_url
    
    titulo = esperar_elemento(driver, By.CLASS_NAME, "title").text
    assert titulo == "Products"

def test_navegacion_y_verificacion_catalogo(driver):
    hacer_login(driver)
    
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No hay productos visibles en la página"
    
    menu = esperar_elemento(driver, By.ID, "react-burger-menu-btn")
    filtro = esperar_elemento(driver, By.CLASS_NAME, "product_sort_container")
    assert menu.is_displayed()
    assert filtro.is_displayed()
    
    primer_nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_precio = driver.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"\nPrimer producto en catálogo: {primer_nombre} - {primer_precio}")
    assert primer_nombre != ""

def test_interaccion_carrito(driver):
    """Valida la interacción al agregar el primer producto al carrito."""
    hacer_login(driver)
    btn_agregar = esperar_elemento(driver, By.XPATH, "(//button[contains(@class, 'btn_inventory')])[1]")
    btn_agregar.click()    
    badge = esperar_elemento(driver, By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"