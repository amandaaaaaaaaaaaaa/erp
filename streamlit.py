from cProfile import label
import streamlit as st
import folium
from streamlit_folium import folium_static
from data import *
st.set_page_config(
    page_title='ERP Charges',
    page_icon=':shark:',
    layout="wide")

with st.expander("Vehicle Type"):
    filter_type = st.multiselect("You may select more than one", vehicle_type)
if len(filter_type) != 0:
    for index in range(len(list)):
        if list[index][0] not in filter_type:
            pass
        else:
            type_selected = list[index][0]
            StartTime = list[index][1]
            ChargeAmount = list[index][2]
with st.expander("Vehicle Type"):
    filter_time = st.multiselect("You may select more than one", start_time)
if len(filter_time) != 0:
    for index in range(len(list)):
        if list[index][0] not in filter_type:
            pass
        else:
            type_selected = list[index][0]
            StartTime = list[index][1]
            ChargeAmount = list[index][2]
st.metric(label=type_selected, value=StartTime, value=ChargeAmount) 