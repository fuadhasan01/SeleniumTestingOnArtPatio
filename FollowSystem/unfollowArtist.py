from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://localhost/Art_patio/html/login.php")
title = driver.title
driver.implicitly_wait(0.5)

email = driver.find_element(by=By.NAME, value="email")
password = driver.find_element(by=By.NAME, value="password")
submit = driver.find_element(by=By.NAME, value="create")
email.send_keys("demo1@gmail.com")
password.send_keys("1234")
submit.click()

time.sleep(2)
driver.get("http://localhost/Art_patio/html/Artist/Artists.php")
title = driver.title
driver.implicitly_wait(0.5)


buttons = driver.find_elements(by=By.CLASS_NAME, value="artistDetailBtn")
button_to_hover = buttons[2]
hover = ActionChains(driver).move_to_element(button_to_hover)
hover.perform()
wait = WebDriverWait(driver, 10)
buttons[2].click()

time.sleep(2)

unfollow = driver.find_element(By.ID, 'unfollow')

unfollow.click()

time.sleep(2)