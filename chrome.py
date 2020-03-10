import os
import time
from selenium import webdriver


class Chrome:

    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.web = webdriver.Chrome(os.getcwd() + '/chromedriver')
        # self.web = webdriver.Chrome(os.getcwd() + '/chromedriver', options=options)

    def get_url(self, url):
        self.web.get(url)

    def load_element(self, element, element_to_compare=None):
        for i in range(100):
            time.sleep(.1)
            results = self.web.find_elements_by_xpath('//' + element)
            if element is None:
                continue
            elif len(results) == 1:
                return results[0]
            elif results != element_to_compare:
                return results

        return results
