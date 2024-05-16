import pandas as pd 
import streamlit as st

DATA_URL = ('https://raw.githubusercontent.com/CruzDataConsulting/appweb1/master/dataset.csv')
st.cache_data
def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state=st.text("Cargando datos...")
data=load_data(1000)
data_load_state.text("Hecho! (con st.cache)")

st.dataframe(data)