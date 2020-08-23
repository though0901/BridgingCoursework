from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

MAX_WAIT_TIME = 10


class FunctionalTestClass(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_go_to_cv_then_can_go_to_blog_site(self):
        # go to the cv link
        self.browser.get("http://localhost:8000/cv")

        # the title should say "Tom Hough's CV"
        self.assertIn("Tom Hough's CV", self.browser.title)

        # expect to see 4 h2 tags with all the sectors
        header_twos = self.browser.find_elements_by_tag_name('h2')
        expected = ["Personal Details", "Qualifications", "Projects", "Experiences"]
        outliers = [h for h in header_twos if h.text not in expected]
        self.assertEqual(len(outliers), 0)

        # the cv button should be red as we are on that page
        cv = self.browser.find_element_by_id('cv_redirect')
        color = cv.value_of_css_property('color')
        self.assertEqual('rgb(224, 48, 30)', color)

        # click the button which will send us to the blog page
        # the button which should be white
        blog = self.browser.find_element_by_id('blog_redirect')

        # the button should be white now
        color = blog.value_of_css_property('color')
        self.assertEqual('rgb(255, 255, 255)', color)
        blog.click()

        start_time = time.time()
        while True:
            try:
                # should see the title saying "Tom Hough's Blog"
                self.assertIn("Tom Hough's Blog", self.browser.title)
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT_TIME:
                    raise e
                time.sleep(0.5)

        # when arriving at the new page the same button should now be red in colour
        blog = self.browser.find_element_by_id('blog_redirect')
        color = blog.value_of_css_property('color')
        self.assertEqual('rgb(224, 48, 30)', color)

        # now the cv button should now be white
        cv = self.browser.find_element_by_id('cv_redirect')
        color = cv.value_of_css_property('color')
        self.assertEqual('rgb(255, 255, 255)', color)

    def test_check_when_logged_in_can_add_edit_and_remove(self):
        # first go to the cv page then log in
        self.browser.get('http://localhost:8000/cv/')
        login_button = self.browser.find_element_by_id('login_button')
        login_button.click()

        start_time = time.time()
        while True:
            try:
                username = self.browser.find_element_by_id('id_username')
                password = self.browser.find_element_by_id('id_password')
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT_TIME:
                    raise e
                time.sleep(0.5)

        username.send_keys('TestUser')
        password.send_keys('TestUser')
        password.send_keys(Keys.ENTER)

        # want to see if we are now at the cv page
        start_time = time.time()
        while True:
            try:
                self.assertEqual(len(self.browser.find_elements_by_tag_name('h2')), 4)
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT_TIME:
                    raise e
                time.sleep(0.5)

        # at this point edit some personal details and save
        personal_details_edit = self.browser.find_element_by_id("personal_details_edit")
        personal_details_edit.click()

        name_field = self.browser.find_element_by_id('id_name')
        name_field.clear()
        flag = (name_field.text == 'Tom Hough')
        if flag:
            name_field.send_keys('Thomas Hough')
        else:
            name_field.send_keys('Tom Hough')
        name_field.send_keys(Keys.ENTER)

        while True:
            try:
                self.assertEqual(len(self.browser.find_elements_by_tag_name('h2')), 4)
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT_TIME:
                    raise e
                time.sleep(0.5)

        # see if the changes are present
        name = self.browser.find_element_by_id("name").text
        if flag:
            self.assertEqual("Name: Thomas Hough", name)
        else:
            self.assertEqual("Name: Tom Hough", name)

        # create a new qualification
        qual_new = self.browser.find_element_by_id("qual_new")
        qual_new.click()

        while True:
            try:
                self.assertEqual("New Qualification", self.browser.find_element_by_tag_name('h2').text)
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT_TIME:
                    raise e
                time.sleep(0.5)

        institution, grades = self.browser.find_element_by_id("id_institution"), self.browser.find_element_by_id(
            "id_grades")
        institution.send_keys("SCHOOL 1")
        grades.send_keys("Subject Alpha A*")
        institution.send_keys(Keys.ENTER)

        while True:
            try:
                self.assertEqual(len(self.browser.find_elements_by_tag_name('h2')), 4)
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT_TIME:
                    raise e
                time.sleep(0.5)

        # check the changes
        paragraphs = self.browser.find_elements_by_tag_name('p')
        self.assertIn("Subject Alpha A*", [p.text for p in paragraphs])

        # edit said qualification
        edit_button = self.browser.find_element_by_id("qual_edit1")
        edit_button.click()

        while True:
            try:
                self.assertEqual("Edit Qualification", self.browser.find_element_by_tag_name('h2').text)
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT_TIME:
                    raise e
                time.sleep(0.5)

        institution, grades = self.browser.find_element_by_id("id_institution"), self.browser.find_element_by_id(
            "id_grades")
        grades.clear()
        grades.send_keys("Subject Beta A*")
        institution.send_keys(Keys.ENTER)

        # check changes, delete this qualification
        while True:
            try:
                self.assertEqual(len(self.browser.find_elements_by_tag_name('h2')), 4)
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT_TIME:
                    raise e
                time.sleep(0.5)

        paragraphs = self.browser.find_elements_by_tag_name('p')
        self.assertIn("Subject Beta A*", [p.text for p in paragraphs])

        remove = self.browser.find_element_by_id("qual_remove1")
        remove.click()

        while True:
            try:
                self.assertEqual(len(self.browser.find_elements_by_tag_name('h2')), 4)
                break
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT_TIME:
                    raise e
                time.sleep(0.5)

        paragraphs = self.browser.find_elements_by_tag_name('p')
        self.assertNotIn("Subject Beta A*", [p.text for p in paragraphs])

if __name__ == '__main__':
    unittest.main(warnings='ignore')
