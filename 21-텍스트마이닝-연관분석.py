import os.path
import webbrowser

import pandas as pd
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as par
from konlpy.tag import Okt
from mlxtend.frequent_patterns import apriori
from mlxtend.preprocessing import TransactionEncoder
import networkx as nx
from pyvis.network import Network

keyword = input("검색어 입력 >> ")
encoded = par.quote(keyword) # URL 인코딩
page_num = 1
okt = Okt()
dataset = []

while True:
    url = f"https://www.joongang.co.kr/_CP/496?keyword={encoded}&startDate=&endDate=&sfield=&serviceCode=&sourceCode=&accurateWord=&searchin=&stopword=&sort%20=&pageItemId=439&page={page_num}"
    code = req.urlopen(url)
    soup = BeautifulSoup(code, "html.parser")
    title = soup.select("ul.story_list h2.headline > a")
    if len(title) == 0:
        break
    for i in title:
        print(f"제목 : {i.text.strip()}")
        # 명사 추출
        nouns_list = okt.nouns(i.text.strip())
        # 불용어 제거
        for noun in nouns_list[:]:
            if len(noun) == 1:
                nouns_list.remove(noun)
        dataset.append(nouns_list)
        print("--------------------------------")
    if page_num == 1:
        break
    page_num += 1

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
df_apr = apriori(df, use_colnames=True, min_support=0.02)

df_apr["length"] = df_apr["itemsets"].str.len()
df_apr = df_apr[df_apr["length"]==2]
df_apr["itemssets"] = df_apr["itemsets"].apply(lambda x:list(x))
df_apr["source"] = df_apr["itemsets"].str[0]
df_apr["target"] = df_apr["itemsets"].str[1]
print(df_apr)

G = nx.from_pandas_edgelist(df_apr, source="source", target="target", edge_attr="support")
net = Network(height="1000px", width= "1500px")
net.from_nx(G)
net.show_buttons(fillter_=["physics"])
net.show("./network.html")

ap = os.path.abspath("./network.html")
webbrowser.open(ap)
