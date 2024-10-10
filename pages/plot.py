import streamlit as st
from functions import *
import matplotlib.pyplot as plt
import numpy as np

menu()

df = read_df()

team = st.selectbox("Team: ", df['Team'].sort_values().unique(), index=None)
pos = st.selectbox("Postion: ", df['Pos'].sort_values().unique(), index=None)
games = st.slider("Games played:", min_value=0, max_value=82, value=50)
minutes = st.slider("Minutes played:", min_value=0, max_value=36, value=20)
x = st.selectbox("x axis: ", df.select_dtypes(include=np.number).columns.sort_values().unique(), index=None)
y = st.selectbox("y axis: ", df.select_dtypes(include=np.number).columns.sort_values().unique(), index=None)
df_filter = filter_df(df, team, pos, games, minutes)

fig, ax = plt.subplots(figsize = (5, 5))

ax = scatter_plot(df_filter, x, y, ax)

st.pyplot(fig)