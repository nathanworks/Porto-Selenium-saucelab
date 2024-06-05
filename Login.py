from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver, username, password):
    username_field = driver.find_element(By.ID, "user-name")
    username_field.send_keys(username)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(password)

    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Products')]"))
        )
        print("Berhasil login!")
        return True
    except:
        try:
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//h3[contains(text(),'Epic sadface: Username and password do not match any user in this service')]"))
            )
            print("Gagal login! Pesan kesalahan:", error_message.text)
        except:
            print("Gagal login karena waktu tunggu habis.")
