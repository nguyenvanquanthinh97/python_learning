from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="./chromedriver")
chrome_browser = webdriver.Chrome(service=service)

chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
assert "Selenium Easy Demo" in chrome_browser.title

input_message = chrome_browser.find_element(By.ID, "user-message")
button_show_message = chrome_browser.find_element(By.CLASS_NAME, "btn-default")
# button_css_select = chrome_browser.find_element(By.CSS_SELECTOR, "form#get-input button.btn,button.btn-default")
display_message = chrome_browser.find_element(By.ID, "display")
test_message = "This is a test!!!"

input_message.clear()
input_message.send_keys(test_message)
button_show_message.click()
assert display_message.get_attribute('innerText') == test_message

chrome_browser.close()


