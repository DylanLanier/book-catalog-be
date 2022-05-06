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

        driver = self.driver
        driver.maximize_window()
        driver.get("https://illustrious-fenglisu-42aedd.netlify.app")
        time.sleep(10)
        elem=driver.find_element(by=By.XPATH, value="/html/body/div/ul/li[3]/a").click()
        time.sleep(5)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div/div/div[2]/div/div/input[1]")
        elem.send_keys(user)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div/div/div[2]/div/div/input[2]")
        elem.send_keys(pwd)
        time.sleep(3)
        elem = driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div/div/div/div[2]/button").click()
        time.sleep(3)
        # assert "Logged In"
        try:
            # attempt to find 'Logout' button - if found, logged in
            elem = driver.find_element(by=By.XPATH, value="/html/body/div/ul/li[3]/a")

            assert True

        except NoSuchElementException:
            self.fail("Login Failed - user may not exist")
            assert False

        time.sleep(3)

def teardown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()