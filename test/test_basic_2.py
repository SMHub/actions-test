import datetime, os
from unittest import TestCase
from utility import utility
from locators import locators
from expect import expect
from data import data
from actions import actions

U = utility.Util()
L = locators.Common()
E = expect.Common()
D = data.Common()
A = actions.Common()

APP_URL = 'https://www.python.org/'


class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        U.start_browser()

    @classmethod
    def tearDownClass(cls):
        U.quit()

    def setUp(self):
        U.go_to(APP_URL, 0)

    def tearDown(self):
        print('test ended')




    def test_1_verify_page_title(self):
        assert 'Python.org' in U.get_title()

    def test_2_verify_page_title(self):
        assert 'Python.org2' in U.get_title()


