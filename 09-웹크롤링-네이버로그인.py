import pyperclip
from selenium import webdriver
from chromedriver_autoinstaller import install
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def input_id_pw(browser, css, id_or_pw):
    pyperclip.copy(id_or_pw)  # id 복사
    blank = browser.find_element_by_css_selector(css)
    blank.click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

    time.sleep(1)  # 완전범죄


browser = webdriver.Chrome(install())
browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
time.sleep(1)

input_id_pw(browser, "input#id", "osj5137@naver.com")
input_id_pw(browser, "input#pw", "jin51378946MIZ55")

button = browser.find_element_by_css_selector("button.btn_login")
button.click()
time.sleep(3)
