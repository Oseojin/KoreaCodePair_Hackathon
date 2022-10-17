from selenium import webdriver
from chromedriver_autoinstaller import install
import time

from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(install())
browser.get("https://www.youtube.com/watch?v=fhkQcCmkt6s")
time.sleep(6)
# 스크롤 많이 내려서 댓글 생성 시키기
browser.find_element_by_css_selector("html").send_keys(Keys.END)
time.sleep(6)
comments = browser.find_elements_by_css_selector("#content-text")

idx = 0
while True:
    try:
        print(comments[idx].text)
    except:
        print("[알림] 크롤링이 끝났습니다.")
        break
    print("-----------------------------")
    idx += 1
    if idx % 20 == 0:
        browser.find_element_by_css_selector("html").send_keys(Keys.END)
        time.sleep(4)
        comments = browser.find_elements_by_css_selector("#content-text")