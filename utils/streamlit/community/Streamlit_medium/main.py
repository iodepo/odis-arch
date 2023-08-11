import streamlit as st
import pandas as pd
import numpy as np
import pytz
from datetime import datetime
from datetime import date
from PIL import Image
from get_weather import *
from streamlit_autorefresh import st_autorefresh

# Page setting
st.set_page_config(layout="wide", page_title="Robins cool dash")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#Autorefresh:
# count = st_autorefresh(interval=5000, limit=100, key="fizzbuzzcounter")

#Put your logo here:
logo = Image.open('resources/oih.png')
logo = logo.resize((100, 100))#and make it to whatever size you want.

#Time
nowTime = datetime.now()
current_time = nowTime.strftime("%H:%M:%S")
today = str(date.today())
# st.write(today)
timeMetric,= st.columns(1)
timeMetric.metric("",today)

# Row A
a1, a2, a3 = st.columns(3)
a1.image(logo)
a2.metric("Stockholm Temperature", f"{get_temp()}", f"{temp_difference()}"+"%")
a3.metric("Stockholm time", current_time)


# Row B
b1, b2, b3, b4 = st.columns(4)
b1.metric("Humidity", f"{get_humidity()}"+"%")
b2.metric("Feels like", f"{get_feel()}")
b3.metric("Highest temperature", f"{get_temp_max()}")
b4.metric("Lowest temperature", f"{get_temp_min()}")

# Row C
#C1 being the graph, C2 The Table.
c1, c2 = st.columns((7,3))

#Graph:
with c1:

    chart_data = pd.DataFrame(
         np.random.randn(20, 3),
         columns=['Low', 'High', 'Close'])
    st.line_chart(chart_data)

#The fake nonsens table:
with c2:
    df = pd.DataFrame(
        np.random.randn(7, 5),
        columns=('Paris','Malta','Stockholm','Peru','Italy')
    )

    st.table(df)

#Manually refresh button
st.button("Run me manually")
