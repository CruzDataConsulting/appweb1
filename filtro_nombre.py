import streamlit as st
import pandas as pd 

st.title("Streamlit - Busca nombres")

DATA_URL = ('https://raw.githubusercontent.com/CruzDataConsulting/appweb1/master/dataset.csv')
st.cache_data
def load_data_byname(name):
    data=pd.read_csv(DATA_URL)
    datos_filtrados_nombre=data[data['name'].str.contains(name)]
    return datos_filtrados_nombre

minombre=st.text_input("Nombre: ")
if (minombre):
    filtronombre=load_data_byname(minombre)
    cuenta_filas=filtronombre.shape[0] #numero de filas
    st.write(f"Nombres totales: {cuenta_filas}")
    
    st.dataframe(filtronombre)