from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
chrome.get("https://the-internet.herokuapp.com/add_remove_elements/")
for i in range(5):
    chrome.find_element(By.XPATH, '//button[text()="Add Element"]').click()

quantity=chrome.find_elements(By.XPATH,'//button[text()="Delete"]')
print(len(quantity))