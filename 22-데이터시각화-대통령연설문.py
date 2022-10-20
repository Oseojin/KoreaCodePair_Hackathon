import json

import pandas as pd
import wordcloud
from matplotlib import pyplot as plt

import matplotlib as mat
mat.rcParams["font.family"] = "Malgun Gothic"

df = pd.read_excel("./대통령연설문.xlsx")
df.reset_index(drop=True, inplace=True)
# print(df)

sort_list = ["이승만", "윤보선", "박정희", "최규하", "전두환", "노태우", "김영삼", "김대중", "노무현", "이명박", "박근혜"]

# 대통령별, 연설문 개수
result = []
for name in df["이름"].unique():
    result.append([name, len(df[df["이름"] == name])])
# print(result)

new_result = []
for i in sort_list:
    for j in result:
        if j[0] == i:
            new_result.append(j)
            break
print(new_result)

values = []
for i in new_result:
    values.append(i[1])

f = open("./연설문 단어 빈도수.txt", "r", encoding="UTF8")
wc_list = []
rows = f.readlines()
for row in rows:
    row = row.split("\t") # ["김대중", "{....}"]
    name = row[0]
    data = json.loads(row[1])
    wc = wordcloud.WordCloud(font_path="./NanumMyeongjo.ttf", background_color="white").generate_from_frequencies(data)
    wc_list.append(wc)



# 대통령 별 연설문 개수 시각화
plt.subplot(3, 4, 1)
plt.bar(range(len(sort_list)), values)
plt.xticks(range(len(sort_list)), sort_list)
plt.title("대통령 별 연설문 개수")

for i in range(len(wc_list)):
    ax = plt.subplot(3, 4, 2 + i)
    ax.imshow(wc_list[i], interpolation="bilinear")
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    plt.title(sort_list[i])

    plt.tight_layout(pad=0)

plt.show()
