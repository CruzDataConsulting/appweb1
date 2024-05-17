import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as ptl

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

optionals=st.expander("Despliega control slider",True)
fare_select=optionals.slider("Elige fare",
                             min_value=float(titanic_data['fare'].min()),
                             max_value=float(titanic_data['fare'].max())
                             )
subset_fare=titanic_data[(titanic_data['fare']<=fare_select)]
st.write(f"Numero de registros con este fare {fare_select}: {subset_fare.shape[0]}")
st.markdown("____________")
st.dataframe(subset_fare)

st.markdown("____________")
fig, ax = plt.subplots() 
ax.hist(titanic_data.fare) 
st.header("Histograma del Titanic") 
st.pyplot(fig)
st.markdown("____________")
fig2, ax2 = plt.subplots()
y_pos = titanic_data['class'] 
x_pos = titanic_data['fare']
ax2.barh(y_pos, x_pos) 
ax2.set_ylabel("Class") 
ax2.set_xlabel("Fare") 
ax2.set_title('¿Cuánto pagaron las clases del Titanic')
st.header("Grafica de Barras del Titanic") 
st.pyplot(fig2)
st.markdown("____________")
fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.age, titanic_data.fare) 
ax3.set_xlabel("Edad") 
ax3.set_ylabel("Tarifa")
st.header("Grafica de Dispersión del Titanic")
st.pyplot(fig3)