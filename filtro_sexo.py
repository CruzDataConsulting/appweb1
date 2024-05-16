import streamlit as st
import pandas as pd 

st.title("Streamlit - Filtra sexo")

DATA_URL = ('https://raw.githubusercontent.com/CruzDataConsulting/appweb1/master/dataset.csv')
st.cache_data
def load_data_sex(sex):
    data=pd.read_csv(DATA_URL)
    datos_filtrados_sexo=data[data['sex']]
    return datos_filtrados_sexo

sexo_elegido = st.selectbox("Elige Sexo", load_data_sex['sex'].unique())
st.write(f"Selected Option: {sexo_elegido!r}")

filtro_por_sexo = load_data_sex['sexo'] == sexo_elegido

cuenta_filas=filtro_por_sexo.shape[0]
st.write(f"Total coincidencias {cuenta_filas}")

st.dataframe(filtro_por_sexo)