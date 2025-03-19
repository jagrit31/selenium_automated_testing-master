from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time, random


class BaseScreen(object):
    """Base class for other Page Objects"""

    def __init__(self, driver):
        self.driver = driver
        self.title = driver.instance.title

    def select_element(self, locator):
        """Select an element by waiting for it to become visible"""
        wait = WebDriverWait(self.driver.instance, 10)
        element = wait.until(EC.visibility_of_element_located(locator))
        return element

    def select_elements(self, locator):
        """Select multiple element by waiting for them to become visible"""
        wait = WebDriverWait(self.driver.instance, 10)
        elements = wait.until(EC.visibility_of_all_elements_located(locator))
        return elements

    def wait_until_clickable(self, locator):
        wait = WebDriverWait(self.driver.instance, 10)
        element = wait.until(EC.element_to_be_clickable(locator))
        return element

    def page_title_equals_to(self, title):
        assert self.title == title

    def take_screenshot(self):
        """Take a screenshot with a defined name based on the time and the browser"""
        millis = int(round(time.time() * 1000))
        if self.driver.name:
            driver_name = self.driver.name
        else:
            driver_name = ""
        self.driver.save_screenshot("screenshots/{}-{}-screenshots.png".format(driver_name, millis))

    def hover_one_of_elements(self, locator):
        """Hover a randomly chosen element from a list of elements
        :return: string
        """
        webelements = WebDriverWait(self.driver.instance, 10).until(
            EC.visibility_of_all_elements_located(locator)
        )
        webelement = random.choice(webelements)
        webdriver.ActionChains(self.driver.instance).move_to_element(webelement).perform()
        return webelement

    def mouse_hover(self, element):
        """Hover the mouse over element
        :return: None
        """
        webdriver.ActionChains(self.driver.instance).move_to_element(element).perform()

    def is_element_visible(self, locator, timeout=7):
        """Checks if element is visible within given timeout
        :param timeout: int
        :return: boolean
        """
        try:
            is_visible = WebDriverWait(self.driver.instance, timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            is_visible = False

        return bool(is_visible)
