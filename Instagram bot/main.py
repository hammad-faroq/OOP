USER_NAME="asaprogrammer@gmail.com"
PASSWORD="Password"
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get(url='https://www.instagram.com/chefsteps/')
time.sleep(10)
login=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[2]/div/div/div[2]/div[1]/a')
login.click()
time.sleep(4)
email=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div/div[2]/form/div/div[1]/div/label/input')
time.sleep(2)
email.send_keys(USER_NAME)
time.sleep(2)
password=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div/div[2]/form/div/div[2]/div/label/input")
password.send_keys(PASSWORD)
time.sleep(2)
button=driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
time.sleep(2)
button.click()
total_followers=driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
time.sleep(2)
total_followers.click()
time.sleep(100000)