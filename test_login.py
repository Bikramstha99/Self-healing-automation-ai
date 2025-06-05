import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Load locators
with open('C:/Users/bikramshrestha/Desktop/Self-healing/self-healing-automation-ai/locators.json', 'r') as f:
    locators = json.load(f)

driver = webdriver.Chrome()
driver.get("http://localhost:4200")
time.sleep(1)

try:
    driver.find_element(By.CSS_SELECTOR, locators["login_usernamesInput"]).send_keys("testuser")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, locators["login_passwordInput"]).send_keys("testpass")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    time.sleep(2)
    print("✅ Login successful.")

    driver.find_element(By.CSS_SELECTOR, locators["dashboard_addcardButton"]).click()
    time.sleep(1)
    print("✅ Card added.")

    cards = driver.find_elements(By.CSS_SELECTOR, "[id^='card-']")
    print(f"🟢 {len(cards)} card(s) found after adding.")

    if cards:
        delete_button = cards[0].find_element(By.CSS_SELECTOR, "button[id^='delete-card-button-']")
        delete_button.click()
        time.sleep(1)
        print("✅ First card deleted.")

        cards_after = driver.find_elements(By.CSS_SELECTOR, "[id^='card-']")
        print(f"🟢 {len(cards_after)} card(s) remain after deletion.")

except Exception as e:
    print("❌ Error:", str(e))

finally:
    time.sleep(2)
    driver.quit()
