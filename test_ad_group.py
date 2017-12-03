# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_ad_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_ad_group(self):
        success = True

        self.open_start_page()
        self.login( username="admin", password="secret")
        self.open_groups_page()
        self.create_group( Group(group_name="ddfg", header="4fff", footer="fbhj"))
        self.return_to_groups_page()
        self.logout()
        self.assertTrue(success)

    def test_ad_empty_group(self):
        success = True

        self.open_start_page()
        self.login( username="admin", password="secret")
        self.open_groups_page()
        self.create_group( Group(group_name="", header="", footer=""))
        self.return_to_groups_page()
        self.logout()
        self.assertTrue(success)

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        #init group creation
        wd = self.wd
        wd.find_element_by_name("new").click()
        #fill group
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        #submit
        wd.find_element_by_name("submit").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_start_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
