from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
# driver.get(url="https://en.wikipedia.org/wiki/Main_Page")
# data=driver.find_element(By.CSS_SELECTOR,"#articlecount a")
# print(data.text)
driver.get(url="http://secure-retreat-92358.herokuapp.com/")
driver1=driver.find_element(By.NAME,"fName")
driver1.send_keys("Hammad")
driver2=driver.find_element(By.NAME,"lName")
driver2.send_keys("farooq")
driver3=driver.find_element(By.NAME,"email")
driver3.send_keys("farooqHmamad@gmail.com")
submit=driver.find_element(By.CSS_SELECTOR,"form button")
submit.click()
time.sleep(5)