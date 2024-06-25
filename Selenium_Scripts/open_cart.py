from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import service
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import os
import time

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

print(email)
print(password)

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://awesomeqa.com/ui/")
mac_element = driver.find_element(By.XPATH,"//a[text()='Desktops']")
hov=ActionChains(driver)
hov.move_to_element(mac_element).perform()
driver.implicitly_wait(3)
driver.find_element(By.PARTIAL_LINK_TEXT,"Mac").click()
driver.find_element(By.XPATH,"//a[text()='iMac']").click()
driver.find_element(By.XPATH,"//button[text()='Add to Cart']").click()
driver.implicitly_wait(3)

driver.find_element(By.ID,"cart").click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//a[@href='https://awesomeqa.com/ui/index.php?route=checkout/cart']").click()
driver.find_element(By.XPATH,"//input[contains(@name,'quantity')]").send_keys("2")
driver.find_element(By.XPATH,"//input[contains(@name,'quantity')]/following-sibling::*[1]//button[1][@data-original-title='Update']").click()
driver.find_element(By.LINK_TEXT,"Checkout").click()
driver.implicitly_wait(3)

driver.find_element(By.XPATH,"//input[@value='Continue']").click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//input[@placeholder='First Name']").send_keys("Jon")
driver.find_element(By.XPATH,"//input[@placeholder='Last Name']").send_keys("Snow")
driver.find_element(By.XPATH,"//input[@placeholder='E-Mail'][@id='input-payment-email']").send_keys(email)
driver.find_element(By.XPATH,"//input[@placeholder='Telephone']").send_keys("5378296457")
driver.find_element(By.XPATH,"//input[@placeholder='Password'][@id='input-payment-password']").send_keys(password)
driver.find_element(By.XPATH,"//input[@placeholder='Password Confirm']").send_keys(password)
driver.find_element(By.XPATH,"//input[@placeholder='Address 1']").send_keys("3450 Chemin De La Cote De Neiges")
driver.find_element(By.XPATH,"//input[@placeholder='City']").send_keys("Montreal")
driver.find_element(By.XPATH,"//input[@placeholder='Post Code']").send_keys("H3H 3P1")
country = driver.find_element(By.XPATH,"//select[@name='country_id']")
Select(country).select_by_visible_text("Canada")
driver.implicitly_wait(3)
state = driver.find_element(By.XPATH,"//select[@name='zone_id']")
Select(state).select_by_visible_text("Québec")

driver.find_element(By.XPATH,"//input[@name='agree']").click()
driver.find_element(By.ID,"button-register").click()

driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//textarea[@name='comment']").send_keys("Purchasing iMac through automation")
driver.find_element(By.ID,"button-shipping-method").click()

driver.refresh()

driver.implicitly_wait(3)
driver.find_element(By.ID,"button-payment-address").click()

driver.implicitly_wait(3)
driver.find_element(By.ID,"button-shipping-address").click()

driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//textarea[@name='comment']").send_keys("Purchasing iMac through automation")
driver.find_element(By.ID,"button-shipping-method").click()

driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//textarea[@name='comment']").send_keys("Purchasing iMac through automation")
driver.find_element(By.XPATH,"//input[@name='agree']").click()
driver.find_element(By.ID,"button-payment-method").click()

driver.implicitly_wait(3)
driver.find_element(By.ID,"button-confirm").click()
driver.implicitly_wait(3)
assert "Your order has been placed!" == driver.find_element(By.XPATH,"//h1[text()='Your order has been placed!']").text
assert "Your order has been successfully processed!" == driver.find_element(By.XPATH,"//p[text()='Your order has been successfully processed!']").text
driver.get_screenshot_as_file(os.getcwd()+"/screenshots/"+"order_confirmation.png")
