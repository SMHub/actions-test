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

    def screenshot_on_fail(func):
        def wrapper(arg):
            try:
                func(arg)
            except:
                print("test failed", "{0}".format(func.__name__))
                U.take_screenshot("{0}".format(func.__name__))
                raise

        return wrapper

    @U.screenshot_on_fail
    def test_1_show_error_messages_when_required_fields_are_empty(self):
        U.click(L.LOGIN_BTN)
        assert E.ERR_EMAIL_REQUIRED == U.get_texts(L.INPUT_ERR_MSG)

    def test_2_show_error_messages_for_invalid_credentials(self):
        U.type('Enter Email', "Admin")
        U.type('Enter Password', "admin12")
        U.click_button('Login', 0)
        assert E.ERR_EMAIL_REQUIRED in U.get_texts(L.INPUT_ERR_MSG)

    def test_3_show_correct_error_message_for_invalid_credentials(self):
        def enter_credentials(email, password):
            U.type_text(L.LOGIN_EMAIL, email)
            U.type_text(L.LOGIN_PASSWORD, password)
            U.click(L.LOGIN_BTN, 0)
            err_msg = U.get_texts(L.INPUT_ERR_MSG)
            print(err_msg)
            return err_msg

        credentials = [('wrong@mail.com', 'wrong_pwd'), ('sm4@mail.com', 'wrong_pwd'), ('wrong@mail.com', '123123')]
        results = []
        for cred in credentials:
            err_msg = 'Password is incorrect.' if 'sm4' in cred[0] else E.ERR_EMAIL_REQUIRED
            result = err_msg in enter_credentials(cred[0], cred[1])
            results.append(result)
            print(result, cred)
        assert all(results)

    def test_4_login_with_valid_credentials(self):
        # U.type_text(L.LOGIN_EMAIL, D.email_4, 0)
        # U.type_text(L.LOGIN_PASSWORD, D.pwd_4, 0)
        # U.click(L.LOGIN_BTN, 1)
        # assert "Logout" in U.get_text(L.LOGOUT_TAB)
        assert A.login()

    def test_05(self):
        U.go_to()
        U.get_text()
        U.type('Enter Email', 'sm@mail.com')
        U.click_button('Save')
