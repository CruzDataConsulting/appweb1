import pandas as pd 
import streamlit as st

names_link = 'C:/Users/hdcb1/appweb1/dataset.csv'
names_data = pd.read_csv(names_link)

# Create the title for the web app 
st.title("Streamlit and pandas") 
# depliega frame del csv
st.dataframe(names_data)