import streamlit as st
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import numpy as np

map_data = pd.DataFrame(np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], 
                        columns=['lat', 'lon'])

# titulo de la ap 
st.title("San francisco Map") 
st.header("Using Streamlit and Mapbox")

st.map(map_data)
