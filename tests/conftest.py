import pytest
import os
from selenium import webdriver

@pytest.fixture(scope="function")
def driver(request):
    opciones = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=opciones)
    driver.maximize_window()
    yield driver
    
    if request.node.rep_call.failed:
        os.makedirs("reports", exist_ok=True)
        driver.save_screenshot(f"reports/error_{request.node.name}.png")
        
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)