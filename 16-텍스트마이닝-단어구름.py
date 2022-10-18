from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from PIL import Image
from wordcloud import ImageColorGenerator

keyword = input("검색어 입력 >> ")
encoded = par.quote(keyword) # URL 인코딩
page_num = 1
okt = Okt()
nouns_result = []

while True:
    url = f"https://www.joongang.co.kr/_CP/496?keyword={encoded}&startDate=&endDate=&sfield=&serviceCode=&sourceCode=&accurateWord=&searchin=&stopword=&sort%20=&pageItemId=439&page={page_num}"
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("ul.story_list h2.headline > a")
    if len(title) == 0:
        break
    for i in title:
        print(f"제목 : {i.text.strip()}")
        content_url = i.attrs["href"]
        code_news = req.urlopen(content_url)
        soup_news = BeautifulSoup(code_news, "html.parser")
        content = soup_news.select_one("div#article_body")
        content_result =content.text.replace("\n", " ").strip()
        print(content_result)
        # 명사만 추출
        nouns_list = okt.nouns(content_result)

        for noun in nouns_list[:]:
            if len(noun) == 1:
                nouns_list.remove(noun)

        print(nouns_list)
        nouns_result += nouns_list

        print("--------------------------------")
    if page_num == 1:
        break
    page_num += 1

print(nouns_result)
# 단어 빈도수 카운트
count_result = Counter(nouns_result)
print(count_result)

# 이미지 가져오기
image_list = np.array(Image.open("./masking.png"))
image_color = ImageColorGenerator(image_list)

# 단어 구름 그리기
wc = WordCloud(background_color="white", font_path="./NanumMyeongjo.ttf", mask=image_list)\
    .generate_from_frequencies(count_result)\
    .recolor(color_func=image_color)

# 이미지 파일로 저장하기
f = open("./wordCloud.svg", "w")
f.write(wc.to_svg())
f.close()

# 단어 빈도수 데이터 프레임에 저장
df = pd.DataFrame().from_dict(count_result, orient="index", columns=["빈도수"])
df.sort_values(by="빈도수", ascending=False, inplace=True)
print(df.to_string())

# 단어 구름 화면에 띄우기
plt.figure() # 창 만들기
plt.imshow(wc, interpolation="bilinear") # 창에 이미지 넣기
plt.axis("off") # x축 y축 표시 제거
plt.show() # 창을 화면에 띄움

# 막대 그래프 화면에 띄우기
plt.figure()
sns.set(font="NanumMyeongjo", style="darkgrid")
sns.barplot(data=df.iloc[:20, :], x = "빈도수", y =df.iloc[:20, :].index)

plt.show()