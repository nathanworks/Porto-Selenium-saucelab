from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time 

from Config import *
from Login import login
from Add_to_Cart import add_to_cart
from Checkout import checkout

# Konfigurasi opsi Chrome untuk mode headless
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=chrome_options)

# service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=chrome_options)

# driver.maximize_window()
action = ActionChains(driver)

driver.get('https://www.saucedemo.com/')

try:
    logo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'login_logo'))
    )

    print('Logo Swag Labs muncul')

except Exception as e:
    print("Elemen tidak ditemukan atau waktu tunggu habis:", e)

login(driver, username, password)
add_to_cart(driver, items, xpath_items)
checkout(driver, buyer_name, buyer_last_name, zip_code)
