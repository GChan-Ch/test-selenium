from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TestTest1():
    def __init__(self):
        self.PATH = "C:\\Program Files (x86)\\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test1(self):
        self.driver.get("https://www.gsmarena.com/")
        self.driver.set_window_size(784, 816)
        self.driver.find_element(By.ID, "topsearch-text").click()
        self.driver.find_element(By.ID, "topsearch-text").send_keys("iphone 13")
        self.driver.find_element(By.ID, "topsearch-text").send_keys(Keys.ENTER)
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) img").click()
        element = self.driver.find_element(By.LINK_TEXT, "Announced")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.find_element(By.CSS_SELECTOR, ".article-info .article-info-meta-link:nth-child(4) > a").click()
        self.driver.find_element(By.ID, "sSearch2").click()
        self.driver.find_element(By.ID, "sSearch2").send_keys("asus rog phone 8")
        self.driver.find_element(By.CSS_SELECTOR, "li:nth-child(1) span").click()

if __name__ == "__main__":
    test_instance = TestTest1()
    test_instance.test_test1()
    test_instance.teardown_method(None)
