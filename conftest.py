import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', default='ru')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    language = request.config.getoption("language")
    options = Options()
    browser = None
    if language == "ru":
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome("./chromedriver", options=options)
    elif language == "es":
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome("./chromedriver", options=options)
    elif language == "fr":
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome("./chromedriver", options=options)
    yield browser
    browser.quit()