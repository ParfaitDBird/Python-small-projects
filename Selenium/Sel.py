from selenium import webdriver

FF_browser = webdriver.Firefox()
FF_browser.firefox_profile("--incognito")
FF_options = webdriver.FirefoxOptions()
FF_options.add_argument("--Incognito")
FF_browser.maximize_window()
FF_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in FF_browser.title

popup = FF_browser.find_element_by_class_name('at-cm-no-button')
popup.click()


button_text = FF_browser.find_element_by_class_name("btn-default")
print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in FF_browser.page_source

user_message = FF_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I AM A MO****** T-REX')

show_message_button = FF_browser.find_element_by_class_name("btn-default")
show_message_button.click()
FF_browser.close()
