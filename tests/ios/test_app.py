from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_text_output():
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('hello@browserstack.com' + '\n')

    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('hello@browserstack.com'))
