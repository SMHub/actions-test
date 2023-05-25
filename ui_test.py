# selenium 4
import unittest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeType
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import logging
import logging.handlers

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())

chrome_options = Options()
options = [
"--headless",
"--disable-gpu",
"--window-size=1920,1200",
"--ignore-certificate-errors",
"--disable-extensions",
"--no-sandbox",
"--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


def log_msg(msg_type='i', msg='na'):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    logger_file_handler = logging.handlers.RotatingFileHandler(
        "status.log",
        maxBytes=1024 * 1024,
        backupCount=1,
        encoding="utf8",
    )
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logger_file_handler.setFormatter(formatter)
    logger.addHandler(logger_file_handler)
    if msg_type == 'i':
        logger.info(msg)

class Test(unittest.TestCase):

    # def screenshot_on_fail(func):
    #     def wrapper(arg):
    #         try:
    #             func(arg)
    #         except:
    #             print("Test failed", "{0}".format(func.__name__))
    #             driver.save_screenshot("{0}".format(func.__name__))
    #             raise
    #
    #     return wrapper

    def test_01_verify_title(self):
        driver.get('https://www.python.org/')
        title = driver.title
        log_msg(msg='Page loaded:'+title)
        driver.quit()
        print('Page loaded:', title)
        assert 'Python.org' in title

    def test_01_verify_title(self):
        driver.get('https://www.python.org/')
        title = driver.title
        log_msg(msg='Page loaded:'+title)
        driver.quit()
        print('Page loaded:', title)
        assert 'Python.org' in title





if __name__ == '__main__':
    unittest.main()
