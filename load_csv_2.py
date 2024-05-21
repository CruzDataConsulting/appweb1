import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd

path="https://raw.githubusercontent.com/CruzDataConsulting/appweb1/master/"#titanic_data.csv"
path2="C:/Users/hdcb1/OneDrive/Documentos/SeniorDataSciense/"
# para acceder mediante credenciales
cred=credentials.Certificate(path2+"titanic-project-d9f2b-firebase-adminsdk-42mmi-225c58cf39.json")
firebase_admin.initialize_app(cred)

# Seccion de importacion
db=firestore.client()
doc_ref=db.collection(u"pasajeros") #names es nombre de la coleccion en firebase
# para importar csv
df=pd.read_csv(path+"titanic_data.csv")
tmp=df.to_dict(orient="records")
list(map(lambda x: doc_ref.add(x), tmp))