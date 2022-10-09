from bs4 import BeautifulSoup
import urllib.request as req

code = req.urlopen("http://www.cgv.co.kr/movies/?lt=1&ft=0")
# print(code.read())

soup = BeautifulSoup(code , "html.parser")
# print(soup)

title = soup.select("strong.title")
num = 1
f = open("./test.txt", "w")
for i in title:
    print(f"{num}위 : {i.text}")
    f.write(f"{num}위 : {i.text}\n")
    num += 1
f.close()