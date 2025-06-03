# update_script.py
import json
from extract_locators_from_html import extract_locators_from_html
from ai_locator_comparator import detect_changes_using_ai
from update_automation_script import update_automation_script_with_new_locators

# Paths to files
html_file_path = 'C:/Users/Acer/OneDrive/Desktop/Self-healing/self-heating-automation-project/src/app/login/login.component.html'
selenium_script_path = 'C:/Users/Acer/OneDrive/Desktop/Self-healing/self-heating-automation-ai/test_login_ai.py'

# Step 1: Extract locators from updated HTML
new_locators = extract_locators_from_html(html_file_path)

# Step 2: Load existing locators from locators.json
try:
    with open('locators.json', 'r') as f:
        old_locators = json.load(f)
except FileNotFoundError:
    old_locators = {}

# Step 3: Detect locator changes using AI-based comparison
matched_locators = detect_changes_using_ai(old_locators, new_locators)

# If there are any changes, update the locators and automation script
if matched_locators:
    # Step 4: Save updated locators to locators.json
    with open('locators.json', 'w') as f:
        json.dump(new_locators, f, indent=4)

    # Step 5: Update the Selenium automation script
    update_automation_script_with_new_locators(selenium_script_path, matched_locators)
else:
    print("❌ No changes detected in the locators.")
