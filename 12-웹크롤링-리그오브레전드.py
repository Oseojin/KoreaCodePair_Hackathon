from selenium import webdriver
from chromedriver_autoinstaller import install
import time

your_champ = input("상대 챔프 입력 >> ")
browser = webdriver.Chrome(install())
browser.get("https://www.op.gg/champions")
time.sleep(4)

champ_names = browser.find_elements_by_css_selector("a.css-mtyeel.e1y3xkpj0 > span")
for champ_name in champ_names:
    if champ_name.text == your_champ:
        champ_name.click()
        time.sleep(6)
        break

counter_menu = browser.find_element_by_css_selector("a.css-1wm6rnm.e8v1v350")
counter_menu.click()
time.sleep(5)

counter_champs = browser.find_elements_by_css_selector("div.css-aj4kza.eocu2m71")
win_percent = browser.find_elements_by_css_selector("span.css-ekbdas.eocu2m73")
game_num = browser.find_elements_by_css_selector("span.css-1nfew2i.eocu2m75")

for i in range(len(counter_champs)):
    print(f"챔프 : {counter_champs[i].text}")
    print(f"승률 : {win_percent[i].text}")
    print(f"게임 횟수 : {game_num[i].text}")
    print("----------------------------------")

browser.close()