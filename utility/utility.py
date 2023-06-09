import datetime, os
from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeType
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import logging
import logging.handlers

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())

chrome_options = Options()
options = [

"--disable-gpu",
"--window-size=1920,1200",
"--ignore-certificate-errors",
"--disable-extensions",
"--no-sandbox",
"--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

# "--headless",
cwd = os.getcwd()


class Util:


    def start_browser(self):
        global driver
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        print(" Chrome started")


    def go_to(self, url, wait=3):
        driver.get(url)
        driver.maximize_window()
        print("Page loaded: "+url)
        sleep(wait)

    def get_title(self):
        return driver.title



    def wait_until_loads(self, locator):
        loaded = self.get_elements(locator)
        i = 0
        text = 'loaded in'
        loaded = self.get_elements(locator)
        while not loaded:
            sleep(.25)
            i = i + 1
            loaded = self.get_elements(locator)
            if i == 80:
                text = 'time out in'
                break  # Just timeout
        if i > 2: print('Element with', locator, text, str(int(i / 4)), 'second(s)')
        return loaded

    def get_elements(self, locator):
        """ first function to locate elements """
        if "//" in locator:
            eles = driver.find_elements(By.XPATH, locator)

        elif 'link*=' in locator:
            locator = str(locator).split('=')[1]
            eles = driver.find_elements(By.PARTIAL_LINK_TEXT, locator)

        elif 'link' in locator:
            locator = str(locator).split('=')[1]
            eles = driver.find_elements(By.LINK_TEXT, locator)

        else:
            eles = driver.find_elements(By.CSS_SELECTOR, locator)
        return eles

    def get_element(self, locator):
        # SM 211021-Do not edit this core function
        self.wait_until_loads(locator)
        if "//" in locator:
            ele = driver.find_element(By.XPATH, locator)
        elif 'link*=' in locator:
            ele = driver.find_element(By.PARTIAL_LINK_TEXT, str(locator).split('=')[1])
        elif 'link=' in locator:
            ele = driver.find_element(By.LINK_TEXT, str(locator).split('=')[1])
        else:
            ele = driver.find_element(By.CSS_SELECTOR, locator)
        return ele

    def get_texts(self, locator, wait=True):
        if wait: self.wait_until_loads(locator)
        eles = self.get_elements(locator)
        return [str(ele.text).strip() for ele in eles]

    def click(self, locator, wait=1):
        self.get_element(locator).click()
        print(" - clicked ", locator)
        sleep(wait)

    def click_btn(self, locator, wait=1):
        driver.find_element(By.XPATH, locator).click()
        sleep(wait)


    def click_button(self, button_name, wait=1):
        locator = "//button[contains(.,'{}')]".format(button_name)
        self.highlight(locator)
        self.click(locator, wait)

    def type(self, placeholder, text, wait=1, clear=True):
        locator = "//input[@placeholder='{}']".format(placeholder)
        self.highlight(locator)
        self.type_text(locator, text, wait, clear)


    def type_text(self, locator, text, wait=1, clear=True):
        if clear: self.get_element(locator).clear()
        sleep(wait)
        self.get_element(locator).send_keys(text)
        print(" entered ", text, "into", locator)

    def type_into_text_box(self, pos=1, text='', wait=3):
        locator = "(//input[@type='text'])[{}]".format(pos)
        self.type_text(locator, text, wait)

    def get_text(self, locator):
        self.highlight(locator)
        return self.get_element(locator).text

    def quit(self):
        driver.quit()
        driver.stop_client()

    def upload_file(self, file_path):
        # file should be in 'data\asset' directory
        full_file_path = str(os.getcwd()).split('\\test')[0]+'\\data'+file_path  # '/test' for linux
        self.type_text("//input[@type='file']", full_file_path, 3, False)
        print(' - uploaded file', file_path)

    def is_element_present(self, locator):
        return len(self.get_elements(locator)) > 0

    def select_option(self, option_text):
        """ opt_loc locator may vary in applications"""
        try:
            opt_loc = "//select[@id='options']/option[text()='{}']".format(option_text)
            self.click(opt_loc, 3)
            return True
        except:
            return "Locator Err"
    # basic functions
    def highlight(self, locator):
        element = self.get_element(locator)
        previous_style = element.get_attribute("style")
        driver.execute_script(
            "arguments[0].setAttribute("
            "'style', 'border: 2px solid blue; font-weight: bold;'"
            ");", element
        )
        driver.execute_script(
            "var target = arguments[0];"
            "var previousStyle = arguments[1];"
            "setTimeout("
            "function() {"
            "target.setAttribute('style', previousStyle);"
            "}, 2000"
            ");", element, previous_style
        )

    def wait(self, wait_sec=3):
        sleep(wait_sec)

    def repeat(self, times):
        def repeat_helper(f):
            def call_helper(*args):
                for i in range(0, times):
                    f(*args)
            return call_helper
        return repeat_helper


    def take_screenshot(self, name):
        path_ss = cwd.replace('test', 'report')+"\\fail_{}.png".format(name)
        print(path_ss)
        driver.save_screenshot(path_ss)

    def screenshot_on_fail(self, func):
        def wrapper(arg):
            try:
                func(arg)
            except:
                print("test failed", "{0}".format(func.__name__))
                self.take_screenshot("{0}".format(func.__name__))
                raise
        return wrapper

    def safe_str(self, obj):
        try:
            return str(obj)
        except UnicodeEncodeError:
            return obj.encode('ascii', 'ignore')

    def partial_match(self, expect, actual, condition=""):
        missing = [item for item in expect if item not in ''.join(map(str, actual))]
        print("", condition)
        print('\tExpected:', expect)
        print('\tActual:', self.safe_str(actual))
        print('\tMissing:', missing)
        print('\tChecked', len(expect), 'items')
        print('\t-------------------------------\n')
        return missing == []

