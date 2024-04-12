import os
import pandas as pd
import streamlit as st


st.header('Vehicles for Sale')
st.write('Filter the data below to see the available vehicles by maker')

df_vehicles = pd.read_csv('./vehicles_us.csv')

vehicle_type_choice = df_vehicles['type'].unique()

selected_menu = st.selectbox('Select Vehicle Type', vehicle_type_choice)

min_year, max_year = int(df_vehicles['model_year'].min()), int(df_vehicles['model_year'].max())

year_range = st.slider('Choose Model Years', value=(min_year, max_year), min_value=min_year, max_value=max_year)

actual_range = list(range(year_range[0], year_range[1]+1))

df_filtered = df_vehicles[(df_vehicles.type == selected_menu) & (df_vehicles.model_year.isin(list(actual_range)))]
