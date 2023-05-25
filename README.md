# Selenium Automated Test
GUI automated test with Selenium and Python

## Getting started

### Supported Python Versions
Python 3.7+

### Installing

    pip install -r requirements.txt

### Drivers
Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it's in your PATH,e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.

| Browser        |    Driver    | Download url                                |
| ------------- |:------------:|:--------------------------------------------|
| Chrome      | chromedriver | https://chromedriver.chromium.org/downloads |
| Edge      | msedgedriver | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/                                        |
| Firefox | geckodriver  | https://github.com/mozilla/geckodriver/releases                                          |
| Safari      | safaridriver | https://webkit.org/blog/6900/webdriver-support-in-safari-10/ |


### Example 0:
1.  open a new Firefox browser
2. load the page at the given URL

Here is Python's code

    
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('http://selenium.dev/')


### Example 1:
1. open a new Firefox browser
2. load the Yahoo homepage
3. search for "seleniumhq"
4. close the browser

Here is Python's code


    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    
    browser = webdriver.Firefox()
    
    browser.get('http://www.yahoo.com')
    assert 'Yahoo' in browser.title
    
    elem = browser.find_element(By.NAME, 'p')  # Find the search box
    elem.send_keys('seleniumhq' + Keys.RETURN)
    
    browser.quit()


### Example 2:
Here is a simple example using Python's standard unittest library:

    import unittest
    from selenium import webdriver
    
    class GoogleTestCase(unittest.TestCase):

        def setUp(self):
            self.browser = webdriver.Firefox()
            self.addCleanup(self.browser.quit)
    
        def test_page_title(self):
            self.browser.get('http://www.google.com')
            self.assertIn('Google', self.browser.title)
    
    if __name__ == '__main__':
        unittest.main(verbosity=2)
# SMS-AutoTest
GUI automated test with Selenium and Python

## Getting started

### Supported Python Versions
Python 3.7+

### Installing

    pip install -r requirements.txt

### Drivers
Selenium requires a driver to interface with the chosen browser. Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. Make sure it's in your PATH,e. g., place it in /usr/bin or /usr/local/bin.

Failure to observe this step will give you an error selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.

| Browser        |    Driver    | Download url                                |
| ------------- |:------------:|:--------------------------------------------|
| Chrome      | chromedriver | https://chromedriver.chromium.org/downloads |
| Edge      | msedgedriver | https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/                                        |
| Firefox | geckodriver  | https://github.com/mozilla/geckodriver/releases                                          |
| Safari      | safaridriver | https://webkit.org/blog/6900/webdriver-support-in-safari-10/ |


### Example 0:
1.  open a new Firefox browser
2. load the page at the given URL

Here is Python's code

    
    from selenium import webdriver
    browser = webdriver.Chrome()
    browser.get('http://selenium.dev/')


### Example 1:
1. open a new Firefox browser
2. load the Yahoo homepage
3. search for "seleniumhq"
4. close the browser

Here is Python's code


    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    
    browser = webdriver.Firefox()
    
    browser.get('http://www.yahoo.com')
    assert 'Yahoo' in browser.title
    
    elem = browser.find_element(By.NAME, 'p')  # Find the search box
    elem.send_keys('seleniumhq' + Keys.RETURN)
    
    browser.quit()


### Example 2:
Here is a simple example using Python's standard unittest library:

    import unittest
    from selenium import webdriver
    
    class GoogleTestCase(unittest.TestCase):

        def setUp(self):
            self.browser = webdriver.Firefox()
            self.addCleanup(self.browser.quit)
    
        def test_page_title(self):
            self.browser.get('http://www.google.com')
            self.assertIn('Google', self.browser.title)
    
    if __name__ == '__main__':
        unittest.main(verbosity=2)
