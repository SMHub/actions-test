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

app_url = D.comp_overview_url



class Test(TestCase):
    
    @classmethod
    def setUpClass(cls):
        U.start_browser()
        U.go_to(app_url, 1)

    @classmethod
    def tearDownClass(cls):
        U.quit()

    def setUp(self):
        print("-test started")

    def tearDown(self):
        print(" -test complete")

    def test_01_verify_page_title(self):
        assert E.comp_overview_title == U.get_title()
        

    def test_02_verify_page_banner(self):
        self.assertEqual(E.page_banner, U.get_text(L.header_2))

    def test_03_verify_left_tabs(self):
        ''' partial match of items '''
        self.assertTrue(U.partial_match(E.left_tabs, U.get_texts(L.tab)))

    def test_04_verify_search_compontent(self):
        U.type_into_text_box(1, 'button', 3)
        self.assertEqual("3 components found",  U.get_text("//span[@id='component-count']"))

    def test_05_verify_button_groups(self):
        U.click("(//a[contains(.,'Button')])[3]", 5)
        self.assertTrue(U.is_element_present("(//button[contains(.,'Default')])[1]"))
   
    def test_06_verify_file_upload(self):
        U.go_to(D.uswds_url+'/components/file-input/#file-input-preview')
        file_path = '\\asset\\sample_1.txt'
        U.upload_file(file_path)

    def test_07_verify_select(self):
        U.go_to(D.uswds_url+'/components/select')
        self.assertTrue(U.select_option('Option A'))





if __name__ == '__main__':
    unittest.main()