from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def add_to_cart(driver, items, xpath_items):
    for item, xpath_item in zip(items, xpath_items):
        try:
            link_element = driver.find_element(By.ID, "add-to-cart-"+xpath_item)
            link_element.click()

            try:
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, "remove-"+xpath_item))
            )
                print("Berhasil add to cart:", item)
            except:
                print("Button Add to Cart tidak berubah menjadi Remove")
                continue
        except:
            print("Gagal add to cart:", item)
            continue

    # Pindahkan blok kode di bawah ke luar dari blok `except`
    cart_element = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_element.click()

    idx = 1
    for item in items:
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'inventory_item_name') and contains(text(), '"+item+"')]"))
            )
            print("Barang ke #"+ str(idx) +" adalah "+item)
            idx = idx+1
        except:
            print("Tidak ada "+item+" dalam cart")
            continue