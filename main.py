import os
import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np


st.header('Vehicles for Sale')
st.write('Filter the data below to see the available vehicles by vehicle model.')

df_vehicles = pd.read_csv('./vehicles_us.csv')

vehicle_type_choice = df_vehicles['model'].unique()

selected_menu = st.selectbox('Select Vehicle Type', vehicle_type_choice)

min_year, max_year = int(df_vehicles['model_year'].min()), int(df_vehicles['model_year'].max())

year_range = st.slider('Choose Model Years', value=(min_year, max_year), min_value=min_year, max_value=max_year)

actual_range = list(range(year_range[0], year_range[1]+1))

df_filtered = df_vehicles[(df_vehicles.model == selected_menu) & (df_vehicles.model_year.isin(list(actual_range)))]

st.write(df_filtered)

st.header('Price Analysis')

st.write("""
###### View pricing based on selectable vehicle attributes.""")

list_hist = ['type', 'fuel', 'transmission', 'paint_color']

selected_attribute = st.selectbox('Attribute for Price Distribution', list_hist)

fig1 = px.histogram(df_vehicles, x='price', color = selected_attribute)
fig1.update_layout(title= "<b> Attribute of price by {}</b>".format(selected_attribute))

st.plotly_chart(fig1)


def categorize_age_group(year, show_age_group):
    if not show_age_group:
        return ''
    if year <= 1969: return 'Old'
    elif 1970 <= year <= 1999: return 'Middle'
    else: return 'New'

# Add a checkbox to toggle the age group function
show_age_group = st.checkbox('Show Age Group', value=True)

df_vehicles['age_group'] = df_vehicles['model_year'].apply(lambda x: categorize_age_group(x, show_age_group))

scatter_list = ['condition', 'odometer', 'days_listed']
selected_scatter = st.selectbox('Price dependency on', scatter_list)

fig2 = px.scatter(df_vehicles, x='price', y=selected_scatter, color ='age_group', hover_data=['model_year'])

st.plotly_chart(fig2)
