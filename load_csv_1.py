import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

path="https://raw.githubusercontent.com/CruzDataConsulting/appweb1/master/dataset.csv"
path2="C:/Users/hdcb1/OneDrive/Documentos/SeniorDataSciense/"

cred=credentials.Certificate(path2+"primera-base-5bb2f-firebase-adminsdk-2ch28-b147cbc93b.json")
firebase_admin.initialize_app(cred)