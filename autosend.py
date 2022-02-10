from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

with open("texts.txt", "r") as file: 
    lines=file.read().split("\n")

texts = [line for line in lines if line != '']

##### TO BE CHANGED ######
target = ''

driver = webdriver.Chrome('')
##### TO BE CHANGED ###### 

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 600)
 
x_arg = '//span[contains(@title, '+ '"' +target + '"'+ ')]'
print(x_arg)
person_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
print(person_title)
person_title.click()
inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"]'
inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))

for text in texts:
    input_box.send_keys(text + Keys.ENTER)
    time.sleep(0.4)