
from selenium import webdriver
from pytest import mark

@mark.ui
@mark.entertainment
def test_can_navigate_to_entertainment_page(chrome_browser):
    #browser = webdriver.Chrome(executable_path='/Users/hilalkocak/PycharmProjects/udemyTest/chromedriver')
    #browser.get('https://www.siriusxm.com/')
    chrome_browser.get('https://www.siriusxm.com/')
    assert True