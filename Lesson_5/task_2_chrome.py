from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
chrome.get("http://uitestingplayground.com/dynamicid")
for i in range(3):
    chrome.find_element(By.CSS_SELECTOR,".btn-primary").click()
    sleep(1)