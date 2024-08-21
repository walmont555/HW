from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_calculator():
    chrome = webdriver.Chrome()
    chrome.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    chrome.find_element(By.ID, "delay").clear()
    chrome.find_element(By.ID, "delay").send_keys("45")
    chrome.find_element(By.XPATH, "//span[text() = '7']").click()
    chrome.find_element(By.XPATH, "//span[text() = '+']").click()
    chrome.find_element(By.XPATH, "//span[text() = '8']").click()
    chrome.find_element(By.XPATH, "//span[text() = '=']").click()
    WebDriverWait(chrome, 46).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    assert chrome.find_element(By.CLASS_NAME, "screen").text == "15"
