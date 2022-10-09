from bs4 import BeautifulSoup
import urllib.request as req

code = req.urlopen("https://www.naver.com/")
soup = BeautifulSoup(code, "html.parser")
naver_string = soup.select_one("a#NM_set_home_btn")


title = soup.select("a.nav")
for i in title:
    print(i.text)