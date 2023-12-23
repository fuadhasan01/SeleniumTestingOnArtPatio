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
driver.get("http://localhost/Art_patio/html/purchasedtickets.php")
title = driver.title
driver.implicitly_wait(0.5)
time.sleep(2)

buttons = driver.find_elements(by=By.CLASS_NAME, value="ticket")
button_to_hover = buttons[0]
hover = ActionChains(driver).move_to_element(button_to_hover)
hover.perform()
wait = WebDriverWait(driver, 10)
buttons[0].click()

time.sleep(2)
download = driver.find_element(by=By.ID, value="download")
download.click()
time.sleep(2)

driver.quit()