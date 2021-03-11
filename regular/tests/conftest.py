import pytest
from selenium import webdriver
from regular.tests import config


def pytest_addoption(parser):
    parser.addoption("--baseurl",
                     action="store",
                     default="http://the-internet.herokuapp.com",
                     help="base URL for the application under test")
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="the name of the browser you want to test with")
    parser.addoption("--host",
                     action="store",
                     default="selenoid",
                     help="where to run your tests: localhost or selenoid")
    parser.addoption("--browserversion",
                     action="store",
                     default="85.0",
                     help="the browser version you want to test with")


@pytest.fixture
def driver(request):
    global driver

    config.baseurl = request.config.getoption("--baseurl")
    config.browser = request.config.getoption("--browser").lower()
    config.host = request.config.getoption("--host").lower()
    config.browserversion = request.config.getoption("--browserversion").lower()

    if config.host == "selenoid":

        if config.browser == 'chrome':
            desiredCapabilities = {
                "browserName": "chrome",
                "version": f"{config.browserversion}",
                "enableVNC": True,
                "enableVideo": False,
                "screenResolution": "1920x1080x24"
            }

            chromeOptionsRemote = webdriver.ChromeOptions()
            chromeOptionsRemote.add_argument('--window-size=1920,1080')
            chromeOptionsRemote.add_argument("--disable-session-crashed-bubble")
            driver = webdriver.Remote(options=chromeOptionsRemote, command_executor='http://192.168.0.194'
                                                                                    ':80/wd/hub',
                                      desired_capabilities=desiredCapabilities)
        elif config.browser == 'firefox':
            desiredCapabilities = {
                "browserName": "firefox",
                "version": "80.0",
                "enableVNC": True,
                "enableVideo": False,
                "screenResolution": "1920x1080x24"
            }
            fireOptionsRemote = webdriver.FirefoxOptions()
            fireOptionsRemote.add_argument('--window-size=1920,1080')
            fireOptionsRemote.add_argument("--disable-session-crashed-bubble")
            driver = webdriver.Remote(options=fireOptionsRemote, command_executor='http://localhost'
                                                                                  ':4444/wd/hub',
                                      desired_capabilities=desiredCapabilities)
            driver.set_window_size(1920, 1080)
        return driver

    elif config.host == "localhost":
        path = "/Users/dmytro.maksymov/PycharmProjects/self/regular/drivers/chromedriver"
        driver = webdriver.Chrome(executable_path=path)

