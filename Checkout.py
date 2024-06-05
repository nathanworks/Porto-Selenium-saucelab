from selenium.webdriver.common.by import By
import time

def checkout(driver, buyer_name, buyer_last_name, zip):
    button_co = driver.find_element(By.ID, "checkout")
    button_co.click()

    name_field = driver.find_element(By.ID, "first-name")
    name_field.send_keys(buyer_name)

    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys(buyer_last_name)

    zip_field = driver.find_element(By.ID, "postal-code")
    zip_field.send_keys(zip)

    button_continue = driver.find_element(By.ID, "continue")
    button_continue.click()

    button_finish = driver.find_element(By.ID, "finish")
    button_finish.click()
    print('Berhasil checkout')
