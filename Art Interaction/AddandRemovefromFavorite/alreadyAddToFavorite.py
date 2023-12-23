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
arts = driver.find_element(by=By.ID, value="arts")
arts.click()
time.sleep(2)

buttons = driver.find_elements(by=By.CLASS_NAME, value="artDetail")
button_to_hover = buttons[2]
hover = ActionChains(driver).move_to_element(button_to_hover)
hover.perform()
wait = WebDriverWait(driver, 10)
buttons[2].click()

addToFavBtn = driver.find_element(By.ID, 'favBtn')

addToFavBtn.click()

favYesBtn = driver.find_element(By.ID, 'favYesBtn')

favYesBtn.click()

time.sleep(2)
