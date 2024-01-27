from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get(url="https://tinder.com/")
time.sleep(5)
i_accept = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
time.sleep(1)
i_accept.click()
sign_in=driver.find_element(By.XPATH,'//*[@id="c-1445344539"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')
time.sleep(5)
sign_in.click()
time.sleep(4)
sign_in_fb=driver.find_element(By.XPATH,'//*[@id="c1121241681"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
time.sleep(2)
sign_in_fb.click()
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
sign_in_fb1=driver.find_element(By.NAME,'email')
sign_in_fb1.send_keys("bsdsf22a026@pucit.edu.pk")
sign_in_fb2=driver.find_element(By.NAME,'pass')
sign_in_fb2.send_keys("punjabuni0123")
sign_in_login=driver.find_element(By.NAME,"login")
time.sleep(3)
sign_in_login.click()
# # for i in sign_in:
driver.switch_to.window(base_window)
print(driver.title)

time.sleep(15)
location=driver.find_element(By.CLASS_NAME,'c1p6lbu0')
time.sleep(2)
location.click()
time.sleep(3)
not_interested=driver.find_element(By.CLASS_NAME,'c1p6lbu0')
time.sleep(1)
not_interested.click()
time.sleep(5)
dislike=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[4]/div/div[2]/button')
time.sleep(2)
dislike.click()

time.sleep(5000)