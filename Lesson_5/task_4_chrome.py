from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


chrome = webdriver.Chrome()
chrome.get("https://the-internet.herokuapp.com/entry_ad")
sleep(3)
chrome.find_element(By.CSS_SELECTOR, ".modal-footer").click()
sleep(1)
