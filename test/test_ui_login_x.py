import datetime, os
from unittest import TestCase

import pytest

from test.utility import utility
from test.Test import locators, expect, data
from test.Test import library_main

U = utility.Util()
L = locators.Common()
E = expect.Common()
D = data.Common()
A = library_main.Actions()

APP_URL = "http://127.0.0.1:5000"


class Login(TestCase):

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


    def test_1_show_error_messages_when_required_fields_are_empty(self):
        U.click(L.LOGIN_BTN)
        assert E.ERR_EMAIL_REQUIRED == U.get_texts(L.INPUT_ERR_MSG)

    def test_2_show_error_messages_when_required_fields_are_empty(self):
        U.click(L.LOGIN_BTN)
        assert E.ERR_EMAIL_REQUIRED == U.get_texts(L.INPUT_ERR_MSG)
