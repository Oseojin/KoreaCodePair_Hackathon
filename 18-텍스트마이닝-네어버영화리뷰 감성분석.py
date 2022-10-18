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
sentiment_result = {"매우긍정" : 0, "긍정" : 0, "중립" : 0, "부정" : 0, "매우부정" : 0}
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

        if 0.8 <= score <= 1:
            sentiment_result["매우긍정"] += 1
        elif 0.6 <= score < 0.8:
            sentiment_result["긍정"] += 1
        elif 0.4 <= score < 0.6:
            sentiment_result["중립"] += 1
        elif 0.2 <= score < 0.4:
            sentiment_result["부정"] += 1
        elif 0 <= score < 0.2:
            sentiment_result["매우부정"] += 1
        print("----------------------")
    if page_num == 10:
        break
    page_num += 1

from pyecharts import Bar3D
import webbrowser
import os

bar3d = Bar3D("감성분석 결과", width=1200, height=600)
x_axis = ["매우긍정", "긍정", "중립", "부정", "매우부정"]
y_axis = []
data = [[0, 0, sentiment_result["매우긍정"]], 
        [0, 1, sentiment_result["긍정"]], 
        [0, 2, sentiment_result["중립"]], 
        [0, 3, sentiment_result["부정"]], 
        [0, 4, sentiment_result["매우부정"]]]
range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
               '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
bar3d.add("", x_axis, y_axis, [[d[1], d[0], d[2]] for d in data],
    is_visualmap=True, visual_range=[0, max(sentiment_result.values())], visual_range_color=range_color,
    grid3d_width=200, grid3d_depth=40, grid3d_shading="lambert")
bar3d.render("./bar.html")

ap = os.path.abspath("./bar.html")
webbrowser.open(ap)