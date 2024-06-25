from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

driver.maximize_window()
driver.get("https://katalon-demo-cura.herokuapp.com/")
driver.find_element(By.ID,"btn-make-appointment").click()

driver.find_element(By.NAME,"username").send_keys("John Doe")
driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
driver.find_element(By.ID,"btn-login").click()

drop_downs = driver.find_element(By.ID,"combo_facility")
facility = Select(drop_downs)

# facility.select_by_value("Hongkong CURA Healthcare Center")
# facility.select_by_index(1)

facility.select_by_visible_text("Hongkong CURA Healthcare Center")

driver.find_element(By.NAME,"hospital_readmission").click()
driver.find_element(By.ID,"radio_program_medicaid").click()
driver.find_element(By.XPATH,"//input[@placeholder='dd/mm/yyyy']").click()

switch = driver.find_elements(By.CLASS_NAME,"datepicker-switch")
prev_buttons = driver.find_elements(By.XPATH,"//th[@class='prev']")
next_buttons = driver.find_elements(By.XPATH,"//th[@class='next']")

switch[0].click()

current_year = int(switch[1].text)
expected_year = 2005
expected_month = 'Feb'
expected_day = 4

if(current_year > expected_year):
    
    while (current_year > expected_year):
        prev_buttons[1].click()
        current_year -= 1

    # print(switch[1].text)

elif(current_year < expected_year):

    while (current_year < expected_year):
        next_buttons[1].click()
        current_year += 1

    # print(switch[1].text)

driver.find_element(By.XPATH,f"//span[text()='{expected_month}']").click()
driver.find_element(By.XPATH,f"//td[@class='day'][text()='{expected_day}']").click()

# driver.find_element(By.XPATH,"//div[@class='datepicker-years']//table//tbody//tr//td//span[text()=2020]]")
# driver.find_element(By.ID,"txt_visit_date").send_keys("21/02/2025")

driver.find_element(By.NAME,"comment").send_keys("Automation by Parth Modi")
driver.find_element(By.ID,"btn-book-appointment").click()

driver.implicitly_wait(3)

comment = driver.find_element(By.ID,"comment")
facility = driver.find_element(By.ID,"facility")
date = driver.find_element(By.ID,"visit_date")

# appointment = driver.find_element(By.CSS_SELECTOR,"h2")
appointment = driver.find_element(By.XPATH, "//h2")
program = driver.find_element(By.XPATH, "//p[@id='program']")

def test_cura_health_appointment_confirmation():
    assert "Appointment Confirmation" == appointment.text

def test_cura_health_facility_name():
    assert "Hongkong CURA Healthcare Center" == facility.text

def test_cura_health_customer_comment():
    assert "Automation by Parth Modi" == comment.text

def test_cura_health_booking_date():
    assert "04/02/2005" == date.text

def test_cura_health_booked_program():
    assert "Medicaid" == program.text

    print("Test Passed")
