from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("http://localhost/Art_patio/html/signup.php")
title = driver.title
driver.implicitly_wait(0.5)



name = driver.find_element(by=By.NAME, value="name")
email = driver.find_element(by=By.NAME, value="email")
password = driver.find_element(by=By.NAME, value="password")
cpassword = driver.find_element(by=By.NAME, value="cpassword")
address = driver.find_element(by=By.NAME, value="address")
contact = driver.find_element(by=By.NAME, value="contact")
description = driver.find_element(by=By.NAME, value="description")
userImg = driver.find_element(by=By.NAME, value="image-upload")
userType = driver.find_element(by=By.NAME, value="user_type")
dropdown = Select(userType)
submit = driver.find_element(by=By.NAME, value="create")


name.send_keys("Dhaka Gallery"); time.sleep(1)
email.send_keys("dhakaGallery@gmail.com"); time.sleep(1)
password.send_keys("1234"); time.sleep(1)
cpassword.send_keys("1234"); time.sleep(1)
address.send_keys("Dhaka"); time.sleep(1)
contact.send_keys("01711111111"); time.sleep(1)
description.send_keys("I sign up as an Gallary owner"); time.sleep(1)
path="C:/Users/labib/OneDrive/Desktop/Selenium/dhakaGallery.jpg"
userImg.send_keys(path)
dropdown.select_by_index(2)
submit.click()
time.sleep(3)
driver.quit()