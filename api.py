import requests, datetime, time, json
import streamlit as st

url = "http://datamall2.mytransport.sg/ltaodataservice/ERPRates"
#headers = {"AccountKey": "",
#           "accept": "application/json"}
headers = {"AccountKey": st.secrets["LTA_APIKEY"],
           "accept": "application/json"}
response = requests.request(method="get", url=url, headers=headers)
lta_data = response.json()
#print(json.dumps(lta_data, indent=4))