from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


firefox = webdriver.Firefox()
firefox.get("https://the-internet.herokuapp.com/entry_ad")
sleep(3)
firefox.find_element(By.CSS_SELECTOR, ".modal-footer").click()
sleep(1)
