import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class hooqTestExample(unittest.TestCase):

    def setUp(self):
        hooq = DesiredCapabilities.CHROME
        self.driver = webdriver.Remote(desired_capabilities=hooq)

    def check_title_page(self):
        self.driver.get("https://m-nightly.hooq.tv")
        assert "HOOQ.TV" in self.driver.title

    def press_button_register(self):
        button_sign_up = self.driver.find_element_by_id("mount")
        button_sign_up.click()

    def press_button_signup_email(self):
        button_signup_email = self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div[1]/a")
        button_signup_email.click()

    def input_email(self, email):
        input_email = self.driver.find_element_by_id("email")
        input_email.click()
        input_email.send_keys(email)

    def input_password(self, password):
        input_password = self.driver.find_element_by_id("password")
        input_password.click()
        input_password.send_keys(password)

    def button_berikutnya(self):
        button_next = self.driver.find_element_by_id("email_form")
        button_next.click()

    def button_skip(self):
        button_skip = self.driver.find_element_by_id("payment-mount")
        button_skip.click()

    def check_title_success_signup(self):
        title_success = self.driver.find_element_by_css_selector("#responsiveTabs>div>div.innerTab>h5>b")
        assert title_success, " Akun gratis kamu berhasil dibuat! "

    def press_button_start_signup(self):
        button_start_signup = self.driver.find_element_by_id("responsiveTabs")
        button_start_signup.click()

    def start_signup_hooq(self, email, password):
        self.check_title_page()
        self.press_button_register()
        self.press_button_signup_email()
        self.input_email(email)
        self.input_password(password)
        self.button_berikutnya()
        self.button_skip()
        self.check_title_success_signup()
        self.press_button_start_signup()

    def test_sign_up_by_email(self):
        self.start_signup_hooq('faizal@mailinator.com', 'faiz1234')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()