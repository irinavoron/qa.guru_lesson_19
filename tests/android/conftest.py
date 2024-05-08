import os
import pytest
from dotenv import load_dotenv
from selene import browser
from appium.options.android import UiAutomator2Options
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def mobile_management():
    load_dotenv()
    name = os.getenv('BS_USER')
    access_key = os.getenv('BS_ACCESS_KEY')

    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": name,
            "accessKey": access_key
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    browser.config.timeout = float(os.getenv('TIMEOUT', '15.0'))

    yield

    browser.quit()
