
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome WebDriver
driver = webdriver.Chrome()

try:
    # 1. Open Wikipedia homepage
    driver.get("https://www.wikipedia.org")
    driver.maximize_window()
    print("Opened Wikipedia homepage.")
    time.sleep(2)

    # 2. Search for "Python (programming language)"
    search_input = driver.find_element(By.ID, "searchInput")
    search_input.send_keys("Python (programming language)")
    search_input.submit()
    print("Searched for 'Python (programming language)'.")
    time.sleep(3)

    # 3. Wait for article and click it
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "firstHeading"))
    )
    print("Opened article.")

    # 4. Extract and print the first paragraph
    first_para = driver.find_element(By.CSS_SELECTOR, "p")
    print("First paragraph:")
    print(first_para.text)

    input("Done! Press Enter to close...")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
