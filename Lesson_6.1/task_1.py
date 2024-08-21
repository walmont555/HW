from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


def test_form():
    chrome = webdriver.Chrome()
    chrome.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    chrome.find_element(By.NAME, "last-name").send_keys("Иван")
    chrome.find_element(By.NAME, "first-name").send_keys("Петров")
    chrome.find_element(By.NAME, "address").send_keys("Аграрная, 12-3")
    chrome.find_element(By.NAME, "e-mail").send_keys("test@skypro.ru")
    chrome.find_element(By.NAME, "phone").send_keys("+79850009911")
    chrome.find_element(By.NAME, "city").send_keys("Москва")
    chrome.find_element(By.NAME, "country").send_keys("Россия")
    chrome.find_element(By.NAME, "job-position").send_keys("QA")
    chrome.find_element(By.NAME, "company").send_keys("SkyPro")
    chrome.find_element(By.XPATH, '//button[text() = "Submit"]').click()
    assert "danger" in chrome.find_element(By.ID, "zip-code").get_attribute("class")
    assert "success" in chrome.find_element(By.ID, "first-name").get_attribute("class")
    assert "success" in chrome.find_element(By.ID, "last-name").get_attribute("class")
    assert "success" in chrome.find_element(By.ID, "address").get_attribute("class")
    assert "success" in chrome.find_element(By.ID, "e-mail").get_attribute("class")
    assert "success" in chrome.find_element(By.ID, "phone").get_attribute("class")
    assert "success" in chrome.find_element(By.ID, "city").get_attribute("class")
    assert "success" in chrome.find_element(By.ID, "country").get_attribute("class")
    assert "success" in chrome.find_element(By.ID, "job-position").get_attribute("class")
    assert "success" in chrome.find_element(By.ID, "company").get_attribute("class")
    chrome.quit()