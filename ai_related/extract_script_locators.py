# extract_script_locators.py
import re

def extract_locators_from_script(script_path):
    locators = []
    with open(script_path, 'r') as file:
        script = file.read()
        
        # Extract locators like By.ID, By.NAME, By.CSS_SELECTOR
        id_locators = re.findall(r'By\.ID, "([^"]+)"', script)
        class_locators = re.findall(r'By\.CSS_SELECTOR, "([^"]+)"', script)
        
        for id_ in id_locators:
            locators.append({'type': 'id', 'value': id_})
        for class_ in class_locators:
            locators.append({'type': 'class', 'value': class_})
    
    return locators
