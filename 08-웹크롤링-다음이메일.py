from selenium import webdriver
from chromedriver_autoinstaller import install
import time

browser = webdriver.Chrome(install())
browser.get("https://accounts.kakao.com/login?continue=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fwww.daum.net")
# 로그인 하기
kakao_id = browser.find_element_by_css_selector("input#id_email_2")
kakao_id.send_keys("osj5137@naver.com")

pw = browser.find_element_by_css_selector("input#id_password_3")
pw.send_keys("osj38955137")

button = browser.find_element_by_css_selector("form#login-form button.btn_confirm")
button.click()
time.sleep(2) # 로그인 대기 시간

# 이메일함으로 이동
browser.get("https://mail.daum.net/")
time.sleep(2) # 이메일함이 다 뜰 때까지 기다리기
# 이메일 제목 크롤링
page_num = 1
while True:
    title = browser.find_elements_by_css_selector("strong.tit_subject")
    for i in title:
        print(i.text)
    page_num+=1
    # 모든 페이지 버튼들 크롤링
    page_buttons = browser.find_elements_by_css_selector("a.link_page")
    for i in page_buttons:
        if int(i.text) == page_num:
            i.click()
            time.sleep(1)
            break
    else: # 끝 페이지 이상으로 왔다면?
        break

browser.close()