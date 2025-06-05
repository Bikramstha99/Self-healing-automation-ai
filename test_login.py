import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

with open('C:/Users/bikrams/Desktop/Self-healing/self-healing-automation-ai/locators.json', 'r') as f:
    locators = json.load(f)

driver = webdriver.Chrome()
driver.get("http://localhost:4200")
time.sleep(1)

# Login
try:
    driver.find_element(By.ID, locators["usernamesInput"]).send_keys("testuser")
    time.sleep(0.5)
    driver.find_element(By.ID, locators["passwordInput"]).send_keys("testpass")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, locators["loginButton"]).click()
    time.sleep(1)

   
    print("✅ Login successful. Dashboard loaded.")

    add_card_button = driver.find_element(By.ID, locators["addCardButton"])
    add_card_button.click()
    time.sleep(1)
    print("✅ Card added.")

    cards = driver.find_elements(By.CSS_SELECTOR, locators["card1"])
    if len(cards) > 0:
        print(f"✅ {len(cards)} card(s) present after adding.")

    delete_card_button = cards[0].find_element(By.CSS_SELECTOR, locators["delete-card-button-1"])
    delete_card_button.click()
    time.sleep(1)
    print("✅ Card deleted.")

    cards = driver.find_elements(By.CSS_SELECTOR, locators["card1"])
    print(f"✅ {len(cards)} card(s) present after deleting.")

except Exception as e:
    print("❌ An error occurred:", str(e))

finally:
    time.sleep(2)
    driver.quit()
