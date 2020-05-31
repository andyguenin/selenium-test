import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

if __name__ == '__main__':
    driver = webdriver.Chrome()
    xpath = '//input[@name="q"]'

    driver.get('https://google.com')

    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, xpath)))

    input = driver.find_elements_by_xpath(xpath)[0]
    action = ActionChains(driver)
    action.move_to_element_with_offset(input, 1, 1)
    action.click()
    action.perform()

    input.send_keys('python selenium binding')
    input.send_keys(Keys.RETURN)


    time.sleep(20)
