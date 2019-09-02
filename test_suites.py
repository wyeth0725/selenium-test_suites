import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod 

class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(r"C:\Users\koga\Documents\chromedriver_win32\chromedriver.exe")
        cls.driver.implicitly_wait(15)
        cls.driver.get("https://www.monotaro.com")

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))
    
    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, "new_nav"))

    def test_shopping_cart_empty_message(self):
        #id指定
        shopping_cart_icon = self.driver.find_element_by_css_selector("#globalMenu__menu--basket")
        shopping_cart_icon.click()
        #class指定
        shopping_cart_status = self.driver.find_element_by_css_selector("p.basket__iteNone__message").text
        self.assertEqual("現在バスケットには何も入っていません。", shopping_cart_status)
        #class指定
        close_button = self.driver.find_element_by_css_selector("a.basket__iteNone__link")
        close_button.click()
    
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as e:
            return False
        return True 
    
@classmethod
def tear_down(cls):
    cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)


    
