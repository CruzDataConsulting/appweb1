import streamlit as st
import pandas as pd
import datetime

titanic_link=('https://raw.githubusercontent.com/CruzDataConsulting/appweb1/master/titanic_data.csv')
titanic_data=pd.read_csv(titanic_link)

#titulo de appweb
st.title("Segunda app, controles avanzados")
#sidebar
sidebar=st.sidebar
sidebar.title("Esta es la side bar")
sidebar.write("Sea agregan controles en sidebar")

#usuario pide hora actual
today=datetime.date.today()
today_date=st.date_input("Fecha de hoy: ",today)
st.success("Fecha corriente: '%s'"%(today_date))

#Muestra contenido del dataset si selecciona check box
st.header("Dataset Titanic")
agree=st.checkbox("Vista previa del dataset?")
if (agree):
    st.dataframe(titanic_data)

st.header("Descripcion del dataset")
#radio control
elige_clase=st.radio("Elige la clase", titanic_data['class'].unique())
st.write("Usted eligió: ",elige_clase)
st.markdown("______")

optionals=st.expander("Configuración opcional",True)
fare_select=optionals.slider("Elige fare",
                             min_value=float(titanic_data['fare'].min()),
                             max_value=float(titanic_data['fare'].max())
                             )
subset_fare=titanic_data[(titanic_data['fare']<=fare_select)]
st.write(f"Numero de registros con este fare {fare_select}: {subset_fare.shape[0]}")
st.markdown("____________")
st.dataframe(subset_fare)