from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = "chromedriver.exe"

brave_options = webdriver.ChromeOptions()
brave_options.binary_location = r"C:/Program Files/BraveSoftware/Brave-Browser/Application brave.exe"

driver = webdriver.Chrome(options=brave_options)

try:
    driver.get("http://127.0.0.1:5500/index.html")

    # Seleccionar país
    country_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "country"))
    )
    country_dropdown.click() 
    country_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//option[text()='Colombia']"))
    )
    country_option.click()

    # Ingresar ciudad
    city_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "city"))
    )
    city_input.send_keys("Medellin") 

    # Realizar la acción que desencadena la búsqueda del clima 
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "button"))
    )

    search_button.click()

    # Esperar a que la información del clima aparezca 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "clima"))
    )
    #PAusa de segundos
    time.sleep(40)
    # Tomar captura de pantalla
    driver.save_screenshot("captura_de_pantalla.png")

finally:
    driver.quit()