import streamlit as st
import pandas as pd 

st.title("Streamlit - Busca rangos")

DATA_URL = ('https://raw.githubusercontent.com/CruzDataConsulting/appweb1/master/dataset.csv')
st.cache_data
def load_data_byrange(starid, endid):
    data=pd.read_csv(DATA_URL)
    datos_filtrados_rango=data[(data['index']>=starid) & (data['index']>=endid)]
    return datos_filtrados_rango

starid=st.text_input("Star index: ")
endid=st.text_input("End index: ")
btnRange=st.button("Busca rango")

if (btnRange):
    filtro_por_rango=load_data_byrange(int(starid), int(endid))
    cuenta_filas=filtro_por_rango.shape[0]
    st.write(f"Total itemos(jeje) {cuenta_filas}")

    st.dataframe(filtro_por_rango)