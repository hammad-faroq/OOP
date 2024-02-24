chrome_driver_path="C:\Development/chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
data=driver.get(url="https://www.python.org/")
time=driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
content=driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events={}
for n in range(len(time)):
    events[n]={  #a simple add method to add a key into a dictionary and the key name should be dict["key"]=Value or value can also be a dictionary
    "time":time[n].text,
    "name":content[n].text}
print(events)
# element_link=(driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a'))
# dictionary={
#     "time":element_time,
#     "link":element_link
# }
# element=(driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time'))
# element2=(driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time'))
# print(element.find_element(By.CSS_SELECTOR,"time"))
# driver.close()
