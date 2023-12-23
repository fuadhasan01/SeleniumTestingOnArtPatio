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
email.send_keys("labib.knc@gmail.com"); 
password.send_keys("1234"); 
submit.click()
time.sleep(2)
arts = driver.find_element(by=By.ID, value="arts")
arts.click()
time.sleep(2)
a_tag = driver.find_element(By.XPATH, "//div[@class='card']//a")
a_tag.click()


time.sleep(2)

buy_button = driver.find_element(By.CLASS_NAME, "buyBtn")
buy_button.click()

confirm = driver.find_element(by=By.ID, value="yesBtn")
confirm.click()

time.sleep(2)
driver.quit()