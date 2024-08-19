from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


firefox = webdriver.Firefox()
firefox.get("https://the-internet.herokuapp.com/inputs")
input = firefox.find_element(By.TAG_NAME, "input")
input.send_keys("1000")
input.clear()
sleep(2)
input.send_keys("999")
sleep(1)
