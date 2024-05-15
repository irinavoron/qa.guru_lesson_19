from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_text_output():
    # text_button = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Text Button'))
    # )
    # text_button.click()
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button'))
    
    # text_input = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Text Input'))
    # )
    # text_input.send_keys('hello@browserstack.com' + '\n')
    # time.sleep(5)
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).type('hello@browserstack.com' + '\n')
    
    # text_output = WebDriverWait(driver, 30).until(
    #     EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Text Output'))
    # )
    # if text_output != None and text_output.text == 'hello@browserstack.com':
    #     assert True
    # else:
    #     assert False
    # 
    browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('hello@browserstack.com'))
