from pytest import fixture

from selenium import webdriver

#@fixture(scope = 'function') opens different browser for each test cases
@fixture(scope = 'session') #works one browser for every test

def chrome_browser():
    browser = webdriver.Chrome(executable_path='/Users/hilalkocak/PycharmProjects/udemyTest/chromedriver')
    #return browser
    yield browser # I dont need that browser anymore
    #Teardown
    print("I am tearing down this browser")

