# extract_locators_from_html.py
from bs4 import BeautifulSoup

def extract_locators_from_html(html_file_path):
    locators = {}

    with open(html_file_path, 'r') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # Example: Extract locators based on ID and other attributes
        username_element = soup.find(id="username")
        password_element = soup.find(id="password")
        login_button = soup.find('button', type="submit")
        dashboard_element = soup.find(id="dashboard-welcome")

        # Store locators in a dictionary
        if username_element:
            locators["usernameInput"] = username_element.get("id")
        if password_element:
            locators["passwordInput"] = password_element.get("id")
        if login_button:
            locators["loginButton"] = "button[type='submit']"  # You can choose CSS selector
        if dashboard_element:
            locators["dashboardWelcome"] = dashboard_element.get("id")

    return locators
