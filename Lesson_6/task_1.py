from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
chrome.implicitly_wait(20)
chrome.get("http://uitestingplayground.com/ajax")
chrome.find_element(By.ID, "ajaxButton").click()
text = chrome.find_element(By.CLASS_NAME, "bg-success").text
print(text)
