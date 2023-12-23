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
email.send_keys("dhakaGallery@gmail.com")
password.send_keys("1234")
submit.click()

time.sleep(2)
driver.get("http://localhost/Art_patio/html/Gallery/eventPosting.php")
title = driver.title
driver.implicitly_wait(0.5)

time.sleep(2)

eventImg = driver.find_element(by=By.NAME, value="image-upload")
eventName = driver.find_element(by=By.NAME, value="eventname")
ticketPrice = driver.find_element(by=By.NAME, value="ticektPrice")
startDate = driver.find_element(by=By.NAME, value="startDate")
startTime = driver.find_element(by=By.NAME, value="startTime")
endDate = driver.find_element(by=By.NAME, value="endDate")
endTime = driver.find_element(by=By.NAME, value="endTime")
description = driver.find_element(by=By.NAME, value="description")
post = driver.find_element(by=By.NAME, value="create")

path="C:/Users/labib/OneDrive/Desktop/Selenium/movieGallery.jpg"
eventImg.send_keys(path)
eventName.send_keys("Movie Show")
ticketPrice.send_keys("200")
startDate.send_keys("11-24-2023")
startTime.send_keys("12:30AM")
endDate.send_keys("12-30-2023")
endTime.send_keys("12:30AM")
description.send_keys("This is a movie event")
post.click()
time.sleep(2)
driver.quit()