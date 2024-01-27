from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId="
               "3708172929&distance=25&f_AL=true&geoId=101022442&keywords="
               "data%20scientist%20intern&origin=JOBS_HOME_SEARCH_CARDS#HYM")
submit=driver.find_element(By.XPATH,'/html/body/div[1]/header/nav/div/a[2]')
submit.click()
name=driver.find_element(By.NAME,"session_key")
name.send_keys("asaprogrammer42@gmail.com")
password=driver.find_element(By.NAME,'session_password')
password.send_keys("pucitHammad0123")
button=driver.find_element(By.CLASS_NAME,"from__button--floating")
button.click()
time.sleep(21)
jobs=driver.find_elements(By.CLASS_NAME,'job-card-list__title') #all the applications
for i in jobs:
    i.click()
    time.sleep(5)
    try:
        jobs_button=driver.find_element(By.CSS_SELECTOR,".jobs-s-apply button")#job apply button
        time.sleep(4)
        jobs_button.click()
    except:
        continue
    else:
        contact_button=driver.find_element(By.CSS_SELECTOR,".artdeco-text-input--input")
        contact_button.send_keys("")
        contact_button.click()
        next_button=driver.find_element(By.CSS_SELECTOR,".artdeco-button--primary")
        next_button.click()
        next_button1=driver.find_element(By.CSS_SELECTOR,".artdeco-button--primary")
        next_button1.click()
        next_button1 = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        next_button1.click()  #Review button
        time.sleep(30)
        # next_button5 = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
        # next_button5.click() ##submit application
        # next_button5 = driver.find_element(By.CSS_SELECTOR, ".ml2")
        # next_button5.click()  #done button
        # time.sleep(4)
        # time.sleep(100000)