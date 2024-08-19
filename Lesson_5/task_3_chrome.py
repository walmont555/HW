from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
chrome.get("http://uitestingplayground.com/classattr")
for i in range(3):
    chrome.find_element(By.XPATH,"//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
    sleep(1)
    chrome.switch_to.alert.accept()