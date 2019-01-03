import unittest
from tests_1.base_test_case import BaseTestCase
from selenium.webdriver.common.keys import Keys


class TestCase(BaseTestCase):

    class TestSettings:
        about_us = "O nas"
        change_tab = "BODY_BLOCK_JQUERY_REFLOW"
        link_1 = "Informacje"
        link_2 = "Relacje z inwestorami"
        new_site = "Wróć do TripAdvisor"
        alert = "/html/body/div[12]/div/div[2]"

    def test_about_us(self):
        self.driver.execute_script("window.scrollTo(0,5000)")
        self.about_us()

    def about_us(self):
        alert = self.driver.find_element_by_xpath(self.TestSettings.alert)
        alert.click()
        about_us = self.driver.find_element_by_link_text(self.TestSettings.about_us)
        self.assertTrue(self.TestSettings.about_us in about_us.text)
        about_us.click()
        self.driver.find_element_by_id(self.TestSettings.change_tab).send_keys(Keys.CONTROL + Keys.TAB)
        self.driver.switch_to.window(self.driver.window_handles[1])
        new_site = self.driver.find_element_by_link_text(self.TestSettings.new_site)
        self.assertTrue(new_site.text in self.TestSettings.new_site)
        self.assertTrue(new_site.is_displayed())


if __name__ == "__main__":
    unittest.main(verbosity=1)
