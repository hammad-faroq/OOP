from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get(url="https://orteil.dashnet.org/cookieclicker/")
time.sleep(7)
button=driver.find_element(By.CSS_SELECTOR,'.langSelectButton')
print(button.tag_name)
print(button.text)
button.click()
time.sleep(5)
actual_price_grandma=101
i=0
while True:
    button1=driver.find_element(By.CSS_SELECTOR,'#bigCookie')
    button1.click()
    time.sleep(1)
    i=i+1
    button1=driver.find_element(By.CSS_SELECTOR,'#bigCookie')
    button1.click()
    time.sleep(1)
    i = i + 1
    button1=driver.find_element(By.CSS_SELECTOR,'#bigCookie')
    button1.click()
    time.sleep(1)
    i = i + 1
    cookies=driver.find_element(By.XPATH,'/html/body/div/div[2]/div[15]/div[4]')
    cookiess=cookies.text
    num=cookiess.split(" ")[0]
    actual_num=int(num)
    button3 = driver.find_element(By.CSS_SELECTOR, '#productPrice0')
    price1=button3.text
    curosr_price=int(price1)
    if actual_num>actual_price_grandma:
        button4 = driver.find_element(By.CSS_SELECTOR, '#productPrice1')
        price2 = button4.text
        actual_price_grandma = int(price2)
        time.sleep(7)
        i = i + 7
        button2=driver.find_element(By.CSS_SELECTOR,'#product1')
        button2.click()
    elif actual_num > curosr_price:
        time.sleep(7)
        i = i + 1
        button2 = driver.find_element(By.CSS_SELECTOR, '#product0')
        button2.click()
    print(i)
    if i>300:
        break


# print(button2.tag_name)
# cookies1=driver.find_element(By.CSS_SELECTOR,'div span ')