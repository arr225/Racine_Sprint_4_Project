import os
import pandas as pd
import streamlit as st

df_vehicles = pd.read_csv('./vehicles_us.csv')

st.header('Vehicles for Sale')
st.write('Filter the data below to see the available vehicles by maker')

vehicle_type_choice = df_vehicles['type'].unique()

selected_menu = st.selectbox('Select Vehicle Type', vehicle_type_choice)


st.write(df_vehicles.head())
 
