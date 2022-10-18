from bs4 import BeautifulSoup
import urllib.request as req
import sentiment_module

print("======== 영화 감성 분석 프로그램 ========")
code = req.urlopen("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
soup = BeautifulSoup(code, "html.parser")
title = soup.select("div.tit3 > a")[:10]
print(" << 현재 상영중이 영화 순위 >> ")
num = 1
for i in title:
    print(f"({num}) {i.text}")
    num += 1
print("========================================")
menu = int(input("감성 분석 진행할 영화 선택 >> "))
print("========================================")
print(f"[알림] <{title[menu-1].text}> 감성분석을 실시합니다.")
print("========================================")

selected_movie = title[menu-1]
movie_code = selected_movie.attrs["href"].replace("/movie/bi/mi/basic.naver?code=", "")

page_num = 1
while True:
    url = f"https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code={movie_code}&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={page_num}"
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    comment = soup.select("div.score_reple > p > span:nth-child(2)")
    for i in comment:
        user_review = i.text.strip()
        if user_review == "스포일러가 포함된 감상평입니다. 감상평 보기":
            continue
        print(user_review)
        score = sentiment_module.sentiment_predict(user_review)
        if score >= 0.5:
            print(f"{score * 100: .2f}% 확률로 긍정입니다.")
        else:
            print(f"{100 - score * 100: .2f}% 확률로 부정입니다.")
        print("----------------------")
    page_num += 1
