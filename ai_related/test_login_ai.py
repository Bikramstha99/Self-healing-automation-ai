# test_login_ai.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

# Load locators from locators.json
with open('locators.json', 'r') as f:
    locators = json.load(f)

driver = webdriver.Chrome()

driver.get("http://localhost:4200")
time.sleep(1)

# Wait until the user_id input element is present before interacting with it
user_id_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, locators["user_idInput"]))
)
user_id_element.send_keys("testuser")
time.sleep(0.5)

# Wait until the user_pass input element is present before interacting with it
user_pass_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, locators["user_passInput"]))
)
user_pass_element.send_keys("testpass")
time.sleep(0.5)

# Wait until the login button is clickable before interacting with it
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, locators["loginButton"]))
)
login_button.click()
time.sleep(1)

# Wait for dashboard to load
try:
    dashboard_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, locators["dashboardWelcome"]))
    )
    print("✅ Login successful. Dashboard loaded.")
except Exception as e:
    print("❌ Login failed or dashboard not loaded:", str(e))

finally:
    time.sleep(2)
    driver.quit()
