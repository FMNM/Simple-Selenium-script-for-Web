from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = "./edgedriver_win64/msedgedriver.exe"

options = webdriver.EdgeOptions()
options.add_argument("--inprivate")
driver = webdriver.Edge(options=options)

site_url = "https://taylorswift.ticketek.com.au/"
driver.get(site_url)

try:
    while True:
        try:
            button_element_x = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "syd-frontier-btn")))
            button_element_x.click()
            break
        except:
            continue

    while True:
        try:
            response_element_y = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.ID, "id_of_element_y")))
            response_element_y.click()
            break
        except:
            continue

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    driver.quit()
