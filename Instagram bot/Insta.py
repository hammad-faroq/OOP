USER_NAME = "hammadf2003@gmail.com"
PASSWORD = "Unipunjab0123"
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
class Instagram:
    def __init__(self):
        self.user_name=USER_NAME
        self.password=PASSWORD
        self.driver=webdriver.Chrome()
        self.driver.get(url='https://www.instagram.com/')
    def login2(self):
        self.login = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/nav/div[2]/div/div/div[3]/div/div/div[2]/div[1]/a')
        time.sleep(2)
        self.login.click()
        time.sleep(4)
        self.email = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div/div[2]/form/div/div[1]/div/label/input')
        time.sleep(2)
        self.email.send_keys(USER_NAME)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div/div[2]/form/div/div[2]/div/label/input")
        password.send_keys(PASSWORD)
        time.sleep(2)
        self.button = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button')
        time.sleep(2)
        self.button.click()
        time.sleep(13)
        self.not_now=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div")
        time.sleep(2)
        self.not_now.click()
    def follow(self):
        time.sleep(8)
        self.total_followers = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
        time.sleep(2)
        self.total_followers.click()
        time.sleep(10)
        follower_window = self.driver.find_element(By.CSS_SELECTOR,'div._aano')##This is the div of the pop up window
        time.sleep(12)
        for _ in range(100):##it will scroll down the window 100 times
            scroll_window = self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight",
                                                  follower_window)#This code is used too scroll that div
            time.sleep(5)
        self.buttons =self.driver.find_elements(By.CSS_SELECTOR, 'div._aano  button._acan._acap._acas._aj1-')##this is the follow buttons in the pop up untill end
        print(f"Found {len(self.buttons)} buttons")
        time.sleep(2)
        # iterate over the buttons and print their text content
        for button in self.buttons:
            button.click()#this will click that button in all the scrolled and also go back to scroll while loop
            time.sleep(1)

insta=Instagram()
time.sleep(5)
insta.login2()
insta.follow()
# /html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button

# _acan _acap _acas _aj1-