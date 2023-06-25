from selenium import webdriver
import time


driver = webdriver.Chrome()

driver.get('https://opendj.jd.com/')
driver.implicitly_wait(10)
time.sleep(30)
coo = driver.get_cookies()
print(coo)
driver.quit()
