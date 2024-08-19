from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


firefox = webdriver.Firefox()
firefox.get("http://uitestingplayground.com/classattr")
for i in range(3):
    firefox.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
    sleep(1)
    firefox.switch_to.alert.accept()