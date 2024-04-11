import os
import pandas as pd
import streamlit as st

df_vehicles = pd.read_csv('./vehicles_us.csv')

st.header('Vehicles for Sale')
st.write(df_vehicles.head())
