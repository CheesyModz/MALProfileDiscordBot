from selenium import webdriver

PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(PATH, chrome_options=options)

url = "https://impomu.com/"
driver.get(url)


while True:
    button = driver.find_element_by_id("im-pomu")
    button.click()

