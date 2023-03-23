from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard, time

PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(PATH, chrome_options=options)
options.add_experimental_option("detach", True)

url = "http://orteil.dashnet.org/cookieclicker/"
driver.get(url)

# wait for cite to load
time.sleep(3)

button = driver.find_element(By.ID, "langSelect-EN")
button.click()

# Wait 2 seconds for the page to load after selecting language
time.sleep(2)

bigCookieButton = driver.find_element(By.ID, "bigCookie")
def gameLoop():
    while True:
        bigCookieButton.click()

        # Try to purchase an upgrade
        try:
            items = driver.find_elements(By.CLASS_NAME, "enabled")
            for item in items[::-1]:
                item.click()
        except:
            print("Not enough cookies")

        # Pause
        if keyboard.is_pressed('p'):
            print("Stopped")
            break

while True:
    # Start
    if keyboard.is_pressed('s'):
        print("Started")
        gameLoop()
    # Quit
    elif keyboard.is_pressed('q'):
        print("GoodBye")
        break
    
# Close browser
driver.close()

