from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://github.com/UskOops')
while True:
    time.sleep(1)
    driver.refresh()
driver.quit()