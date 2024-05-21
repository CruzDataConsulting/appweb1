import streamlit as st
import pandas as pd
from google.cloud import firestore

path="https://raw.githubusercontent.com/CruzDataConsulting/appweb1/master/"#dataset.csv"
path2="C:/Users/hdcb1/OneDrive/Documentos/SeniorDataSciense/"
# para acceder mediante credenciales
#cred=credentials.Certificate(path2+"primera-base-5bb2f-firebase-adminsdk-2ch28-b147cbc93b.json")
#firebase_admin.initialize_app(cred)

db=firestore.Client.from_service_account_json(path2+"primera-base-5bb2f-firebase-adminsdk-2ch28-b147cbc93b.json")
dbNames=db.collection("names")

st.header("Nuevo registro")

index=st.text_input("Index: ")
name=st.text_input("Nombre: ")
sex=st.selectbox("Elige sexo: ",('M','F','Otro'))

submit=st.button("Crear nuevo registro")

# rutina de append en firebase
if index and name and sex and submit:
    doc_ref=db.collection("names").document(name)
    doc_ref.set({
        "index":index,
        "name":name,
        "sex":sex
    })

st.sidebar.write("Registro añadido correctamente")