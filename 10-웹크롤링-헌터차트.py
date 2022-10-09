from selenium import webdriver
from chromedriver_autoinstaller import install
import time

browser = webdriver.Chrome(install())
browser.get("https://www.hanteochart.com/chart/world/weekly")
time.sleep(2)

for i in range(4):
    see_more_btn = browser.find_element_by_css_selector("div.see-more-btn")
    see_more_btn.click()
    time.sleep(0.3)

items = browser.find_elements_by_css_selector("div.chart-item-b.rank-data.single-col.single-stat.long")
num = 1
for item in items:
    title = item.find_element_by_css_selector("div.center div.top").text
    try:
        team = item.find_element_by_css_selector("pre.left").text
    except:
        team = ""
    worldindex = item.find_element_by_css_selector("div.stat-container > div.left").text
    print(f"<{num}>")
    print(f"가수 : {title}")
    print(f"소속사 : {team}")
    print(f"wordIndex : {worldindex}")
    print("-----------------------------------------")
    num += 1