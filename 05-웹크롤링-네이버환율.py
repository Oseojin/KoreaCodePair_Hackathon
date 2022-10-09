from bs4 import BeautifulSoup
import urllib.request as req

while True:
    print("============= 메뉴 =============")
    print("1. 미국 USD")
    print("2. 일본 JPY")
    print("3. 유럽 EUR")
    print("4. 중국 CNY")
    print("===============================")
    menu = int(input("선택 >> "))
    unit = ["달러", "엔", "유로", "위안"]
    user_input = float(input(f"게산하고 싶은 금액 입력 (단위 : {unit[menu-1]})>> "))

    if menu == 2:
        user_input /= 100

    code = req.urlopen("https://finance.naver.com/marketindex/")
    soup = BeautifulSoup(code, "html.parser", from_encoding="euc-kr")
    price = soup.select("ul#exchangeList span.value")
    country = soup.select("ul#exchangeList h3.h_lst")

    f = open("./환율.txt", "w")
    for i in range(len(price)):
        # print(f"{country[i].text} : {price[i].text}원")
        f.write(f"{country[i].text} : {price[i].text}원\n")
    f.close

    result = float(price[menu-1].text.replace(",", "")) * user_input
    print(f"계산 결과 : {result:,}원")
    key_input = input("[알림]엔터 키를 입력하세요. (종료하시려면 0을 누르세요)")
    if key_input == "0":
        print("[알림] 프로그램을 종료합니다.")
        break
