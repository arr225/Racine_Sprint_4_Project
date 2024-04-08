import os
import pandas as pd
import streamlit as st
df_vehicles = pd.read_csv('./vehicles_us.csv')
st.write(df_vehicles.head())
