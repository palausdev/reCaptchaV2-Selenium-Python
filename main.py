import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com/recaptcha/api2/demo")

time.sleep(2)

driver.switch_to.frame(0)

driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]').click()
