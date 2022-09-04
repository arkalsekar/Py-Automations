from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as pg

url = "https://www.google.com/imghp"

driver = webdriver.Chrome(executable_path= "C:\\Users\\sulta_000\\Downloads\\Driver\\chromedriver.exe")

driver.get(url)

username = driver.find_elements_by_css_selector('input.gLFyf')
time.sleep(5)
pg.write("Programming")
time.sleep(3)
pg.press('Enter')
time.sleep(5)
image = driver.find_elements_by_id('islmp').copy()
image.save()

# username.send_keys("Programming")