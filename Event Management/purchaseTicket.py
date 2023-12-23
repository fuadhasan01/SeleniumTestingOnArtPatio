from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("http://localhost/Art_patio/html/login.php")
title = driver.title
driver.implicitly_wait(0.5)

email = driver.find_element(by=By.NAME, value="email")
password = driver.find_element(by=By.NAME, value="password")
submit = driver.find_element(by=By.NAME, value="create")
email.send_keys("labib.knc@gmail.com");     
password.send_keys("1234"); 
submit.click()
time.sleep(2)

events = driver.find_element(by=By.ID, value="events")
events.click()
time.sleep(2)

buttons = driver.find_elements(by=By.CLASS_NAME, value="eventDetail")
button_to_hover = buttons[2]
hover = ActionChains(driver).move_to_element(button_to_hover)
hover.perform()
wait = WebDriverWait(driver, 10)
buttons[2].click()
time.sleep(2)
