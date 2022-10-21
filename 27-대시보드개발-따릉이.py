import streamlit as st
import requests
import json
import pandas as pd
import pydeck as pdk

api_key = ""


num = 0
while True:
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/json/bikeList/{1 + 1000*num}/{1000 + 1000 * num}/"
    data = requests.get(url)
    result = json.loads(data.text)
    result_element_length = len(result["rentBikeStatus"]["row"])
    if result_element_length != 1000:
        max_value = 1 + 1000 * num + result_element_length
    num += 1


bike_dict = {"rackTotCnt" : [], "stationName" : [],
             "parkingBikeTotCnt": [], "shared" : [],
             "latitude" : [], "longitude" : []}
num = 0
while True:
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/json/bikeList/{1 + 1000 * num}/{1000 + 1000 * num}/"
    data = requests.get(url)
    result = json.loads(data.text)
    for row in result["rentBikeStatus"]["row"]:
        bike_dict["rackTotCnt"].append(int(row["rackTotCnt"]))
        bike_dict["stationName"].append(row["stationName"])
        bike_dict["parkingBikeTotCnt"].append(int(row["parkingBikeTotCnt"]))
        bike_dict["shared"].append(int(row["shared"]))
        bike_dict["latitude"].append(int(row["stationLatitude"]))
        bike_dict["longitude"].append(int(row["stationLongitude"]))
    if len(result["renBikeStatus"]["row"]) != 1000:
        break
    num += 1

    df = pd.DataFrame(bike_dict)
    st.dataframe(df)

    pdk.Layer(
        "ScatterplotLayer",
        df,
        get_position=["longitude", "latitude"],
        get_radius = "60 * shared / 100",
        get_fill_color="[255-shared,255-shared,255]",
        pickable=True
    )

    lat_center = df["latitude"].mean()
    lon_center = df["longitude"].mean()
    initial_state = pdk.ViewState(latitude=lat_center, longitude=lon_center, zoom = 10)

    map = pdk.Deck(map_style="dark",layers=[layer], initial_view_state = initial_state,
                   tooltip={
                       "html" : "정류장 : {stationName}<br/>현재 주차 대수 : {parkingBikeTotcnt}",
                       "style" : {"color" : "white"}
                   })

    st.pydeck_chart(map)