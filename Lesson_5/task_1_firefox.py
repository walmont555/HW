from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


firefox = webdriver.Firefox()
firefox.get("https://the-internet.herokuapp.com/add_remove_elements/")
for i in range(5):
    firefox.find_element(By.XPATH, '//button[text()="Add Element"]').click()

quantity=firefox.find_elements(By.XPATH, '//button[text()="Delete"]')
print(len(quantity))