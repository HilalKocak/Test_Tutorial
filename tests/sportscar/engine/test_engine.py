
from pytest import mark
from selenium import webdriver
import time

@mark.smoke
@mark.engine
@mark.ui
def test_can_navigate_to_engine_page(chrome_browser):
    #browser = webdriver.Chrome(executable_path='/Users/hilalkocak/PycharmProjects/udemyTest/chromedriver')
    #browser.get('https://www.artofmanliness.com/skills/manly-know-how/how-a-cars-engine-works/')
    #my_browser= chrome_browser
    #my_browser.get("http://amozon.com/")
    #time.sleep(5)
    second_browser= chrome_browser
    second_browser.get('http://google.com')
    #time.sleep(5)
    chrome_browser.get('http://bilisimsistemleri.mu.edu.tr/tr/yaz-staji-belgeleri-2320')
    assert True
    # Because of the scope just 1 browser can work.