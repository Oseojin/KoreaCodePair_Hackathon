import time
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par

keyword = input("검색 키워드 입력 >> ")
encoded = par.quote(keyword)
page_num = 1
while True:
    url = f"https://underkg.co.kr:44391/?act=&vid=&mid=news&category=&search_keyword={encoded}&search_target=title_content&page={page_num}&division=-2908172&last_division=-2811727"
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("h1.title > a")
    if len(title) == 0:
        print("[알림] 크롤링이 끝났습니다!")
        break
    for i in title:
        print(f"페이지 : {page_num}")
        print(f"제목 : {i.text}")
        print(f"링크 : {i.attrs['href']}")
        code_news = req.urlopen(i.attrs['href'])
        soup_news = BeautifulSoup(code_news, "html.parser")
        content = soup_news.select_one("div.read_body")
        print(content.text.replace("\n", "").strip())
        print("---------------------------")
    # 쫄리면 조금씩 느리게
    time.sleep(5)
    page_num += 1
