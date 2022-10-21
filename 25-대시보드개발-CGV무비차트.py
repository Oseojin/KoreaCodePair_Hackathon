import webbrowser

from bs4 import BeautifulSoup
import urllib.request as req
import streamlit as st

code = req.urlopen("http://www.cgv.co.kr/movies/?lt=1&ft=0")
soup = BeautifulSoup(code , "html.parser")
title = soup.select("strong.title")
img = soup.select("span.thumb-image > img")
button_elements = soup.select("a.link-reservation")
num = 1
for i in range(len(title)):
    st.write(f"**{num}위** : {title[i].text}")
    st.image(img[i].attrs["src"], width=150)
    reservation_url = "http://www.cgv.co.kr"+button_elements[i].attrs["href"]
    if st.button("예매하기", key=title[i].text):
        webbrowser.open(reservation_url)
    num += 1