import os
import pandas as pd
import streamlit as st

df_vehicles = pd.read_csv('./vehicles_us.csv')

st.header('Vehicles for Sale')
st.write('Filter the data below to see the available vehicles by maker')

vehicle_type_choice = df_vehicles['type'].unique()

selected_menu = st.selectbox('Select Vehicle Type', vehicle_type_choice)

min_year, max_year = int(df_vehicles['model_year'].min()), int(df_vehicles['model_year'].max())
                         
year_range = st.slider('Select Year', value=(min_year, max_year), min_value=min_year,max_value=max_year)


st.write(df_vehicles.head())
 
