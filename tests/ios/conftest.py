from appium import webdriver
from appium.options.ios import XCUITestOptions
from selene import browser
import pytest

from config import config


@pytest.fixture(autouse=True, scope='function')
def mobile_ios_management():
    options = XCUITestOptions().load_capabilities({
        'app': config.APP_URL,

        'deviceName': 'iPhone 11 Pro',
        'platformName': 'ios',
        'platformVersion': '13',

        'bstack:options': {
            'userName': config.BS_USER,
            'accessKey': config.BS_ACCESS_KEY,
            'projectName': 'First Python project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test'
        }
    })

    browser.config.driver = webdriver.Remote(config.BS_URL, options=options)
    browser.config.timeout = config.TIMEOUT

    yield

    browser.quit()
