import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

#crea puntos de gps
map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], 
                        columns=['lat', 'lon'])
# titulo de la app
st.title("San francisco Map") 
st.header("Using Streamlit and Mapbox")
#muestra el mapa
st.map(map_data)
st.markdown("____________")

st.title("Viajes uber")

DATE_COLUMN='date/time'
DATA_URL=('c:\Users\hdcb1\OneDrive\Documentos\SeniorDataSciense\uber_dataset.csv')

@st.cache
def load_data(nrows):
    data=pd.read_csv(DATA_URL,nrows=nrows)
    lowercase=lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state=st.text('Cargando...')
data=load_data(1000)
data_load_state=st.text('Hecho, con cache')

#alguna hora entre 0 y 23
hour_to_filter=st.slider('Hora', 0, 23, 17)
filtered_data=data[data[DATE_COLUMN].dt.hour==hour_to_filter]

st.subheader("Mapa de pickups a las %s:00" % hour_to_filter)
st.map(filtered_data)