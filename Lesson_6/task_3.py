from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome()
chrome.implicitly_wait(15)
chrome.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
wait = WebDriverWait(chrome, 40, 0.1)
wait.until(EC.text_to_be_present_in_element((By.ID, "text"), 'Done!'))
attribute = chrome.find_element(By.ID, "award").get_attribute("src")
print(attribute)