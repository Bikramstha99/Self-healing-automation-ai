import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with open('C:/Users/Acer/OneDrive/Desktop/Self-healing/self-heating-automation-ai/locators.json', 'r') as f:
    locators = json.load(f)

driver = webdriver.Chrome()
driver.get("http://localhost:4200")
time.sleep(1)

# === Use dynamic locators ===
driver.find_element(By.ID, locators["usernameInput"]).send_keys("testuser")
time.sleep(0.5)

driver.find_element(By.ID, locators["passwordInput"]).send_keys("testpass")
time.sleep(0.5)

driver.find_element(By.CSS_SELECTOR, locators["loginButton"]).click()
time.sleep(1)

# === Wait for dashboard ===
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
