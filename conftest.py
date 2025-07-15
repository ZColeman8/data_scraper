import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless") 
    options.add_argument("--disable-dev-shm-usage")

    driver_path = ChromeDriverManager().install()
    if not driver_path.endswith("chromedriver"):
        raise RuntimeError(f"Unexpected driver path: {driver_path}")
    
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    yield driver
    driver.quit()