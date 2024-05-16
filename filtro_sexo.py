import streamlit as st
import pandas as pd 

st.title("Streamlit - Busca rangos")

DATA_URL = ('https://raw.githubusercontent.com/CruzDataConsulting/appweb1/master/dataset.csv')
st.cache_data
def load_data_sex(sex):
    data=pd.read_csv(DATA_URL)
    datos_filtrados_sexo=data[data['sex']]
    return datos_filtrados_sexo

sexo_elegido = st.selectbox("Elige Sexo",load_data_sex['sex'].unique())
st.write(f"Selected Option: {sexo_elegido!r}")
if (sexo_elegido):
     filtrosexo=load_data_sex(sexo_elegido)
     cuenta_filas=filtrosexo.shape[0] #numero de filas
     st.write(f"Coincidencias encontradas: {cuenta_filas}")

#st.dataframe(filtronombre)
#st.dataframe(filtro_por_rango)
st.dataframe(filtrosexo)