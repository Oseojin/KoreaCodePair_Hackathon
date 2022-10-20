import pandas as pd
import pydeck as pdk


def str_to_int(x):
    if x == "자동":
        return 1
    elif x == "수동":
        return 0
    elif x == "반자동":
        return 0.5


df = pd.read_excel("./로또당첨지역.xlsx", index_col=0)
df["구분"] = df["구분"].map(str_to_int)



layer = pdk.Layer(
    "ScatterplotLayer",
    df,
    get_position=["longitude", "latitude"],
    get_radius=600,
    get_fill_color="[255, 255*(1-구분), 255*(1-구분)]",
    pickable=True
)

layer2 = pdk.Layer(
    "CPUGridLayer",
    df,
    get_position=["longitude", "latitude"],
    auto_highlight = True,
    elevation_scale = 50,
    pickable=True,
    elevation_rane=[0, 3000],
    extruded=True,
    coverage=1
)

initial = pdk.ViewState(latitude=36.0126214, longitude=127.9929026, zoom=7)
map = pdk.Deck(map_style="dark", layers=[layer, layer2], initial_view_state=initial)
map.show()
map.to_html("./lotto.html")

import os
import webbrowser

ap = os.path.abspath("./lotto.html")
webbrowser.open(ap)