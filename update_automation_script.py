def update_automation_script_with_new_locators(script_path, matched_locators):
    # Open the file with utf-8 encoding to avoid encoding issues
    with open(script_path, 'r', encoding='utf-8') as file:
        script_content = file.read()
    
    # Replace old locators with new ones
    for old_locator, new_locator in matched_locators.items():
        script_content = script_content.replace(old_locator, new_locator)
    
    # Write the updated content back to the same file
    with open(script_path, 'w', encoding='utf-8') as file:
        file.write(script_content)

# Assuming the correct path to the script
selenium_script_path = 'C:/Users/Acer/OneDrive/Desktop/Self-healing/self-heating-automation-ai/test_login_ai.py'

# Your matched locators
matched_locators = {
    "username": "user_id",
    "password": "user_pass",
    "login-btn": "login_button"
}

# Update the automation script
update_automation_script_with_new_locators(selenium_script_path, matched_locators)
