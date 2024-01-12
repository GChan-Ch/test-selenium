from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

# opsi 1 python 2.7
# PATH = ("C:\\Users\\gold.aptaworks\\OneDrive\\Documents\\Learn selenium\\chrome v120\\chromedriver.exe")
# driver = webdriver.Chrome(PATH)

# opsi 2 python 3.10
service = webdriver.ChromeService(
    executable_path='C:\\Users\\gold.aptaworks\\OneDrive\\Documents\\Learn selenium\\chrome v120\\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://www.gsmarena.com/compare.php3")
print(driver.title)

time.sleep(5)
# driver.set_page_load_timeout(5)
# search = driver.find_element_by_id("sSearch2")
search = driver.find_element(By.ID, 'sSearch2')
search.send_keys("Samsung A54")
search.send_keys(Keys.RETURN)

time.sleep(5)
# driver.set_page_load_timeout(5)
# search = driver.find_element_by_id("sSearch3")

search = driver.find_element(By.ID, 'sSearch3')
search.send_keys("Samsung S23 FE")
search.send_keys(Keys.RETURN)

# print(driver.page_source)
# driver.set_page_load_timeout(5)
# time.sleep(5)

driver.quit()
