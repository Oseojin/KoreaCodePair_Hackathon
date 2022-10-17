from bs4 import BeautifulSoup
import urllib.request as req

your_champ = input("상대 챔프 입력 >> ")
header = req.Request("https://www.op.gg/champions", headers={"accept-language" : "ko-KR"})
code = req.urlopen(header)
soup = BeautifulSoup(code, "html.parser")
champs = soup.select("a.css-mtyeel.e1y3xkpj0")

for i in champs:
    if i.text == your_champ:
        champ_url = "https://www.op.gg" + i.attrs["href"]
        break

counter_url = champ_url.replace("?", "/counters?")
print(counter_url)

header = req.Request(counter_url, headers={"accept-language" : "ko-KR"})
code = req.urlopen(header)
soup = BeautifulSoup(code, "html.parser")

counter_champs = soup.select("div.css-aj4kza.eocu2m71")
win_percent = soup.select("span.css-ekbdas.eocu2m73")
game_num = soup.select("span.css-1nfew2i.eocu2m75")

for i in range(len(counter_champs)):
    print(f"챔프 : {counter_champs[i].text}")
    print(f"승률 : {win_percent[i].text}")
    print(f"게임 횟수 : {game_num[i].text}")
    print("----------------------------------")