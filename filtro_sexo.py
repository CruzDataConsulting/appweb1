import streamlit as st
import pandas as pd 

st.title("Streamlit - Busca rangos")

DATA_URL = ('https://raw.githubusercontent.com/CruzDataConsulting/appweb1/master/dataset.csv')
#st.cache_data
#def load_data_sex(sex):
#    data=pd.read_csv(DATA_URL)
#    datos_filtrados_sexo=data[data['sex'].str.contains(sex)]
#    return datos_filtrados_sexo

sexo_elegido = st.selectbox("Select Sexo",load_data_sex['sex'].unique())
st.write(f"Selected Option: {sexo_elegido!r}")
filtered_data_sex = load_data_sex[load_data_sex['sex'] == sexo_elegido]