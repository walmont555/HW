from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
chrome.implicitly_wait(10)
chrome.get("http://uitestingplayground.com/textinput")
chrome.find_element(By.ID, "newButtonName").send_keys("SkyPro")
chrome.find_element(By.ID, "updatingButton").click()
text = chrome.find_element(By.ID, "updatingButton").text
print(text)