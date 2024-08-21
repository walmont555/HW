from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



def test_shop():
    chrome = webdriver.Chrome()
    chrome.get("https://www.saucedemo.com/")
    chrome.find_element(By.ID, "user-name").send_keys("standard_user")
    chrome.find_element(By.ID, "password").send_keys("secret_sauce")
    chrome.find_element(By.ID, "login-button").click()
    chrome.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    chrome.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    chrome.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    chrome.find_element(By.ID, "shopping_cart_container").click()
    chrome.find_element(By.ID, "checkout").click()
    chrome.find_element(By.ID, "first-name").send_keys("Владимир")
    chrome.find_element(By.ID, "last-name").send_keys("Васильев")
    chrome.find_element(By.ID, "postal-code").send_keys("111222")
    chrome.find_element(By.ID, "continue").click()
    assert chrome.find_element(By.CLASS_NAME, "summary_total_label").text == "Total: $58.29"



