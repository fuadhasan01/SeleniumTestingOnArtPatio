from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
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
# time.sleep(2)
driver.get("http://localhost/Art_patio/html/Artist/uploadTheArt.php")
title = driver.title
driver.implicitly_wait(0.5)
# time.sleep(2)

title = driver.find_element(by=By.NAME, value="title")
type = driver.find_element(by=By.NAME, value="type")

material = driver.find_element(by=By.NAME, value="material")
select = Select(material)
price = driver.find_element(by=By.NAME, value="price")
initialbid = driver.find_element(by=By.NAME, value="initialbid")
bidamount = driver.find_element(by=By.NAME, value="bidamount")
height = driver.find_element(by=By.NAME, value="height")
width = driver.find_element(by=By.NAME, value="width")
description = driver.find_element(by=By.NAME, value="description")
image_upload = driver.find_element(by=By.NAME, value="image-upload")

title.send_keys("Monalisa")
# time.sleep(1)
type.send_keys("Painting")
# time.sleep(1)
select.select_by_visible_text("Oil")
# time.sleep(1)
price.send_keys("2000")
# time.sleep(1)
# initialbid.send_keys("1500")
# time.sleep(1)
bidamount.send_keys("3500")
# time.sleep(1)
height.send_keys("1200")
# time.sleep(1)
width.send_keys("1200")
# time.sleep(1)
description.send_keys("This is the alternative art of Monalisa")
time.sleep(2)
# image_path = '/UploadTheArt/user.jpg/'
image_upload.send_keys(os.getcwd()+"/UploadTheArt/monalisa.jpg")
time.sleep(2)
driver.find_element(by=By.NAME, value="create").click()
time.sleep(2)
driver.quit()