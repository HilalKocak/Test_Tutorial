
from pytest import mark
from selenium import webdriver

@mark.smoke
@mark.body
class BodyTests:
    @mark.ui
    def test_can_navigate_to_body_page(self, chrome_browser):
        #browser = webdriver.Chrome(executable_path='/Users/hilalkocak/PycharmProjects/udemyTest/chromedriver')
        #browser.get('http://www.motortrend.com/')
        chrome_browser.get('http://www.motortrend.com/')
        assert True

    def test_bumper(self):
        assert True

    def test_windshield(self):
        assert True
