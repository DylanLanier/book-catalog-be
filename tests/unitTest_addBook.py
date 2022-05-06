import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class ll_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/dylan/PycharmProjects/FinalProjectBackend/myvenv/bookLibrary/tests/chromedriver.exe')

    def test_ll(self):
        user = "dlanier"
        pwd = "password"
        update = "test"
        year = "1990"
        rating = "3"

        driver = self.driver
        driver.maximize_window()
        driver.get("https://illustrious-fenglisu-42aedd.netlify.app")
        time.sleep(3)
        elem=driver.find_element(by=By.XPATH, value="/html/body/div/ul/li[3]/a").click()
        time.sleep(3)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div/div/div[2]/div/div/input[1]")
        elem.send_keys(user)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div/div/div[2]/div/div/input[2]")
        elem.send_keys(pwd)
        time.sleep(3)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div/div/div[2]/button").click()
        time.sleep(3)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/ul/li[2]/a").click()
        time.sleep(3)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[2]/button").click()
        time.sleep(3)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div[2]/div/div/div[2]/form/div/div[1]/div/input")
        elem.send_keys(update)
        time.sleep(2)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div[2]/div/div/div[2]/form/div/div[2]/div/input")
        elem.send_keys(update)
        time.sleep(2)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div[2]/div/div/div[2]/form/div/div[3]/div/input")
        elem.send_keys(update)
        time.sleep(2)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div[2]/div/div/div[2]/form/div/div[4]/div/input")
        elem.send_keys(update)
        time.sleep(2)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div[2]/div/div/div[2]/form/div/div[5]/div/input")
        elem.send_keys(year)
        time.sleep(2)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div[2]/div/div/div[2]/form/div/div[6]/div/input")
        elem.send_keys(rating)
        time.sleep(2)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div[2]/div/div/div[2]/form/div/div[7]/div[1]").click()
        time.sleep(2)

        try:
            elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div[2]/div[2]/table/tbody/tr[4]/th")
            assert True

        except NoSuchElementException:
            self.fail("Book was not added")
            assert False

    time.sleep(3)

def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()

