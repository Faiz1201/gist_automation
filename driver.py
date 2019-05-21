import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

class shopeeTestExample(unittest.TestCase):

    def setUp(self):
        browser = DesiredCapabilities.CHROME
        self.driver = webdriver.Remote(desired_capabilities=browser)
        self.driver.get("https://gist.github.com/")
        assert "Create a new Gist" in self.driver.title

    #Sign In Github
    def button_sign_in_github(self):
        button_sign_in = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[3]/a[1]')
        button_sign_in.click()

    def input_username_github(self, username):
        input_username = self.driver.find_element_by_id('login_field')
        input_username.click()
        input_username.send_keys(username)

    def input_password_github(self, password):
        input_password = self.driver.find_element_by_id('password')
        input_password.click()
        input_password.send_keys(password)

    def button_log_in_github(self):
        button_login = self.driver.find_element_by_class_name('btn btn-primary btn-block')
        button_login.click()

    #Create Gist
    def logo_gist_homepage(self):
        button_homepage = self.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/a')
        button_homepage.click()

    def input_gist_description(self, desc):
        input_desc = self.driver.find_element_by_name('gist[description]')
        input_desc.click()
        input_desc.send_keys(desc)

    def input_gist_content(self, content):
        input_content = self.driver.find_element_by_name('gist[contents][][name]')
        input_content.click()
        input_content.send_keys(content)

    def input_gist_note(self, note):
        input_note = self.driver.find_element_by_xpath('//*[@id="gists"]/div[2]/div/div[2]/div/div[5]')
        input_note.click()
        input_note.send_keys(note)

    def button_create_public_gist(self):
        button_public = self.driver.find_element_by_class_name('btn js-gist-create ')
        button_public.click()

    def button_create_secret_gist(self):
        button_secret = self.driver.find_element_by_class_name('btn btn-secret js-gist-create ')
        button_secret.click()

    def button_list_gist(self):
        button_list = self.driver.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div/ul/li[3]/a')
        button_list.click()

    def select_list_gist(self):
        list_gist = self.driver.find_element_by_xpath('//*[@id="gist-pjax-container"]/div/div[1]/div[2]/div[2]/div[2]/a')
        list_gist.click()

    def button_edit_gist(self):
        button_edit = self.driver.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[1]/ul/li[1]/a')
        button_edit.click()

    def button_update_gist(self):
        button_update = self.driver.find_element_by_class_name('btn btn-primary')
        button_update.click()

    def button_cancel_gist(self):
        button_cancel = self.driver.find_element_by_xpath('//*[@id="edit_gist_96315569"]/div/div[2]/a')
        button_cancel.click()

    def button_delete_list_gist(self):
        button_delete = self.driver.find_element_by_xpath('//*[@id="gist-pjax-container"]/div[1]/div/div[1]/ul/li[2]/form/button')
        button_delete.click()
        button_delete.send_keys(Keys.RETURN)

    #Command
    def log_in_to_github(self, username, password):
        self.button_sign_in_github()
        self.input_username_github(username)
        self.input_password_github(password)
        self.button_log_in_github()

    def fill_note_gist(self, desc, content, note):
        self.input_gist_description(desc)
        self.input_gist_content(content)
        self.input_gist_note(note)

    def create_public_gist(self, username, password, desc, content, note):
        self.log_in_to_github(username, password)
        self.logo_gist_homepage()
        self.fill_note_gist(desc, content, note)
        self.button_create_public_gist()

    def view_list_gist(self, username, password):
        self.log_in_to_github(username, password)
        self.logo_gist_homepage()
        self.button_list_gist()

    def choose_gist_list(self, username, password):
        self.view_list_gist(username, password)
        self.select_list_gist()

    def edit_list_gist(self, username, password, desc, content, note):
        self.choose_gist_list(username, password)
        self.button_edit_gist()
        self.fill_note_gist(desc, content, note)
        self.button_update_gist()

    def delete_list_gist(self, username, password, desc, content, note):
        self.create_public_gist(username, password, desc, content, note)
        self.button_delete_list_gist()

    #Runner
    def test_create_public_gist(self):
        self.create_public_gist('Faiz1201', 'quantityb4quality', 'Shopee', 'Python', 'Automation Test Public Gist')

    def test_edit_existing_gist(self):
        self.edit_list_gist('Faiz1201', 'quantityb4quality', 'Shopee Mobile', 'Javascript', 'Automation Test Update Gist')

    def test_delete_existing_gist(self):
        self.delete_list_gist('Faiz1201', 'quantityb4quality', 'Shopeeee', 'Java', 'Automation Test Delete Gist')

    def test_view_list_gist(self):
        self.view_list_gist('Faiz1201', 'quantityb4quality')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()