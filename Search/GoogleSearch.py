from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time

# Get user input for google search
find = input("Enter what you want to search for: ")

PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(PATH, chrome_options=options)

url = "https://www.google.com/"
driver.get(url)

search = driver.find_element_by_name("q")
search.send_keys(find)
search.send_keys(Keys.RETURN)

# return whats found to the user
# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "main"))
#     )


#     print("\n\n\n\n\n")
#     texts = main.find_elements("g")

#     for text in texts:
#         link = texts.find_element_by_class_name("yuRUbf")
#         print(link.text)

# finally:
#     driver.quit()

time.sleep(15)
