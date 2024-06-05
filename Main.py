from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

from Config import *
from Login import login
from Add_to_Cart import add_to_cart
from Checkout import checkout

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
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
# checkout(driver, buyer_name, buyer_last_name, zip_code)
