import unittest
import time
from tests_1.base_test_case import BaseTestCase


class TestCase(BaseTestCase):

    class TestSettings:
        hotels = ".hotels"
        where = ".brand-trip-search-geopill-flyout-geoPillCommon__overlayContents--yWQ_N"
        click_to_where = ".input-text-input-ManagedTextInput__managedInput--106PS"
        popularne_miejsca = "POPULARNE MIEJSCA"
        alert = "/html/body/div[12]/div/div[2]"

    def test_hotels(self):
        self.find_hotel()

    def find_hotel(self):
        alert = self.driver.find_element_by_xpath(self.TestSettings.alert)
        alert.click()
        hotels = self.driver.find_element_by_css_selector(self.TestSettings.hotels)
        hotels.click()
        where = self.driver.find_element_by_css_selector(self.TestSettings.where)
        self.assertTrue(where.is_displayed())
        self.assertTrue(self.TestSettings.popularne_miejsca in where.text)
        time.sleep(2)
        click_to_where = self.driver.find_element_by_css_selector(self.TestSettings.click_to_where)
        click_to_where.click()
        click_to_where.send_keys("Grecja Santorini")


if __name__ == "__main__":
    unittest.main(verbosity=1)