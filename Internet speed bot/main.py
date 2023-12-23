MAX_UP=10
MAX_DOWN=1
TWITTER_EMAIL="asaprogrammer42@gmail.com"
TWITTER_PASSWORD="punjabuni0123"
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
class InternetSpeedTwitterBot:
    def __init__(self):
        self.up=MAX_UP
        self.down=MAX_DOWN
        self.twitter_email=TWITTER_EMAIL
        self.password=TWITTER_PASSWORD
        self.data=""

    def password1(self, driver1):
        time.sleep(3)
        password = driver1.find_element(By.XPATH,
                                        '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(self.password)
        time.sleep(2)
        login = driver1.find_element(By.XPATH,
                                     '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
        time.sleep(2)
        login.click()
        time.sleep(3)
        tweet = driver1.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet.click()
        time.sleep(8)
        text = driver1.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        time.sleep(2)
        text.send_keys(f"{self.data}")
        time.sleep(4)
        button2= driver1.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]')
        time.sleep(1)
        button2.click()
    def get_internet_speed(self,driver):
        driver.get("https://www.speedtest.net/")
        time.sleep(5)
        go=driver.find_element(By.CLASS_NAME,"js-start-test")
        go.click()
        time.sleep(40)
        data=driver.find_element(By.CLASS_NAME,"result-data-large")
        time.sleep(2)
        print(f"The Download speed is {data.text}Mbps")
        data1=driver.find_element(By.CLASS_NAME,"upload-speed")
        time.sleep(2)
        print(f"The upload speed is {data1.text}Mbps")
        self.data=f"The uploading speed is {data.text} and The dowload speed is {data1.text} Please Help!"
        time.sleep(10)

    def tweet(self):
        driver=webdriver.Chrome()
        self.get_internet_speed(driver=driver)
        driver.get("https://twitter.com/?lang=en")
        time.sleep(10)
        login=driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a")
        login.click()
        time.sleep(10)
        email=driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        time.sleep(2)
        email.send_keys(self.twitter_email)
        next=driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        time.sleep(2)
        next.click()
        time.sleep(2)
        try:
            password = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            time.sleep(2)
            password.send_keys(self.password)
            time.sleep(2)
        except:
            time.sleep(2)
            user_name = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            time.sleep(2)
            user_name.send_keys("alishah01048173")
            time.sleep(3)
            button1 = driver.find_element(By.XPATH,'/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div')
            time.sleep(2)
            button1.click()
            self.password1(driver1=driver)
        else:
            self.password1(driver1=driver)
        time.sleep(10000)

speed=InternetSpeedTwitterBot()
speed.tweet()


