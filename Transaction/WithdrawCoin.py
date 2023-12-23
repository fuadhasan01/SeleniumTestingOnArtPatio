from selenium import webdriver
from selenium.webdriver.common.by import By
import time
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
email.send_keys("labib@gmail.com");     
password.send_keys("123"); 
submit.click()
time.sleep(2)
driver.get("http://localhost/Art_patio/html/Artist/withdraw1.php")
title = driver.title
driver.implicitly_wait(0.5)
time.sleep(2)

withdeawRequest = driver.find_element(by=By.NAME, value="request1")
withdeawRequest.click()
time.sleep(2)

driver.quit()