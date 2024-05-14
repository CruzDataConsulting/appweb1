import pandas as pd 
import streamlit as st

DATA_URL = ('C:/Users/hdcb1/appweb1/dataset.csv')
st.cache
def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state=st.text("Cargando datos...")
data=load_data(1000)
data_load_state.text("Hecho! (con st.cache)")

st.dataframe(data)