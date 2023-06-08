from utility import utility
from locators import locators
from expect import expect
from data import data


U = utility.Util()
L = locators.Common()
E = expect.Common()
D = data.Common()


class Common:

    def login(self):
        U.type_text(L.LOGIN_EMAIL, D.email_4, 0)
        U.type_text(L.LOGIN_PASSWORD, D.pwd_4, 0)
        U.click(L.LOGIN_BTN, 1)
        return "Logout" in U.get_text(L.LOGOUT_TAB)