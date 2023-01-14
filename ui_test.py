# selenium 4
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import logging
import logging.handlers

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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

    def test_01_get_title(self):
        driver.get('https://www.python.org/')
        title = driver.title
        log_msg(msg=title)
        driver.quit()
        print(title)
        assert 'Python.org' in title


if __name__ == '__main__':
    unittest.main()