import os
import pandas as pd
import streamlit as st

df_vehicles = pd.read_csv('./vehicles_us.csv')

st.header('Vehicles for Sale')
st.writer('Filter the data below to see the available vehicles by maker')

vehicle_type_choice = df_vehicles['type'].unique()


st.write(df_vehicles.head())
 
