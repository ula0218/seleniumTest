from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com.tw/?hl=zh_TW")

element = driver.find_element(By.NAME, "q")
element = driver.find_element(By.CLASS_NAME,"gLFyf")
element.send_keys("Selenium Python")
time.sleep(2) 
button = driver.find_element(By.CLASS_NAME,"gNO89b")
button.click()
time.sleep(2) 
driver.quit()